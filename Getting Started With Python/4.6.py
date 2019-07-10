def computepay(hrs,rate_per_hour):
    # if gross pay is less than equal 40hrs compute directly
    if hrs <= 40:
        return hrs * rate_per_hour
    else:
        # same for first 40 hours and 1.5x for remaining hours
        return (40 * rate_per_hour) + (hrs - 40) * (rate_per_hour * 1.5)


# Input both values
hrs = input("Enter Hours:")
rate_per_hour = input("Enter Pay:")

# convert them to float
hrs = float(hrs)
rate_per_hour = float(rate_per_hour)

#compute and print
p = computepay(hrs,rate_per_hour)
print(p)
