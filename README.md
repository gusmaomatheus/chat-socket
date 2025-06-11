# 💬 Chat com Sockets TCP em Python

Este projeto foi desenvolvido com fins acadêmicos como parte de uma avaliação da disciplina de Redes de Computadores.

Este projeto implementa um **sistema de chat simples** utilizando **sockets TCP** com suporte a múltiplos clientes. Ele é uma ótima introdução à comunicação em rede com Python, utilizando `socket` e `threading`.

---

## 🚀 Funcionalidades

- ✅ Múltiplos clientes conectados simultaneamente
- ✅ Troca de mensagens em tempo real
- ✅ Comunicação usando TCP/IP
- ✅ Arquitetura cliente-servidor
- ✅ Interface em terminal (linha de comando)

---

## 🧱 Estrutura

O projeto é composto por dois arquivos principais:

- `server.py`: roda o servidor que gerencia conexões e transmite mensagens.
- `client.py`: roda um cliente que envia e recebe mensagens no chat.

---

## 🔧 Requisitos

- Python 3.x instalado
- Terminal ou prompt de comando

---

## ▶️ Como executar

### 1. Clonar o repositório

```bash
> $ git clone https://github.com/gusmaomatheus/chat-socket.git
> $ cd chat-socket-python
```

### 2. Iniciar o servidor (em um terminal):

```bash
> $ python server.py
```

### 3. Iniciar um ou mais clientes (em outro(s) terminal(is)):

```bash
> $ python client.py
```

```bash
Terminal 1 (servidor):
[Servidor iniciado] Aguardando conexões em 127.0.0.1:12345...
[Nova conexão] ('127.0.0.1', 54321) conectado.

Terminal 2 (cliente):
Digite seu nome: Ana
Pedro: Oi Ana!
Ana: Oi Pedro! Tudo bem?

Terminal 3 (cliente):
Digite seu nome: Pedro
Ana: Oi Pedro! Tudo bem?

```

# 🧠 Como funciona

- O servidor escuta novas conexões e cria uma thread para cada cliente.

- Cada cliente roda duas threads:

    - Uma para enviar mensagens digitadas.

    - Outra para receber mensagens do servidor.

- O servidor recebe as mensagens dos clientes e as retransmite para todos os outros conectados.

# 🎬 Demonstração

[Vídeo do YouTube](https://)

# 📜 Licença

Este projeto está licenciado sob a licença **MIT**. Sinta-se livre para usar e modificar!