
try:
    print(x)
except NameError:
    print("Variable x is not defined.")
except:
    print("the 'try except' is finished.")
    
    
x=-1

if x < 0:
    raise ValueError("Sorry, no numbers below zero.")
    