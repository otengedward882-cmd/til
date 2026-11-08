#!/usr/bin/env python3
"""
Graph-Greener
=============
Author: otengedward882-cmd
License: MIT
Description: A lightweight, dependency-free Python tool to generate backdated
             Git commits across the past year to populate GitHub contribution graphs.
"""

import os
import random
import subprocess
from datetime import datetime, timedelta


def get_positive_int(prompt: str, default: int = 20) -> int:
    """Prompt the user for a positive integer with a fallback default."""
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("⚠️ Please enter a positive integer greater than 0.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid whole number.")


def get_repo_path(prompt: str, default: str = ".") -> str:
    """Prompt the user for a valid local Git repository path."""
    while True:
        user_input = input(f"{prompt} (default current directory): ")
        if not user_input.strip():
            return default
        if os.path.isdir(user_input):
            return user_input
        else:
            print("⚠️ Directory does not exist. Please enter a valid local path.")


def get_filename(prompt: str, default: str = "data.txt") -> str:
    """Prompt the user for the file to modify."""
    user_input = input(f"{prompt} (default {default}): ")
    if not user_input.strip():
        return default
    return user_input.strip()


def random_date_in_last_year() -> datetime:
    """Generate a random datetime within the past 365 days."""
    today = datetime.now()
    start_date = today - timedelta(days=365)
    random_days = random.randint(0, 364)
    random_seconds = random.randint(0, 23 * 3600 + 3599)
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return commit_date


def make_commit(date: datetime, repo_path: str, filename: str, message: str = "graph-greener!") -> None:
    """Append a timestamp line to the file, stage it, and commit with custom date environment variables."""
    filepath = os.path.join(repo_path, filename)
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")

    subprocess.run(["git", "add", filename], cwd=repo_path, check=True)

    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env, check=True)


def main() -> None:
    print("=" * 60)
    print("🌱 Welcome to graph-greener - GitHub Contribution Graph Commit Generator 🌱")
    print("=" * 60)
    print("This tool will help you fill your GitHub contribution graph with custom commits.\n")

    num_commits = get_positive_int("How many commits do you want to make", 20)
    repo_path = get_repo_path("Enter the path to your local git repository", ".")
    filename = get_filename("Enter the filename to modify for commits", "data.txt")

    print(f"\n🚀 Making {num_commits} commits in repo: {repo_path}")
    print(f"📝 Modifying file: {filename}\n")

    for i in range(num_commits):
        commit_date = random_date_in_last_year()
        print(f"[{i + 1}/{num_commits}] Committing at {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        make_commit(commit_date, repo_path, filename)

    print("\n🚀 Pushing commits to your remote repository...")
    push_result = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)

    if push_result.returncode == 0:
        print("\n✅ All done! Check your GitHub contribution graph in a few minutes.\n")
    else:
        print("\n⚠️ Push encountered an issue. You can manually run: git push -u origin main")

    print("Tip: Use a dedicated repository for best results. Happy coding!\n")


if __name__ == "__main__":
    main()
