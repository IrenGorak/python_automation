# UI testing in Python and pytest
This project for https://demoqa.com/ site.
This repository contains a UI testing framework developed in 
Python using the Pytest framework. It is designed to automate the testing of web applications' user interfaces. 
UI testing is essential for ensuring that your web application functions correctly from a user's perspective.



Table of Contents 
  - Getting Started
       - Prerequisites
       - Installation
  - Running Tests
  - Project Structure
  

**Getting Started**

 - Prerequisites 
Before running the tests, make sure you have the following prerequisites installed:

Python (version 3.7 or higher)
Pytest (installed via pip)
Webdriver (e.g., ChromeDriver, GeckoDriver) compatible with your browser
Any other dependencies specific to your project


- Installation
1. Clone this repository to your local machine: 
git clone https://github.com/IrenGorak/python_automation.git

2. Navigate to the project directory:
cd select_own_directory

3. Install the required Python packages:
pip install -r requirements.txt

4.Download and configure the appropriate Webdriver for your browser and operating system. 
Make sure the Webdriver executable is in your system's PATH.


**Running Tests**
pytest tests/

**Project Structure**

- data = needed data for generated functions
- generator = functions for generated color/ person_info/ file
- locators = locators for current page
- pages = functions/method for special page
- tests = assert/ test for special page
