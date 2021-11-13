# Prompts
adjective1 = input('Enter adjective: ').lower()
game = input('Enter name of an outdoor game: ').lower()
adjective2 = input('Enter 2nd adjective: ').lower()
friend = input('Enter name of a friend: ').capitalize()
verb = input('Enter verb ending in ing: ').lower()
adjective3 = input('Enter 3rd adjective: ').lower()

story = (f'The adjectives I used in this mad libs are {adjective1}, {adjective2}, and {adjective3}. The last game I watched was {game} with my friend {friend}. We both thought it was {verb}.')

print(story)
