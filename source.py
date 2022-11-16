class Automat:
	#T = [[]]
	
	
	def __init__(self, T):
			self.T = T
			
	def lambda_(self, s, p):
		while len(str(p)) > 1:
			x = int(p[0])
			p = p[1:]
			output += self.lambda_(s, x)
			s = self.delta_(s, x)
		output = self.T[s-1][x-1+(len(T[0])/2]
		return output
	
	
	#def delta_(self, s, x):
	#	return T[s-1][x-1]
	
	def delta_(self, s, p):
		while len(str(p)) > 1:
			x = int(p[0])
			p = p[1:]
			s = self.delta_(s, x)
		x = int(p)
		return T[s-1][int(x)-1]
		
	def printTable(self):
		print(' '*4, end="")
		for i in range(0, len(self.T[0])):
			if i == 0 or i == 2:
				print(" "*1 + "x", end="")
			else:
				print("x",end="")
			print(str(i % (int(len(T[0])/2))+1 ), " ", end='')
		print()
		for i in range(0, len(self.T)):
			print("s" + str(i+1), end=" ")
			for j in range(0, len(self.T[i])):
				if j == 0 or j == 2:
				    print("| ", end="")
				
				print(self.T[i][j], ' ', end=" ")
			print()

T = [
[3, 2, 0, 0],
[8, 5, 0, 0],
[4, 5, 0, 0],
[1, 5, 0, 0],
[8, 2, 0, 0],
[7, 8, 1, 1],
[6, 8, 1, 1],
[9, 8, 1, 1],
[9, 8, 1, 1]
]

A = Automat(T)
A.printTable()
while(True):
	cmess = str(input("# "))
	if cmess == "help":
		print("lambda")
		print("delta")
		print("print")
		print("exit")
	elif cmess == "lambda":
		print("A.lambda_(s, p)")
		s = int(input("s = "))
		p = input("p = ")
		print(A.lambda_(s, p))
	elif cmess == "delta":
		print("A.delta_(s, p)")
		s = int(input("s = "))
		p = input("p = ")
		print(A.delta_(s, p))
	elif cmess == "print":
		A.printTable()
	elif cmess == "exit":
		break
	else:
		print("Wrong input, type \"help\" to look at all commands")
	