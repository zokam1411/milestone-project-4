# Milestone Project 4

---

<p id="top"></p>

<p align="center">
    <img src="media/logo.png" alt="FFRCCC logo">
</p>

## Fast & Furious RC Car Club

### 👉 [Heroku App](https://ffrccc-project.herokuapp.com/)

This Milestone project is a summary of learning and study from all modules of the Full Stack Developer Course, culminating in the creation of this Full Stack Framework Django project.

FFRCCC is a radio controlled car club. There are a number of users that the website will target and each of these user types will have a different need when using the website.

## Table of contents

- <a href="#project">Project Construction 👷</a>
- <a href="#ux">User Experience Design 🧠</a>
    - <a href="#us">User Stories</a>
    - <a href="#us">Design</a>
- <a href="#features">Features List 😲</a>
  - <a href="#existing">Existing Features</a>
  - <a href="#future">Future Features</a>
  - <a href="#defensive">Defensive Design</a>
- <a href="#databases">Databases 😲</a>
  - <a href="#dbchoice">Database Choice</a>
  - <a href="#dbmodeling">Data Modeling</a>
- <a href="#testing">Testing 🔥</a>
  - <a href="#manualtesting">Manual Testing</a>
  - <a href="#ustesting">User Stories</a>
  - <a href="#bugs">Bugs</a>



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

- As a Superuser, I want to add, edit and delete news.
- As a Superuser, I want to delete comments under individual news.#
- As a Superuser, I want to add, edit and delete products in shop.
- As a Superuser, I want to delete products reviews.

#### Administrator:

- As an Administrator, I want to be able to login to an administration panel.

<p id="design"></p>

### Design:

#### Color Scheme:

The main three colors in the app:

- ![007A47](docs/readmeimages/007A47.jpg) #007A47 used as a background for navbar

- ![198754](docs/readmeimages/198754.jpg) #198754 bootstrap "success" color used to higlight text and for buttons

- ![1F2A34](docs/readmeimages/1F2A34.jpg) #1F2A34 used as footer background

#### Typography:

The "Lato" font is the main font used throughout the whole website with Sans Serif as the fall back font in case the font isn't imported into the site correctly.
Lato offers a pleasing reading ability to the user and is easy on the eyes. Font is  clean, professional and very readable amongst all major languages.

#### Content Structure:

The application is primarily rectangular shaped. Buttons, cards have sharp edges to create consistent view for the user. Content is grouped in sections, an example of this would be the Home page:
- The main body of the page is horizontally separated into sections, we have a hero section, about section where user can read  about the club, and finally we have membership section where are informations about membership. Page is finished by footer where user can find quick site links, club address, email address and social links.

#### Wireframes:

The first raw design wos drawn on a piece of paper and then the idea was transferred to an advanced creator.

##################################################################################################################

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

<p id="features"></p>

## 3️⃣ Features List 😲

<p id="existing"></p>

### Existing features:

This application has different features for different user types. User status determines what kind of functions a given user has:
- Guest - unregistered / not logged in user.
- User - registered in database and logged in to application.
- Superuser - User with higher level of permissions. The Superuser can add, edit, delete news and shop products from the application level. He also ensures that comments and reviews does not break ethical rules.
- Admin - has the highest level of permissions and can login to admin panel.

#### Navigation:

The navbar serves as the main navigation for the site. It has bootstrap class="sticky" so it's always visible at the top of the page accross all pages of the site. The navbar has four links, which go to the home page, the news page, the the memberships page and shop.

The top header shows links to login and register and basket which is the link to the basket page and also to keep track of the ammount of the current basket.

Bottom header contains FFRCCC club logo, which links to the homepage.

![navigation1](docs/readmeimages/navigation-user.jpg)

- While user is logged in, instead of login and register links, he can see a 'My account' dropdown with options to go to the profile page or logout.

![navigation2](docs/readmeimages/navigation.jpg)

#### Footer:

The footer serves as secondary navigation. It has the same links as the navbar and also features the car club address and some external links to facebook, twitter and youtube.

![footer](docs/readmeimages/footer.jpg)

#### Home:

The home page is the landing page upon sign-up and login and the main hub for the app. The main features on this site is the hero image and a statement in header to say to check the online shop.

![home1](docs/readmeimages/home1.jpg)


Beneath all this there are about section where user can find info about club

![home2](docs/readmeimages/home2.jpg)


and membership section where user can find membership info and redirection button to membership page.

![home3](docs/readmeimages/home3.jpg)

#### News:

The news page serves as a place listing all of the news posts one page. The news are stacked in a single column vertically down the page on all screen sizes. Each news post shows the title, date of post, the author, the first 200 characters of introduction. By clicking on title user will be redirected to post view page.

![news1](docs/readmeimages/news1.jpg)

- Superuser can also add, edit and delete a post from this page.

![news2](docs/readmeimages/news2.jpg)

While adding post, Superuser can use HTML language to style post content.

![add_post](docs/readmeimages/add_post.jpg)

#### Post view

The post page shows the full details of the individual news. On the top users can see handy web navigation to back to all news.

![post1](docs/readmeimages/post1.jpg)

Underneath the post, there is an option to leave a comment about post.

- Guest users are limited to view the comments only.

![post2](docs/readmeimages/post2.jpg)

- User will only be able to leave a comment if he is logged in.

![post3](docs/readmeimages/post3.jpg)

