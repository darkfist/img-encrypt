"""
Algorithm :
Message in converted in binary values.
Binary digit 0 corresponds to an odd RGB value and binary digit 1 corresponds to an even RGB value of the image.
If binary value of the message is 1 then the sum of R, G and B values will be an even integer otherwise it will be odd.
"""

from PIL import Image
from numpy import array
import numpy as np


# taking msg as input and converting it to binary
msg = input("Enter the message to encrypt in the image: ")
bmsg = []
for i in msg:
	bmsg.append(format(int(ord(i)), '08b'))

bmsg = "".join(bmsg)
print("Encrypting.........\nPlease Wait! It may take few minutes.......")


img = Image.open('test.jpg') # path of the image to encrypt (with extension)
rows, columns, channels = np.shape(img)
arr = array(img)

# function to check a number is even or not
def is_even(x):
	if(x%2==0):
		return 1

# converting every pixel of the image into a odd number
for i in range(rows):
	for j in range(columns):
		tmp = arr[i][j]
		for k in range(3):
			arr[i][j][k] = tmp[k] + 1 if is_even(tmp[k]) else tmp[k]

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
print("Done!\nThe image with encrypted message is stored in the same directory.")
