# lab14-Pick6.py
import random

#numberOfTickets = int(input("How many tickets do you want?  >> "))
allNumbers = list(range(1, 100, 1))
winner = []
my_tickets = []
ticketValue = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}
tickets_wanted = 100000
expences = tickets_wanted * 2
runningTotal = 0

def pick_winner():
    for i in range(6):
        winner.append(random.choice(allNumbers))


#crates as many tickets as you want to buy
def create_tickets(numtickets):
    for i in range(numtickets):
        oneTicket = []
        for n in range(6):
            oneTicket.append(random.choice(allNumbers))
            if len(oneTicket) == 6:
                my_tickets.append(oneTicket)
                oneTicket = []


def check_tickets(tickets, expences):
    runningTotal = 0
    for t in tickets:
        matches = 0
        for n in range(len(t)):
            if t[n] == winner[n]:
                matches += 1
        runningTotal += ticketValue[matches]
       # print(runningTotal, end=', ')
    print("\nmy ROI is: " + str((runningTotal - expences)/expences) + "\nearnings: " + str(runningTotal) + "\nexpences: " + str(expences))


pick_winner()
create_tickets(tickets_wanted)
check_tickets(my_tickets, expences)
print(winner)



