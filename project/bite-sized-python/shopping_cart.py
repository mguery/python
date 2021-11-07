flowerpot = int(input('how many pots? '))
seeds = int(input('how many packs of seeds? '))
soil = int(input('how many bags of soil? '))

flowerpot_price = 4.00
seeds_price = 1.00
soil_price = 5.00

tax_rate = 0.06 # convert percentage to decimal 6/100 = .06

cost_of_items = (flowerpot_price * flowerpot) + (seeds * seeds_price) + (soil * soil_price)

total_cost = (cost_of_items * tax_rate) + cost_of_items

print(total_cost)
