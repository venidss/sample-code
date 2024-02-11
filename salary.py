hrs=int(input("Enter your hours:"))

if hrs != 0:
		if hrs <= 40:
			salary = hrs * 200
		elif hrs > 40:
				exhrs= hrs - 40
				exPay = 200 * 1.5
				ex = exhrs * exPay
				salary = 40 * 200 + ex
		print("Salary:" +str(salary))
else:
		print("Invalid hours")
			
			

	