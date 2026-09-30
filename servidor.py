import socket
from datetime import datetime

HOST = "0.0.0.0"   # aceita conexões de qualquer IP
PORTA = 5000

# cria o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # permite reiniciar sem erro de porta ocupada

# associa o socket ao endereço e porta, e começa a escutar
servidor.bind((HOST, PORTA))
servidor.listen()
print(f"Servidor iniciado na porta {PORTA}")

# while principal atende um cliente de cada vez
while True:
    conexao, endereco = servidor.accept()   # espera um cliente conectar
    print(f"Cliente conectado ({endereco[0]})")

    # while de conversa com o cliente conectado
    while True:
        dados = conexao.recv(1024)          # recebe até 1024 bytes
        if not dados:                       # cliente fechou sem mandar EXIT
            break

        mensagem = dados.decode().strip()
        print(f"Comando recebido: {mensagem}")

        # interpreta o comando (o "protocolo")
        if mensagem == "TIME":
            resposta = "Hora atual: " + datetime.now().strftime("%H:%M:%S")
        elif mensagem == "STATUS":
            resposta = "Servidor ativo e aguardando conexões"
        elif mensagem.startswith("ECHO "):
            resposta = mensagem[5:]         # devolve o texto depois de "ECHO "
        elif mensagem == "EXIT":
            resposta = "Conexão encerrada"
        else:
            resposta = "Erro: comando desconhecido"

        # envia a resposta ao cliente
        conexao.sendall(resposta.encode())

        if mensagem == "EXIT":
            break

    # fecha a conexão com esse cliente e volta a esperar outro
    conexao.close()
    print("Conexão encerrada.")
