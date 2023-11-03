from tkinter import *
from random import choice
from random import sample
from pygame import mixer


def clicked():
    key = ''
    symbols = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789"
    for i in range(3):
        part_of_key = ''
        for j in range(3):
            part_of_key += choice(symbols)
            part_of_key += choice(numbers)
        part_of_key_list = list(part_of_key[:-1])
        part_of_key_random = sample(part_of_key_list, len(part_of_key_list))
        part_of_key = ''.join(part_of_key_random)
        key += part_of_key+"-"
    print(key[:-1])
    res = key[:-1]
    lbl.configure(text=f"Ваш ключ:{res}")


window = Tk()
mixer.init()
mixer.music.load('sound8bit.wav')
mixer.music.play(-1)
window.geometry('450x600')
c = Canvas(window, bg="green", height=1920, width=1080)
file = PhotoImage(file="BioWall.png")
background_label = Label(window, image=file)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
button = Button(window, text="Сгенерировать ключ", command=clicked, bg='#c7e2eb')
lbl = Label(window, text='Генератор ключей', bg="#feffeb")
lbl.place(x=170, y=335)
button.place(x=170, y=295)
window.wm_attributes("-transparentcolor", "white")
c.pack()
window.title("Генератор ключей")
window.mainloop()
