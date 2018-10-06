# reverse algorithm of encrypter.py for decrypting the secret message from the image.

from PIL import Image
from numpy import array
import numpy as np

img = Image.open('encrypted.png') # path of the encrypted image (with extension)
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
print('The encrypted message in the image : ' + msg)

			