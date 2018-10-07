#!/usr/bin/env python3

'''-------------------------------------------------------------
* Pixel Wise Image Modification cum Encryption Utility.
* (Embeds String data into an image.)
* 07OCT2018
* Authors: Mohamed S. Haque <ubdussamad@gmail.com> , Nishant Ranjan <nishantranjan1998@gmail.com>
* Primarily Built around Python3.x

* This program is intended to work with many methods of
* storing data using image manipulation and is not just
* supposed to store text but any kind of data may it be
* another image or an octet stream application into an image. 
*
* This program currently utilizes an even odd scheme to store/read binary data into/from an image.
*
* Working Principle:
* Reads a Portable Network Graphic or JPEG (.png|.jpg) and converts it to a 2D array.
* An odd color value represents binary 0 and an even color value represents binary 1.
* Primarily color values in the image's matrix are converted into odd integer by adding
* integer value 1 if the color value is even else 0 if the color value is already odd.
*
* Scheme: Odd if 0 , even if 1
------------------------------------------------------------------------------------------'''

from PIL import Image
import numpy as np
arr = np.array(Image.open('Desktop/test.jpg')) #Converting the Image into a 2D array
x,y,z  = np.shape(arr) #Reading the dimensions of the array to determine the storage.
arr |= 1
print("The amount of data you can store in this image is: %d kiBs"%((x*y*z)/(1024*8)))
z = input("Enter the string:") # Scanning the string to be stored.
long_array = [] #Array containing the binary values.
for i in z:long_array += list(map(int,list(format(ord(i), '#010b')[2:]))) #Storing the characters in binary form (ASCII)
arr.ravel()[:len(long_array)] += np.array(long_array, arr.dtype) #Adds one if there is a one else adds zero hence making even odd pairs. 
image = Image.fromarray(arr) #Recreating the image from the modified array.
image.show() #Displaying the picture.
image.save("secret.png") #Saving the Image for transfer or future use. Note: The output picture must be in PNG format
#As other formats try to compress the data corrupting the encoded data within the image.
