import mycinema as mc
welcome = '''Welcome to bookmyticket.com'''
Tagline = 'Wear mask and use hand sanatizer'
print(welcome.center(90))
print(Tagline.center(90))
row = int(input('Enter no of row for making auditorium\n'))
col = int(input('Enter no of column for making auditorium\n'))
theater = mc.Theater(row,col)
theater.price_menu()
print('\n We have these options for further processing')
theater.interaction()

while (True):
    choice = int(input())
    if choice == 1:
        print( "Avilable seats:" )
        theater.show_seats()
        print( "Would You Like To Do Anything Else" )
        theater.interaction()
    elif choice == 2:
        print( "Enter The Row And Column Number You Would Like To seat" )
        buy_row, buy_col = input().split()
        theater.buy_tickets(buy_row, buy_col)
        theater.show_seats()
        print( "Would You Like To Do Anything Else" )
        theater.interaction()
    elif choice == 3:
        print( " We are at Statistics" )
        theater.show_seats()
        theater.statistics()
        print( "Would You Like To Do Anything Else" )
        theater.interaction()
    elif choice == 4:
        print( "Enter Booked Seat Number To Get Booked Ticket User Info" )
        getrow, getcol = input().split()
        theater.user_info(getrow, getcol)
        print( "Would You Like To Do Anything Else" )
        theater.interaction()
    elif choice == 0:
        print( "Thank You for visiting here" )
        exit()
    else:
        print( "Please Enter Valid Input" )




