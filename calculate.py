def calculate(num1, num2, operation):
    if operation ==1:
        answer = str(num1) + ' + ' + str(num2) +' = '+ str(num1 + num2)
    elif operation == 2:
        answer = str(num1) + ' - ' + str(num2) +' = '+ str(num1 - num2)
    elif operation == 3:
        answer = str(num1) + ' x ' + str(num2) +' = '+  str(num1 * num2)
    elif operation == 4:
        answer = str(num1) + ' / ' + str(num2) +' = '+ str(num1 / num2)
    elif operation == 5:
        answer = str(num1) + ' ^ ' + str(num2) +' = '+ str(num1 ** num2)
    elif operation == 6:
        answer = str(num1) + ' ^ (1/' + str(num2) +') = '+ str(num1**(1/num2))
    else:
        answer= 'UNKNOWN OPERATION'
    return answer


while True:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    print("Operations to carry out \n Addition = 1 \n Subtraction= 2, \n multiplication = 3, \n, Division = 4,\n Exponential =5,\n root= 6")
          
    operation = int(input('Enter operation: '))

    print(calculate(num1, num2, operation))

    q= input('Do you want to continue: ')
    q = q.lower()
    if q != 'yes' and q != 'y':
        print('Thank you for using the program')
        break
    
    
