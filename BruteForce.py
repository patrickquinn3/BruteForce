# Libraries
import random # Generate choices for password guessing
import pyautogui # Generate GUI for user
import string

chars = string.digits + string.ascii_letters + string.punctuation; # holds characters

allchar = list(chars) # convert chars into list

pwd = pyautogui.password("Enter a Password:") # User enters password

sample_pwd= "" # Stores password

while(sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd)) # generates random choices

    print("<===" + str(sample_pwd) + "===>") # values being checked

    if(sample_pwd == list(pwd)):
        print("The password is: " + "".join(sample_pwd)) # displays guessed password
        break
