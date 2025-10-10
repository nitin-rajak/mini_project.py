# Inputs we need to the user 
# total rent 
# Total food orderd for snacking 
# electricity unots spend 
# charge per unit 

# Output 
# total aamount you've to pay is 

rent = int(input("Enter your Hostel /flat rent = "))
food = int (input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)