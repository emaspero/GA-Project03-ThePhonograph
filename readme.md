![General Assembly's Logo](https://camo.githubusercontent.com/603ef5eae7d28900a9678ae96c6c60a9c72f8a059c328b28cf978df999cea1f8/68747470733a2f2f692e696d6775722e636f6d2f6c7a56493364382e706e67)

# The Phonograph - A Collection of Records

## Overview
![App home page screenshot](/thephonograph/main_app/static/images/Homepage%20Screenshot.png)
![Record detail page screenshot](/thephonograph/main_app/static/images/Record%20Detail%20Screenshot.png)


### Requirements
- The application includes at least 2 related models, one of them being the User, and the major CRUD functions have been implemented
- Some pages have a restricted access, therefore they can only be viewed by logged-in Users, the User is also able to sign-up/login, change the password and logout
- The Users receives feedback messages for success/fail form submissions, some of the forms have mandatory fields otherwise the User is not allowed to submit them; after every submission the forms are cleared of the data

### Technologies Used
- Git/GitHub
- HTML and CSS
- CSS Library
- Python
- Django
- PostgreSQL
- pgAdmin 4

### Team Members
- Elisabetta Maspero - [GitHub](https://github.com/emaspero) | [LinkedIn](https://www.linkedin.com/in/elisabetta-maspero-990bb3111/)
- Cristopher Carey - [GitHub](https://github.com/christopher-k-c) | [LinkedIn](https://www.linkedin.com/in/chriskcarey/)
- Sam Hackwood - [GitHub](https://github.com/samhackwood) | [LinkedIn](https://www.linkedin.com/in/samuel-hackwood-40b050233/)

### Process
##### Day 1
As a first step we started laying out the several connections using ERDs as that helped us to determine which Models were going to be part of the application and how they would interact with each other. We proceeded with creating a Trello board and assigning tasks to each member of the Team and, subsequently, using Figma we created a basic layout on how we would like the application to look like.

The focus for the first day was mainly to create the starting code for this project, creating our first two Models (Record and Tracklist) and adding the User auth functionality. At the end of the day, the User was able to sign-up, login and create/update/delete a Record and while in the record detail page the User was also able to add tracks to that specific record's tracklist.

###### Trello
![Trello board screenshot picture](/thephonograph/main_app/static/images/Trello%20Screenshot.png)
[Trello Board](https://trello.com/b/NnHgZg5d/project-03)
###### ERD (Entity Relationship Diagrams)
![ERDs screenshot](/thephonograph/main_app/static/images/ERDs%20Screenshot.png)
###### Wireframes
![Figma screenshot](/thephonograph/main_app/static/images/Figma%20Screenshot.png)
###### User Stories
![User Stories](/thephonograph/main_app/static/images/User%20Stories.png)

##### Day 2
During the second day, part of the time was dedicate to edit the sign-up form allowing the User to also input first name, last name and email address alongside the standard username and password. The functionality to allow the User to reset the password was also implemented. Two additional Models were created (Artist and Crate). The User was now allowed to add the favorite Records to its own Crate. The links-display has been amended, now a logged-in User can see and access several more pages compared to a non-logged-in User.

##### Day 3
Several bugs were fixed during the third day, starting from the one that was preventing the Artist's name to show up on the Record's detail page. We have added the functionality to clear a form after submission and the feedback messages after success/fail form submission were now fully functioning.

During the afternoon part of the Team started working on the styling for the application and the other part of the time started working on the readme file. 

##### Day 4
The Team has been focusing mainly on the styling using Tailwind CSS Library and deploying the app on Heroku.

### Deployed application link
[The Phonograph](https://thephonographsei64.herokuapp.com/)
### Challenges
As a Team we did find it challenging to fully understand what happens in the background with the CBVs, as the code is a lot shorter and less obvious than express, it's not always immediate to fully comprehend and subsequently work with the code. We did struggle understanding how to pull the data from models that were linked by relationships and show it on the page (eg. how to display the Artist name from the Record page considering that the relationship was a many to many). We decided to implement a CSS Library that we did not use during the lectures before, Tailwind, and does take time and understanding to be able to fully make the best out of these kind of features. When debugging we did run a vast amount of Google searches and the answers that we get from the web are not always the easiest to understand/implement due to the wide amount of different ways in which developers work, especially based on their experience. 

### Features to be added in the future
- The password reset email only gets sent to the Terminal at the moment, the link fully works and the functionality fully works, but it would be good to have it as an actual sent email instead. As well, we could implement a verification email to be sent upon registration of a new User.
- Implement on the homepage a carousel showing the latest record that have been added to the database.
- Different levels of privileges based on the User type. 
- User profile page.
- Make the app fully responsive.
- Install Tailwind with the config file, rather than just import it via the link, to fully explore how to personalize it.
- Embed Youtube video related to Artist/Record on the detail pages.
- Utilize a third party API, in this case Discogs API and include pagination. 
- Create a Label model that behaves in a similar way to the Artist model.