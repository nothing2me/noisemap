import random
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def displayPhoto(mapArray, root):
    length, height = len(mapArray[0]), len(mapArray)  # Corrected length and height
    image_data = np.array(mapArray, dtype=np.uint8)  # Corrected array reshaping
    img = Image.fromarray(image_data)  # No need to specify mode here

    img = ImageTk.PhotoImage(img)

    canvas = Canvas(root, width=length, height=height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=img)
    root.title("Map Generator")
    root.mainloop()

def generate_random_values(chance):
    chance = chance / 10# 70% chance of getting 1 for variable 1
    value1 = 255 if random.random() < chance else 0
    return value1

def createMap(length, height,chance):
    from random import randint
    mapArray = [[0 for _ in range(height)] for _ in range(length)]
    for i in range(length):
        for j in range(height):
            mapArray[i][j] = generate_random_values(chance)
    return mapArray

def compileMap(length, height, chance):
    mapArray = createMap(length, height, chance)
    root = Tk()
    displayPhoto(mapArray, root)

def displayUI():
    win = Tk()
    win.geometry("300x220")
    win.title("Map Generator")
    def getData():
        length = int(getLength.get())
        height = int(getHeight.get())
        chance = float(getChance.get())
        # Destroy the original window
        win.destroy()
        # Call main to complie map with input values
        compileMap(height, length, chance)

    # Create spacing
    space_label = Label(win, text="", font=("Monospace", 2))
    space_label.pack()

    # Display entry label for length
    label = Label(win, text="Enter Length:", font=("Monospace", 12))
    label.pack()
    getLength = Entry(win, width=40)
    getLength.focus_set()
    getLength.pack()

    # Create spacing
    space_label.pack()

    label = Label(win, text="Enter Height:", font=("Monospace", 12))
    label.pack()

    # Display entry label for height
    getHeight = Entry(win, width=40)
    getHeight.focus_set()
    getHeight.pack()

    space_label.pack()

    label = Label(win, text="Enter Chance:", font=("Monospace", 12))
    label.pack()

    # Display entry label for height
    getChance = Entry(win, width=40)
    getChance.focus_set()
    getChance.pack()

    # Display button to enter in values from entry
    ttk.Button(win, text="Enter", width=20, command=getData).pack(pady=20)

    # Call to loop
    win.mainloop()

if __name__ == '__main__':
    displayUI()
