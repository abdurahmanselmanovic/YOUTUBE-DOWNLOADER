from cProfile import label
from cgitb import text
import imp
import tkinter as tk
from tkinter import *
from tkinter.tix import COLUMN
from pytube import YouTube
from tkinter import filedialog, messagebox


def createWidgets():
    link_label = label(root, text="Youtube URL:  ", bg="#E8D579")
    link_label.grid(row=1, column=1, pady=5, padx=5)


root = tk.Tk()

root.geometry('600x120')
root.resizable(False, False)
root.title("Youtube Downloader")
root.config(background="#000000")

createWidgets()

root.mainloop()
