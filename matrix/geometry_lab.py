from mat import Mat
from matutil import *
import math

## Task 1
def identity(labels = {'x','y','u'}):
		'''
		In case you have never seen this notation for a parameter before,
		the way it works is that identity() now defaults to having labels 
		equal to {'x','y','u'}.	 So you should write your procedure as if 
		it were defined 'def identity(labels):'.	However, if you want the labels of 
		your identity matrix to be {'x','y','u'}, you can just call 
		identity().	 Additionally, if you want {'r','g','b'}, or another set, to be the
		labels of your matrix, you can call identity({'r','g','b'}).	
		'''
		return Mat((labels,labels), {(l,l):1 for l in labels})

## Task 2
def translation(x,y):
		'''
		Input:	An x and y value by which to translate an image.
		Output:	 Corresponding 3x3 translation matrix.
		'''
		T=identity()
		T[('x','u')]=x
		T[('y','u')]=y
		return T

## Task 3
def scale(a, b):
		'''
		Input:	Scaling parameters for the x and y direction.
		Output:	 Corresponding 3x3 scaling matrix.
		'''
		T=identity()
		T[('x','x')]=a
		T[('y','y')]=b
		return T

## Task 4
def rotation(angle):
		'''
		Input:	An angle in radians to rotate an image.
		Output:	 Corresponding 3x3 rotation matrix.
		Note that the math module is imported.
		'''
		T=identity()
		T[('x','x')]=math.cos(angle)
		T[('y','y')]=math.cos(angle)
		T[('x','y')]=-math.sin(angle)
		T[('y','x')]=math.sin(angle)
		return T		

## Task 5
def rotate_about(x,y,angle):
		'''
		Input:	An x and y coordinate to rotate about, and an angle
		in radians to rotate about.
		Output:	 Corresponding 3x3 rotation matrix.
		It might be helpful to use procedures you already wrote.
		'''
		return translation(x,y)*rotation(angle)*translation(-x,-y)

## Task 6
def reflect_y():
		'''
		Input:	None.
		Output:	 3x3 Y-reflection matrix.
		'''
		T=identity()
		T[('x','x')]=-1
		return T

## Task 7
def reflect_x():
		'''
		Inpute:	 None.
		Output:	 3x3 X-reflection matrix.
		'''
		T=identity()
		T[('y','y')]=-1
		return T
		
## Task 8		 
def scale_color(scale_r,scale_g,scale_b):
		'''
		Input:	3 scaling parameters for the colors of the image.
		Output:	 Corresponding 3x3 color scaling matrix.
		'''
		T=identity({'r','g','b'})
		T[('r','r')]=scale_r
		T[('g','g')]=scale_g
		T[('b','b')]=scale_b
		return T

## Task 9
def grayscale():
		'''
		Input: None
		Output: 3x3 greyscale matrix.
		'''
		T=Mat(({'r','g','b'},{'r','g','b'}),{})
		(T[('r','r')],T[('r','g')],T[('r','b')])=(77/256,151/256,28/256)
		(T[('g','r')],T[('g','g')],T[('g','b')])=(77/256,151/256,28/256)
		(T[('b','r')],T[('b','g')],T[('b','b')])=(77/256,151/256,28/256)
		return T

## Task 10
def reflect_about(p1,p2):
		'''
		Input: 2 points that define a line to reflect about.
		Output:	 Corresponding 3x3 reflect about matrix.
		'''
		pass


