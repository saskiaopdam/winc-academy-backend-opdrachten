# Assignment Report

## Three components of my solution

1. A test file testing different routes
2. A yml file defining a build - test - deploy sequence
3. A secret key set up at the VPS and GitHub

The routes defined in main.py (index, cow, donkey and duck) are tested in test_main.py. The yml file makes sure that after pushing changes tests are run and if they pass the content of the VPS gets updated. The "secrets" variable in the yml file refers to the secrets set in the GitHub repo.

## Three problems I encountered (when running pipeline jobs)

1. flask not found - solution: add flask to requirements.txt
2. assertion error - solution: fix typo in test_main.py
3. ssh not found - added -----BEGIN OPENSSH PRIVATE KEY----- and -----END OPENSSH PRIVATE KEY----- to GitHub settings

When making changes and pushing them to GitHub the pipeline I set up failed a few times. I read the error annotations in the Actions section of the repo to understand the cause and find a solution.

## Another thing I want to share

The flask app was already set up on my Digital Ocean droplet with the index and cow route. (WSGI and Gunicorn + Deployment exercise). For the CD (continuous deployment) assignment I added 2 more routes. I can see those changes reflected in my folder on the VPS when logging in through the terminal app. However, I don't see them in my browser when opening <IP>/donkey or <IP>/duck. So far I haven't been able to figure out why.
