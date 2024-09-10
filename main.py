# function with no parameters
def printMessage():
    print('Hello, I just print and do not return a value')

printMessage()

def printMessageWithParameters(value1, value2):
    print("Here is my first parameter {} with my second parameter {}".format(value1, value2))

printMessageWithParameters(5, 'Tacos')
phone = 'iPhone'
device = 'Android'
printMessageWithParameters(phone,device)

def sumItUp(value1, value2):
    answer = value1 + value2
    return answer

mySum = sumItUp(5,4)
print('mySum now has the value of', mySum)