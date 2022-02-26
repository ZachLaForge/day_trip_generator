import random

#User Story: Store values in separate lists
destinations = ['Fiji', 'Greece', 'Mars', 'Moon']
resturants = ['Mcds', 'Cookout', 'BDubs', 'Kobe']
transportations = ['Rocket', 'Broom', 'Teleport', 'Walk']
entertainments = ['Movies', 'Biking', 'Shooting', 'People Watching']

#User Story: Randomly select or re-select (four user stories)
#User Story: Function to have a single responsibility

def random_choice(the_list):
    potato = random.choice(the_list)
    return potato

destination = random_choice(destinations)
resturant= random_choice(resturants)
transporation=random_choice(transportations)
entertainment = random_choice(entertainments)

isFirst = True
notOkay = True
while notOkay:
    if isFirst:
        print(f"""
This is your current day trip

Destination: {destination}
Resturant: {resturant}
Transportation: {transporation}
Entertainment: {entertainment}
        """)
        isFirst = False

    change_or_not = input("""
would you like to change anything?

1. Destination
2. Resturant
3. Transportation
4. Entertainment
    """)

    if change_or_not == '1':
        destinations.remove(destination)
        destination = random_choice(destinations)
    elif change_or_not == '2':
        resturants.remove(resturant)
        resturant= random_choice(resturants)
    elif change_or_not == '3':
        transportations.remove(transporation)
        transporation=random_choice(transportations)
    elif change_or_not == '4':
        entertainments.remove(entertainment)
        entertainment = random_choice(entertainments)
        

    print(f"""
This is your current day trip

Destination: {destination}
Resturant: {resturant}
Transportation: {transporation}
Entertainment: {entertainment}
        """)
#User Story: Confirm y/n if you're satisfied with your trip selections 
    user_choice=input(f'Are you satisfiied with your current day trip? Y/n')
    if(user_choice.lower() == 'y'):
        notOkay = False

#User Story: Display completed trip into the console

        print(f"""
        
Enjoy your stay at {destination}  !
I heard the food at {resturant} is wonderful !
I hope {transporation} is as comfortable as possible !
Have a great time during {entertainment}
        
        """)