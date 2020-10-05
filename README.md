# ASAPP QA Automation Challenge

## Project Structure:

#### api:
- tests: API automation suites
- models.py: data models
- services.py: API service controllers
- urls.py: API resources end-points

#### base:
- setup.py: base API/UI setup classes.
- constants.py: constants used in the tests (messages, logs, etc.).
- utils.py: helper methods
- urls.ini: property file for API/UI base URLS (set your IP address there)
 
#### ui:
- tests: UI automation suites
- page_elements.py: page element and locator classes
- pages.py: page objects

### video_demos:
Demos for some execution performed locally and from Docker.

## Setup
### Clone repo:
- Install Python 3.8 (recommended)
- git clone https://github.com/automatedguy/asapp-qa-challenge.git

### Create Virtual Environment:
- virtualenv asapp-env
- asapp-env\Scripts\activate

### Install packages:
- pip install requests
- pip install -U pytest
- pip install selenium
- pip install webdriver_manager
- pip install softest (soft assertions)

## Run tests
### Run test locally:
- Make sure you started qa_auto_challenge_prj-master project (on localhost)
- cd asapp-qa-challenge
- API suite: python -m unittest api\tests\auth_tests.py
- UI suite: python -m unittest ui\tests\login_tests.py

### Run test from Docker:
- Make sure you started qa_auto_challenge_prj-master project (on localhost)
- cd asapp-qa-challenge
- Edit urls.ini with you IP address (not localhost)
- docker pull python
- docker build -t asapp-qa-challenge .
- docker run -it --rm --name asapp-qa asapp-qa-challenge

## Notes:
### chromedriver 
Installed with an experimental library webdriver manager (download chromedriver automatically based on chrome version installed)
It is not 100% stable but I used in order to avoid chrome driver version mismatch

### Virtual Display Issues:
I need to fix some configuration issues with virtual display settings when running in the Docker container. :)
There are some issues while trying to locate elements in some cases. 