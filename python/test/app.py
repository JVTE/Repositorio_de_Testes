import tkinter as tk
from tkinter import messagebox
import pandas as pd

class Estoque:
    def __init__(self):
        self.estoque = {}

    def adicionar_item(self, item, quantidade):
        if item in self.estoque:
            self.estoque[item] += quantidade
        else:
            self.estoque[item] = quantidade

    def remover_item(self, item, quantidade):
        if item in self.estoque:
            if self.estoque[item] >= quantidade:
                self.estoque[item] -= quantidade
                if self.estoque[item] == 0:
                    del self.estoque[item]
            else:
                messagebox.showinfo("Erro", "Quantidade insuficiente no estoque.")
        else:
            messagebox.showinfo("Erro", "Item não encontrado no estoque.")

    def exibir_estoque(self):
        estoque_str = "Estoque:\n"
        for item, quantidade in self.estoque.items():
            estoque_str += f"{item}: {quantidade}\n"
        messagebox.showinfo("Estoque", estoque_str)

    def exportar_para_excel(self):
        df = pd.DataFrame.from_dict(self.estoque, orient='index', columns=['Quantidade'])
        df.index.name = 'Item'
        df.reset_index(inplace=True)
        df.to_excel('estoque.xlsx', index=False)

def adicionar_item():
    item = entry_item.get()
    quantidade = int(entry_quantidade.get())
    estoque.adicionar_item(item, quantidade)
    messagebox.showinfo("Sucesso", "Item adicionado ao estoque.")
    entry_item.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

def remover_item():
    item = entry_item.get()
    quantidade = int(entry_quantidade.get())
    estoque.remover_item(item, quantidade)
    messagebox.showinfo("Sucesso", "Item removido do estoque.")
    entry_item.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

def exibir_estoque():
    estoque.exibir_estoque()

def exportar_para_excel():
    estoque.exportar_para_excel()
    messagebox.showinfo("Sucesso", "Dados exportados para o arquivo estoque.xlsx.")

# Criar a janela principal
window = tk.Tk()
window.title("Sistema de Estoque")

# Criar widgets
label_item = tk.Label(window, text="Item:")
label_item.pack()
entry_item = tk.Entry(window)
entry_item.pack()

label_quantidade = tk.Label(window, text="Quantidade:")
label_quantidade.pack()
entry_quantidade = tk.Entry(window)
entry_quantidade.pack()

btn_adicionar = tk.Button(window, text="Adicionar", command=adicionar_item)
btn_adicionar.pack()

btn_remover = tk.Button(window, text="Remover", command=remover_item)
btn_remover.pack()

btn_exibir = tk.Button(window, text="Exibir Estoque", command=exibir_estoque)
btn_exibir.pack()

btn_exportar = tk.Button(window, text="Exportar para Excel", command=exportar_para_excel)
btn_exportar.pack()

# Criar instância do estoque
estoque = Estoque()

# Iniciar o loop principal da interface gráfica
window.mainloop()