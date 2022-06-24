
# setting variables to be used later

wrong = "Wrong! the answer is {}: "
correct = "Correct! the answer is {}: "
congratulation = "\n Congratulations {}! You scored {}/3"
low_score = "\n Oops {}! you scored {}/3"

# setting up game for beginner level
def beginner():
    score = 0
    print("\nOk {}, you'll be playing a beginner level".format(name))
    play_on = input("\nDo you want to continue? yes/no: ")
    if play_on == 'yes':
        print("Ok let's Go \n")

        # question1
        print(" Question 1")
        question1 = input("What is the square root of 16: ")
        if question1 == "4":
            print(correct.format('4'))
            score += 1
        else:
            print(wrong.format('4'))

        # question2
        print("\n Question 2")
        question2 = input("What is 17 - 9: ")
        if question2 == "8":
            print(correct.format('8'))
            score += 1
        else:
            print(wrong.format('8'))

        # question3
        print("\n Question 3")
        question3 = input("What is 3 * 8: ")
        if question3 == "24":
            print(correct.format('24'))
            score += 1
        else:
            print(wrong.format('24'))

        # sending out score
        if score >= 2:
            print(congratulation.format(name, score))
        else:
            print(low_score.format(name, score))

def intermediate():
    score = 0
    print("\nOk {}, you'll be playing an intermediate level".format(name))
    print("NOTE: You'll probably need a jotter for this")
    play_on = input("\nDo you want to continue? yes/no: ")
    if play_on == 'yes':
        print("Ok let's Go \n")

        # question1
        print(" Question 1")
        question1 = input("What is 5 * (48 - 37) - 12: ")
        if question1 == "43":
            print(correct.format('43'))
            score += 1
        else:
            print(wrong.format('43'))

        # question2
        print("\n Question 2")
        question2 = input("What is 7 ^ 3: ")
        if question2 == "343":
            print(correct.format('343'))
            score += 1
        else:
            print(wrong.format('343'))

        # question3
        print("\n Question 3")
        question3 = input("What is 5!: ")
        if question3 == "120":
            print(correct.format('120'))
            score += 1
        else:
            print(wrong.format('120'))

        # sending out score
        if score >= 2:
            print(congratulation.format(name, score))
        else:
            print(low_score.format(name, score))

# setting condition to restart game
play_again = "yes"
while play_again == "yes":
    name = input("Enter your name: ")

    #setting while loop to run until a valid age is entered 
    while True:
        try:
            age = int(input('Enter your age: '))
            break
        except ValueError:
            print("Enter a valid age")
    if age <= 12:
        beginner()
    else:
        intermediate()
    play_again = input("\nDo you want to play again? yes/no: ")
