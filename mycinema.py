#project for booking movie ticket by using python

class Theater:
    def interaction(self):
        print('Press 1 for show the tickets')
        print('Press 2 for buy a ticket')
        print('Press 3 for statistics')
        print('Press 4 for user information')
        print('Press 0 for exit')

    def __init__(self,row,column):# fun for create auditorium
        print('Total seats')
        self.Row = row
        self.Col = column
        self.matrix = []
        self.user_details = {} # details can be stored in dict
        self.income = {}

        for i in range(self.Row): # loop will be iterate for row
            var = []
            for j in range(self.Col):# nested loop will be iterate for col
                var.append('S')
            self.matrix.append(var)
        print(end="  ")

        for j in range(self.Col):# for typing col no on matrix
            print(j+1, end=" ") # for increment th value
        print()
        for i in range(self.Row):#for typing row no on matrix
            print(i+1, end=" ")
            for j in range(self.Col): #nested loop WILL ITERATE TO THE COLUMN NUMBER GIVEN BY USER
                print(self.matrix[i][j],end=" ")
            print() # for next line


    def show_seats(self):   # to display updated seat in our matrix
        x = 0
        y = 0
        print(end="  ")
        for j in range(1,self.Col+1):
            y = y+1
            print(y,end=" ")
        print()
        for i in self.matrix:
            x = x+1
            print(x,end=" ")
            print(" ".join(i),sep=" , ")    #join and sep used for print without brackets and comas

    def price_menu(self): #  prince calculation
        if self.Row*self.Col<= 60:  # if the seats are less than 60 price will be 10
            for i in range(1,self.Row+1):
                for j in range(1,self.Col+1):
                    a = {}
                    a[i,j] = 10
                    self.income.update(a)
        elif self.Row*self.Col>60:    # if the seats are less than 60 price will be 10
            c = self.Row//2
            b = self.Col//2
            for i in range(1,self.Row+1):
                a = {}
                for j in range(1,self.Col+1):
                    a[i,j] = 8
                    self.income.update(a)
            for i in range((c+1),self.Row+1):
                a = {}
                for j in range(1, self.Col + 1):
                    a[i,j] = 10
                self.income.update(a)

    def statistics(self): # for statistics purpose
        booked = 0
        vacant = 0
        current_revenue = 0
        total_revenue = 0
        for i in self.user_details.items():

            current_revenue = current_revenue + i[1][4]
        for i in self.income.items():
            total_revenue = total_revenue + i[1]
        for i in self.matrix:
            for j in i:
                if j == 'B':   #IF THE VALUE OF SEAT IS B IT WILL INCREMENT THE VALUE OF BOOKED SEAT
                    booked = booked+1
                elif j == 'S':
                    vacant = vacant+1
        print('Your booked tickets',booked)
        print('Percentage of booked tickets',(booked/(booked + vacant))*100 )
        print('Current revenue generated',current_revenue)
        print('Total revenue generated',total_revenue)

    def user_info(self,row,col):   # to get booked ticked user information
        self.getrow = row
        self.getcol = col
        print('Name',self.user_details[int(self.getrow),int(self.getcol)][0])
        print('Gender',self.user_details[int(self.getrow),int(self.getcol)][1])
        print("Age: ", self.user_details[int(self.getrow), int(self.getcol)][2])
        print("Mobile Number: ", self.user_details[int(self.getrow), int(self.getcol)][3])
        print("Ticket Price: ", self.user_details[int(self.getrow), int(self.getcol)][4],"\n")

    def buy_tickets(self,row,col): # for buying tickets
        self.buyrow = row
        self.buycol = col
        if self.matrix[int(self.buyrow)][int(self.buycol)] == "B":  # IF THE SEAT IS ALREADY BOOKED
            print("Seat Already Booked Book Another Seat" )  # IT WILL DISPLAY ALREADY BOOKED
        else:  # IF THE SEAT IS VACANT IT WILL DISPLAY THE PRICE OF TICKET AND ASK FOR CONFIRMATION
            print("Price Of The Ticket: ", self.income[(int(self.buyrow), int(self.buycol))])

            confirm = input('TO confirm your ticket please press Y\n')
            if confirm == 'Y':
                a = {}
                customer_name, customer_gender, customer_age, customer_phone = input(
                    "Enter Your Name ,Gender ,Age ,"
                    "Phone Number: \n").split()
                a[int(self.buyrow), int(self.buycol)] = list((customer_name, customer_gender, int(customer_age),
                                                              int(customer_phone),
                                                              self.income[(int(self.buyrow), int(self.buycol))]))
                self.user_details.update(a)
                self.matrix[int(self.buyrow)][int(self.buycol)] = "B"
                print('Your booking is done successfully')
            else:
                print('Your current booking is terminated')













