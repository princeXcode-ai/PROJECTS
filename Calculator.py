while True:
    

    num1= int(input("Enter Number 1 :- "))
    num2=int(input("Enter Number 2 :- "))

    print(f"for ADDTION : + \n SUBTRACTION : - \n MULTIPLY : * \n DIVIDE : / \n power operation : **")

    check = input("operation = " )



    if check == "+":
        print("answer = ",num1+num2)
        
    elif check == "-":
        print("answer = ",num1 -num2)
        
    elif check == "*":
        print("answer = ",num1 *num2)
        
    elif check == "**":
        print("answer =",num1 ** num2)
        
    elif check == "/":
     while True:
        if num2 == 0:
            print("Can't divide by zero.")
            num2 = int(input("Enter second number again: "))
            print("answer =", num1 / num2)
            
        else:
            print(num1/num2)
            break
        
    
    else:
        print("You want to perform invalid operation b/w Numbers")
        
        
    user =input("do you want to do another calculation [yes/no]:- ").lower()
    
    if user == "yes":
        continue

    elif user== "no":
        print("THANKS for using calculator")
        break
    else:
        print("Invalid input! please enter only 'yes' or 'no'.")
        