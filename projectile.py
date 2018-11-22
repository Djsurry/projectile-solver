#ex physics
from math import cos, sqrt, sin, radians, degrees, atan
import cutie, readchar
from sys import exit as close
from os import system
GRAVITY = -9.8
SIZE = 10


def quad(a, b, c):
	a2 = a*2

	#(-b +- sqrt(b^2-4*a*c))2a
	d = (b * b) - 4 * a * c
	if d < 0:
		return None
	a1 = (-b + sqrt(d))/a2
	a2 = (-b - sqrt(d))/a2

	return (a1,) if a1 == a2 else (a1, a2)

def clear(n):
	print("\033[{}A".format(n+1))
	for i in range(n):
		print("\033[K")
	print("\033[{}A".format(n))

class Kinematic:
	def __init__(self, a, v1, v2, t, s):
		self.a = a
		self.v1 = v1
		self.v2 =v2
		self.t = t
		self.s = s

def isFloat(n):
	try:
		t = float(n)
		return t
	except:
		return None


def getInputs():
	active  = True
	currentLevel = 0
	f = True
	inputs = ['', '', '']
	while active:
	    
	    if not f:
	        print("\033[4A")
	    else:
	        f = False
	    if currentLevel == 0:
	        print(f"\033[K\x1b[38;5;1m Height: {inputs[0]} \x1b[0m")
	        print(f"\033[KAngle: {inputs[1]}")
	        print(f"\033[KInitial Velocity: {inputs[2]}")
	    elif currentLevel == 1:
	        print(f"\033[KHeight: {inputs[0]}")
	        print(f"\033[K\x1b[38;5;1m Angle: {inputs[1]} \x1b[0m")
	        print(f"\033[KInitial Velocity: {inputs[2]}")
	    elif currentLevel == 2:
	        print(f"\033[KHeight: {inputs[0]}")
	        print(f"\033[KAngle: {inputs[1]}")
	        print(f"\033[K\x1b[38;5;1m Initial Velocity: {inputs[2]} \x1b[0m")

	   
	    char = readchar.readkey()
	    if char == "\x03":
	        close(0)
	    elif char == '\x1b\x5b\x42':
	        currentLevel = currentLevel + 1 if currentLevel != 2 else 0
	    elif char == '\x1b\x5b\x41':
	    	currentLevel = currentLevel - 1 if currentLevel != 0 else 2
	    elif char == '\x0d':
	        if '' not in inputs:
	            break
	    elif char == '\x7f':
	    	inputs[currentLevel] = inputs[currentLevel][:-1]
	    elif char in '1234567890.':
	        if char == '.':
	            if '.' in inputs[currentLevel]:
	                continue
	        if inputs[currentLevel] == "9" and currentLevel == 1:
	        	if char != "0":
	        		continue
	       	if currentLevel == 1 and len(inputs[currentLevel]) == 2:
	       		continue
	        inputs[currentLevel] += char
	clear(3)
	return inputs



def splitVel(a, vel, h):
	opp = sin(radians(a))*vel
	adj = cos(radians(a))*vel
	x = Kinematic(0,adj,adj, None, None)
	y = Kinematic(GRAVITY, opp, None, None, -h)
	return x, y

