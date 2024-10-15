import random
import csv

# Define sample data for random generation
toy_names = ['Teddy Bear', 'Lego Set', 'Dollhouse', 'Action Figure', 'Puzzle', 'RC Car', 'Building Blocks', 'Water Gun', 'Board Game', 'Stuffed Elephant']
manufacturers = ['ToyCo', 'Lego', 'PlayHouse', 'HeroToys', 'BrainGames', 'Speedsters', 'BuildIt', 'SplashToys', 'FunGames', 'ToyLand']
age_ranges = ['1-3', '2-5', '3-6', '4-7', '5-10', '6-12', '7-14', '8-14', '9-15']

# Generate a large number of toy data entries (e.g., 100,000 entries)
num_entries = 100000
toy_data = [['SKU', 'Toy Name', 'Price', 'Quantity', 'Age Range', 'Manufacturer']]

for i in range(1, num_entries + 1):
    sku = str(100 + i)  # Sequential SKU
    toy_name = random.choice(toy_names)
    price = round(random.uniform(5.00, 100.00), 2)  # Random price between 5 and 100
    quantity = random.randint(1, 100)  # Random quantity between 1 and 100
    age_range = random.choice(age_ranges)
    manufacturer = random.choice(manufacturers)
    
    toy_data.append([sku, toy_name, str(price), str(quantity), age_range, manufacturer])

# Define file path
file_path_large = './large_toy_inventory.csv'

# Write the large dataset to a CSV file
with open(file_path_large, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(toy_data)

file_path_large
