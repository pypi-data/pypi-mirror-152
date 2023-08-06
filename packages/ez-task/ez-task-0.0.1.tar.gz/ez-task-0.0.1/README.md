# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.


install: pip install -i https://test.pypi.org/simple/ ez-task==0.0.1 

# Deploying:
    Step 1 - python3 -m build
    Step 2 - python3 -m twine upload dist/*
    Step 3 - for username, enter `__token__` for password paste in production token
    