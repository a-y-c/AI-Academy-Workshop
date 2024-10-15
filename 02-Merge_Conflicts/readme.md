# Git Merge Conflict Resolution Exercise

## Preparation 
- Go back to your Git Repository.
    ```bash
    git pull
    git checkout main
    echo "Initial content" > file.txt
    git add file.txt
    git commit -m "Initial commit"
    ```

## Creating Branches and Making Changes 
- Create and switch to a new branch called `feature-branch-conflict-yourname`.
    ```bash
    git checkout -b feature-branch-conflict-yourname
    ```
- Modify `file.txt` in `feature-branch-conflict-yourname`:
    ```bash
    echo "Change from feature branch" > file.txt
    git add file.txt
    git commit -m "Change from feature branch"
    ```
- Switch back to `main` branch and make a different change to `file.txt`:
    ```bash
    git checkout main
    echo "Change from main branch" > file.txt
    git add file.txt
    git commit -m "Change from main branch"
    ```

## Creating the Conflict 
- Merge `feature-branch-conflict-yourname` into `main` to create a conflict.
    ```bash
    git merge feature-branch-conflict-yourname
    ```

## Resolving the Conflict 
- Open `file.txt` to see the conflict markers.
- Manually resolve the conflict by choosing which change to keep or by combining both changes.
- Remove conflict markers and save the file.
- Add the resolved file and commit the merge.
    ```bash
    git add file.txt
    git commit -m "Resolved merge conflict"
    ```

## Additional Git Commands

### Using `git diff` 
- Make another change in the `main` branch:
    ```bash
    echo "Another change from main branch" >> file.txt
    git add file.txt
    ```
- Before committing, use `git diff` to see the changes.
    ```bash
    git diff
    ```
- Now commit the changes:
    ```bash
    git commit -m "Another change from main branch"
    ```

### Using `git log`
- View the commit history to see all your changes:
    ```bash
    git log
    ```
- Explore different options with `git log` to see more details or a shorter summary:
    ```bash
    git log --oneline
    git log --stat
    ```


## Exercise: Using `git reset` to Undo a Commit

#### Scenario:
You have a commit history like this:
```
a1b2c3 (HEAD -> main) Fix bug
d4e5f6 Add new feature
g7h8i9 Initial commit
```

You realize the commit `Add new feature` shouldn't be there.

#### Task:
1. Use `git reset` to remove the last commit but keep the changes in your working directory.
2. Use `git reset` to remove the last commit and discard the changes.

#### Solution:
To remove the last commit but keep the changes in your working directory, use:
```bash
git reset --soft HEAD~1
```

To remove the last commit and discard the changes, use:
```bash
git reset --hard HEAD~1
```

Use `git status` to see your history now;



# Conclusion
Completing this exercise will give you a hands-on understanding of resolving conflicts. Dive in, and let the merge magic happen!
