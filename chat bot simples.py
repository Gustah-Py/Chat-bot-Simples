import tkinter as tk
from tkinter import scrolledtext

# Base de perguntas e respostas
respostas = {
    "ola": "ola,como vai?.",
    "tudo bem??": "Sim","e voce?"
    "voce é um bot simples?": "sim,sou um bot simples",
    "que horas são?": "agora são 09:00.",
    "qual seu nome?": "SympleBot."
}

# Função que lida com a pergunta
def responder():
    pergunta = entrada.get().strip().lower()
    entrada.delete(0, tk.END)

    if pergunta == "sair":
        janela.quit()

    resposta = respostas.get(pergunta, "Desculpe, não entendi sua pergunta. 😕")
    
    historico.configure(state='normal')
    historico.insert(tk.END, f"Você: {pergunta}\nBot: {resposta}\n\n")
    historico.configure(state='disabled')
    historico.see(tk.END)

# Criar janela
janela = tk.Tk()
janela.title("🤖 SympleBot")
janela.geometry("400x400")

# Histórico de mensagens
historico = scrolledtext.ScrolledText(janela, wrap=tk.WORD, state='disabled')
historico.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack(padx=10, pady=5, fill=tk.X)
entrada.focus()

# Botão de enviar
botao = tk.Button(janela, text="Enviar", command=responder)
botao.pack(padx=10, pady=5)

# Permitir uso da tecla Enter
janela.bind('<Return>', lambda event: responder())

# Rodar janela
janela.mainloop()