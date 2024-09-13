#This program added bonuses
EmployeeName = None 
numShifts = 1
numTransactions = 0
dollarValue = 0.00 
score = 0
Bonus = score

EmployeeName = input("Enter Employee name: ") 
numShifts = int(input("Enter number of shifts: "))
numTransactions = int(input("Enter the number of transactions: "))
dollarValue = float(input("Enter the dollar value of transactions: "))

score = (dollarValue / numTransactions) / numShifts

if score <= 30:
  Bonus= 50.00
elif score >= 31 and score <= 69:
  Bonus= 75.00 
elif score >= 70 and score <= 199:
  Bonus= 100.00
elif score >= 200:
  Bonus= 200.00

print("Employee Name: " + EmployeeName)
print(f"Epmployee Bonus: ${Bonus: .2f}") 
