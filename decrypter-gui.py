from tkinter import *
from tkinter import filedialog

from PIL import Image
from numpy import array
import numpy as np

window = Tk()

def browse():
	filename = filedialog.askopenfilename(filetypes=[("PNG", "*.png")])
	entry.insert(END, filename)

def status(event):
	label2.config(text="Encrypting your message. Please wait....")

def decryption(event):
	img = Image.open(entry.get())
	rows, columns, channels = np.shape(img)
	arr = array(img)

	# function to check a number is even or not
	def is_even(x):
		if(x%2==0):
			return 1

	# decrypting binary message from the RGB values of each pixels
	bmsg = []
	bmsg_chunks = []
	counter = 0
	flag = 0
	for i in range(rows):
		for j in range(columns):
			tmp = arr[i][j]
			if(counter > 7):
				if(any(bmsg_chunks)):
					bmsg.append(bmsg_chunks)
					bmsg_chunks = []
					counter = 0
				else:
					flag = 1
					break

			if(flag == 0):
				if(is_even(int(tmp[0]) +int(tmp[1]) +int(tmp[2]))):
					bmsg_chunks.append(int(1))
				else:
					bmsg_chunks.append(int(0))
				counter += 1
			else:
				break

	# converting binary message in ASCII
	for i in range(int(len(bmsg))):
		bmsg[i] = chr(int("".join(map(str, bmsg[i])), 2))
	msg = "".join(bmsg)
	label2.config(text="Encrypted the message successfully!")
	label3.config(text="Decrypted Message: " + str(msg))



label1 = Label(window, text="Select the image for decrypting: ")
entry = Entry(window)

label2 = Label(window, text="Status: Waiting....")
label3 = Label(window, text="")

label1.grid(row=0, column=0, sticky=E, padx=3, pady=15)
entry.grid(row=0, column=1, sticky=W, ipadx=50, pady=15)

label2.grid(row=2, columnspan=2, sticky=W, padx=3, pady=10)
label3.grid(row=3, columnspan=2, sticky=W, padx=3, pady=5)

button = Button(window, text="Browse", command=browse)
button.grid(row=0, column=1, sticky=E)

button = Button(window, text="Click here to decrypt", fg="red")
button.bind('<ButtonPress-1>', status)
button.bind('<ButtonRelease-1>', decryption)
button.grid(row=1, columnspan=2)

window.title("Text-to-Image Decrypter by !!!! DARKFIST !!!!")
window.geometry("500x160")

window.mainloop()