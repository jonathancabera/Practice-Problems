# FutureCode Algos — Practice Problems

Welcome to the **FutureCode Weekly Algorithm Practice** repository. Every week, a new algorithmic pattern is introduced along with a set of curated problems.

This repository is designed to be **forked**. You complete your work in your own personal fork and pull in new problems from this main repository each week.

---

## 🚀 Setup Instructions

### 1. Fork the repository

Click the **Fork** button at the top right of the [`FutureCode-Algos/Practice-Problems`](https://github.com/FutureCode-Algos/Practice-Problems) repository page to create a copy under your own GitHub account.

### 2. Clone your fork

Clone the forked repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/Practice-Problems.git
cd Practice-Problems
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

### 3. Add the upstream remote

Link your local repository to the original main repository so you can pull down new weekly patterns:

```bash
git remote add upstream https://github.com/FutureCode-Algos/Practice-Problems.git
```

Verify your remotes — you should see both `origin` (your fork) and `upstream` (the main repo):

```bash
git remote -v
```

Expected output:

```text
origin    https://github.com/YOUR_USERNAME/Practice-Problems.git (fetch)
origin    https://github.com/YOUR_USERNAME/Practice-Problems.git (push)
upstream  https://github.com/FutureCode-Algos/Practice-Problems.git (fetch)
upstream  https://github.com/FutureCode-Algos/Practice-Problems.git (push)
```

---

## 🔄 Weekly Workflow

Every week, a new pattern folder is pushed to the upstream repository. Follow these steps to pull the new folder into your local repository without overwriting your existing solutions.

### 1. Fetch upstream changes

Download the latest changes from the main repository:

```bash
git fetch upstream
```

### 2. Merge the updates into main

Make sure you are on your `main` branch, then merge the upstream changes:

```bash
git checkout main
git merge upstream/main
```

> **Note:** Because you only edit files inside existing weekly folders, and new weeks are added as entirely new folders, you should rarely encounter merge conflicts.

### 3. Push to your fork

Push the newly added pattern folder up to your GitHub fork:

```bash
git push origin main
```

### 4. Solve the problems

Navigate to the new week's folder, open the problems file, and start coding. Commit and push your solutions to your own fork as you normally would.

---

## ⚠️ Best Practices

- **Don't edit the original problem prompts or structure.** This ensures smooth merging when pulling from upstream.
- **Keep your `main` branch clean.** If you want to experiment with multiple solutions to the same problem, create a new branch in your local repo:

  ```bash
  git checkout -b optimize-sliding-window
  ```