class Problem:
	def __init__(self, h, ang, v):
		self.height = h
		self.angle = ang
		self.initVel = v
		self.x, self.y = splitVel(self.angle, self.initVel, self.height)
	def solve(self):
		# solve t for y: ds = v1*dt + (1/2)a(dt)^2
		
		self.y.t = quad(0.5*self.y.a, self.y.v1, -1*self.y.s)
		if not self.y.t:
			print("No solution")
			close(0)
		if len(self.y.t) == 2:
			
			options = ["Which of these is right for time", self.y.t[0], self.y.t[1]]

			option = options[cutie.select(options, caption_indices=[0],selected_index=1)]
			if option == self.y.t[0]:
				self.y.t = self.y.t[0]
			else:
				self.y.t = self.y.t[1]
			print("\033[4A")
			print("\033[K")
			print("\033[K")
			print("\033[K")
			print("\033[K")
			print("\033[5A")
		else:
			self.y.t = self.y.t[0]

		# add to x
		self.x.t = self.y.t
		#solve for ds for x: ds = v1*dt
		self.x.s = self.x.v1*self.x.t
		# solve for v2 for y
		self.y.v2 = sqrt(2*self.y.a*self.y.s + self.y.v1*self.y.v1)

	def range(self):
		clear(SIZE)
		print("Range is {0:.2f}m\n".format(self.x.s))

	def maxHeight(self):
		a = GRAVITY
		v1 = self.y.v1
		clear(7)
		#v2^2 - v1^2 = 2*a*ds
		
		s = (-1*v1*v1)/(a*2) + self.height
		print("Max Height is {0:.2f}m\n".format(s))

	def speedAtGround(self):
		clear(SIZE)
		print("Speed on impact with ground is {0:.2f}m/s\n".format(sqrt(self.x.v1 * self.x.v1 + self.y.v2 * self.y.v2)))

	def velocityAtGround(self):
		clear(SIZE)
		print("Velocity on impact with ground is {0:.2f}m/s offset {1:.2f} degress down\n".format(sqrt(self.x.v1 * self.x.v1 + self.y.v2 * self.y.v2), degrees(atan(self.y.v2/self.x.v1))))
	def totalTime(self):
		clear(SIZE)
		print("Time is {0:.2f}\n".format(self.x.t))
	def xyT(self):
		clear(SIZE)
		toRemove = 0
		while True:
			t = input("At what time: ")
			toRemove += 1
			t = isFloat(t)
			if t:
				if t > self.x.t:
					print("Out of domain")
					toRemove += 1
					continue
				break
		clear(toRemove)
		# FOR X
		# ds = None, dt = t, v1 = self.x.v1, v2 = self.x.v1, a = 0
		x, y = splitVel(self.angle, self.initVel, self.height)
		x.t = t
		# ds = ((v1 + v2)/2*t
		x.s = ((x.v1 + x.v2)/2)*x.t
		# FOR Y
		# ds = None, dt = t, a = -9.8, v1 = self.y.v1, v2 = None
		y.t = t
		# ds = v1 * t + 1/2 * a * t
		y.s = y.v1 * y.t + 0.5*y.a*(y.t*y.t)
		print("It has traveled {0:.2f}m in the x direction and is {2:.2f}m off the ground at {1}s\n".format(x.s, x.t, self.height+y.s))

	def xyD(self):
		clear(SIZE)
		a = GRAVITY
		v1 = self.y.v1
		#v2^2 - v1^2 = 2*a*ds
		
		s = (-1*v1*v1)/(a*2) + self.height
		toRemove = 2
		options = ["Find X from Y", "Find Y from X"]
		option = options[cutie.select(options, selected_index=0)]
		while True:
			if option == "Find Y from X":
				t = input("At what distance from the starting point? ")
				toRemove += 1
				t = isFloat(t)
				if t:
					if t > self.x.s and option =="Find Y from X":
						print("Out of domain")
						toRemove += 1
						continue
					else:
						break
			elif option == "Find X from Y":
				t = input("At what distance from the ground? ")
				toRemove += 1
				t = isFloat(t)
				if (t > self.height + s or t < 0) and option == "Find X from Y":
					print("Out of domain")
					toRemove += 1
					continue
				else:
					break
		
	
		if option == "Find X from Y":
			t = self.y.s + t
			# ds = self.height + t, t = None, a = -9.8, v1 = initVel, v2 = None
			# ds = v1 * t + 0.5 * a * t^2
			a = 0.5*GRAVITY
			b = self.y.v1
			c = -1*t

			answers = quad(a, b, c)
			if answers:
				if len(answers) == 2:
					correct = cutie.select(["Which is correct for time?"] + list(answers), caption_indices = [0])
					toRemove += 3
				else:
					correct = answers[0]

			else:
				clear(toRemove)
				print("Bad input")
				
				
				return
			# find for x
			# ds = None, t = t, a = 0, v1 = v1, v2=v2
			# ds = v1*t + 0.5*a*t^2
			s = self.x.v1*correct
			clear(toRemove)
			print("It will have traved {0:.2f}m in the X direction when it is {1:.2f}m off the ground\n".format(s, t-self.y.s))
			
		elif option == "Find Y from X":
			# ds = input, t = None, a = 0, v1 = v1, v2 = v2
			# ds = v1 * t + 0.5 * a * t^2

			time = t/self.x.v1
			# find for y
			# ds = None, t = t, a = 0, v1 = v1, v2=v2
			# ds = v1*t + 0.5*a*t^2
			s = self.y.v1 * time + 0.5 * self.y.a * (time*time)
			clear(toRemove)
			
			print("It will be {0:.2f}m off the ground when it has gone {1:.2f}m on the X axis\n".format(self.height + s, t))

			

def main():
	i = getInputs()
	p = Problem(isFloat(i[0]), isFloat(i[1]), isFloat(i[2]))
	p.solve()
	first = True
	choices = ["What would you like to know?", "Range", "Total Time", "X and Y at specific time", "X or Y at cooresponding distance", "Maximum height", "Speed at impact on ground", "Velocity at impact on ground", "New problem", "Quit"]
	while True:
		choice = choices[cutie.select(choices, caption_indices=[0], selected_index=1)]
		if choice == "Range":
			p.range()
		elif choice == "Quit":
			close(0)
		elif choice == "Maximum height":
			p.maxHeight()
		elif choice == "X and Y at specific time":
			p.xyT()
		elif choice == "X or Y at cooresponding distance":
			p.xyD()
		elif choice == "Total Time":
			p.totalTime()
		elif choice == "Speed at impact on ground":
			p.speedAtGround()
		elif choice == "Velocity at impact on ground":
			p.velocityAtGround()
		elif choice == "New problem":
			system("clear")
			print("\n")
			main()

if __name__ == "__main__":
	main()
		

		
