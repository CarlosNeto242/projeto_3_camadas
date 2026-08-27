#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np
import struct

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)  detectar sua porta e substituir aqui


def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        com1.enable()
        print("Abriu a comunicação")
        print("esperando 1 byte de sacrifício")
        rxBuffer, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(.1)
        # --- RECEBENDO O HAND SHAKE ---
        handshake = com1.rx.getNData(1)
        hand_int = int.from_bytes(handshake, 'big')
        print(f"Chegou o número {hand_int}")
        com1.sendData(handshake)
        # --- ESPERANDO ENVIAR TOTALMENTE --- 
        # while com1.tx.getIsBussy():
        #       time.sleep(0.05)
        # print("Foi tudo enviado")
        # com1.rx.clearBuffer()
        # --- ESPERANDO OS NÚMEROS PARA A SOMA ---
        # while com1.rx.getBufferLen() < qtd_int*4:
        #     time.sleep(0.05)
        # print("Chegou os numero")
        # soma_total = 0.0
        # for i in range(qtd_int):
        #     numero = com1.rx.getNData(4) 
        #     float = struct.unpack(">f", numero)   
        #     print(f"Número atual: {float[0]:.6f}")
        #     soma_total += float[0]
        # print(f"Soma feita: {soma_total}")
        # txBuffer = struct.pack(">f", soma_total)
        # com1.sendData(txBuffer)
        # while com1.tx.getIsBussy():
        #       time.sleep(0.05)
        # print("Foi tudo enviado")
        # com1.disable()

    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
if __name__ == "__main__":
    main()
