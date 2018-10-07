from tkinter import *
from tkinter import filedialog

from PIL import Image
from numpy import array
import numpy as np

window = Tk()

def browse():
	filename = filedialog.askopenfilename(filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
	entry2.insert(END, filename)

def status(event):
	label3.config(text="Encrypting your message. Please wait....")

def encrytion(event):
	# taking msg as input and converting it to binary
	# msg = input("Enter the message to encrypt in the image: ")

	msg = entry1.get()
	img = Image.open(entry2.get()) # path of the image to encrypt (with extension)

	bmsg = []
	for i in msg:
		bmsg.append(format(int(ord(i)), '08b'))

	bmsg = "".join(bmsg)

	rows, columns, channels = np.shape(img)
	arr = array(img)

	# function to check a number is even or not
	def is_even(x):
		if(x%2==0):
			return 1

	# converting every pixel of the image into a odd number
	counter = 0
	for i in range(rows):
		for j in range(columns):
			tmp = arr[i][j]
			for k in range(3):
				if counter < (len(bmsg)*3 + 24):
					arr[i][j][k] = tmp[k] + 1 if is_even(tmp[k]) else tmp[k]
					counter += 1

	# encrypting the binary msg in the RGB values of the image by using the algorithm
	counter = 0
	for i in range(rows):
		for j in range(columns):
			tmp = arr[i][j]
			if counter < len(bmsg):
				arr[i][j][2] = (tmp[2] + 1 if int(bmsg[counter]) else tmp[2])
				counter += 1

	# forming and then saving image with encrypted RGB values
	img = Image.fromarray(arr, 'RGB')
	img.save('encrypted.png')
	label3.config(text="Encrypted the message successfully!")

label1 = Label(window, text="Enter the text to be encrypted: ")
entry1 = Entry(window)

label2 = Label(window, text="Select the image for encrypting: ")
entry2 = Entry(window)

label3 = Label(window, text="Status: Waiting....")

label1.grid(row=0, column=0, sticky=E, padx=2, pady=10)
entry1.grid(row=0, column=1, sticky=W, ipadx=50, pady=10)
label2.grid(row=1, column=0, sticky=E, padx=3, pady=10)
entry2.grid(row=1, column=1, sticky=W, ipadx=15, pady=10)
label3.grid(row=3, columnspan=2, sticky=W, padx=3, pady=10)

button = Button(window, text="Browse", command=browse)
button.grid(row=1, column=1, sticky=E)


button = Button(window, text="Click here to encrypt", fg="red")
button.bind('<ButtonPress-1>', status)
button.bind('<ButtonRelease-1>', encrytion)
button.grid(row=2, columnspan=2)

window.title("Text-to-Image Encrypter by !!!! DARKFIST !!!!")
window.geometry("500x160")

window.mainloop()