#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
####################################################

from enlace import *
import time
import numpy as np
import struct 
from math import *

serialName = "COM5"

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        com1.enable()
        print("Abriu a comunicação")
        #  byte de sacrifício
        time.sleep(.2)
        com1.sendData(b'00')
        time.sleep(1)
        print("bit de sacrifício enviado")
        # enviar mensagem perguntando quais arquivos estão disponíveis
        
        # aguardar 
        

        print(txBuffer)
        com1.sendData(txBuffer)
        # esperando saber que eu posso mandar os números
        while com1.tx.getIsBussy():
            time.sleep(0.05)
            print('esperando buffer tx')
        print('acabou de enviar')
        txLen = len(txBuffer)
        print('esperando confirmação')
        rxBuffer, nRx = com1.getData(txLen)
        if rxBuffer == txBuffer:
            # significa que posso enviar os números
            print(sum((lista)))
            #soma = struct.pack('>f', sum(lista))
            soma = sum(lista)
            for num in lista:
                print('vou enviar')
                txBuffer = struct.pack('>f', num)
                com1.sendData(txBuffer)
                while com1.tx.getIsBussy():
                    time.sleep(0.05)
                    print('esperando buffer tx')
                print('acabou de enviar')
            start_time = time.monotonic()          
            while (time.monotonic() - start_time < 5) and (com1.rx.getBufferLen() < 4):
                time.sleep(0.05)
            if time.monotonic() - start_time >= 5:
                print('time out')
            else:
                rxBuffer, nRx = com1.getData(4)
                rxB = struct.unpack('>f', rxBuffer)[0]
                if isclose(soma, rxB, abs_tol=1e-5):
                    print('acertou!')
                else:
                    print('tem algo de errado na soma')

            print("-------------------------")
            print("Comunicação encerrada")
            print("-------------------------")
            com1.disable()


        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()    

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
