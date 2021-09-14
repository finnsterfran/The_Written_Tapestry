# GitHub
1. Create Project Repository in GitHub using Code Institute template.
Repository can be found here : [The Written Tapestry](https://github.com/finnsterfran/The_Written_Tapestry)
2. From GitHub repository, click green Gitpod button to open a workspace for this repository on Gitpod.
3. All codes were written in Gitpod. 

<br>

# Gitpod - IDE
1. For connection to a database and for deployment of this app, an env.py needs to be set up. This file also has to be listed in .gitignore so that it will not be pushed to Github as it contains sensitive information.
2. Generate secret_key for app. 
3. Set up env.py like so: 
    * import os
    * os.environ.setdefault("IP", "0,0,0,0")
    * os.environ.setdefault("PORT", "5000")
    * os.environ.setdefault("SECRET_KEY", "(**insert generated secret key in there**)")
    * os.environ.setdefault("MONGO_URI", "(**insert copied connection string from MongoDB in here**)")
    * os.environ.setdefault("MONGO_DBNAME", "(**insert database name here**)")

<br>

# MongoDB 
1. Create an account in MongoDB.
2. Create new cluster.
3. In database, create a new database 
    * tapestry 
4. In database, create new collections:
    * category_name
    * stories
    * users
5. Back in database deployment page, click on CONNECT
    * Select the second option out of three - Connect your application
    * Ensure that the correct driver is selected - Python, 3.12 or later
    * Copy connection string to clipboard - THIS information goes into MONGO_URI in env.py and Heroku config vars.

<br>

# Heroku
1. In Gitpod, set up files that Heroku need:
    * requirements.txt specifies what packages (python) are needs for this app. 
    * This can be created in the terminal like so : 
        **pip3 freeze --local > requirements.txt**
    * A Procfile is needed to specify where Heroku will look to kick start this app. 
    * This can be created in the terminal like so: 
        **echo web: python app.py > Procfile**

2. A heroku account is needed to deploy the app to this platform.
    * Go to [Heroku](https://heroku.com)
    * Create an account

3. Create an app.
    * Select option to create an app
    * Name the app and select the region Europe
    * Create the app

4. Connect Heroku to the Github repository 
    * Click button to connect to Github
    * Search for the repository to connect to 
    * Connect to said repository

4. Set up configuration variables in Heroku
    * In settings, scroll down to 'Reveal Config Vars'
    * Inputs:
        * IP | 0.0.0.0
        * PORT | 5000
        * MONGO_DBNAME | (**database name**)
        * MONGO_URI | (**url that was copied from the database connection**)
        * SECRET_KEY | (**secret key that was generated for this app**)


5. Push requirements.txt and Profile to Github 
    * git add -A 
    * git commit -m "add requirements.txt and Procfile"

6. Enable automatic deployment
    * In Heroku app, select enable automatic deploys > deploy branch
    * When app is successfully built, you will see the success message "Your app was successfully deployed"
    * From this point forth, your app is live and you can click the VIEW to launch it.

<hr>
End of Page





