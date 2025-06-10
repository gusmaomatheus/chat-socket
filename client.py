import socket
import threading

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            print(mensagem)
        except:
            print("Conexão encerrada.")
            cliente.close()
            break

def enviar_mensagens(cliente, nome):
    while True:
        mensagem = input()
        cliente.send(f"{nome}: {mensagem}".encode('utf-8'))

def iniciar_cliente():
    server_host = '127.0.0.1'
    server_port = 12345

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((server_host, server_port))

    nome = input("Digite seu nome: ")

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread_receber.start()

    thread_enviar = threading.Thread(target=enviar_mensagens, args=(cliente, nome))
    thread_enviar.start()

if __name__ == "__main__":
    iniciar_cliente()
