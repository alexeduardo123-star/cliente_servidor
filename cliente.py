import socket

HOST = "127.0.0.1"   # IP do servidor (127.0.0.1 = mesma máquina)
PORTA = 5000

# cria o socket TCP e conecta ao servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Conectando ao servidor...")

try:
    cliente.connect((HOST, PORTA))
except ConnectionRefusedError:
    print("Não foi possível conectar. O servidor está rodando?")
    exit()

# while, lê um comando, envia e espera a resposta e mostra
while True:
    comando = input("Digite um comando: ").strip()
    if not comando:
        continue                            # ignora linha vazia

    cliente.sendall(comando.encode())       # envia o comando
    resposta = cliente.recv(1024).decode()  # espera a resposta
    print(f"Resposta do servidor: {resposta}")

    if comando == "EXIT":
        break

# fecha o socket
cliente.close()
