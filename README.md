# REVU

REVU is a movie reviewing full-stack CRUD application with user login capabilities.
Users can create accounts, sign in, sign out and delete their accounts with ease.
Users can write film reviews that can then be read by both themselves and other users.
Users can then edit and delete their work.

## Demo

Click [here](https://revu-webapp.herokuapp.com/) for a demo...

###### Demo Log In Details:
email: test1@mail.com

password: @123456Aa

## UX

The functional requirements for this project are:
1. The ability for users to create, read, update and delete their content
2. User accounts so user data and content is accessible from any device
3. The ability for users to read other users content
4. The ability for users to be able to search content

### Wireframes: 
Click [here](https://github.com/Olan1/revu/tree/master/wireframes) for the wireframe designs.

## Technologies
1. Python
2. Flask
3. Jinja
4. MongoDB
5. HTML
6. CSS
7. JavaScript
8. jQuery
9. Materialize

## Features

### Existing Features
REVU allows for users to create accounts with login validation and password encryption.
Users can sign in and out, and delete their accounts.

Once logged in users can use the search bar feature to search reviews created by both themselves and other users.
Users can create reviews, edit them, view both their work and others, and delete them.
Users can only edit and delete reviews that are linked to their profile.

All forms validate the data entered:
- The sign-up form ensures no empty fields, verifies email address and ensures password has uppercase and lowercase letters, a digit, a special character, and is at least 8 characters long
- The sign-in page verifies that both the email address and password are in the database and are linked to the same user
- The Edit/New REVU forms check for empty fields, valid URLs, fields requiring numeric values are numbers, and the rating falls within the specified range
- Local storage is used to auto-fill form data when invalid values are entered

### Features Left to Implement
I would like to link the search bar directly to the database as opposed to sifting through data on the page.
The current method works fine with a small number of users but would not scale well, and would also not work well in the case of pagination.

I would also like to give users the option to update and add more personal data, as well as display it in a user profile section.

I would like to add the ability for users to comment on, like and/or rate each others reviews.

The user agreement also needs to be filled with relevant content as it currently it contains Lorem Ipsum text.

## Testing

### Code Validation:
The HTML code was validated using [The W3C Markup Validation Service](https://validator.w3.org/)

The CSS code was validated using [The W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/)

The JavaScript code was validated using [JSHint](https://jshint.com/), [Code Beautify](https://codebeautify.org/jsvalidate), and [Esprima](https://esprima.org/demo/validate.html)

The Python code was validated using [Extends Class](https://extendsclass.com/python-tester.html)

### UX Testing:
Testing was carried out manually for this project. Error and exception handling was used for validating form data.

The sign-in page was tested by entering a combination of passwords and email addresses into the form input fields.
It was tested by entering both the password and email correctly, the correct email and incorrect password, and vice versa.
The correct email from one account and correct password from another was tested, and both values entered incorrectly was tested.
It was also tested by removing the required attribute from the HTML inputs leaving blank values.

The sign-up page was tested by removing the required attribute from the HTML inputs and leaving blank values.
Multiple emails, both valid and invalid were tested.
Passwords that satisfied none of the validation criteria, some of it and all of it, in different variations were tested.

On the index page, all links were checked to see if they directed to the correct URL.
The Sign Out link was tested to ensure that it ended the user's session.
The delete account link was verified against the database that it was being permanently deleted.
The review sections were checked to ensure they matched the database, in number and content.

The REVU page was checked for each review to ensure the correct data was being rendered, and that it was being rendered correctly.

The New REVU page was tested to see if form data was being submitted correctly and if form validation was working.
Error and exception handling was used to validate the image URL, rating, run-time, budget, and earnings form fields.
The database was checked to verify that the data was being inserted correctly, and not inserting when an error was thrown.
When the form validation threw an error, the form textarea values were verified to contain the correct auto-filled data, and that no data was auto-filled if the user navigated away from the New REVU page.

The My REVUs page was tested in the same manner as the index page.
The edit button was checked to ensure that it linked to an update form with the correct info auto-filled in the form input fields.
The delete button was verified against the database to ensure the record was permanently deleted.

The Edit REVU page was tested in the same manner as the New REVU page.
The input fields were verified against the database to ensure the correct data was auto-filled.

The sign out functionality was tested to ensure that it ended the user session and redirected to the login page.

This site was tested on multiple screen sizes (4.7" - 27") and devices (iPhone 6, 7, 7+, X, iPad, iPad pro, several laptop screens and monitors)

## Deployment
GitHub was used for version control. Separate branches were used to implement each feature and merged with the master branch.

This site is hosted on Heroku. It is linked directly to the GitHub master branch and is deployed manually.

The live site can be found [here](https://revu-webapp.herokuapp.com/).

###### Demo Log In Details:
email: test1@mail.com

password: @123456Aa

## Credits

### Content
- All film info for Star Wars Episodes IV was taken from [Wikipedia](https://en.wikipedia.org/wiki/Star_Wars_(film)) and [IMDB](https://www.imdb.com/title/tt0076759/):
- All film info for Star Wars Episodes V was taken from [Wikipedia](https://en.wikipedia.org/wiki/The_Empire_Strikes_Back) and [IMDB](https://www.imdb.com/title/tt0080684/):
- All film info for Star Wars Episodes VI was taken from [Wikipedia](https://en.wikipedia.org/wiki/Return_of_the_Jedi) and [IMDB](https://www.imdb.com/title/tt0086190/):

### Media
- The images for Star Wars Episodes [IV](https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg), [V](https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg), and [VI](http://t0.gstatic.com/images?q=tbn:ANd9GcRnTSmH4ckpqTGuLeBlI6DEnAagQq1Oha9c8fDlm2SRbcpEKZK0) can be found at these sources.

### Acknowledgements
- The log in/out functionality was sourced from [this YouTube tutorial](https://www.youtube.com/watch?v=vVx1737auSE&list=WL&index=6&t=0s)
- The flash functionality was sourced from the [Message Flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/) documentation
- The error and exception handling was sourced from [this](https://docs.python.org/2/tutorial/errors.html) documentation
- Other sources included [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [W3Schools](https://www.w3schools.com/)

This site is for educational purposes.
