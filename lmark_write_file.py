path_depth="/Users/normand/Documents/Processing/communicate/depth.jpg"
path_color="/Users/normand/Documents/Processing/communicate/color.jpg"
from PIL import Image
import numpy as np
import time

#Some functions that I wrote to check the environment with the Kinect, but here are not used.

def paint(x,y,imarray):
	for i in range(-5,5):
		for j in range(-5,5):
			imarray[y+i][x+j][0]=200
			imarray[y+i][x+j][1]=0
			imarray[y+i][x+j][2]=0

def free_way(y,imarray):
	for x in range(0,640):
		for s in range(-20,20):
			if imarray[y][x+s][0]<50:
				break
			return x


def is_free(y,imarray):
	
	for s in range(-30,30):
		if imarray[y][300+s][0]>120:
			return False
	return True

def free_right(y,imarray):

	for s in range(-30,30):
		if imarray[y][400+s][0]>120:
			return False
	return True	

def free_left(y,imarray):

	for s in range(-30,30):
		if imarray[y][200+s][0]>120:
			return False
	return True	


#Analyzes the color image and tries to detect a red landmark, 
#storing in a file the x coordinate of the weighted center of the red pixels.



i=0

img = Image.open(path_color)
red, green, blue = img.split()
red=np.array(red)
green=np.array(green)
blue=np.array(blue)

print(len(red))
new=np.array(red)
nn=np.array(new)
tot_x=0
tot_y=0
n_x=0
n_y=0
for k in range(len(red)):
	for l in range(len(red[0])):
		if red[k][l]>100 and green[k][l]<60 and blue[k][l]<60:
			new[k][l]=200
			tot_x+=l
			tot_y+=k
			n_x+=1
			n_y+=1
		else:
			new[k][l]=0
center_x=tot_x/n_x

with open("/Users/normand/Desktop/center.txt", 'w') as file:
	file.write(str(int((center_x-320))))

print(tot_x/n_x)
print(tot_y/n_y)


new=Image.fromarray(new)
new.show()
"""
a = Image.open(path_color)
a = np.array(a)
a[:,:,1] *=0
a[:,:,2] *=0
a = Image.fromarray(a)
"""
red=Image.fromarray(red)
green=Image.fromarray(green)
blue=Image.fromarray(blue)

red.show()
green.show()
blue.show()

#Loop to update the file with the new center coordinates of the red landmark.

while(i<1000):

	i+=1
	try:

		

		img = Image.open(path_color)
		red, green, blue = img.split()
		red=np.array(red)
		green=np.array(green)
		blue=np.array(blue)

		print(len(red))
		new=np.array(red)
		nn=np.array(new)
		tot_x=0
		tot_y=0
		n_x=0
		n_y=0
		for k in range(len(red)):
			for l in range(len(red[0])):
				if red[k][l]>100 and green[k][l]<60 and blue[k][l]<60:
					new[k][l]=200
					tot_x+=l
					tot_y+=k
					n_x+=1
					n_y+=1
				else:
					new[k][l]=0
		center_x=tot_x/n_x

		with open("/Users/normand/Desktop/center.txt", 'w') as file:
			file.write(str(int((center_x-320)*0.8)))

		print(tot_x/n_x)
		print(tot_y/n_y)


		new=Image.fromarray(new)


		#new.show()
		"""
		
		"""
		red=Image.fromarray(red)
		green=Image.fromarray(green)
		blue=Image.fromarray(blue)

	
	except Exception as e:

		print("skip")
		print(e)
		time.sleep(0.5)

	