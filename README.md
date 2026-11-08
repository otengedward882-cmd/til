# 🌿 Graph-Greener

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Git](https://img.shields.io/badge/git-compatible-orange.svg)](https://git-scm.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](#prerequisites)

> **Paint your GitHub contribution graph green with realistic backdated commits.**  
> A lightweight, dependency-free automation tool for developers who want a vibrant and active profile.

---

## 📑 Table of Contents
- [What is Graph-Greener?](#-what-is-graph-greener)
- [How It Works](#-how-it-works)
- [Prerequisites](#-prerequisites)
- [Quick Start Guide](#-quick-start-guide)
  - [Step 1: Create a Dedicated Repository](#step-1-create-a-dedicated-repository)
  - [Step 2: Clone or Download](#step-2-clone-or-download)
  - [Step 3: Run the Script](#step-3-run-the-script)
- [Enabling Private Contributions on GitHub](#-enabling-private-contributions-on-github)
- [Troubleshooting & FAQs](#-troubleshooting--faqs)
- [Project Structure](#-project-structure)
- [License & Disclaimer](#-license--disclaimer)

---

## 🚀 What is Graph-Greener?

**Graph-Greener** is an interactive, zero-dependency Python utility designed to generate backdated Git commits across the past 365 days.

Whether you're starting fresh, recovering lost activity from an old account, testing Git commit timestamps, or creating custom profile patterns, Graph-Greener automates the entire process in seconds.

### ✨ Key Features
- **Zero Third-Party Dependencies**: Runs on standard Python 3 (`subprocess`, `datetime`, `random`, `os`).
- **Realistic Timestamp Generation**: Distributes commits randomly across days, hours, and minutes of the past year.
- **Interactive Prompts**: Choose your own commit volume, target repository, and data file.
- **Safe & Isolated**: Works best inside a dedicated dummy repository so your real codebase history remains 100% clean.
- **Automated Staging & Pushing**: Stages, commits with custom `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`, and pushes directly to GitHub.

---

## 🔍 How It Works

GitHub's contribution graph tracks commits using two pieces of metadata:
1. **Author/Committer Email**: Must match an email address associated with your GitHub account.
2. **Commit Timestamp (`GIT_AUTHOR_DATE` & `GIT_COMMITTER_DATE`)**: Tells GitHub when the commit took place.

Graph-Greener modifies a tracking file (`data.txt`), sets the appropriate Git environment variables to random points in the past 365 days, creates the commit, and pushes the history to your remote repository.

---

## 📋 Prerequisites

Before running the tool, ensure you have:
1. **Python 3.6+** installed on your system. Verify with:
   ```bash
   python --version
   ```
2. **Git** installed and configured with your GitHub credentials:
   ```bash
   git config --global user.name "YOUR_GITHUB_USERNAME"
   git config --global user.email "YOUR_GITHUB_EMAIL@example.com"
   ```

---

## 🛠️ Quick Start Guide

### Step 1: Create a Dedicated Repository
1. Go to [github.com/new](https://github.com/new).
2. Name your repository (e.g., `priv` or `activity-log`).
3. Set visibility to **Private** (recommended) or **Public**.
4. **Important**: Leave "Add a README file", `.gitignore`, and license **unchecked** (an empty repository).
5. Click **Create repository**.

### Step 2: Clone or Download
Clone your new repository to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/priv.git
cd priv
```

Place `main.py` inside this folder.

### Step 3: Run the Script
Open your terminal inside the repository folder and execute:
```bash
python main.py
```

Follow the prompts:
```text
============================================================
🌱 Welcome to graph-greener - GitHub Contribution Graph Commit Generator 🌱
============================================================
This tool will help you fill your GitHub contribution graph with custom commits.

How many commits do you want to make (default 20): 50
Enter the path to your local git repository (default current directory): .
Enter the filename to modify for commits (default data.txt): data.txt

Making 50 commits in repo: .
Modifying file: data.txt

[1/50] Committing at 2026-03-12 14:22:10
[2/50] Committing at 2026-07-08 19:40:55
...
Pushing commits to your remote repository...
✅ All done! Check your GitHub contribution graph in a few minutes.
```

---

## 💡 Enabling Private Contributions on GitHub

If you created a **Private** repository, GitHub hides private activity on your public profile by default. To make your green squares visible:

1. Navigate to your GitHub profile (`https://github.com/YOUR_USERNAME`).
2. Scroll to your **Contribution Graph**.
3. In the top-right corner above the graph, click the **Contribution settings** dropdown.
4. Check **Private contributions**.

Your green squares will now appear on your public profile while your repository remains strictly private!

---

## ❓ Troubleshooting & FAQs

### Q: Why aren't the green squares appearing on my profile?
Check the following:
1. **Email Address Mismatch**: GitHub only attributes commits if the commit email exactly matches a verified email in your account.
   - Run `git config user.email` in your terminal to see the email used.
   - Go to [github.com/settings/emails](https://github.com/settings/emails) to ensure that email is present and shows **Verified**.
2. **Private Contributions Toggled Off**: Follow the steps in [Enabling Private Contributions](#-enabling-private-contributions-on-github).
3. **Correct Year Selected**: Make sure the current year is selected on the right sidebar of your contribution graph.
4. **GitHub Cache Delay**: GitHub contribution graphs typically take between 1 to 5 minutes to rebuild after a push.

### Q: Can I delete the commits later?
Yes! Since you created this in a dedicated repository (e.g., `priv`), simply delete the repository on GitHub (`Settings` -> `Danger Zone` -> `Delete this repository`), and all associated contribution squares will be removed.

---

## 📁 Project Structure

```text
priv/
├── main.py          # Main execution script
├── data.txt         # File appended by commits
├── requirements.txt # Documentation of dependencies (Standard Library only)
├── .gitignore       # Standard git ignore file
├── LICENSE          # MIT Open Source License
└── README.md        # Comprehensive documentation
```

---

## 📄 License & Disclaimer

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

> **Disclaimer**: This tool is created for educational exploration of Git internals, timestamp experimentation, and profile customization. Users are responsible for using it in accordance with GitHub's Community Guidelines.
