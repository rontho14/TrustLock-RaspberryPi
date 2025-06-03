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