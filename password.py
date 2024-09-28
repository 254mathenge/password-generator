import random
import string

# Define the function to generate a random password
def passwordStrong(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    print(password)


generate_password = input("generate password? ").lower()
if generate_password == "yes":
    #the number of characters in the password
    number_of_passwords = input("type the number of passwords you want: ")
    print("okay lets start!")
    #loops the number of time  the user wants
    for i in range(int(number_of_passwords)):
        #calling the function to be executed
        passwordStrong()
else:
    print("goodbye")
    quit()
