
def main():
	#write your code here
	first = input("input first number: ")
	second = input("input seconds number: ")
	oper = input("Choose the operation (+, -, /, *): ")

	if first.isdigit() and second.isdigit():
		first = int(first)
		second = int(second)
		if oper == "+" :
			print ("the answer is", first+second)
		elif oper == "-":
			print ("the answer is", first-second)
		elif oper == "/":
			print ("the answer is", first/second)
		elif oper == "*":
			print ("the answer is", first*second)
		else:
			print ("invalid operation, please input again:")
	else:
		print("Please input valid numbers: ")





if __name__ == '__main__':
	main()
