from tkinter import *
from tkinter import ttk

def calcula_imc():
    imc = float(peso.get()) / float(altura.get()) ** 2
    reusltado['text'] = f'O seu imc é {imc}'

root = Tk()
root.title = ('Calculadora de IMC')
root.geometry('250x200')
root.config(bg='#9FD996')

frame = Frame(root, padx=40, pady=40).grid(column=1, row=1)
Label(frame, text='Para saber seu IMC digite os valores abaixo',bg='#9FD996', pady=40).grid(column=1, row=1, columnspan=2)

Label(frame, text='Qual seu peso (Kl)?', bg='#9FD996').grid(column=1, row=2)
peso = Entry(frame)
peso.grid(column=2, row=2)

Label(frame, text='Qual sua Altura (m)?', bg='#9FD996').grid(column=1, row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)

Button(frame, text='Calcular', command=calcula_imc).grid(column=2, row=4)

reusltado = Label(frame, bg='#9FD996')
reusltado.grid(column=1, row=5, columnspan=2)
root.mainloop()
