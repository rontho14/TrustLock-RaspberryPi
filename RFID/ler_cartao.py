import utime
from machine import Pin, SPI
from RFID.MFRC522 import MFRC522

# Inicializa o leitor RC522
reader = MFRC522(18, 16, 19, 14, 15) # SCK, MOSI, MISO, CS, Reset

def read_card():
    # Tenta ler cartao
    (status, tag_type) = reader.request(reader.REQIDL)
    if status == reader.OK:
        print('Cartao detectado!')
        (status, uid) = reader.anticoll()
        if status == reader.OK:
            print("UID do cartao: {}".format(uid))
            return uid
        return None
    
