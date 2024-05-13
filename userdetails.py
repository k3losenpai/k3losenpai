def main():
    
    age = int(input("Enter your age: "))
    name = str(input("Enter your name: "))

    print(f"Your name is {name.capitalize()} and you are {age} year(s) old, is that correct?")
    
    confirm()
     
def confirm():
    confirmation = input("Y or N?: ")
        
    if "Y" in confirmation.upper():
     print("Thank you for the info!")
     
    elif "N" in confirmation.upper():
     print("Please input your correct details: ")
     main()
     
    else:
     print("Sorry, I do not recognise that input. Please try again!")
     main()
    
main()