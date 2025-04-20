import os
import subprocess
import random
import time

# Set your repository path
repo_path = r"D:\Likhith\PROJECT\git_cloner\daily_commit_bot"

# Change directory to the repo
os.chdir(repo_path)

# Number of commits (random between 5 to 10)
num_commits = random.randint(5, 10)

for i in range(num_commits):
    # Modify the file (increment the number)
    with open("number.txt", "r+") as f:
        number = int(f.read().strip())
        number += 1
        f.seek(0)
        f.write(str(number))
        f.truncate()

    # Run Git commands to commit changes
    subprocess.run(["git", "add", "number.txt"], check=True)
    subprocess.run(["git", "commit", "-m", f"Automated commit {i+1}"], check=True)

    # Wait for a random time (20-30 sec) between commits
    time.sleep(random.randint(5,10))

# Push all commits at once
subprocess.run(["git", "push", "origin", "main"], check=True)  # Change 'main' if needed
