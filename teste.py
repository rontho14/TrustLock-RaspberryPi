from Teclado.keyboard import MatrixKeyboard
from machine import Pin, I2C
from OLED.ssd1306 import SSD1306_I2C
from RFID.MFRC522 import MFRC522
import utime

# Configuracao hardware
rows_pins = [6, 7, 8, 9]
cols_pins = [2, 3, 4, 5]
debounce_time = 5
keyboard = MatrixKeyboard(rows_pins, cols_pins, debounce_time)

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
display = SSD1306_I2C(128, 32, i2c)

buzzer = Pin(28, Pin.OUT)
lock = Pin(13, Pin.OUT)

reader = MFRC522(18, 19, 15, 14) # SCK, MOSI, MISO, RST, SDA

# Estado do sistema
password_entering = False
entered_password = ""
password_start_time = None
correct_password = "12345"
last_activity_time = utime.time()
inactive_timeout = 7
password_timeout = 7

access_granted_time = None
access_granted = False

def beep(times, duration_on=0.05, duration_off=0.05):
    for _ in range(times):
        buzzer.on()
        utime.sleep(duration_on)
        buzzer.off()
        utime.sleep(duration_off)
        
def display_message(line1="", line2=""):
    display.fill(0)
    display.text(line1, 0, 0, 1)
    display.text(line2, 0, 10, 1)
    display.show()

def check_rfid():
    try:
        status, _ = reader.request(reader.REQIDL)
        if status == reader.OK:
            status, uid = reader.anticoll()
            if status == reader.OK:
                return uid
    except Exception as e:
        print("RFID error: ", e)
        return None
        
def open_lock(duration=5):
    lock.on()
    utime.sleep(duration)
    lock.off()
    
print("Aproxime um cartão RFID ou digite senha")
display_message("Aproxime RFID", "ou digite senha")

while True:
    keys = keyboard.get_pressed_keys()
    current_time = utime.time()
    
    # Limpa apos acesso
    display.show()
    access_granted = False
    
    # Limpa apos inatividade
    if  not access_granted and (current_time - last_activity_time > inactive_timeout):
        display.show()
        
    # RFID sempre ativo (independente do modo senha)
    uid = check_rfid()
    if uid and not access_granted:
        display_message("Acesso Liberado")
        print(f"UID: {uid}")
        beep(3, 0.1, 0.1)
        open_lock()  # <- Fechadura acionada
        access_granted_time = current_time
        access_granted = True
        last_activity_time = current_time


    
    

        


