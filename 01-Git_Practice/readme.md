# Lab Exercise: Git and Pull Requests

## Objective
Learn the basics of Git, create a repository, make changes, and submit a pull request.

## Prerequisites
- Git installed on your machine
- Bitbucket/GitHub account

## Steps

### 1. Setup and Initialization 
- **Clone the repository to your local machine:**
  ```bash
  git clone https://bitbucket.org/blbitbucket01/software-engineering-ai/src/main/
  ```
  ### Group Repos: 
  - https://bitbucket.org/blbitbucket01/AI-Academy-Group1/src/main/
  - https://bitbucket.org/blbitbucket01/AI-Academy-Group2/src/main/
  - https://bitbucket.org/blbitbucket01/AI-Academy-Group3/src/main/
  - https://bitbucket.org/blbitbucket01/AI-Academy-Group4/src/main/


- **Create a new repository on GitHub:** (if not using bitbucket)

  1. Go to GitHub.
  2. Click on the **New** button to create a new repository.
  3. Name your repository (e.g., `git-lab-exercise`), add a description, and choose whether it will be public or private.
  4. Initialize the repository with a README file.

### 2. Creating a Branch 
- **Create and switch to a new branch:**
  ```bash
  git checkout -b feature-branch-yourname
  ```
- **Verify that you are on the new branch:** 
  ```bash
  git branch
  ```

### 3. Making Changes 
- **Create a new file called hello_world.txt and add some content:**
  ```bash
  echo "Hello, World!" > hello_world.txt
  ```
- **Add the new file to the staging area:** 
  ```bash
  git add hello_world.txt
  ```
- **Commit your changes with a descriptive message:** 
  ```bash
  git commit -m "Add hello_world.txt with a greeting message"
  ```

### 4. Pushing Changes 
- **Push your branch to GitHub:**
  ```bash
  git push origin feature-branch-yourname
  ```

### 5. Creating a Pull Request 
- **Go to your repository on Bitbucket/GitHub:**

  1. Navigate to your repository page.
  2. You should see a prompt to compare & pull request for your recently pushed branch.

- **Click on the "Compare & pull request" button:**

  1. Review the changes you made.
  2. Add a title and description for your pull request.
  3. Click on **Create pull request**.

### 6. Review and Merge 
- **Review the pull request:**

  1. Check the changes and ensure everything looks good.
  2. Optionally, request a review from a teammate.

- **Merge the pull request into the main branch:**

  1. Click on the **Merge pull request** button.
  2. Confirm the merge.

- **Delete the feature branch (optional):**
  ```bash
  git branch -d feature-branch
  git push origin --delete feature-branch
  ```

Navigate to your repository page.
You should see a prompt to compare & pull request for your recently pushed branch.


## Conclusion
You’ve successfully created a repository, made changes in a new branch, and submitted a pull request! This exercise helps you understand the basic workflow of Git.