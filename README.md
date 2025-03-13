This code will open a Chrome test browser, and then will log in through its login page, and will then navigate to the overview landing page and then will read in the portfolio balance value and output that value as a command line print statement.

This program must be executed in the following way:
python main_calvin.py "URL of the login page" "URL of the account overview page" "username or email address" "password"

Once the balance value has been reviewed, the program will shut down and will output the value of the portfolio on the command line.

NOTE: Please note that this program will only work on accounts that don't require 2FA/MFA.  In the event that the account is set up with 2FA/MFA the user may be required to manually intervene to get the overview page to appear.

NOTE: This program was based on an assignment I did for a data science course that I took last year, however I did use GeminiAI to help me with some syntax issues that I was having as well as how to grab data from the screen using XPath

NOTE: This program was created in Windows and it will be necessary to download the ChromeDriver folder from https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/win32/chromedriver-win32.zip and extract the folder to the folder where the program is located, or whatever chrome driver is necessary for the system it's being run on.  Other versions of the chrome driver can be found here: https://googlechromelabs.github.io/chrome-for-testing/

