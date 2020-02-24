#HW4_PLOT_2018033.py
#Date: 08-11-2018

#Name: DUSHYANT PANCHAL
#Roll No.: 2018033
#Section: A    Group: 1

import matplotlib.pyplot as plt  #For plotting
from math import cos,sin,pi      #For calculations

class Matrix:	#Defining class for Matrix objects
	mat=list()	#Data member to store matrix as a list
	m=0		#No. of rows
	n=0		#No. of columns

	def __init__(self,mat):	#Constructor
		self.mat=mat
		self.m=len(self.mat)
		self.n=len(self.mat[0])
	
	def __str__(self):	#For printing
		string=''
		for i in self.mat:
			for j in i:
				string += str(j) + ' '
			string+='\n'
		return string
	
	def __mul__(self,other):	#Multiplication operation
		if(self.n!=other.m): #If they can't be multiplied, return None
			return None
		else:
			new=list()
			for i in range(self.m):
				temp=list()
				for j in range(other.n):
					sum=0
					for k in range(self.n):
						sum+=self.mat[i][k]*other.mat[k][j]
					temp.append(sum)
				new.append(temp)
			return Matrix(new)

class ellipse:	#Ellipse class
	x=0	#x-coordinate of center
	y=0	#y-coordinate of center
	a=0 #x - Radius
	b=0 #y - Radius

	xL=list()
	yL=list()

	def __init__(self,x,y,r):	#Constuctor
		self.x=x
		self.y=y
		self.a=r
		self.b=r
		
		rad=0		#Generating plottable points
		a=list()
		b=list()
		while(rad<=2*pi):
			a.append(x+r*cos(rad))
			b.append(y+r*sin(rad))
			rad+=0.01

		self.n=len(a)
		self.xL=a
		self.yL=b
	
	def __str__(self):	#Implementing print
		return str(self.x)+' '+str(self.y)+' '+str(self.a)+' '+str(self.b)

	def rotate(self,theta):	#Method to perform rotation by theta degrees
		theta=theta*pi/180
		rot=Matrix([[cos(theta),sin(-theta)],[sin(theta),cos(theta)]])
		trans=rot*Matrix([self.xL,self.yL])
		self.xL=trans.mat[0]
		self.yL=trans.mat[1]
		
	def scale(self,a,b):	#Method to perform scaling
		sca=Matrix([[a,0],[0,b]])
		trans=sca*Matrix([self.xL,self.yL])
		self.xL=trans.mat[0]
		self.yL=trans.mat[1]
		self.a*=a
		self.b*=b

	def translate(self,a,b):	#Method to perform translation
		tran=Matrix([[1,0,a],[0,1,b],[0,0,1]])
		trans=tran*Matrix([self.xL,self.yL,[1]*(self.n)])
		self.xL=trans.mat[0]
		self.yL=trans.mat[1]
		self.x+=a
		self.y+=b

	def plot(self,clear=False):	#Method to plot the polygon using matplotlib module
		if(clear):
			plt.gcf().clear()
		plt.plot(self.xL,self.yL)
		plt.pause(0.0001)

class polygon:	#Polygon class
	x=list()	#List of x-coordinates
	y=list()	#List of y-coordinates
	n=0		#stores n for n-sided polygon

	def __init__(self,x,y):	#Constructor
		self.x=x
		self.y=y
		self.n=len(x)
		self.x.append(self.x[0])
		self.y.append(self.y[0])

	def __str__(self):	#Implementing print
		return str(self.x[:-1])+','+str(self.y[:-1])

	def rotate(self,theta):	#Method to perform rotation by theta degrees
		theta=theta*pi/180
		rot=Matrix([[cos(theta),sin(-theta)],[sin(theta),cos(theta)]])
		trans=rot*Matrix([self.x,self.y])
		self.x=trans.mat[0]
		self.y=trans.mat[1]
		
	def scale(self,a,b):	#Method to perform scaling
		sca=Matrix([[a,0],[0,b]])
		trans=sca*Matrix([self.x,self.y])
		self.x=trans.mat[0]
		self.y=trans.mat[1]

	def translate(self,a,b):	#Method to perform translation
		tran=Matrix([[1,0,a],[0,1,b],[0,0,1]])
		trans=tran*Matrix([self.x,self.y,[1]*((self.n)+1)])
		self.x=trans.mat[0]
		self.y=trans.mat[1]

	def plot(self,clear=False):	#Method to plot the polygon using matplotlib module
		if(clear):
			plt.gcf().clear()
		plt.plot(self.x,self.y)
		plt.pause(0.0001)
		#plt.show()

def mainUI():	#The core function of the program
	sel=input("Enter shape(disk/polygon): ")	#Select the shape (case-insensitive)
	if(sel.lower()=='polygon'):	#If polygon chosen
		x=list(map(int,input("Enter x coordinates: ").split()))	#List of x-coordinates
		y=list(map(int,input("Enter y coordinates: ").split()))	#List of y-coordinates
		obj=polygon(x,y)	#Create a polygon object
		plt.ion()	#Begin interactive plot
		obj.plot()	#Plot the initial polygon
		
		while(True):	#Stay in the loop unless user wants to quit
			s=input("Enter operation: ")
			if(len(s)==0):
				print("Invalid Input")
				print("Please Try Again")
			elif(s[0]=='S'):	#Scale operation
				s1=s.split(' ')
				obj.scale(float(s1[1]),float(s1[2]))
				print(obj)
				obj.plot()
			elif(s[0]=='R'):	#Rotation operation
				s1=s.split(' ')
				obj.rotate(float(s1[1]))
				print(obj)
				obj.plot()
			elif(s[0]=='T'):	#Translation operation
				s1=s.split(' ')
				obj.translate(float(s1[1]),float(s1[2]))
				print(obj)
				obj.plot()
			elif(s=='quit'):
				break
			else:	
				print("Invalid Input")
				print("Please Try Again")

	elif(sel.lower()=='disk'):	#If disk is selected
		x,y,r=map(int,input('Enter centre\'s coordinates and radius: ').split())	#Get the center and radius
		obj=ellipse(x,y,r)	#Create a disk object
		plt.ion()	#Begin with interactive plot
		obj.plot()	#Plot the initial disk
		
		while(True):	#Stay in the loop unless user wants to quit
			s=input("Enter operation: ")
			if(len(s)==0):
				print("Invalid Input")
				print("Please Try Again")
			elif(s[0]=='S'):	#Scale operation
				s1=s.split(' ')
				obj.scale(float(s1[1]),float(s1[2]))
				print(obj)
				obj.plot()
			elif(s[0]=='R'):	#Rotation operation
				s1=s.split(' ')
				obj.rotate(float(s1[1]))
				print(obj)
				obj.plot()
			elif(s[0]=='T'):	#Translation operation
				s1=s.split(' ')
				obj.translate(float(s1[1]),float(s1[2]))
				print(obj)
				obj.plot()
			elif(s=='quit'):
				break
			else:
				print("Invalid Input")
				print("Please Try Again")

	print("Terminating Program ...")
	input("Press any key to Exit ...")

if( __name__=="__main__" ):
	mainUI()	#main function call