- Superuser can delete any comment.

![post4](docs/readmeimages/post4.jpg)

#### Membership

The memberships page serves as the page to buy club membership. First two paragraphs are to explain membership conditions. On the bottom of the page - membership card is displayed.

![membership](docs/readmeimages/membership.jpg)


The content of membership card is dependent on the current membership of the user.

- Guest user will see membership card however 'Join' button will be disabled and 'You must login to purchase membership' text will be displayed.

![card1](docs/readmeimages/card1.jpg)

- Logged in user will see card with active button.

![card2](docs/readmeimages/card2.jpg)

Button click will take them to the stripe checkout page where they would add their card details and become member.

![stripe-checkout](docs/readmeimages/stripe-checkout.jpg)

After successful payment, succeess page will show up.

![success](docs/readmeimages/success.jpg)

- Now when the logged in user is also a member, card on membership page will display

![card3](docs/readmeimages/card3.jpg)

#### Shop

The shop page lists all the products which are listed on the product database and some tools to help user navigate these products so he can find exactly what he want when there are a lot more items in the store.

1. Search bar which filters the results down by taking the search criteria and matching it to the product title, the product description. If nothing is entered into the search box when the user presses submits a search query, the page will a toast error message to let the user know he needs to enter search criteria to search the store.

2. Above the products on the left user can find a total count of the number of items currently listed on the page. If a category has been chosen, the count will show the category selected and the total number of ptoducts e.g "Accessories (4)". If the user has used the search box, instead total producs user will see e.g 'Search query: "motor"'.

3. Above the products on the right user can find a sort dropdown which lets the user sort by 6 different criteria - Price (high - low), price (low - high), name (a - z), name (z - a), category (a - z), category (z -a).

4. All the products are listed in individual cards which show the, title, SKU, price and 'add to bag' button if product has no options to select or 'select option' button if it does. Clicking the image or title will take the user to the product detail page. Clicking on the 'add to bag' button will automatically add product to bag.

5. On the left of the website user can select one of the category to filter products or see all products.

![shop](docs/readmeimages/shop.jpg)

- Superuser can also add new add from this page.

![shop2](docs/readmeimages/shop2.jpg)

#### Product details

The prduct detail page shows more information about a particular product. This has some of the same information seen on the product detail card in the store page, with some extra details. On the product detail page the user can see the product image, title, SKU, price, full description and reviews with number of reviews. On top of this, the user can update the quantity and select the options of the product to purchse, if the product has options. There is also a primary button here to add the product to the basket, and a secondary button to go back to the store. On the top of the page there is handy site nav where user can back to prouct category. This will take user back to the store, but the products will be filtered by that category.

![Product detail](docs/readmeimages/product-detail.jpg)

- Guest users are limited to view the reviews only.

![review1](docs/readmeimages/review1.jpg)

- User will only be able to leave a review if he is logged in.

![review2](docs/readmeimages/review2.jpg)

- Superuser can delete any review.

![review3](docs/readmeimages/review3.jpg)

#### Bag

The basket page shows a summary of the products in the basket and the amount that the current basket equates to. Here, the user has the ability to update the quantity of each product or delete it entirely from the basket, or drop the whole basket.
On the right side of the bag page, there is summary section that shows Total, Discount, Delivery and Grand Total. This way, user is able to check the order summary at first glance even if he has added a lot of products to the shopping cart.

![bag](docs/readmeimages/bag.jpg)

If the user will enter the basket without products the information that bag is empty will show up.

![bag2](docs/readmeimages/bag2.jpg)

#### Checkout

The checkout page has two sections, the delivery and personal information details and the total of the order. The details is a form when, if logged in, lets the user save their information to their profile for a quicker checkout next time. The order summary is similar to the basket page, and shows the breakdown of the amounts with the option ot edit the basket and a final summary of how much will be charged. The final feature on the page is the payment information which uses Stripe to handle the payments. A successfull payment will take the users to the order success page showing the order summary.

![checkout](docs/readmeimages/checkout.jpg)

#### Profile

Logged in user have access to profile page. The profile page is split into two sections, delivery details and order history. The delivery details is a simple form and has an 'update information' button below to update their details on their profile, which would also reflect on the delivery details on the checkout page.

The order history shows a summary of the users previous orders. It is in the layout of a table and shows the order number, date, items and the grand total. Clicking the order number would take the user to the order summary where they would see a more detailed breakdown of the order.

![profile](docs/readmeimages/profile.jpg)

<p id="future"></p>

### Future Features:

**Watch product:** I would like to implement a feature to save favorite products, so that users can have quick access to this products in profile.

#### Features left for implementation (features required by this release but they were not implemented due to time)
- Integration with Travis for CI/CD and unit-test.

<p id="defensive"></p>

### Defensive Design:

- If 404 and 500 error occured within the site, a page that has the message of the error and 'Back to Home' button so that the user would not be lost. The templates of 404.html and 500.html are added to the root template directory

- Django Form Validation

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>


<p id="databases"></p>

## 4️⃣ Databasaes:

<p id="dbchoice"></p>

### Database Choice:

- Development phase SQLight database was used for the development which is installed with Django.

- Deployment phase PostgreSQL was used on deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by [Django's authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/).

<p id="dbmodeling"></p>

### Data Modeling:

Entity Relationship Diagram of this project:

![dbmodel](docs/readmeimages/dbmodel.jpg)

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

