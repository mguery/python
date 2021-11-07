name = input('whats your name? ').capitalize()
city = input('whats the city? ').capitalize()
temp = int(input('whats the temp now? '))

# if >80 degrees, wear shorts and bring shades
if temp >= 80:
           outfit = 'wear shorts and bring shades'
# if 60-79 degress, bring light jacket
elif temp <=79 and temp >=60:
           outfit = 'bring a light jacket'
# if <59, wear coat, hat, gloves, and scarf
else:
    outfit = 'wear coat, hat, gloves, and scarf'

advice = (f'Hi {name}! It is {temp} degrees in {city}. Today you should {outfit}.')

print(advice)
