import socket
import threading

clientes = []

def broadcast(mensagem, cliente_atual):
    for cliente in clientes:
        if cliente != cliente_atual:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                clientes.remove(cliente)

def tratar_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            broadcast(mensagem, cliente)
        except:
            cliente.close()
            clientes.remove(cliente)
            break

def iniciar_servidor():
    host = '127.0.0.1'
    porta = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()

    print(f"[Servidor iniciado] Aguardando conexões em {host}:{porta}...")

    while True:
        cliente, endereco = servidor.accept()
        print(f"[Nova conexão] {endereco} conectado.")
        clientes.append(cliente)

        thread = threading.Thread(target=tratar_cliente, args=(cliente,))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
