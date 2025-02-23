import os
import subprocess

# Set your repository path
repo_path = r"D:\Likhith\PROJECT\git_cloner\daily_commit_bot"

# Change directory to the repo
os.chdir(repo_path)

# Run Git commands to commit and push changes
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Automated daily commit"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)  # Change 'main' if needed
