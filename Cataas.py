from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from bottle import response
from gevent.testing.travis import command
from pygame.examples.cursors import image


def load_image(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        image_data=BytesIO(response.content)
        img=image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

def exit():
    window.destroy()

window=Tk()
window.title("Cats!")
window.geometry("600x520")

label=Label()
label.pack()

# update_button=Button(text="Обновить", command=set_image)
# update_button.pack()

menu_bar=menu(window)
window.config(menu=menu_bar)

fail_menu=menu(menu_bar, tearoff=0)
menu_bar.add_coscade(label="Файл", menu=fail_menu)
fail_menu.add_command(label="Загрузить фото", command=set_image)
fale_menu.add_separator()
fail_menu.add_command(label="Выход",command=exit)

url="https://cataas.com/cat"

set_image()

window.mainloop()


