a = int(input("Enter the weight:"))
w= input("Do you want the weight in kg or lbs:")

if w.lower() == 'kg':
    weight = a*0.45359237
    print("Your weight in kg is:",weight)
    
else:
    weight = a*2.2046226218
    print("Your weight in lbs is:",weight)