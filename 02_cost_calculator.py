def num_check(question):

    valid = False

    while not valid:
        error = "please enter a number greater than 0, try again"

        try:
            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)

        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Fence cost per unit: ")
    print()
    print("Width", width)
    print("Height", height)
    print("Cost/unit", cost)
    print()

    perimeter = 2*(width+height)
    fenceCost = cost*perimeter

    print("Perimeter of fence is {} units".format(perimeter))
    print("Cost of the fence is {} dollars".format(fenceCost))

    keep_going = input("Press <enter> to keep going or press any key to quit")


