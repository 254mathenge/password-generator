import random
import string


def passwordStrong(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    print(password)


generate_password = input("generate password? ").lower()
if generate_password == "yes":
    number_of_passwords = input("type the number of passwords you want: ")
    print("okay lets start!")
    for i in range(int(number_of_passwords)):
        # for i in range(int(number_of_passwords)):
        passwordStrong()
else:
    print("goodbye")
    quit()
