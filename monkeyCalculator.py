def calculateTime():
    
    # This first line is provided for you
    try: 
        monkey_one = input("Is the first monkey smiling?:  (y/n) ").lower()
        monkey_two = input("Is the second monkey smiling?: (y/n) ").lower()

        if monkey_one == "y" and monkey_two == "y":
            print("Uh Oh! We're in trouble!")

        elif monkey_one == "n" and monkey_two == "n":
            print("Uh Oh! We're in trouble!")

        elif monkey_one == "y" and monkey_two == "n":
            print("Yay! We're going to have a good day!")

        elif monkey_one == "n" and monkey_two == "y":   
            print("Yay! We're going to have a good day!")

        else:
            print("Please enter y or n")
    except:
        print("Please enter y or n")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateTime() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateTime()