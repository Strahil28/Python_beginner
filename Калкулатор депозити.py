deposite_sum = float(input("Enter deposite sum: "))
deposite_time = int(input("Enter deposite month: "))
year_interest_percent = float(input("Enter percent: "))

sum = deposite_sum + deposite_time * ((deposite_sum * year_interest_percent / 100) / 12)
print(sum)