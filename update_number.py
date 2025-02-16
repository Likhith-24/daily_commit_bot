import os

# Read the current number from the file
with open("number.txt", "r") as f:
    number = int(f.read().strip())

# Increment the number
number += 1

# Write the updated number back to the file
with open("number.txt", "w") as f:
    f.write(str(number))

# Run Git commands to commit and push
os.system("git add number.txt")
os.system(f'git commit -m "Auto-incremented number: {number}"')
os.system("git push origin main")  # Change "main" if your branch is different
