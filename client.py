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

from utils import build_header

serialName = "COM5"

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        com1.enable()
        print("Abriu a comunicação")
        # bit de sacrifício
        time.sleep(.2)
        com1.sendData(b'00')
        time.sleep(1)
        print("bit de sacrifício enviado")
        # enviar mensagem perguntando quais arquivos estão disponíveis
        header = build_header(h0=1)
        com1.tx.sendBuffer(header)
        # aguardar 
        start_time = time.monotonic() 
        while (time.monotonic() - start_time < 3) and (com1.rx.getBuffer() < 10):
            time.sleep(0.05)
        if time.monotonic() - start_time >= 3:
            print('time out')
            # TEM QUE ENVIAR O PACOTE QUE ESTAVA ENVIANDO NOVAMENTE
        header_b = com1.rx.getNData(10)
        print("Recebi as opções de arquivos")
        header = int.from_bytes(header_b)
        if header[0] == 3:
            # signifca que eu recebi os nomes dos arquivos
            print("Essas são as opções de arquivo:")
            tam_pacote = header[3]
            payload_b = com1.rx.getNData(tam_pacote)
            payload = int.from_bytes(payload_b)
            for p in payload:
                print(f"Arquivo {p}")
            arq_escolhido = int(input("Digite o número do arquivo que você deseja: "))
            
        


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
