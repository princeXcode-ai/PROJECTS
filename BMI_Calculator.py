# BMI = BODY MASS INDEX
while True:
    weight = float(input("Weight(kg) :- "))
    height = float(input("\nHeight(m) :- "))

    bmi = weight/height**2

    if bmi <= 18.5 :
        print("Under weight")
        
    elif bmi <= 24.9:
        print("Normal Weight")
        
    elif bmi <= 29.9: 
        print("Over Weight")
        
    else:
        print("Obese")
    
    while True:    
        user = input("\ndo you want to calculate again (yes/no):- ").lower()
        
        if user =="yes":
            break
        
        elif user == "no":
            print("thanks for using BMI Calculator")
            exit()
        
        else:
            print("Please enter only 'yes' or 'no'.")