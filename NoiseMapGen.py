import random
import tkinter
import numpy as np
from tkinter import *
from tkinter import ttk
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageTk


# Display the image to a new window
def displayPhoto(mapArray, root):
    # Original logic to get image data
    length, height = len(mapArray[0]), len(mapArray)
    image_data = np.array(mapArray, dtype=np.uint8)
    img = Image.fromarray(image_data)

    # Resize image to 800x800 using resize() method
    resized_img = img.resize((800, 800), Image.BICUBIC)  # Resize with bicubic interpolation

    # Convert to PhotoImage format
    resized_img = ImageTk.PhotoImage(resized_img)

    # Create canvas and display image
    canvas = Canvas(root, width=800, height=800)  # Set canvas size to 800x800
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=resized_img)
    root.title("Map Generator")
    root.mainloop()

# Apply a gaussian filter to the map
def applyGaussianFilter(mapArray, gaussSigma):
    mapArray = gaussian_filter(mapArray, sigma=gaussSigma, mode='reflect')
    return mapArray

# Generate a random value based on the given chance
def generate_random_values(chance):
    chance = chance / 10  # Convert to percentage from user entered whole number
    value1 = 255 if random.random() < chance else 0
    return value1


# Assemble the map
def createMap(length, height, chance):
    from random import randint
    mapArray = [[0 for _ in range(height)] for _ in range(length)]
    for i in range(length):
        for j in range(height):
            mapArray[i][j] = generate_random_values(chance)
    return mapArray


# Compile the map and apply conditional filters
def compileMap(length, height, chance, gaussianBlur, gaussSigma):
    # Create the inital map
    mapArray = createMap(length, height, chance)
    # Gaussian Filter
    if gaussianBlur:
        mapArray = applyGaussianFilter(mapArray, gaussSigma)
    root = Tk()
    displayPhoto(mapArray, root)

# Display the UI gather needed entries
def displayUI():
    win = Tk()
    win.geometry("300x450")
    win.title("Map Generator")

    gaussianBlur = BooleanVar()
    gaussianBlur.set(False)
    gauss_sigma = 3

    def getData():
        # Initialize values from entry field
        global gauss_sigma  # Declare gauss_sigma as global
        length_entry = getLength.get()
        height_entry = getHeight.get()
        chance_entry = getChance.get()
        gauss_blur = gaussianBlur.get()

        print("Gaussian Blur checkbox state:", gaussianBlur.get())
        if gauss_blur:
            gauss_sigma_entry = gaussSigma.get()
            if gauss_sigma_entry:
                gauss_sigma = int(gauss_sigma_entry)
            else:
                gauss_sigma = 3
        else:
            gauss_sigma = 3  # Default value if Gaussian blur checkbox is unchecked

        # Validate input values
        if not length_entry or not height_entry or not chance_entry:
            # Display error message or provide a default value
            print("Please provide values for Length, Height, and Chance.")
            return

        # Sanitize fields to desired types
        length = int(length_entry)
        height = int(height_entry)
        chance = float(chance_entry)

        # Destroy the original window
        win.destroy()
        # Call main to compile map with input values
        compileMap(height, length, chance, gauss_blur, gauss_sigma)

    space_label = Label(win, text="", font=("Monospace", 2))
    space_label.pack()
    # Gaussian blur checkbox
    gaussBlur = tkinter.Checkbutton(win, text='Gaussian Blur', variable=gaussianBlur, onvalue=1, offvalue=0, command="")
    gaussBlur.pack()

    # Sigma value entry field
    label = Label(win, text="Sigma", font=("Monospace", 9))
    label.pack()
    gaussSigma = Entry(win, width=10)
    gaussSigma.focus_set()
    gaussSigma.pack()

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
