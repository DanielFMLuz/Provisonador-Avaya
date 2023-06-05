import telnetlib
import time

# Função para estabelecer a conexão com o telefone
def conectar_telefone(ip_address):
    tn = telnetlib.Telnet(ip_address)
    return tn

# Função para autenticar o telefone
def autenticar_telefone(tn, username, password):
    tn.read_until(b"login: ")
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Função para configurar o endereço IP do telefone
def configurar_ip(tn, server_address, path_address):
    tn.write(b"setIpConfig\n")
    tn.read_until(b"server address: ")
    tn.write(server_address.encode('ascii') + b"\n")
    tn.read_until(b"path address: ")
    tn.write(path_address.encode('ascii') + b"\n")

# Função para reiniciar o telefone
def reiniciar_telefone(tn):
    tn.write(b"restart\n")
    time.sleep(10)  # Aguardar o reinício

# Função para encerrar a conexão com o telefone
def encerrar_conexao(tn):
    tn.write(b"exit\n")
