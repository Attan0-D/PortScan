import socket
import threading 

# O arquivo TXT possui as portas par escanear.
with open("ports.txt","r") as file:
    ports = file.readlines()


def portScan(t):

    # Index tratanto as portas como lista
    for i in ports:
        
        #Definindo tipo de endereco e protocolo que sera usado
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5)

        # O conectando com a porta - usando strip para retirar quebra de texto 
        result = sock.connect_ex((t, int(i.strip("\n"))))

        # Verificando e Mostrando Banner (Caso exista)
        try:
            if result == 0:
                banner = sock.recv(2048)
                print("\n SSH Banner Found: ", banner)

        except Exception:
            print("\nBanner Not Found")

        sock.close()

        # O resultado retornando 0 -> a Porta em questao esta aberta
        if result == 0:
            print(i.strip("\n"), "- OPEN ")


def init_scan():

    try:
        target_ = input("Digite o Alvo da consulta: ")
    except Exception:
        print("Alvo Invalido")

    #Usando threading para maior velocidade de execucao
    thr = threading.Thread(target=portScan, args=(str(target_),))
    thr.start()
    thr.join()

init_scan()
