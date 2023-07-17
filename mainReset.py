from tkinter import Tk, Label, Entry, Button
from functools import partial
from reset import automatizar_paginas

def start_automatizacao(enderecos_ip):
    automatizar_paginas(enderecos_ip)

def main():
    # Função para obter os números IPs ao clicar no botão
    def obter_ips():
        enderecos_ip = ip_entry.get().split(',')  # Obtém os números IPs separados por vírgula
        window.destroy()  # Fecha a janela
        start_automatizacao(enderecos_ip)  # Chama a função de automatização com os números IPs

    # Configuração da janela principal
    window = Tk()
    window.title("Automação de Páginas")
    window.geometry("300x200")

    # Rótulo e campo de entrada para os números IPs
    ip_label = Label(window, text="Digite os números IPs separados por vírgula:")
    ip_label.pack()
    ip_entry = Entry(window)
    ip_entry.pack()

    # Botão para iniciar a automatização
    start_button = Button(window, text="Iniciar", command=partial(obter_ips))
    start_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()