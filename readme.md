![General Assembly's Logo](https://camo.githubusercontent.com/603ef5eae7d28900a9678ae96c6c60a9c72f8a059c328b28cf978df999cea1f8/68747470733a2f2f692e696d6775722e636f6d2f6c7a56493364382e706e67)

# SEI Project 3: The Phonograph - A Collection of Records

### Table of Contents
- Project Overview
    - Team Members
- Goal
    - Technologies Used
- Approach Taken
- Challenges and Wins
    - Challenges
    - Wins
    - Bugs
    - Key Learnings
- Future Enhancements 

---

# Project Overview
![App home page screenshot](/main_app/static/images/Homepage%20Screenshot.png)
![Record detail page screenshot](/main_app/static/images/Record%20Detail%20Screenshot.png)

### Link to the deployed app: [The Phonograph](https://hydro-keener-88414.herokuapp.com/)

## Team Members
- Elisabetta Maspero - [GitHub](https://github.com/emaspero) | [LinkedIn](https://www.linkedin.com/in/elisabetta-maspero-990bb3111/)
- Cristopher Carey - [GitHub](https://github.com/christopher-k-c) | [LinkedIn](https://www.linkedin.com/in/chriskcarey/)
- Sam Hackwood - [GitHub](https://github.com/samhackwood) | [LinkedIn](https://www.linkedin.com/in/samuel-hackwood-40b050233/)


# Goal
- The application includes at least 2 related models, one of them being the User, and the major CRUD functions have been implemented
- Some pages have a restricted access, therefore they can only be viewed by logged-in Users, the User is also able to sign-up/login, change the password and logout
- The Users receives feedback messages for success/fail form submissions, some of the forms have mandatory fields otherwise the User is not allowed to submit them; after every submission the forms are cleared of the data

## Technologies Used
- Git/GitHub
- HTML and CSS
- CSS Library
- Python
- Django
- PostgreSQL
- pgAdmin 4


# Approach Taken
##### Day 1
As a first step Chris and I started laying out the several connections using ERDs as that helped us to determine which Models were going to be part of the application and how they would interact with each other. We proceeded with creating a Trello board and assigning tasks to each member of the Team and, subsequently, using Figma we created a basic layout on how we would like the application to look like. For this project I was the Team Leader. I took charge of creating the Git Repository and shared that with the Team Members at first and to create the User authentication functionality.

The focus for the first day was mainly to create the starting code for this project, creating our first two Models (Record and Tracklist) and adding the User authentication functionality. At the end of the day, the User was able to sign-up, login and create/update/delete a Record and while in the record detail page the User was also able to add tracks to that specific record's tracklist.

###### Trello
Our Trello board was an incredible tool which allowed us to always know what each Team member was working on, in order to avoid working on the same tasks. Unfortunately one of the Teammates fell ill during the initial stages of the project, therefore two of us ended up setting up the board and the first tasks. We virtually met every single day attending daily stand-ups and deciding, each day, what we were going to work on and spend some time debugging and tackling bugs/bockers. We started by setting up the skeleton of the project together and we proceeded by discussing which item we wanted to work on. 
![Trello board screenshot picture](/main_app/static/images/Trello%20Screenshot.png)
[Trello Board](https://trello.com/b/NnHgZg5d/project-03)
###### ERD (Entity Relationship Diagrams)
![ERDs screenshot](/main_app/static/images/ERDs%20Screenshot.png)
###### Wireframes
![Figma screenshot](/main_app/static/images/Figma%20Screenshot.png)
###### User Stories
- As a User, I want to be able to store all my favorite records in one place.
- As a User, I want an easy way to access information about each record that I have stored in the database.
- As a User, I want to be able to see which records were produced by one specific Artist.
- As a User, I want to scroll through the record database in an interactive way which resembles going through a real record collection.
- As a User, I want to be able to easily add records to the database.
- As a User, I want to be able to quickly scan the latest uploads when I open the application in the browser.
- As a User, I want the application to have a stylish and clean design, emphasizing each Album’s image.
- As a User, I want to see ho9w many other Users have one same record in their collections.

##### Day 2
During the second day, I worked on editing the sign-up form allowing the User to also input first name, last name and email address alongside the standard username and password. 
I achieved so by implementing the below code:
```
class NewUserForm(UserCreationForm):
   email = forms.EmailField(required=True)
   first_name = forms.CharField(max_length=100, required=False)
   last_name = forms.CharField(max_length=100, required=False)
 
   class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
 
   def save(self, commit=True):
       user = super(NewUserForm, self).save(commit=False)
       user.email = self.cleaned_data['email']
       user.first_name = self.cleaned_data['first_name']
       user.last_name = self.cleaned_data['last_name']
 
       if commit:
           user.save()
       return user
```
The functionality to allow the User to reset the password was also implemented. 
Two additional Models were created (Artist and Crate), Chris worked on the Artist model while I took charge of the Crate one instead. The Crate displays the User’s favorite Records by fetching the records with a for loop in the crate_detail.html page.
```
class Crate(models.Model):
   name = models.CharField(max_length=100)
   records = models.ManyToManyField(Record)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
 
   def __str__(self):
       return self.name
 
   def get_absolute_url(self):
       return reverse('crates_detail', kwargs = {'pk': self.id})
```
The authorisation features were implemented as a logged-in User could see and access several more pages compared to a non-logged-in User. In order to achieve this I imported and implemented the below items in the views.py:
```
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
```

##### Day 3
Several bugs were fixed during the third day, starting from the one that was preventing the Artist's name from showing up on the Record's detail page. We have added the functionality to clear a form after submission and the feedback messages after success/fail form submission were now fully functioning.

During the afternoon Chris started working on the styling for the application while I spent my time working on the ReadMe file.

##### Day 4
The Team has been focusing mainly on the styling using Tailwind CSS Library and deploying the app on Heroku. We decided to implement Tailwind as we wanted to challenge ourselves with implementing a new library and upon doing some research we came to the conclusion that Tailwind has become more and more popular. Using Tailwind ended up being a little more challenging than expected as we spent quite some time researching the documentation, but it ended up being more intuitive than creating CSS styling from scratch.

# Challenges and Wins
## Challenges
This was my first experience as a Team Leader and it started in an arduous situation as, unfortunately, one of the Team Members got sick and was unable to attend during several days spent working on this project. The best decision, upon having an open conversation with the other Member, was to remove some features that we wanted to add, for example having pagination and using a third party API. That allowed us to achieve all of our Goals respecting the deadline.
As a Team we did find it challenging to fully understand what happens in the background with the CBVs, as the code is a lot shorter and less obvious than express, it's not always immediate to fully comprehend and subsequently work with the code. We did struggle understanding how to pull the data from models that were linked by relationships and show it on the page (e.g. how to display the Artist name from the Record page considering that the relationship was a many to many). We decided to implement a CSS Library that we did not use during the lectures before, Tailwind, and it does take time and understanding to be able to fully make the best out of these kinds of features. When debugging we did run a vast amount of Google searches and the answers that we got from the web were not always the easiest to understand/implement due to the wide amount of different ways in which developers work, especially based on their experience. When this happened, we ended up spending more time researching the documentation and learning more about how other developers implemented their solutions and fixes and, once we gained a deeper knowledge, we were able to solve our own bugs as well. 
## Wins
- First experience implementing Tailwind. Learning how to implement a different CSS Library is always tricky at the beginning, once we spent some time going through the documentation and started using it, then it became easier to understand how to use Tailwind features. 
- This was my first experience with Python/Django. Django documentation is an incredibly precious resource as it is very intuitive to navigate and allows beginner-level developers to discover built-in functionalities and how to implement them according to the Project’s needs. I truly enjoyed researching the documentation as it helped me understand a lot more of how Django works. 

## Bugs
- While deploying the app something went wrong with Heroku, we ended up re-deploying it on a different link.
- The styling does not work properly in every single page.

## Key Learnings
This project was my first experience as a Team Leader, a few of my biggest takeaways were realizing the importance of listening to my Teammates, being able to take charge and responsibility where needed, ensuring that we all updated our Trello board and respected our daily deadlines that we would decide every morning during our stand-ups. 
Another key learning was experience how different documentation can be. Django documentation was a real pleasure to explore, while Tailwind’s one was trickier to navigate.

# Future Enhancements
- The password reset email only gets sent to the Terminal at the moment, the link fully works and the functionality fully works, but it would be good to have it as an actual sent email instead. As well, we could implement a verification email to be sent upon registration of a new User.
- Implement on the homepage a carousel showing the latest record that have been added to the database.
- Different levels of privileges based on the User type. 
- User profile page.
- Make the app fully responsive.
- Install Tailwind with the config file, rather than just import it via the link, to fully explore how to personalize it.
- Embed Youtube video related to Artist/Record on the detail pages.
- Utilize a third party API, in this case Discogs API and include pagination. 
- Create a Label model that behaves in a similar way to the Artist model.
