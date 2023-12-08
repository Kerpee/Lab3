from tkinter import Tk, Canvas, PhotoImage, Label, Button
from random import choice
from random import sample
from pygame import mixer
SIZE_OF_W_X = 450
SIZE_OF_W_Y = 600


def generator(label):
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
    res = key[:-1]
    label.configure(text=f"Ваш ключ: {res}")


window = Tk()
mixer.init()
mixer.music.load('sound.wav')
mixer.music.play(-1)
mixer.music.set_volume(0.05)
window.geometry(f'{SIZE_OF_W_X}x{SIZE_OF_W_Y}')
c = Canvas(window, bg="green", height=1920, width=1080)
file = PhotoImage(file="BioWall.png")
background_label = Label(window, image=file)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
button = Button(window, text="Сгенерировать ключ", command=lambda: generator(lbl), bg='#c7e2eb')
lbl = Label(window, text='Генератор ключей', bg="#feffeb")
lbl.place(x=170, y=335)
button.place(x=170, y=295)
window.wm_attributes("-transparentcolor", "white")
c.pack()
window.title("Генератор ключей")
window.mainloop()
