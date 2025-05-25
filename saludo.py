hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

if h <= 40:
    pay = h * r
    
else:
    regular = 40 * r
    overtime = (h - 40) * (r * 1.5)
    pay = regular + overtime 
    
print(pay)