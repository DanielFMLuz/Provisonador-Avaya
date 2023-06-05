import tkinter as tk
from tkinter import messagebox

from funcoes import conectar_telefone, autenticar_telefone, configurar_ip, reiniciar_telefone, encerrar_conexao

def configurar_telefones():
    # Obter os valores dos campos de entrada
    phones = txt_phones.get().split(",")
    username = txt_username.get()
    password = txt_password.get()
    server_address = txt_server_address.get()
    path_address = txt_path_address.get()

    # Configurar os telefones
    for phone in phones:
        try:
            tn = conectar_telefone(phone)
            autenticar_telefone(tn, username, password)
            configurar_ip(tn, server_address, path_address)
            reiniciar_telefone(tn)
            encerrar_conexao(tn)
            messagebox.showinfo("Sucesso", f"Telefone {phone} configurado e reiniciado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao configurar o telefone {phone}: {str(e)}")

# Criação da janela principal
window = tk.Tk()
window.title("Configuração de Telefones IP")
window.geometry("400x300")

# Campo de entrada para os endereços IP dos telefones
lbl_phones = tk.Label(window, text="Endereços IP dos telefones (separados por vírgula):")
lbl_phones.pack()
txt_phones = tk.Entry(window)
txt_phones.pack()

# Campo de entrada para o nome de usuário
lbl_username = tk.Label(window, text="Nome de Usuário:")
lbl_username.pack()
txt_username = tk.Entry(window)
txt_username.pack()

# Campo de entrada para a senha
lbl_password = tk.Label(window, text="Senha:")
lbl_password.pack()
txt_password = tk.Entry(window, show="*")
txt_password.pack()

# Campo de entrada para o endereço do servidor
lbl_server_address = tk.Label(window, text="Endereço do Servidor:")
lbl_server_address.pack()
txt_server_address = tk.Entry(window)
txt_server_address.pack()

# Campo de entrada para o caminho do servidor
lbl_path_address = tk.Label(window, text="Caminho do Servidor:")
lbl_path_address.pack()
txt_path_address = tk.Entry(window)
txt_path_address.pack()

# Botão para configurar os telefones
btn_configurar = tk.Button(window, text="Configurar Telefones", command=configurar_telefones)
btn_configurar.pack()

# Iniciar a execução da janela
window.mainloop()


