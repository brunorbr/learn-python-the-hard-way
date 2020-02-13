name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_centimeters = round(height * 2.54)  # convert to centimeters
weight_kilograms = round(weight / 2.2046)  # convert to kilograms
print(f"Let's talk about {name}.")
print(f"He's {height} inches or {height_centimeters} centimeters tall.")
print(f'He {weight} pounds or {weight_kilograms} kilograms heavy.')
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
