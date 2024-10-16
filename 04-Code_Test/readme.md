# Python Program Exercise with Bitbucket Pipelines

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

### Step 2: Create Python Program and Tests 

1. **Create `html_color_changer.py`:**
    - Add the following content to `html_color_changer.py`:

    ```python
    # html_color_changer.py
    import random

    def change_background_color(file_path):
        colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33C4"]
        new_color = random.choice(colors)
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            new_content = content.replace('<body>', f'<body style="background-color:{new_color};">')
            with open(file_path, 'w') as file:
                file.write(new_content)
            return new_color
        except Exception as e:
            return str(e)


    if __name__ == "__main__":
        file_path = "index.html"  # Update this to your actual file path
        change_background_color(file_path)
    ```

2. **Create `index.html`:**
    - Add the following content to `index.html`:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fun Page</title>
    </head>
    <body>
        <p>Welcome to the fun page!</p>
    </body>
    </html>
    ```

3. **Create `test_html_color_changer.py`:**
    - Add the following content to `test_html_color_changer.py`:

    ```python
    # test_html_color_changer.py
    import pytest
    from html_color_changer import change_background_color

    @pytest.fixture
    def sample_html(tmpdir):
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Fun Page</title>
        </head>
        <body>
            <p>Welcome to the fun page!</p>
        </body>
        </html>
        """
        file_path = tmpdir.join("index.html")
        file_path.write(html_content)
        return str(file_path)

    def test_change_background_color(sample_html):
        new_color = change_background_color(sample_html)
        assert new_color in ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33C4"]
        
        with open(sample_html, 'r') as file:
            content = file.read()
        
        assert f'style="background-color:{new_color};"' in content
    ```

### Step 3: Install Dependencies 
1. **Create `requirements.txt`:**
    - Add your project's dependencies to a `requirements.txt` file in the root directory.
    ```text
    pytest
    pylint
    ```

2. **Commit and Push:**
    - Commit and push the `requirements.txt` file and Python files.
    ```bash
    git add requirements.txt html_color_changer.py test_html_color_changer.py index.html
    git commit -m "Add requirements.txt and Python files"
    git push origin main
    ```

### Step 4: Running the Pipeline 
1. **Trigger the Pipeline:**
    - Push any changes to your repository to trigger the pipeline and monitor its progress in Bitbucket.

2. **Check Pipeline Status:**
    - Navigate to the Pipelines section in Bitbucket to view the status of your pipeline and ensure it completes successfully.

### Step 5: Interpreting the Results
1. **Review the Output:**
    - Examine the output logs of each step (Install dependencies, Run tests, Lint code) to understand what happened during the pipeline execution.

2. **Fix Any Issues:**
    - If there are errors, fix them in your code, commit the changes, and push again to re-trigger the pipeline.

## Additional Task:
- Experiment with modifying the `bitbucket-pipelines.yml` to add more steps or integrate additional tools as you grow more comfortable.

# Conclusion
Completing this exercise will give you hands-on experience with setting up and using Bitbucket Pipelines along with running tests and modifying HTML files. 
