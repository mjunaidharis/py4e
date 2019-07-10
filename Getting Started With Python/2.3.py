# Input both values
hrs = input("Enter Hours:")
rate_per_hour = input("Enter Pay:")

#convert them to float
hrs = float(hrs)
rate_per_hour = float(rate_per_hour)

#calculate gross pay by multiplying
gross_pay = hrs * rate_per_hour

#print the pay
print("Pay:",gross_pay)