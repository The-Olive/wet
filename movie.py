# This is a program that will take me to the movies

def initialPrintMessage():
    print('Good afternoon, and welcome to the Guzzo cinema')
initialPrintMessage()

# Asking the user for the name of the movie they want to watch
movieName = input("What is the name of the movie you want to watch? \n")

# Asking

def movie_info(value1, value2):
    print('The only available movie is {} and it costs ${} to see.'.format(value1, value2))
movie_info(movieName, 13)

# Food menu
def menu():
    print('1. Popcorn, 2. Hot Dogs, 3. Nachos')

def choice(myChoice):
    if (myChoice == 1):
        print("Popcorn is $1.00")
    elif (myChoice == 2):
        print("Hot Dogs is $2.00")
    else:
        print("Nachos is $3.00")

money = int(input("Please enter money greater than 13 to see the movie \n"))
if(money >= 13):
    menu()
    selection =