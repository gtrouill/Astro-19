import numpy as np

def main():
	print("index|    x-value    |    f(x)-value")
	for i in range(1, 1001):
		x = i*2*np.pi/1000
		print( i ,"|", x ,"|", np.sin(x))

main()