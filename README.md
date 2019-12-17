# REVU

REVU is a movie reviewing full-stack CRUD application with user login capabilities.
Users can create accounts, sign in, sign out and delete their accounts with ease.
Users can write film reviews that can then be read by both themselves and other users.
Users can then edit and delete their work.

## Demo

Click [here](https://revu-webapp.herokuapp.com/) for a demo...

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

### Features Left to Implement
I would like to link the search bar directly to the database as opposed to sifting through data on the page.
The current method works fine with a small number of users but would not scale well, and would also not work well in the case of pagination.

Also, further form validation is required, such as ensuring a more secure password is picked and a valid URL is being entered.

I would also like to give users the option to update and add more personal data, as well as display it in a user profile section.

I would like to add the ability for users to comment on, like and/or rate each others reviews.

## Testing

### Code Validation:
The HTML code was validated using [The W3C Markup Validation Service](https://validator.w3.org/)

The CSS code was validated using [The W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/)

The JavaScript code was validated using [JSHint](https://jshint.com/), [Code Beautify](https://codebeautify.org/jsvalidate), and [Esprima](https://esprima.org/demo/validate.html)

The Python code was validated using [Extends Class](https://extendsclass.com/python-tester.html)

### UX Testing:
Testing was carried out manually for this project, although error and exception handling was used for validating form data.

The sign-in page was tested by entering a combination of passwords and email addresses into the form input fields.
It was tested by entering both the password and email correctly, the correct email and incorrect password and vice versa.
The correct email from one account and correct password from another was tested, and both values entered incorrectly was tested.
It was also tested by leaving blank values. If the values are left blank the form will not submit, it is, however, reliant on the HTML rendered on the page which can be altered using developer tools and therefore is not secure.
The sign-up page was tested similarly. It has the same weakness with blank values.
It also needs further validation on the email and the password strength.
All links on both the sign up and sign in page were tested.

On the index page, all links were checked to see if they directed to the correct URL.
The Sign Out link was tested to ensure that it ended the user's session.
The delete account link was verified against the database that it was being permanently deleted.
The review sections were checked to ensure they matched the database, in number and content.

The REVU page was checked for each review to ensure the correct data was being rendered, and that it was being rendered correctly.

The New REVU page was checked for all links working, to see if form data was being submitted correctly and if form validation was working.
Error and exception handling was used to validate the rating, run-time, budget, and earnings form fields.
The database was checked to verify that the data was being inserted correctly, and not inserting when an error was thrown.

The My REVUs page was tested in the same manner as the index page.
The edit button was checked to ensure that it linked to an update form with the correct info pre-filled in the form input fields.
The delete button was verified against the database to ensure the record was permanently deleted.

The Edit REVU page was tested in the same manner as the New REVU page.

The sign out functionality was tested to ensure that it ended the user session and redirected to the login page.

This site was tested on multiple screen sizes (4.5" to 27") and devices (iPhone 6, 7, 7+, X, iPad, iPad pro, laptop screens and monitors)

## Deployment
GitHub was used for version control. Separate branches were used to implement each feature and merged with the master branch.

This site is hosted on Heroku. It is linked directly to the GitHub master branch and is deployed manually.

The live site can be found [here](https://revu-webapp.herokuapp.com/).

## Credits

### Content
- All film info for Star Wars Episodes IV, V, and V was taken from Wikipedia and IMBD
- The plots and reviews for Star Wars Episodes IV, V, and V were taken from IMBD

### Media
- The images for Star Wars Episodes [IV](https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg), [V](https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg), and [VI](http://t0.gstatic.com/images?q=tbn:ANd9GcRnTSmH4ckpqTGuLeBlI6DEnAagQq1Oha9c8fDlm2SRbcpEKZK0) can be found at these sources.

### Acknowledgements
- The log in/out functionality was taken from [this](https://www.youtube.com/watch?v=vVx1737auSE&list=WL&index=6&t=0s) tutorial
- The flash functionality was taken from the [Message Flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/) documentation
- The error and exception handling was taken from [this](https://docs.python.org/2/tutorial/errors.html) documentation
- Other sources included PEP 8 and W3Schools

This site is for educational purposes.