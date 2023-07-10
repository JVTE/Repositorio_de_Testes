import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import locale

class BancoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicativo de Banco")
        
        self.saldo = 0
        
        self.saldo_label = tk.Label(self, text="Saldo: {}".format(self.formatar_moeda(self.saldo)))
        self.saldo_label.pack(pady=10)
        
        self.deposito_button = tk.Button(self, text="Depositar", command=self.depositar)
        self.deposito_button.pack(pady=5)
        
        self.saque_button = tk.Button(self, text="Sacar", command=self.sacar)
        self.saque_button.pack(pady=5)
        
        self.sair_button = tk.Button(self, text="Sair", command=self.sair)
        self.sair_button.pack(pady=5)
        
        self.configurar_saldo_inicial()
    
    def configurar_saldo_inicial(self):
        saldo_inicial = float(self.askstring("Saldo Inicial", "Informe o saldo inicial:"))
        self.saldo = saldo_inicial
        self.saldo_label.config(text="Saldo: {}".format(self.formatar_moeda(self.saldo)))
    
    def askstring(self, title, prompt):
        self.withdraw()
        valor = simpledialog.askstring(title, prompt)
        self.deiconify()
        return valor
    
    def depositar(self):
        deposito = float(self.askstring("Depósito", "Informe o valor do depósito:"))
        
        if deposito > 0:
            self.saldo += deposito
            self.saldo_label.config(text="Saldo: {}".format(self.formatar_moeda(self.saldo)))
            messagebox.showinfo("Depósito", "Depósito realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Valor inválido de depósito.")
    
    def sacar(self):
        saque = float(self.askstring("Saque", "Informe o valor do saque:"))
        
        if saque > 0:
            if saque <= self.saldo:
                self.saldo -= saque
                self.saldo_label.config(text="Saldo: {}".format(self.formatar_moeda(self.saldo)))
                messagebox.showinfo("Saque", "Saque realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente.")
        else:
            messagebox.showerror("Erro", "Valor inválido de saque.")
    
    def sair(self):
        if messagebox.askyesno("Sair", "Deseja sair do aplicativo?"):
            self.destroy()
    
    def formatar_moeda(self, valor):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(valor, grouping=True)

if __name__ == "__main__":
    app = BancoApp()
    app.mainloop()