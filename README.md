# BM Excel Blaze - Interactive Digital Resume & Portfolio

A premium, interactive, and fully responsive digital resume website featuring glassmorphism design, light/dark themes, interactive skill filtering, clipboard capabilities, and an optimized stylesheet for instant high-contrast PDF printing.

## 🚀 Features

1. **Dual Themes**: Smooth dark (default) and light mode theme transitions with persistence cached in local storage.
2. **Interactive Skill Filtering**: Dynamically filter skills into technical competencies or professional/business skills.
3. **Save as PDF**: Built-in print trigger using a specialized CSS printing stylesheet. Strips background visual noises, adjusts font scales, and formats text in high-contrast monochrome suited for professional resume delivery.
4. **Quick Copy**: Click-to-copy email and phone details with automated toast notification feedback.
5. **Ultra Responsive Layout**: Adapts gracefully across desktop monitors, tablets, and mobile devices.

## 💻 Running Locally

To view the interactive resume on your computer:
1. Open the `resume/` folder.
2. Double-click the `index.html` file to launch it directly in any modern browser (Chrome, Edge, Firefox, Safari).

---

## 🌐 Deploying Live to GitHub Pages

You can host this resume online for free using GitHub Pages. Here is the step-by-step process:

### Step 1: Create a New Repository on GitHub
1. Log in to your GitHub account.
2. Click the **"+"** icon in the top-right corner and select **"New repository"**.
3. Name your repository (e.g., `resume` or `digital-cv`).
4. Keep it **Public** (required for free GitHub Pages).
5. Do **not** initialize it with a README, `.gitignore`, or license (leave those unchecked).
6. Click **"Create repository"**.

### Step 2: Initialize Git and Push Your Files
Open your terminal (PowerShell, Command Prompt, or Git Bash) in this `resume/` folder:

```bash
# Initialize a local Git repository
git init

# Add all files in the resume directory
git add .

# Create the initial commit
git commit -m "feat: initial interactive resume website"

# Rename default branch to main
git branch -M main

# Link to your new GitHub repository (replace with your actual GitHub URL)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git

# Push the code to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository page on GitHub.
2. Click on the **"Settings"** tab at the top.
3. On the left sidebar, click on **"Pages"** (under the "Code and automation" section).
4. Under **"Build and deployment"** -> **"Source"**, make sure it is set to **"Deploy from a branch"**.
5. Under **"Branch"**, select **`main`** (or your branch name) and the folder **`/ (root)`**.
6. Click **"Save"**.

After 1-2 minutes, GitHub will publish your site! The live URL will look like:
`https://YOUR_GITHUB_USERNAME.github.io/YOUR_REPO_NAME/`
