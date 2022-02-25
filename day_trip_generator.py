import random

#User Story: Store values in separate lists
destinations = ['Fiji', 'Greece', 'Mars', 'Moon']
resturants = ['Mcds', 'Cookout', 'BDubs', 'Kobe']
transportations = ['Rocket', 'Broom', 'Teleport', 'Walk']
entertainments = ['Movies', 'Biking', 'Shooting', 'People Watching']

#User Story: Randomly select or re-select (four user stories)
destination = random.choice(destinations)
resturant= random.choice(resturants)
transporation=random.choice(transportations)
entertainment = random.choice(entertainments)

#User Story: Allow user to re-select ANY if they don't like
#need a function to confirm, but has to pull in each of the chosen values from each list
print(f'Is {destination} the choice you want? ')
user_choice = int(input(f'Type 1 for yes or 2 for no '))
    # if(user_choice == 1):
    #     #lock in the first choice from random operation 
    # elif(user_choice == 2):
    #     #run the random operation again
    # else:
    #     #run the choice if/else again

#User Story: Confirm once user likes all options

#User Story: Display completed trip in console

notOkay = True
while notOkay:
    
    dest_choice = int(input(f'Type 1 for yes or 2 for no '))
    if(user_choice == 2):
        destination = random.choice(destination)

    user_choice = int(input(f'Type 1 for yes or 2 for no '))
    if(user_choice == 1):
        notOkay = False
        #lock in the first choice from random operation 
 