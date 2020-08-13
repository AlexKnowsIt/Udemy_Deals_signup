# Udemy_Deals

Signs you up to all temporary free courses on Udemy.

## Requirements

You need to set up selenium webdriver with geckodriver for Firefox for this programm to work. (For a tutorial visit https://www.lambdatest.com/blog/selenium-firefox-driver-tutorial/#Download&Setup)

## Usage

First open create_cookies.py and sign in to your account, so that the cookies are dropped inside a json file. Afterwards you can start UdemyPicker.py as long as your cookies are valid (normally around 60 days) and it will use the links provided (https://gist.github.com/temminks/bc90582aadd7d466fef67aed524d886d) to double check if the courses are free and then will sign you up for all courses.

You have to clone the gistfile into this repository under MydealzInput/gistfile1.txt (via git clone).
I recommend using this script in combination with a bash script to check via git for updates in the gist file.

> First open create_cookies.py and sign in to your account, so that the cookies are dropped inside a json file. 
Than you can start UdemyPicker.py as long as your cookies are valid and it will use the links provided (https://gist.github.com/temminks/bc90582aadd7d466fef67aed524d886d) to double check if the courses are free and then will sign you in.

There are 3 versions available for running this Code.

    Udemy() # uses the standard version, where you can see whats happening in the browser
    Udemy('h') # starts in headless mode for running on a server
    Udemy('d') # is optimized for docker and can be used with the docker image of selenium-firefox-standalone

There is also a docker Image now available. Just save your cookies and run 

    docker-compose up --build

## Contributions
Feel free to fork the project and add features that you miss or that can be improved and open a pull request. If you find a bug in the software or Udemy is changing again it's structure feel free and open an issue and I will see how I can fix the problem or merge your pull request.
