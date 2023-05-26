# simple password generator, with input of max letters
import random
import string


from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()


lowercase = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation

all_characters = lowercase + digits + punctuation



def random_string(maximum):
    count = 0
    password = ""
    while count <= int(maximum):
        temp = random.choice(all_characters)
        password = password + temp
        count += 1
    return(f"here's your password : {Fore.GREEN}{password}")

print(random_string(input("enter maximum lenght of generated password: ")))