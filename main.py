from machine import Pin, I2C
import utime
from OLED.ssd1306 import SSD1306_I2C
from Teclado.keyboard import MatrixKeyboard
from RFID.MFRC522 import MFRC522

# ---- DISPLAY OLED ----
from OLED.ssd1306 import SSD1306_I2C
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
display = SSD1306_I2C(128, 32, i2c)

def display_message(line1="", line2=""):
    display.fill(0)
    display.text(line1, 0, 0, 1)
    display.text(line2, 0, 10, 1)
    display.show()
    
# ---- BUZZER e FECHADURA ----
buzzer = Pin(0, Pin.OUT)
lock = Pin(22, Pin.OUT)
def beep(times, duration_on=0.05, duration_off=0.05):
    for _ in range(times):
        buzzer.on()
        utime.sleep(duration_on)
        buzzer.off()
        utime.sleep(duration_off)
def open_lock(duration=5):
    lock.on()
    utime.sleep(duration)
    lock.off()
    
# ---- TECLADO MATRICIAL ----
from Teclado.keyboard import MatrixKeyboard
rows_pins = [6, 9, 10, 11]
cols_pins = [12, 13, 14, 15]
debounce_time = 5
keyboard = MatrixKeyboard(rows_pins, cols_pins, debounce_time)

# ---- RFID MFRC522 ----
def check_rfid():
    try:
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, raw_uid) = reader.anticoll()
            if stat == reader.OK:
                return raw_uid
    except Exception as e:
        print("RFID error:", e)
    return None

# ---- ESTADO DO SISTEMA ----
password_entering = False
entered_password = ""
password_start_time = None
correct_password = "12345"
last_activity_time = utime.time()
inactive_timeout = 7
password_timeout = 7
access_granted_time = None
access_granted = False
display_cleared = False

# ---- MENSAGEM INICIAL ----
display_message("Aproxime RFID", "ou digite senha")
print("Aproxime um cartão RFID ou digite senha")

# ---- LOOP PRINCIPAL ----
while True:
    keys = keyboard.get_pressed_keys()
    current_time = utime.time()

    # Limpa após acesso
    if access_granted and (current_time - access_granted_time >= 10):
        display.fill(0)
        display.show()
        access_granted = False
        display_cleared = True

    # Limpa após inatividade
    if not access_granted and (current_time - last_activity_time > inactive_timeout):
        if not display_cleared:
            display.fill(0)
            display.show()
            display_cleared = True

    # Mostra mensagem se tela limpa e houve interação
    if display_cleared:
        if keys or check_rfid():
            display_message("Aproxime RFID", "ou digite senha")
            display_cleared = False
            last_activity_time = current_time

    # RFID sempre ativo
    uid = check_rfid()
    if uid and not access_granted:
        display_message("Acesso Liberado")
        print(f"UID: {'-'.join([str(x) for x in uid])}")
        beep(3, 0.1, 0.1)
        open_lock()
        access_granted_time = current_time
        access_granted = True
        last_activity_time = current_time

    # Timeout de senha
    if password_entering and password_start_time is not None:
        if current_time - password_start_time > password_timeout:
            display_message("Tempo esgotado")
            beep(2, 0.2, 0.2)
            password_entering = False
            entered_password = ""
            password_start_time = None
            utime.sleep(1)
            display_message("Aproxime RFID", "ou digite senha")
            last_activity_time = utime.time()

    # Teclado
    if keys:
        for key in keys:
            print(f"Tecla pressionada: {key}")
            last_activity_time = current_time
            if not password_entering:
                password_entering = True
                entered_password = ""
                password_start_time = current_time
            if password_entering:
                if key in "1234567890":
                    entered_password += key
                    display_message("Senha:", "*" * len(entered_password))
                    password_start_time = current_time
                elif key == "*":
                    entered_password = ""
                    display_message("Digite a senha")
                    beep(1, 0.1, 0.05)
                    password_start_time = current_time
                elif key == "#":
                    password_entering = False
                    password_start_time = None
                    display_message("Verificando...")
                    if entered_password == correct_password:
                        display_message("Acesso Liberado")
                        beep(3, 0.1, 0.1)
                        open_lock()
                        access_granted_time = current_time
                        access_granted = True
                    else:
                        display_message("Senha incorreta")
                        beep(2, 0.3, 0.3)
                    entered_password = ""

    utime.sleep_ms(10)




