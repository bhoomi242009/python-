fruits = {}

while True:
    print("1. Buy a fruit")
    print("2. Add a new fruit")
    print("3. Restock a fruit")
    print("4. View all fruits")
    print("5. Exit")

    choice = input("What would you like to do: ")

    if choice == "1":
        fruit = input("What fruit would you like to buy: ")
        if fruit in fruits:
            quantity = int(input("How many would you like to buy: "))
            if quantity <= fruits[fruit]:
                fruits[fruit] -= quantity
            else:
                print("Not enough {}(s) available.".format(fruit))
            if fruits[fruit] == 0:
                print("Not enough available.")
        else:
            print("The fruit is not in our shop.")

    elif choice == "2":
        fruit = input("What fruit would you like to add: ")
        if fruit in fruits:
            ("This fruit alredy exists.")
        else: 
            quantity = int(input("How many would you like to add: "))
            fruits[fruit] = quantity
    
    elif choice == "3":
        fruit = input("Enter the fruit name: ")
        if fruit in fruits:
            quantity = int(input("How many would you like to add: "))
            fruits[fruit] += quantity
        else:
            print("We don't have this fruit.")
    
    elif choice == "4":
        for fruit, quantity in fruits.items():
            print(fruits)

    elif choice == "5":
        break

    else:
        print("Invalid input.")
