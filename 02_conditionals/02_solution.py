# Problem: Movie tickets are priced based on age: $12 for Adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday

age = int(input("Enter the age: "));
Day = input("Enter the day: ");
ticket_price = 0

if age < 19:
    ticket_price = 8
    if Day == "Wednesday":
        ticket_price = ticket_price - 2
        print("---------------------")
        print("Total price of the ticket is $", ticket_price)
else:
    ticket_price = 18
    if Day == "Wednesday":
        ticket_price = ticket_price - 2
        print("---------------------")
        print("Total price of the ticket is $", ticket_price)