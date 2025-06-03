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


