import random

collection = ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet', 'black', 'yellow']

secret_bag = ['pink', 'brown', 'green', 'pink', 'gray', 'red', 'black', 'purple', 'green', 'red', 'blue']

marbles_chosen = []

# can only pick 5 a day
tries_remaining = 5

# number of tries decreases for each marble selected
for x in range(6):
    if tries_remaining > 0:
        selection = random.choice(secret_bag)
        marbles_chosen.append(selection)
        tries_remaining -= 1
        if selection == 'green':
            collection.append(selection)
            secret_bag.remove(selection)
            if ('green' in collection):
                print(f'Green marble found! You have {tries_remaining} tries left.')
                break
    else:
        print('No more tries! See you tomorrow.')

print(f'Here are all the marbles chosen: {marbles_chosen}')

# output
# Green marble found! You have 2 tries left.
# Here are all the marbles chosen: ['purple', 'blue', 'green']
