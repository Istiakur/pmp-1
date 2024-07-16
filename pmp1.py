print("available functions:")
print("1.Guess the Number")
print("2.password generator")

run = int(input("Your answer:"))
#guess the number
import random
correctnum = random.randint(1,10)
#print(correctnum)
if run == 1:
    num = int(input("Your Guess:"))
    while num != correctnum:
        if num > correctnum:
            num = int(input("Try a smaller number:"))
        else:
            num = int(input("Try a bigger number:"))
    else:
        print("Congratulations your number was correct")

#password generator
import string
if run == 2:
    chars = ''
    length = int(input("Password length:"))
    if length <= 0:
        print("Password length should be greater than zero.")

    type = int(input("""Choose one of the following:
    1.only digit
    2.only letter
    3.only special characters
    4.only digits and letter
    5.only digit and special character
    6.only letter and special character
    7.digit, letter and special character
    Your answer:"""))
    print(type)
    while True:
        if type == 1:
            chars += string.digits
        elif type == 2:
            chars += string.ascii_letters
        elif type == 3:
            chars += string.punctuation
        elif type == 4:
            chars += string.digits
            chars += string.ascii_letters
        elif type == 5:
            chars += string.digits
            chars += string.punctuation
        elif type == 6:
            chars += string.ascii_letters
            chars += string.punctuation
        elif type == 7:
            chars += string.digits
            chars += string.ascii_letters
            chars += string.punctuation
        else:
            type  = int(input(("Error, try again:")))
        if 0 < type < 8:
            break
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
    