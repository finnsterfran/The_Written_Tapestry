#### CODE INSTITUTE - Milestone Three Project
# The Written Tapestry



![Responsive-Screens](README_images/responsivecheck_website.png)

This project features a website for short-story writing. User registration of an account is required for stories to be posted. 

View this project here: &nbsp; &nbsp; [The Written Tapestry](https://the-written-tapestry.herokuapp.com/)

#UX 

# User Story

## Vistor to the website 
* I want to know what this website is about at first glance.
* I like to write short stories and want a place to showcase my writing.
* I want the colors to be soft and easy to the eyes as I could stay on this website for a stretch of time.
* I want to be able to delete or edit my writing when or if I want to.
* I want to search for stories that have been posted.
* I do not want any other writers to delete or edit my writing. 

### These goals are accomplished via:
* The story board features all writings posted onto the website by all the authors.
* The stories are searchable through author, category names and keywords.
* In logged in view, story board post will have the option of edit and delete for post of the user that is logged in. 
* Author's profile page is only accessible by user when logged in and features a list of all the stories posted by only this author which they are then able to edit and/or delete.

<hr>

# 1. Strategy
* The target users to this website are people who like to write, or read short stories. 
* The website should be visually balanced in layout and colors. Content should be spread out so information can be easily extracted in a glance. Color should be soft and suitable for viewing over a long period of time.
* Easy to register as a user. 
* The website should be easy to use with straightforward log in and log out function. 
* Search function covers keywords, author and category names.
* Only the owner of a post and administration have the ability to delete or edit said post.
* Provide some information about the different types of short stories.

# 2. Scope 
* Landing page features short description of types of short stories.
* Intent of the website is made clear from the first sentence.
* Registration is easy with just inputs of username, first & last names and a short bio. 
* Edit and deletion of post by owner of post via profile page and also on story board page.
* Administration can delete users and post.

# 3. Structure
* Consistant feature across all pages are:
    * logo at the top
    * navigation bar
    * copyright at footer
    * when logged in, message below navbar to show that user is logged in. 

* Forms:
    * single center aligned 
    * edit, submit, cancel, delete buttons at the bottom of the form

* Stories:
    * each story post is contained in a box with labels title, author, date, category name and composition.
    * all story post will be featured on the board. 
    * search box for easy finding of stories sit at the top of the main content. 

* Profile:
    * Viewable only when logged in as user or administration.
    * Standard(unchangeable) useravatar with username.
    * List of stories written by the user.

* Users:   
    * Viewable only when logged in as administration.
    * Box list of users with button to delete user.

# 4. Skeleton 
## Click [Wireframes](WIREFRAME.md) to view the wireframes.
<br>

# 5. Surface

## Colors:
* Background for all pages is *white*

* Button colors:
    
# 


## Commits 
* Commit 1 : create project skeleton - templates and static folder, app.py, env.py, requirements.txt, Procfile
* Commit 2 : create home.html. implement html for base.html, add styling in style.css
* Commit 3 : create board.html, login.html, profile.html, register.html. add views to app.py
* Commit 4 : layout adjustment for board.html
* Commit 5 : create new_post(add a Story). add url_for in base.html for registration, profile, new-post
* Commit 6 : make some minor tweaks to new_post.html and style.css
* Commit 7: create 404.html and error view in app.py. size change for register form. add icons to register.html and login.html
* Commit 8: add confirm password to register.html and app.py route for register.
* Commit 9: add useravatar image for profile.html and update its style in css. realign cards in profile.html.
* Commit 10: enable view for profile.html to display post by user. 
* Commit 11: add content to home.html. set card size to small for standardization of space and size throughout the grid.
* Commit 12: add edit_post.html. change size of logo.
* Commit 13: make user.html, this page is only accessible by administration. linked up search function. add header on all page to show what username is currently logged in. add materialize javascript code for selecting category name. admininstration received button with option to delete user and post.
* Commit 14: fix search functionality to allow search by category name, author, title and keywords. fix deletion of story, it did not delete from database. add deletion confirmation prompt to deletion button.
* Commit 15: add comments to app.py
* Commit 16: add a message in profile that informs if user has any story post, so that space will not be empty if there aren't any stories by this user.
* Commit 17: remove logo image. adjust placement of logo-brand.
* Commit 18: add structure.txt file. standardize the colors of all the buttons through the project. adjust layout of stories in get_stories.html
* Commit 19: Change debug to False
* Commit 20: fix date formate for registration, edit_story, new_story. remove date input for edit_story and new_story as this will be automatically generated for the db using datetime module. fix max character of story for edit_story
* Commit 21: change debug back to False again after switching it to True to make some minor testing of datetime
* Commit 22: change useravatar img, format style sheet
* Commit 23: add readme folder to store images for readme.md. resize profile image asa the bottom gets cut off. work on readme.md
* Commit 24: move link to log out in mobile view up to the correct line, it was out of the correct if statement block
* Commit 25: fix spacing and alignment for buttons on mobile screen. add if statement to hide registration link from session users
* Commit 26: possible fix for problem with log in format on mobile screen. user was unable to log in due to format match
* Commit 27: reduce the size for H3
* Commit 28: fix size of profile name in card of profile page, it was too wide and the end gets cut off if the name exceeds a certain number of characters
* Commit 29: fix font size for user.html. reduce max characters for username in registration




## Credits 

### Content
* awaitingthemuse.wordpress.com
* wikipedia

useravatar png 
https://www.pngaaa.com/

### Testing

w

