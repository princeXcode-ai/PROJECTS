print("===================")
print("   CONTACT BOOK")
print("===================\n")

contact= {}


def add_contact():
    name = input("Enter name :- ")
    contact_no = input("Enter contact no. :- ")
    
    contact[name]= contact_no
    print("\nContact added successfully")
    
def view_contact():
    if len(contact)== 0:
        print("No contact is available")
        
    else:
        print("\nNAME        CONTACT NO.")
        print("--------------------------\n")
        for name, contact_no in contact.items():
            print(f"{name:<15}{contact_no}")
            
def search_contact():
    user = input("enter name :- ")
    if user in contact.keys() :
        print(contact[user])
        
    else:
        print("Not found")
        
def update_contact():
    if len(contact)== 0:
        print("No contact is available")
        
    else:
        user_p = input("enter name:-")
        
        if user_p in contact:
            user_pp = input("Enter new contact no. :-")
            contact[user_p]= user_pp
            print("Contact updated successfully")
            
        else:
            print("Contact not found")  
            
def delete_contact():
    if len(contact)== 0:
        print("No contact is available")
        
    else:
        user_pk = input("enter name for delete contact:-")
        
        if user_pk in contact:
            contact.pop(user_pk)
            print("Contact deleted successfully ")
            
        else:
            print("Contact not found")
            
            
        
while True:        
    print("Press 1 for add contact :-")
    print("Press 2 for view contact :-")
    print("Press 3 for search contact :-")
    print("Press 4 for update contact :-")
    print("Press 5 for delete contact :-\n")

    check = int(input("Enter :- "))
        
    if check == 1:
        add_contact()
        
    elif check == 2:
        view_contact()
        
    elif check == 3:
        search_contact()
        
    elif check == 4:
        update_contact()
        
    elif check == 5:
        delete_contact()
        
    else:
        print("Invalid input!")
        
    user_l =input("do you want to do again [yes/no]:- ").lower() .strip()
    
    if user_l == "yes":
        continue

    elif user_l== "no":
        print("THANKS for using contact book")
        break
    else:
        print("Invalid input! please enter only 'yes' or 'no'.")