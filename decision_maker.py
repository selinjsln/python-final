import tkinter as tk
from tkinter import ttk
import os

data_directory = r"chatbot\datanew"
list_file = r"datanew/all.txt"


def load_destinations_to_listbox(listbox, category):
    listbox.delete(0, tk.END)
    file_path = os.path.join(data_directory, f"{category.lower()}.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = file.readlines()
            for i in data:
                listbox.insert(tk.END, i.strip())


def on_checkbox1_clicked():
    if checkbox1_var.get() == 1:
        load_destinations_to_listbox(listbox1, "all")
    else:
        listbox1.delete(0, tk.END)
    update_combo_values()


def update_combo_values():
    if checkbox2_var.get() == 1:
        combo["values"] = [
            "Danau",
            "Desa",
            "Family",
            "Fauna",
            "Kebun",
            "Monumen",
            "Museum",
            "Pasar",
            "Pura",
            "Sawah",
            "Sunrise",
            "Sunset",
        ]
        combo_var.set("Pilih Kategori")
    else:
        combo["values"] = ["Pilih Kategori"]
        combo_var.set("Pilih Kategori")
        listbox2.delete(0, tk.END)


def on_selected_button_clicked():
    selected_category = combo_var.get()
    if selected_category != "Pilih Kategori":
        load_destinations_to_listbox(listbox2, selected_category)


root = tk.Tk()
root.title("Decision Maker")

root.geometry("680x400")

label_frame = tk.LabelFrame(root)
label_frame.place(x=10, y=15, width=660, height=350)

label = tk.Label(root, text="Selamat Datang!")
label.place(x=300, y=5)

label2 = tk.Label(root, text="Ayo tentukan destinasi wisata di Pulau Bali sesuai keinginanmu")
label2.place(x=175, y=25)

checkbox1_var = tk.IntVar()
checkbox1 = tk.Checkbutton(
    root,
    text="Daftar Seluruh Wisata",
    variable=checkbox1_var,
    command=on_checkbox1_clicked
)
checkbox1.place(x=13, y=55)

checkbox2_var = tk.IntVar()
checkbox2 = tk.Checkbutton(
    root,
    text="Pilih Wisata Berdasarkan Kategori",
    variable=checkbox2_var,
    command=on_checkbox1_clicked
)
checkbox2.place(x=309, y=55)

listbox1 = tk.Listbox(root, width=47, height=16)
listbox1.place(x=20, y=85)

listbox2 = tk.Listbox(root, width=56, height=11)
listbox2.place(x=315, y=120)

combo_var = tk.StringVar()
combo = ttk.Combobox(
    root, width=40, state="readonly", values=["Pilih Kategori"], textvariable=combo_var
)
combo.place(x=315, y=85)

button = ttk.Button(root, text="Select", command=on_selected_button_clicked)
button.place(x=580, y=83)

root.mainloop()