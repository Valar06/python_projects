print("Welcome to treasure hunt")
direction = input("Enter a direction: ")

if direction.lower() == "left":
    colour = input("Enter a colour (Blue, Red or Green): ")
    if colour.lower() == "blue":
        number = int(input("Enter a number between 1-10: "))
        if number == 10:
            location = input("Enter a city in J&K ")
            if location.lower() == "rajouri":
                print("You won")
            else: 
                print("You lost")
        else:
            print("You lost")
    else:
        print("You lost ")
else:
    print("You lost ")