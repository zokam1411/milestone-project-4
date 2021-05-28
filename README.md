# Milestone Project 3

---

<p id="top"></p>

## Fast & Furious RC Car Club

### 👉 [Heroku App](https://ffrccc-project.herokuapp.com/)

This Milestone project is a summary of learning and study from all modules of the Full Stack Developer Course, culminating in the creation of this Full Stack Framework Django project.

FFRCCC is a radio controlled car club. There are a number of users that the website will target and each of these user types will have a different need when using the website.

## Table of contents

- <a href="#project">Project Construction 👷</a>
- <a href="#ux">User Experience Design 🧠</a>
    - <a href="#us">User Stories</a>
    - <a href="#us">Design</a>

<p id="project"></p>

## 1️⃣ Project Construction 👷

The application uses Django 3 which is one of the most popular development tools. The project uses Separation of Concern amongst the applications to utilise the Django Framework effectively.

In addition to using Django, sqlite was used in the early stages of the project as a test database for local testing. Sqlite is an independent, highly reliable SQL database engine that supports all normal relational database management functions. Before deployment, I switched to Postgres witch is open source software that provides a fully technical and easy-to-use object-oriented relational database management system.

Thanks to Django, the application administrator has full access to a completely custom admin dashboard where he can create, read, update and delete records in any proposed application model as needed.

For the testing of the store and subscriptions, a test credit card can be used by inputting the following details:
- Card Number: 4242 4242 4242 4242
- Exp date: 04/24
- CVC: 424
- ZIP: 42424

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

<p id="ux"></p>

## 2️⃣ User Experience Design 🧠

<p id="us"></p>

### User stories:

#### Guest (un-registered) User:

- As a Guest user, I want to view information about the club.
- As a Guest user, I want to see club contact informations.
- As a Guest user, I want to read the latest news about the club.
- As a Guest user, I want to read about benefits of membership.
- As a Guest user, I want to view all products in the shop.
- As a Guest User, I want to search for an item in the shop.
- As a Guest user, I want to sort prducts by price, name and category.
- As a Guest user, I want to see products within selected category.
- As a Guest User, I want to see detailed view of an item.
- As a Guest User, I want to be able to add items into the bag.
- As a Guest User, I want to be able to manipulate a bag content.
- As a Guest User, I want to see total count of the basket on every page.
- As a Guest User, I want to know how Grand Total was calculated.
- As a Guest User, I want easily fill out delivery information.
- As a Guest User, I want to view an order summary once a purchase is made.
- As a Guest User, I want to recieve an email confirmation when a purchase is made.
- As a Guest User, I want to be able to register for an account.
- As a Guest user, I want to be able to view the site on any device I may have.
- As a Guest user, I want app to be visually appealing and easy in use.

#### Registered User:

- As a Registered User, I want to have the ability to Login to the site via my registered details.
- As a Registered User, I want to be able to recover my account password.
- As a Registered User, I want to be able to comment under individual club news.
- As a Registered User, I want to be able to purchase club membership.
- As a Registered User, I want to have a profile page where I can see my details.
- As a Registered User, I want to have a profile page where I can see my purchase history.
- As a Registered User, I want to write a products reviews.


#### Superuser:

- As a superuser, I want to add, edit and delete news.
- As a superuser, I want to delete comments under individual news.#
- As a superuser, I want to add, edit and delete products in shop.
- As a superuser, I want to delete products reviews.

#### Administrator:

- As an Administrator, I want to be able to login to an administration panel.

