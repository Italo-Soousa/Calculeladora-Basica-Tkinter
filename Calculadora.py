import tkinter as tk


janela = tk.Tk()
janela.title("Calculadora")
janela.resizable(width=True, height=True)

padx = 15
pady = 15

termo = 1

# Campo que coleta o primeiro parametro a ser calculado
label1 = tk.Label(janela, text="Primeiro parametro:")
label1.grid(row=1, column= 0, columnspan=2, padx= padx, pady = pady)
entry1 = tk.Entry(janela)
entry1.grid(row=1, column= 2, columnspan=3, padx= padx, pady = pady)

# Identificador da operacao
OperadorVar = tk.StringVar()
operador = tk.Label(janela, state=tk.ACTIVE, textvariable= OperadorVar)
operador.grid(row=2, column=0, columnspan=1, padx=padx, pady=pady)

# Campo que coleta o segundo paramentro a ser calculado
label2 = tk.Label(janela, text="Segundo parametro:")
label2.grid(row=3, column= 0, columnspan=2,padx= padx, pady = pady)
entry2 = tk.Entry(janela)
entry2.grid(row=3, column= 2,columnspan=3, padx= padx, pady = pady)

# Campo que mostra o resultado
label2 = tk.Label(janela, text="Resultado:")
label2.grid(row= 4, column= 0,columnspan= 2, padx= padx, pady = pady)
resultado = tk.Entry(janela)
resultado.grid(row= 4, column= 2,columnspan=3, padx= padx, pady = pady)


# Grid com os botões e os númenos ==============================================================================================================

# Primeira coluna
botao_7 = tk.Button(janela, text=7, width=4, command=lambda: clicarBotao(7))
botao_7.grid(row=5, column= 0, padx= padx, pady = pady)

botao_8 = tk.Button(janela, text=8, width=4, command=lambda: clicarBotao(8))
botao_8.grid(row=5, column= 1, padx= padx, pady = pady)

botao_9 = tk.Button(janela, text=9, width=4, command=lambda: clicarBotao(9))
botao_9.grid(row=5, column= 2, padx= padx, pady = pady)

botao_multiplicacao = tk.Button(janela, text= "x", width=4, command=lambda: clicarOperador("x"))
botao_multiplicacao.grid(row=5, column= 3, padx= padx, pady = pady)

botao_limpar = tk.Button(janela, text="Limpar", width=4, command= lambda: limparCampos())
botao_limpar.grid(row= 5, column= 4, padx= padx, pady = pady)

botao_decimal = tk.Button(janela, text=".", width=4, command=lambda: clicarBotao("."))
botao_decimal.grid(row= 6, column= 4, padx= padx, pady= pady)

# Segunda coluna
botao_4 = tk.Button(janela, text=4, width=4, command=lambda: clicarBotao(4))
botao_4.grid(row= 6, column= 0, padx= padx, pady = pady)

botao_5 = tk.Button(janela, text=5, width=4, command=lambda: clicarBotao(5))
botao_5.grid(row= 6, column= 1, padx= padx, pady = pady)

botao_6 = tk.Button(janela, text=6, width=4, command=lambda: clicarBotao(6))
botao_6.grid(row= 6, column= 2, padx= padx, pady = pady)

botao_subtracao = tk.Button(janela, text="-", width=4, command=lambda: clicarOperador("-"))
botao_subtracao.grid(row= 6, column= 3, padx= padx, pady = pady)


# Quarta coluna
botao_1 = tk.Button(janela, text=1, width=4, command=lambda: clicarBotao(1))
botao_1.grid(row= 7, column= 0, padx= padx, pady = pady)

botao_2 = tk.Button(janela, text=2, width=4, command=lambda: clicarBotao(2))
botao_2.grid(row= 7, column= 1, padx= padx, pady = pady)

botao_3 = tk.Button(janela, text=3, width=4, command=lambda: clicarBotao(3))
botao_3.grid(row= 7, column= 2, padx= padx, pady = pady)

botao_soma = tk.Button(janela, text="+", width=4, command=lambda: clicarOperador("+"))
botao_soma.grid(row= 7, column= 3, padx= padx, pady = pady)

# Quinta linha
botao_0 = tk.Button(janela, text=0, width=4, command=lambda: clicarBotao(0))
botao_0.grid(row= 8, column= 1, padx= padx, pady = pady)

botao_divisao = tk.Button(janela, text= "/", width=4, command=lambda: clicarOperador("/"))
botao_divisao.grid(row= 8, column= 3, padx= padx, pady = pady)

botao_igual = tk.Button(janela, text="=", width=4, command=lambda: calcular())
botao_igual.grid(row= 8, column= 4, padx= padx, pady = pady)

def clicarBotao(numero):
    # Atualizar o valor no campo de texto do Termo1 ou Termo2
    if termo == 1:
        numeroDigitado =entry1.get()
        entry1.delete(0, tk.END)
        entry1.insert(0, numeroDigitado + str(numero))
    elif termo == 2:
        numeroDigitado = entry2.get()
        entry2.delete(0, tk.END)
        entry2.insert(0, numeroDigitado + str(numero))

def clicarOperador(operador):
    # Declarando como global para que a variável tenha valor
    global termo
    OperadorVar.set(operador)
    termo = 2

def calcular():
    global tipoDeOperacao
    global resultado
    if entry1 != "" and entry2 != "" and OperadorVar != "":
        termo1 = float(entry1.get())
        termo2 = float(entry2.get())
        operador = OperadorVar.get()

        if operador == "/":
            resultado_final = termo1 / termo2
        elif operador == "x":
            resultado_final = termo1 * termo2
        elif operador == "+":
            resultado_final = termo1 + termo2
        elif operador == "-":
            resultado_final = termo1 - termo2


    resultado.delete(0, tk.END)
    resultado.insert(0, str(resultado_final))

def limparCampos():
    global termo
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    resultado.delete(0, tk.END)
    OperadorVar.set("")
    termo = 1

janela.mainloop()