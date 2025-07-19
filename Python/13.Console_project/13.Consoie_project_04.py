# Interest calculator

principal = float(input("Enter your principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

interest = (principal*rate*time)/100

print(interest)