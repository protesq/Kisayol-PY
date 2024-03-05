import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

root = tk.Tk()
root.title("Programlar")

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

def butonlari_gizle():
    button_epic.pack_forget()
    button_steam.pack_forget()

def messagebox_ve_buttonlari_goster():
    messagebox.showinfo("Uyarı !!", "Merhaba nasılsın ?!")
    butonlari_goster()


def butonlari_goster():
    button_steam.pack(pady=10)
    button_epic.pack(pady=10)

# program yolları sizde değişebilir.
button_steam = tk.Button(root, text="Steam", command=lambda: programi_ac("C:/Program Files (x86)/Steam/steam.exe"))
button_epic = tk.Button(root, text="Epic Games", command=lambda: programi_ac("C:/Program Files (x86)/Epic Games/Launcher/Engine/Binaries/Win64/EpicGamesLauncher.exe"))
messagebox_ve_buttonlari_goster()

def programi_ac(program_path):
    subprocess.Popen([program_path])

root.mainloop()
