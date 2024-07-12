def calculate_white_bread_measurements(flour_weight,
                                       hydration_percentage,
                                       long_rise=False):
  # Calculate the weight of water needed (hydration_percentage is in percentage)
  water_weight = (flour_weight * hydration_percentage) / 100

  # Round the water weight to the nearest 5 grams
  water_weight_rounded = round(water_weight / 5) * 5

  # Calculate the weight of salt (typically 2% of flour weight)
  salt_weight = (flour_weight * 2) / 100

  # Convert salt weight to teaspoons based on Diamond Crystal Kosher salt (1 teaspoon is approximately 3 grams)
  salt_teaspoons = salt_weight / 3

  # Round the salt measurement to the nearest 0.5 teaspoon
  salt_teaspoons_rounded = round(salt_teaspoons * 2) / 2

  # Calculate the weight of yeast based on whether it's a long rise (adjust if needed)
  yeast_weight = (flour_weight * 1) / 100
  if long_rise:
    yeast_weight *= 0.5  # Reduce yeast by half for long rise

  # Convert yeast weight to teaspoons based on Lowan Yeast Dried Instant (1 teaspoon is approximately 3 grams)
  yeast_teaspoons = yeast_weight / 3

  # Round the yeast measurement to the nearest 0.5 teaspoon
  yeast_teaspoons_rounded = round(yeast_teaspoons * 2) / 2

  # Calculate the total weight of the dough
  total_weight = flour_weight + water_weight_rounded + salt_weight + yeast_weight

  # Round the total dough weight to the nearest 5 grams
  total_weight_rounded = round(total_weight / 5) * 5

  return {
      'Plain White Flour': flour_weight,
      'Water': water_weight_rounded,
      'Kosher Salt': round(salt_teaspoons_rounded, 1),
      'Instant Dry Yeast': round(yeast_teaspoons_rounded, 1),
      'Total Dough Weight': total_weight_rounded
  }


# Function to display recipe options and get user's choice of hydration percentage
def get_hydration_choice():
  print("Choose a recipe for hydration percentage:")
  print("1. White Bread (70%)")
  print("2. Pizza Dough (75%)")
  print("3. Pitta Bread (75%)")

  choice = input("Enter the number of your choice: ")

  if choice == '1':
    return 70, "White Bread"
  elif choice == '2':
    return 75, "Pizza Dough"
  elif choice == '3':
    return 75, "Pitta Bread"
  else:
    print(
        "Invalid choice. Using a default hydration percentage of 70% for Basic White Bread."
    )
    return 70, "Basic White Bread"  # Default choice


# Get input from the user for flour weight (in grams)
# flour_weight = float(input("Enter the weight of flour you have (in grams): "))

# Get input from the user for flour weight (in grams) with input validation
while True:
  flour_weight_input = input("Enter the weight of flour you have (in grams): ")
  try:
    flour_weight = float(flour_weight_input)
    if flour_weight > 0:
      break  # Break out of the loop if the input is valid
    else:
      print("Please enter a positive number for the flour weight.")
  except ValueError:
    print("Please enter a number.")

# Get the user's choice of hydration percentage and recipe name
hydration_percentage, selected_recipe = get_hydration_choice()

# Ask the user if they're doing a long rise in the refrigerator
long_rise_input = input(
    "Are you doing a long rise in the refrigerator (yes/no)? ").strip().lower(
    )
if long_rise_input == 'yes':
  long_rise = True
else:
  long_rise = False

# Calculate measurements for white bread based on the chosen recipe and long rise option
measurements = calculate_white_bread_measurements(flour_weight,
                                                  hydration_percentage,
                                                  long_rise)

# Display the measurements without trailing zeros and rounded water, salt, yeast, and total dough weight to the nearest 5 grams
print(f"\nMeasurements for {selected_recipe}:")
for ingredient, weight in measurements.items():
  if ingredient == 'Kosher Salt' or ingredient == 'Instant Dry Yeast':
    print(f"{ingredient}: {weight} tsp")
  else:
    formatted_weight = '{:.1f}'.format(weight)
    print(f"{ingredient}: {formatted_weight.rstrip('0').rstrip('.')} g")

