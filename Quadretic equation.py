Cont=float(1)
while Cont!=0:
	import math
	a=float(input("Enter a "))
	while a==0:
		a=float(input("Enter non zero a "))
	b=float(input("Enter b "))
	c=float(input("Enter c "))
	disc=(b**2)-(4*a*c)
	print(disc)
	if disc>0:
		print("They are two roots")
		x1 = (-b - math.sqrt(disc)) / (2 * a)
		x2 = (-b + math.sqrt(disc)) / (2 * a)
		print(x1,'and',x2)    
	elif disc <0:
		print('Imaginary roots')
	elif disc==0 :
		print('One root')
		x1 = (-b - math.sqrt(disc)) / (2 * a)
		print(x1)    	
	v=a*b
	if  v==0:
		print('Vertex is on y-axis')
	elif v>0:
		print ('vertex is left of the orgin')
	elif v<0:
		print ('vertex is right of the orgin')
	if c>0:
		print ('Y-intercept is above the orgin')
	elif c<0:
		print ('Y-intercept is below the orgin')
	h=(-b)/(2*a)
	k=a*(h*h)+b*h+c
	print ('The vertex is (',h,',',k,")")
	if a>0:
		print ('the curve will be shaped like a u and the range is >=', k)	
	elif a<0:
		print ('the curve will be shaped like a n and the range is <=', k)
	Cont=float(input("Press 0 to end "))
