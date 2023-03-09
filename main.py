def decode(password):

    password_lst = []
    decoded_password = ""

    try:
        
        for i in password:
            password_lst.append(i)
        
        for digit in password_lst:
            digit = int(digit)
            digit -= 3
            digit = str(digit)
            decoded_password += digit

        return decoded_password
    
    except TypeError as exc:
        print(exc)

def main():
    main()


def print_menu():
    print("Menu")
    print("------------- ")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")



if __name__ == "__main__":

while True:
    def print_menu():

option = int(input("Please enter an option: "))

if option == 1:
    print("Please enter your password to encode: ")
    def encode():

    print("Your password has been encoded and stored!")
    def print_menu():

elif option == 2:
    def decode():
    print(f"The encoded password is {encoded}, and the original password is {decoded}")

elif option == 3:


