# Calculador da data de nascimento
# Descrição
# dddddd
#
#
#   Historico
#   v1.0 - Versão inicial - 20210130
#
#  (c) 2021 Duarte André

import tkinter as tk
from tkinter import *
import datetime

today = datetime.date.today()


def run():
    name = name_storage.get()
    age = age_storage.get()
    birthday = birthday_storage.get()

    birthday_day, birthday_month = birthday.split("/")
    birthday_day = int(birthday_day)
    birthday_month = int(birthday_month)
    age = int(age)
    if birthday_month < today.month and birthday_day < today.day:
        label = tk.Label(screen, text="")
        label.grid(row=5, column=0)
        birthday_year = today.year - age
        label = tk.Label(screen, text="Hello " + name + " you are " + str(age) + " years old. You were born in " + str(
            birthday_year) + ".")
        label.grid(row=5, column=0)
    elif birthday_month == today.month and birthday_day == today.day:
        label = tk.Label(screen, text="")
        label.grid(row=5, column=0)
        birthday_year = today.year - age
        label = tk.Label(screen, text="Happy birthday " + name + " you are " + str(age) + " years old. You were born in " + str(birthday_year) + ".")
        label.grid(row=5, column=0)
    elif birthday_month > today.month:
        label = tk.Label(screen, text="")
        label.grid(row=5, column=0)
        birthday_year = today.year - 1 - age
        label = tk.Label(screen, text="Hello " + name + " you are " + str(age) + " years old. You were born in " + str(
            birthday_year) + ".")
        label.grid(row=5, column=0)
    else:
        label = tk.Label(screen, text="")
        label.grid(row=5, column=0)
        birthday_year = today.year - age
        label = tk.Label(screen, text="Hello " + name + " you are " + str(age) + " years old. You were born in " + str(
            birthday_year) + ".")
        label.grid(row=5, column=0)


screen = Tk()
screen.title("Birthday Calculator")


first_text = Label(text="Enter your name")
first_text.grid(row=1, column=0)
second_text = tk.Label(text="Enter your age")
second_text.grid(row=2, column=0)
third_text = tk.Label(text="Enter your birthday(dd/mm)")
third_text.grid(row=3, column=0)
click_when_done = Button(text="Click when done", command=run)
click_when_done.grid(row=4, column=0)

name_storage = StringVar()
name = Entry(textvariable=name_storage)
name.grid(row=1, column=1)
age_storage = StringVar()
age = Entry(textvariable=age_storage)
age.grid(row=2, column=1)
birthday_storage = StringVar()
birthday = Entry(textvariable=birthday_storage)
birthday.grid(row=3, column=1)

screen.mainloop()