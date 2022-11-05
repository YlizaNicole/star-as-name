mylist = [2, 3, 5, 4, 1, 6, 8, 1, 9, 10]
print(mylist)
print("pick a number")
operation = input('''
    Select operation:
    [1] Add an element 
    [2] Insert an element 
    [3] Delete an element
    [4] Arrange in ascending order
    [5] Arrange in descending order
    [6] Sum the element
    [7] Lenght of element
    [8] count one element
    [9] Largest element
    [10] Smallest element
    ''')

print(operation)

def list ():
    if operation == '1':
        print("Type the number you would like to add to the list: ")
        number = int(input())
        add = mylist.append(number)
        print(mylist)

    elif operation == '2':
        print("Type position of the number you like to insert from list: ")
        number1 = int(input())
        print("Type the number you want to add: ")
        number2 = int(input())
        insert = mylist.insert(number1, number2)
        print (mylist)

    elif operation == '3':
        print("Type position of the element number you like to remove from the list: ")
        number = int(input())
        remove= mylist.pop(number)
        print(mylist)

    elif operation == '4':
        print("Arrange in ascending order:")
        mylist.sort()
        print(mylist)
        
    elif operation == '5':
        print("Arrange in descending order:")
        rev= mylist.sort()
        verse= mylist.reverse()
        print(mylist)
    
    elif operation == '6':
        print("Total of the list: ")
        total = sum(mylist)
        print(total)

    elif operation == '7':
        print("Lenght of the list: ")
        lenght = len(mylist)
        print(lenght)

    elif operation == '8':
        print("type the number you want to count the times is appear: ")
        number = int(input())
        counter = mylist.count(number)
        print("it appears")
        print (counter)

    elif operation == '9':
        print("Largest number in the list: ")
        large = max(mylist)
        print(large)
    
    elif operation == '10':
        print("Smallest number in the list: ")
        small = min(mylist)
        print(small)
        
    else:
            print('You have not chosen a valid operator, please run the program again.')

    again()

def again():
    list_again = input('''Would you like to see main menu again? (Y/N)''')

    if list_again.upper() == 'Y':
        list()
    elif list_again.upper() == 'N':
        print('OK. Bye bye. :)')
    else:
        again()
list()