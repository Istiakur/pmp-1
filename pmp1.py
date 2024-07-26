print("Available functions:")
print("1.Guess the Number")
print("2.Password generator")
print("3.Grade calculator")
print("4.Trafic light meaning")
while True:
    try:
        run = int(input("Your answer:"))
        break
    except ValueError:
        print("Please enter a valid number")
def number_guess(): 
    import random
    correctnum = random.randint(1,10)
    #print(correctnum)
    while True:
        try:
            num = int(input("Your Guess:"))
            break
        except ValueError:
            print("Please enter a valid number")

    while num != correctnum:
        if num > correctnum:
            num = int(input("Try a smaller number:"))
        else:
            num = int(input("Try a bigger number:"))
    else:
        print("Congratulations your number was correct")

def password_generator():
    import random
    import string
    chars = ''
    while True:
        try:
            length = int(input("Password length:"))
            if length > 0:
                break
            else:
                print("Password length should be greater than zero.")
        except ValueError:
            print("Please enter a valid number")

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
            type  = int(input(("Error, try again: ")))
        if 0 < type < 8:
            break
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Here is your password:" + password)
def grade_calc():
    marks = int(input("marks: "))
    try:
        marks = int(marks)
        if(marks >=80):
            print("A+")
        elif(marks >=70):
            print("A")
        elif(marks >=60):
            print("A-")
        elif(marks >=50):
            print("B")
        elif(marks >=40):
            print("c")
        elif(marks >=33):
            print("D")
        else:
            print("Fail")

    except ValueError:
        print("please enter a valid integer")
def traffic_light_meaning():
    #traffic light
    light = input("Light color: ")
    if(light== "red" or "Red"):
        print("stop")
    elif(light == "yellow" or "Yellow"):
        print("look")
    elif(light == "green" or "Yellow"):
        print("go")
    else:
        print("light is broken")

while True:
    if run == 1:
        number_guess()
    if run == 2:
        password_generator()
    if run == 3:
        grade_calc()
    if run == 4:
        traffic_light_meaning()

    playagain = input("play again? (Yes/No)")
    if playagain != "no":
        print("Available functions:")
        print("1.Guess the Number")
        print("2.Password generator")
        print("3.Grade calculator")
        print("4.Trafic light meaning")

        run = int(input("Your answer:"))
    else:
        break


