import string
import random
import getpass

class UserDetails:
    @staticmethod
    def get_name():
        name = input("Enter Name: ").strip().capitalize()
        if len(name) == 0:
            raise ValueError("Name Section Can't Be Empty")
        elif name.isdigit():
            raise ValueError("Please Enter a Valid Name")
        
        return name
    
    @staticmethod
    def get_age():
        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError("Age Can't Be Negative or 0")
        
        return age
    
    @staticmethod
    def gen_id():
        prefix = "SEC"
        sufiix = "".join(random.choices(string.ascii_uppercase, k = 7))
        return f"#{prefix}{sufiix}"

    @staticmethod
    def get_password():
        password = getpass.getpass("Enter Password(more than or equal to 8 chars): ").strip().lower()
        if len(password) < 8:
            raise ValueError("Password Can't be less than 8 characters")
        
        return password

    
userdetails = []

class SaveDetails:
    @staticmethod
    def save_details():
        global userdetails
        try:
            n = int(input("Enter Number of User: "))
            for i in range(n):
                name = UserDetails.get_name()
                age = UserDetails.get_age()
                ids = UserDetails.gen_id()
                password = UserDetails.get_password()
                
                userdetails.append([name,age,ids,password])
                print(f"{name} of age {age} yrs old details successfully saved. ID: {ids}")
                
        except ValueError as ve:
            print(f"Error: {ve}")
        

notes = []
# tokens = []

class Notes:
    @staticmethod
    def add_note():
        global notes
        n = int(input("Enter Number Of Notes: "))
        for i in range(n):
            note = input(f"Enter Note {i+1}: ").strip()
            prefix = "N"
            suffix = "".join(random.choices(string.ascii_uppercase, k = 5))
            note_id = f"#{prefix}{suffix}"
            
            prefix_n = "".join(random.choices(string.ascii_uppercase,k = 5))
            suffix_n = "".join(random.choices(string.ascii_lowercase,k = 6))

            sub_note = prefix_n + note + suffix_n
            format_n = sub_note[::-1]
            sub_format_n = format_n[::-1]
            sub_sub_format_n = sub_format_n[len(prefix_n):-len(suffix_n)]
            
            notes.append([format_n,note_id,sub_sub_format_n])
            
            print(f"Note With ID {note_id} saved")
    
    @staticmethod
    def view_note():
        global userdetails
        global notes
        user_id = input("Enter Your ID: ").strip().upper()
        is_found = False
        for user in userdetails:
            if user_id == user[2]:
                note_id = input("Enter Your Note Id: ").strip().upper()
                is_is_found = False
                for note in notes:
                    if note_id == note[1]:
                        print(f"Your Note: {note[0]}")
                        is_is_found = True
                        return
                else:
                    print(f"{note_id} doesn't Exist")

                is_found = True
                return
        else:
            print(f"{user_id} doesn't Exist")
    
    @staticmethod
    def decrypt_note():
        global userdetails
        global notes
        user_id = input("Enter Your ID: ").strip().upper()
        is_found = False
        for user in userdetails:
            if user_id == user[2]:
                note_id = input("Enter Your Note Id: ").strip().upper()
                is_is_found = False
                for note in notes:
                    if note_id == note[1]:
                        print(f"Decrypted Note: {note[2]}")
                        is_is_found = True
                        return
                else:
                    print(f"{note_id} doesn't Exist")

                is_found = True
                return
        else:
            print(f"{user_id} doesn't Exist")
    
    @staticmethod
    def delete_note():
        global userdetails
        global notes
        user_id = input("Enter Your ID: ").strip().upper()
        is_found = False
        for user in userdetails:
            if user_id == user[2]:
                note_id = input("Enter Your Note Id: ").strip().upper()
                is_is_found = False
                for note in notes:
                    if note_id == note[1]:
                        notes.remove(note)
                        print("Note Successfully Deleted")
                        is_is_found = True
                        return
                        
                else:
                    print(f"{note_id} doesn't Exist")

                is_found = True
                return
        else:
            print(f"{user_id} doesn't Exist")
            

class Menu:
    def generate_menu():
        # global userdetails
        opt = {
            1: "Add details",
            2: "Add Note",
            3: "View Note",
            4: "Decrypt Note",
            5: "Delete Note"
        }
        print("...MENU...")
        print("...........\n")
        for k,v in opt.items():
            print(f"{k}.{v}")
        
        print("\n")
        try:
            choice = int(input("Enter Choice: "))
            match choice:
                case 1:
                    SaveDetails.save_details()
                case 2:
                    # global userdetails
                    password = getpass.getpass("Enter Password: ").strip().lower()
                    is_found = True
                    for user in userdetails:
                        if password == user[3]:
                            Notes.add_note()
                            is_found = True
                            return
                            return
                        else:
                                print("Access Denied")
                            
                        
                case 3:
                    # global userdetails
                    password = getpass.getpass("Enter Password: ").strip().lower()
                    is_found = True
                    for user in userdetails:
                        if password == user[3]:
                            Notes.view_note()
                            is_found = True
                            return
                        else:
                            print("Access Denied")
                case 4:
                    # global userdetails
                    password = getpass.getpass("Enter Password: ").strip().lower()
                    is_found = True
                    for user in userdetails:
                        if password == user[3]:
                            Notes.decrypt_note()
                            is_found = True
                            return
                        else:
                            print("Access Denied")
                case 5:
                    # global userdetails
                    password = getpass.getpass("Enter Password: ").strip().lower()
                    is_found = True
                    for user in userdetails:
                        if password == user[3]:
                            Notes.delete_note()
                            is_found = True
                            return
                        else:
                            print("Access Denied")
                case 6:
                    print("Invalid Choice")
                    
        except ValueError as ve:
            print(f"Error: {ve}")
        
if __name__ == "__main__":
    while True:
        Menu.generate_menu()
        
        stop = input('Enter 1 to continue and any other key to exit: ').strip().lower()
        if stop != "1":
            break
                


    
    

    
        
