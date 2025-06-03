from machine import Pin, I2C
import utime
from OLED.ssd1306 import SSD1306_I2C
from Teclado.keyboard import MatrixKeyboard
from RFID.MFRC522 import MFRC522

# ---- DISPLAY OLED ----
from OLED.ssd1306 import SSD1306_I2C
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
display = SSD1306_I2C(128, 32, i2c)