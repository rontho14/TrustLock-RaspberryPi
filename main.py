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