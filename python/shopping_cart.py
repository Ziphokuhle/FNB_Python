
focus =[]
prices =[]
total = 0

while True:
    food = input("Enter food item (or 'done' to finish): ") 
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: R"))
        focus.append(food)
        prices.append(price)
        
        print("------YOUR CART------")
        
        for food in foods:
            print(food,end ="")
            
        for price in prices:
            total += price
        
        print("\n")
        print("Your total is: R{total}")