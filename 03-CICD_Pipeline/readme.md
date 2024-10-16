# Bitbucket Pipelines Exercise

### Preparation 

1. **Clone the Repository:**

  - Clone the repository to your local machine.
    ```bash
    git clone https://bitbucket.org/yourpersonalorg/software-engineering-ai/src/main/
    ```

    ### Group Repos: 
    - https://bitbucket.org/yourpersonalorg/AI-Academy-Group1/src/main/
    - https://bitbucket.org/yourpersonalorg/AI-Academy-Group2/src/main/
    - https://bitbucket.org/yourpersonalorg/AI-Academy-Group3/src/main/
    - https://bitbucket.org/yourpersonalorg/AI-Academy-Group4/src/main/

### Step 1: Set Up the Pipeline File 
1. **Create `bitbucket-pipelines.yml`:**
    - In the root directory of your repository, create a new file named `bitbucket-pipelines.yml` and add the following content:

    ```yaml
    image: python:3.8

    pipelines:
      default:
        - step:
            name: Install dependencies
            caches:
              - pip
            script:
              - pip install -r requirements.txt

        - step:
            name: Run tests
            script:
              - pip install pytest
              - pytest

        - step:
            name: Lint code
            script:
              - pip install pylint
              - pylint **/*.py
    ```

2. **Commit and Push:**
    - Commit your changes and push the file to the repository.
    ```bash
    git add bitbucket-pipelines.yml
    git commit -m "Add Bitbucket Pipelines configuration"
    git push origin main
    ```

### Step 2: Install Dependencies 
1. **Create `requirements.txt`:**
    - Add your project's dependencies to a `requirements.txt` file in the root directory.
    ```text
    pytest
    pylint
    ```

2. **Commit and Push:**
    - Commit and push the `requirements.txt` file.
    ```bash
    git add requirements.txt
    git commit -m "Add requirements.txt"
    git push origin main
    ```

### Step 3: Running the Pipeline
1. **Trigger the Pipeline:**
    - Push any changes to your repository to trigger the pipeline and monitor its progress in Bitbucket.

2. **Check Pipeline Status:**
    - Navigate to the Pipelines section in Bitbucket to view the status of your pipeline and ensure it completes successfully.

### Step 4: Interpreting the Results 
1. **Review the Output:**
    - Examine the output logs of each step (Install dependencies, Run tests, Lint code) to understand what happened during the pipeline execution.

2. **Fix Any Issues:**
    - If there are errors, fix them in your code, commit the changes, and push again to re-trigger the pipeline.

## Additional Task:
- Experiment with modifying the `bitbucket-pipelines.yml` to add more steps or integrate additional tools as you grow more comfortable.

# Conclusion
Completing these exercises will not only give you hands-on experience with resolving merge conflicts, but also enhance your understanding of key Git commands. Enjoy the process! What else do you want to dive into next?
