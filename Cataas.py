from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import ttk

ALLOWED_TAGS=["sleep","jump","fight",'black',"white","cute","siamese"]


def load_image(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        image_data=BytesIO(response.content)
        img=Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def open_new_window():
    tag=tag_combobox.get()
    url_tag=f"http://cataas.com/cat/{tag}" if tag else "http://cataas.com/cat"
    img=load_image(url_tag)

    if img:
        new_window=Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")

        label=Label(new_window,image=img)
        label.image = img
        label.pack()

def exit():
    window.destroy()

window=Tk()
window.title("Cats!")
window.geometry("600x520")

menu_bar=Menu(window)
window.config(menu=menu_bar)

file_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход",command=exit)

tag_label=Label(text="Выбери тег")
tag_label.pack()

tag_combobox=ttk.Combobox(values=ALLOWED_TAGS)
tag_combobox.pack()

load_button=Button(text="Загрузить ро тегу", command=open_new_window)
load_button.pack()

window.mainloop()


