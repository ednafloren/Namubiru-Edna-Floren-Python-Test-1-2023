# function to find the average of two numbers
def averageOfTwoNumbers(x,y):
    sum=x+y 
    # calculating the average
    average=sum/2
    print(f'The average of the two numbers is {average}')
# calling the function and adding parameters
averageOfTwoNumbers(2,4)    

# ii)
# function for finding the average
def minimumValue():
# prompting the user to input values
    firstNumber=input('Enter firstnumber: ')
    secondNumber=input('Enter secondnumber: ')
    thirdNumber=input('Enter thirdnumber: ')
# testing for the minimum values using the if conditions
    if(firstNumber<secondNumber and firstNumber<thirdNumber):
        print(f"The minimum number is {firstNumber}")
    elif(secondNumber<firstNumber and secondNumber<thirdNumber):
          print(f"The minimum number is {secondNumber}")
    else:
           print(f"The minimum number is {thirdNumber}")
# calling the function  
minimumValue()    
