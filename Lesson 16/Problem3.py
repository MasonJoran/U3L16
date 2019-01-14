import time 

x = 1000
while x >= 1:
	print(x)
	time.sleep(0.2)
	x = x - 1
	if x == 0:
		print('Blast off!')