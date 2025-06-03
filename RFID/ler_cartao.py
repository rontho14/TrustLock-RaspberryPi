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
    
def main():
    print("Aproxime o cartao ou token para obter o UID...")
    
    while True:
        # Verifica se ha um cartao proximo
        uid = read_card()
        if uid:
            print("UID lido: {}".format(uid))
        utime.sleep(0.5)    # Aguarda antes de tentar ler novamente
        
main()