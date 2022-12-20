import random
import csv
import os
from datetime import datetime, timedelta

# List of first names
first_names = ['John', 'Jane', 'Mike', 'Marry', 'Bob', 'Samantha']

# List of less common last names
last_names = ['Rodriguez', 'Garcia', 'Martinez', 'Lopez', 'Perez', 'Gonzalez']

# Open a CSV file for writing
with open("full_names.csv", "w", newline="") as csvfile:
  # Create a CSV writer
  writer = csv.writer(csvfile)
  
  # Generate 100 random full names and save them to the CSV file
  used_last_names = set()
  for i in range(1, 101):
    # Select a random last name, with a 0.02 probability of selecting a last name that has already been used
    if random.random() < 0.02 and used_last_names:
      last_name = random.choice(list(used_last_names))
    else:
      last_name = random.choice(last_names)
      used_last_names.add(last_name)
      
    # Generate a random date of birth between 01/01/1985 and 01/01/1997
    start_date = datetime(1985, 1, 1)
    end_date = datetime(1997, 1, 1)
    dob = start_date + (end_date - start_date) * random.random()
    
    full_name = random.choice(first_names) + " " + last_name
    writer.writerow([full_name, dob.strftime("%m/%d/%Y")])

# Get the absolute path of the resulting CSV file
csv_path = os.path.abspath("full_names.csv")

# Print a message indicating that the code ran successfully
print("Code ran successfully")

# Print the path of the resulting CSV file
print(f"100 random full names saved to: {csv_path}")
