# Input both values
hrs = input("Enter Hours:")
rate_per_hour = input("Enter Pay:")
gross_pay = 0

# convert them to float
hrs = float(hrs)
rate_per_hour = float(rate_per_hour)

# if gross pay is less than equal 40hrs compute directly
if hrs <= 40:
    gross_pay = hrs * rate_per_hour
else:
    # same for first 40 hours and 1.5x for remaining hours
    gross_pay = (40 * rate_per_hour) + (hrs - 40) * (rate_per_hour * 1.5)

# print the pay
print(gross_pay)