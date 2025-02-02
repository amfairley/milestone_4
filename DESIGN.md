![Website logo](/linktologoimage.png)

---

# Design

See [README.md](/README.md) for information on project goals, user stories, security, future developments, technologies used, user feedback, credits, and acknowledgements. <br>
See [TESTING.md](/TESTING.md) for information on the test driven development of the website, manual and automated testing of the site, bugs encountered, and website analytics. <br>
See [DEV.md](/DEV.md) for an overview of the continuous integration and deployment process, how I set up my development environment, and deployment steps.

---

## Table Of Contents
1. [Five Planes of UX](#five-planes-of-ux)
    - [Strategy](#strategy)
        * [Viability and Feasibility](#viability-and-feasibility)
    - [Scope](#scope)
        * [Back-end](#back-end)
        * [Front-end](#front-end)
    - [Structure](#structure)
        * [base.html](#basehtml)
        * [index.html](#indexhtml)
        * [allauth](#allauth)
        * [search_results.html](#search_resultshtml)
        * [trips.html](#tripshtml)
        * [cancel_trip.html](#cancel_triphtml)
        * [checkout.html](#checkouthtml)
        * [account_settings.html](#account_settingshtml)
        * [delete_account.html](#delete_accounthtml)
        * [rooms.html](#roomshtml)
        * [Information Architecture](#information-architecture)
        * [Interactive Experience](#interactive-experience)
    - [Skeleton](#skeleton)
        * [wireframes](#wireframes)
    - [Surface](#surface)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Images](#images)
2. [Features](#features)



## Five Planes of UX
Outlined here is the design process for this webapp. Building up the webapp using the 5 planes of UX design allows seemless transition from a business idea through to the finished polished product whilst maintaining the criteria for the site are kept, accessibility guidelines are met, and that the final product is fit for purpose.

### Strategy

- **What value does the project provide?** From the business perspective; this project provides a website to display and rent out their rooms to potential guests. It allows the business owner to track trends in booking, see feedback from guests, and edit/update information about their rooms. From a customer perspective it provides a website where they can securely and safely book a room for their visit, find out more about the hotel and resort, and track previous trips that they have taken.
- **What are the business needs?** The business needs are to provide an intuitive, pleasant looking, and accessible website to entice more users to book rooms at their resort. They business also requires agency over the information they give out, being able to update specifications to rooms to reflect renovations. With enough use, the website will be able to provide information about trends in trips (time of year/amount of guests) and feedback in the form of reviews so that the business can continue to grow and match public demand.
- **Who is the target audience?** The target audience will primarily be potential travellers. This will be split into sub sections of international travellers to Georgia who are looking for more of a nature focussed holiday that a city break, and domestic travellers seeking a break from city life. The business owners are another target audience, as they will need to have faith that the website will provide all the functionality that they need and that the website meets their standards for how they wish to portray the hotel. 
- **What are the user requirements and expectations?** The users can make their own profile in order to save their personal details and track previous trips. They also expect to be able to Create, Read, Update, and Delete their own profile, personal data, and reviews whenever they want. It is expected that they can search for available rooms to rent and to safely and securely pay for the rooms.

#### Viability And Feasibility
Followed is an analysis of the user stories and above user and business needs ranked from 1 (least important/viable) to 5 (most important/viable):
|   Task |   Importance | Viability/Feasibility |
| --------- | ------------- | ----------------- |
| Clear home screen showing the purpose of the website | 5 | 5 |
| Intuitive website design | 5 | 5 |
| Resort information | 4 | 5 |
| Information on services offered | 4 | 5 |
| How to get to the resort | 4 | 5 |
| Hotel FAQs | 4 | 5 |
| Show reviews of the hotel | 3 | 3 |
| Clear error pages | 5 | 5 |
| Contact information for the hotel | 5 | 5 |
| Contact information for the developer | 2 | 5 |
| Safe and secure user authentication | 5 | 4 |
| Allow signup/login using email instead of username | 3 | 5 |
| Allow users to delete their account | 5 | 4 |
| Allow users to sign up to a newsletter | 3 | 5 |
| Allow users to leave a review | 5 | 4 |
| Simple search for available rooms | 5 | 4 |
| Filter/sort room search results | 4 | 3 |
| See room information | 5 | 5 |
| Allow users to view previous trips | 4 | 4 |
| Allow users to book through the website | 5 | 3 |

Overall, most of the targets meets a ranking of at least 4 in either importance or viability. Extra effort will be given to those with higher importance but lower viability (due to currently not knowing how to implement the features required) and those with low importance and higher viability will be included due to their ease of inclusion.<br>
Showing reviews of the hotel has been rated a 3/3, as this will depend on the availability of reviews on websites such as TripAdvisor and whether they can be accessed via API if you are not the resort owner. Should this prove not possible, showing reviews will be added to "future development" once reviews have been received through this website, giving a resource of reviews to display. <br>
The "safe and secure user authentication" will be achieved by using Django AllAuth, this will also meet the user story requirements for signing in via social media, email validation, easy login/logout, password updating, and password recovery.
Stripe will be used for payment and booking, meeting the further user stories of seeing an order confirmation and saving their details for future.

### Scope
#### Back-end
Multiple tables in a relational database will be required to meet all of the targets for this project. These models will be:
- **User**: A Django model that will be updated using Django AllAuth and consisting of a number of fields that will not be queried or used in the project. The fields of note will be: ID, email, password, is_superuser (for admin privileges on the site).
- **Profile**: This will handle the user profile data. The fields will be: ID, User (foreign key; one to one), newsletter (True if signed up to a newsletter), and the information fields required for stripe such as first and last names, address information and contact details etc.
- **Room**: This will hold all the information about the specific rooms. The fields will be: ID, name, sanitised_name (for display on the website), amenities (a JSON list of amenity IDs), description, image, price, unavailability (a JSON list of book dates).
- **Amenities**: This will have the amenity information for rooms such as air conditioning, balcony, bed size etc. The fields will be: ID, name, sanitised_name (for display on the website), icon (a string of the html for a fontawesome icon).
- **Trip**: This will hold the information of a trip that has been booked. It will have: ID, Profile (foreign key, many to one), Room (foreign key, one to one), start_date, end_date, cancelled (boolean field with defautl to False).
- **Review**: This will have the information for a review of a trip. The fields will be: ID, Trip (foreign key, one to one), clean_rating (rating cleanliness 1-5), food_rating (rating the food 1-5), service_rating (rating the service received 1-5), staff_rating (rating the staff attitude/helpfulness etc 1-5), overall_rating (1-5), review_content (text). 

#### Front-end
The website will be built using Django, allowing for template inheritance and partitions functionality into different apps, resulting in less duplicate code written and quicker load times for the user.

**Templates**
- **base.html**: This will be the base template that the others call from to ensure a cohesive structure across the website. Present here will be:
    - All the header meta information
    - Links to styling and JavaScript scripts
    - The header with the site logo, a booking form, and account navigation links
    - The footer with the hotel social media links, hotel contact information, the site logo, and developer contact information
- **index.html**: This will act as the website homepage. It will have:
    - Navigation links for the different sections on the page
    - A large hero image and text welcoming the user to the website
    - A booking form
    - Resort information and images
    - Service information and images
    - Location information with a google maps widget
    - Hotel FAQs
    - A carousel of reviews if available
- **allauth**: Django AllAuth provides a host of urls to help with user account management. These are:
    - admin/
    - accounts/ login/
    - accounts/ logout/
    - accounts/ inactive/
    - accounts/ signup/
    - accounts/ reauthenticate/
    - accounts/ email/ 
    - accounts/ confirm-email/ 
    - accounts/ ^confirm-email/(?P<key>[-:\w]+)/$ 
    - accounts/ password/change/ 
    - accounts/ password/set/ 
    - accounts/ password/reset/
    - accounts/ password/reset/done/
    - accounts/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$
    - accounts/ password/reset/key/done/
    - accounts/ login/code/confirm/
    - accounts/ 3rdparty/
    - accounts/ social/login/cancelled/
    - accounts/ social/login/error/
    - accounts/ social/signup/
    - accounts/ social/connections/
    - accounts/ google/
    - accounts/ google/login/token/
- **search_results.html**: This page shows the available rooms based on the search criteria. It will show:
    - Cards of each room showing the name, amenities, description, image, price per night and total price.
    - Each room will have a book button leading the user to the checkout.
- **trips.html**: This page will show the users previous and upcoming trips. There will be:
    - A card for each trip with date, room information, image, and review.
    - If the trip is in the past and there is no review, there will be an add review button.
    - If the trip is in the future there will be a cancel trip button.
- **cancel_trip.html**: This page will have the form for cancelling the trip. It will have a message about cancellation fees, a space for the user to enter a reason for cancellation, a cancel button and some text inviting the user to contact us if they need to amend the trip details.
- **checkout.html**: This page will display the trip information and allow users to input payment information.
- **account_settings.html**: This will allow users to edit their account settings. It will have:
    - A list of current settings
    - A toggle to sign up to a newsletter
    - Buttons to edit
    - A button to delete
- **rooms.html**: This page will be available to the admin user to add, remove, and edit room details.
    - The room information will be shown as a table
    - There will be an add room button
    - Each table entry will have an edit and delete button

### Structure

#### base.html
- As the base template, this will have the site-wide navigation bar and footer
- The navigation bar will meet the requirement for intuitive and responsive navigation, consisting of a site logo, booking form on large screens, and account links. When logged out the links will be to Sign Up / Login. When logged in the links will be to Trips / Account Settings / Logout. When logged in as a Super User the links will be to Rooms / Trips / Account Settings / Logout.
- The footer will meet the requirement for the hotel and developer contact information and will consist of the hotel social media links, contact information for the hotel and developer, and site logo.

#### index.html
- The homepage will display all information about the user, allowing it to be find and look through.
- A home page navigation bar with each homepage section on it meets the requirment for intuitive and responsive navigation.
- The large hero image and text meets the requirement for a clear homescreen showing the website purpose.
- When logged out there will be buttons on the hero image urging the user to sign up or login.
- On smaller than desktop screens (when the booking form disappears from the navigation bar) there will be a booking button on the hero image which takes the user down to the booking form section.
- The section after the hero image will be the booking form on mobile screens, this meets the requirement for users being able to search for available rooms.
- The next section will be a resort info section, meeting the requirement for more information about the hotel. It will consist of a carousel of hotel images, a section title, and a description about the history and key facts of the hotel.
- The next section will be a services section, meeting the requirement for displaying what services are on offer. This will be a carousel of cards, each card will describe the service, cost, how to book, and an image.
- The next section will be the location section, meeting the requirement of showing how to get to the hotel. This will consist of a section title and travel advice and a google maps widget of the hotel location.
- The next section will be the FAQ section. This meets the requirement for providing FAQs. This will have a section title and an unordered list of questions and answers. This will take up 3 columns on desktop, 2 on tablet, and 1 on mobile devices.
- The last section will be a carousel of reviews if reviews are available. This meets the requirement for showing user reviews. They will give a general name e.g. First_name from country, the review content, and a star rating.

#### allauth
- The allauth pages will have the sitewide header and footer and then their key functionality in the centre.
- They meet the requirements for logging in/out, signing up securely, editing email address, email verification, changing/resetting password, and social logins.

#### search_results.html
- The page will consist of available rooms in cards meeting the requirement for showing results.
- There will be a filter button letting the user sort the results by price meeting the requirement for sorting/filtering results.
- If there are no results there will be a message alerting the user.

#### trips.html
- The page will show the users previous and upcoming trips, meeting the requirement for showing trips.
- Each trip will be rendered in a card with a horizontal rule between each card.
- There will be links to add a review if the trip is in the past and edit review if a review exists, meeting the requirements for users to leave reviews and for the business owner to receive reviews.

#### cancel_trip.html
- This page will allow the users to cancel an upcoming trip.
- There will be a message detailing the cancellation fees dependent on how much time there is before the trip.
- There will be a text input allowing users to explain their reason for cancellation.
- There will be some text giving contact details if the user wishes to discuss the trip instead of cancelling.

#### checkout.html
- This page will display 2 columns. The left will be the stripe form for entering payment and personal details and the right column will show the order summary.
- There will be a button for deleting the order.
- There will be a button to confirm payment and open the payment widget.
- All payment will be done via stripe, meeting the requirement for a secure payment method.

#### account_settings.html
- A toggle switch for signing/unsubscribing to the newsletter will be near the top, meeting the requirement for signing up to a newsletter.
- The name/address etc from stripe will be shown and able to be edited/updated meeting the requirement for CRUD functionality of the user details.
- The AllAuth user info will be shown including adding email addresses
- At the bottom there will be a delete account button meeting the requirement for user ability to delete account.

#### delete_account.html
- This page will check that the user does want to delete their account and when confirmed will delete the account.

#### rooms.html
- This admin only page will allow the admin to see and edit the room details, meeting the requirement for easy room administration. 
- The room data will be shown in a table with each entry having buttons to edit or delete the room.
- There will be an "add room" button.
- The add room button will take the admin to a form page for the new room.
- The edit room will take the admin to a form page to edit the room with all fields completed.
- The delete room button will take the admin to a confirmation page to confirm deletion.

#### Information Architecture
**Back-end**: Entity Relationship Diagram (ERD) <br>
Below is a proposed ERD for the tables to be modelled for the database that meets the purpose and requirements of the website.
![Nunisi entity relationship diagram](/documentation/entity_relationship_diagram.png)<br>
**Explanation**
- The relational database will consist of 6 linked tables.
- The User model will use the Django user model and AllAuth to store authentication data including the email address and password.
- The Profile model will have a foreign key to the User model set up in a way as to delete the Profile when the User is deleted. It also has a boolean field for the user to sign up to a newsletter and will have all the contact information required by stripe.
- The Trip model will house the information for each trip. It will be linked with the Profile model and Room model via foreign keys in many to one relationships. It will have the data for the start date, end date, price, and a Boolean field to notify whether the user will cancel the trip. This will be set to False by default.
- The Room model will have all the information for the Rooms, this includes the room name, a sanitised room name for display on the website, the amount of people the room can hold, a description of the room, a list of amentities as a list of integers referring to the ids in the Amenities model, an image of the room, the nightly price, a list of dates in which the room is unavailable.
- The Amenities model will hold information of the amenities. It is referenced from the Room model but set up in a simple easy to understand way rather than a many to many relationship. Each amenity has an ID, name, sanitised name, and an icon which will consist of the HTML for the Font Awesome icon.
- The Review model will hold the information for the reviews. It has a foreign key relationship to the Trip model in a one to one relationship, limiting one review per trip. It also has ratings for cleanliness, food, service, staff, and overall which will be an integer from 1-5. It will also have the written review content as a text field.

#### Interactive Experience
- Clickable links will have animated effects on hover or click, providing clear feedback to the user.
- All external links will open in a new tab. 
- Content hinting will be used where possible to influence the user to scroll down and uncover new content on the pages.

### Skeleton

#### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) was used to create wireframe templates for this webapp.<br>
The Desktop Wireframes can be seen [here](/documentation/wireframes_desktop.png). <br>
Where there were major differences, Mobile Wireframes were mocked up and can be seen [here](/documentation/wireframes_mobile.png).<br>

### Surface

#### Colour Scheme
The colour scheme started as an idea for gold and green to portray the natural aspects of the resort and nature, whilst also conveying sophistication and prestige.

![Colour Scheme](/linktoimage.png)

| Green #3A6B35 | Gold #FDD67C | Gold 2 #B88C26 |
| ----- | ----- | ----- |
| Button font colour | Button background colour | Account menu border |
| Navigation bar background | Button font colour on hover | Homepage header border |
| Booking form labels | Title for the booking form | Border for services cards |
| Account menu background | Booking form input backgrounds | |
| Footer background | Account menu font colour | |
| AllAuth Titles | Background of the homepage header | |
| Homepage navbar font colour | | |
| Homepage horizontal rules | | |
| Next/Previous arrows on services carousel | | |


**Other colours used:**
- Off black: #333A3F for border colours on buttons, dark text throughout
- Off white: #F5F5F5 for text colour which are on a dark image background
- Facebook: Blue and white are used for the Facebook logo
- Instagram and GitHub: Black and white are used for the Instagram and GitHub logos.
- Lava: #CF1020 for error messages

#### Typography

I wanted the typefaces used in this project to reflect the prestige of the hotel and resort as well as highlighting that it is family run.

**[Jost Regular](https://fonts.google.com/specimen/Jost?query=jost)**<br>
![Jost Regular](/documentation/typography_jost.png)
This is my selection for headings across the website. Inspired by the 1920’s German sans-serif; Jost is an elegant and legible font that portrays history and excellence. This makes it a great choice for headings and titles across the website. As a sans-serif font, the backup fonts were Arial, Helvetica, and sans-serif.

**[Caveat Regular](https://fonts.google.com/specimen/Caveat?query=caveat)**<br>
![Caveat Regular](/documentation/typography_caveat.png)
This is my selection for small notes across the website. Caveat is an elegant handwriting font that makes text seem personal and handwritten by giving the letters variations dependent on their placing in a word. This makes it excellent for use for small annotations on the website that give the site a feeling of being family run and personable. As a handwriting font, the backup fonts used were Brush Script MT and cursive.

**[Roboto](https://fonts.google.com/specimen/Roboto?query=roboto)**<br>
![Roboto](/documentation/typography_roboto.png)
This is my selection for block text across the website. Roboto is the most popular google font with high legibility and nice curves. It is used for the bulk text of the website to be easy on user's eyes and not cause strain when reading longer reviews. As a sans serif font, the backup fonts were Arial, Helvetica, and sans-serif.

#### Images
- The site logo was created using [Logo Design AI](https://logodesign.ai/) to create a simple and usable logo throughout the website.
- The icons used across the site were from [Font Awesome](https://fontawesome.com/).

## Features

| **Site Logo** |
| ----- |
| **Page: All - Header and Footer** |
| <details><summary>Site Logo</summary><img src="/documentation/features/site_logo.png"></details> |
| **Details:** The site logo conveys the brand of the website and hotel, immediately conveys the website that the user is on, and acts as a link back to the homepage. |
| **User Stories Covered:** 1, 2 |

| **Booking Form** |
| ----- |
| **Page: All - Header / Homepage** |
| <details><summary>Booking Form</summary><img src="/documentation/features/booking_form.png"></details> |
| **Details:** The booking form is available on all large screens in the header, prompting the user to search for rooms. On smaller screens it appears as it's own section on the homepage. |
| **User Stories Covered:** 2, 22 |

| **Account Menu** |
| ----- |
| **Page: All - Header** |
| <details><summary>Account Menu</summary><img src="/documentation/features/account_menu.png"></details> |
| **Details:** The account menu allows the user to access their Trips, Account details and Log out functionality. When logged out it only displays links to sign up / login and when signed in as an admin, displays a link to add and edit Rooms in the database. |
| **User Stories Covered:** 2, 11, 12, 16, 29, 36 |

| **Footer Hotel Contact Information** |
| ----- |
| **Page: All - Footer** |
| <details><summary>Hotel Contact Information</summary><img src="/documentation/features/footer_hotel_contact.png"></details> |
| **Details:** The Facebook and Instagram icons open the Facebook page and Instagram page in a new tab respectively. The hotel email opens up a new email to the hotel email address in a new tab. The phone number provides an additional way to contact the hotel. |
| **User Stories Covered:** 2, 3 |

| **Footer Developer Information** |
| ----- |
| **Page: All - Footer** |
| <details><summary>Developer Information</summary><img src="/documentation/features/developer_information.png"></details> |
| **Details:** The developer name is proudly displayed on the website along with a link the developer's GitHub profile. |
| **User Stories Covered:** 2, 10 |

| **Allauth: Sign Up** |
| ----- |
| **Page: /accounts/signup** |
| <details><summary>Sign Up</summary><img src="/documentation/features/allauth_sign_up.png"></details> |
| **Details:** The AllAuth sign up form handles all user authentication and allows the user to create an account with their email or through their google account. |
| **User Stories Covered:** 2, 11, 13, 14, 15 |

| **Allauth: Email Validation** |
| ----- |
| **Page: /accounts/^confirm-email/(?P<key>[-:\w]+)/$** |
| <details><summary>Email Validation</summary><img src="/documentation/features/allauth_sign_up.png"></details> |
| **Details:** The AllAuth email validation page allows users to confirm their email. This increases the security of the website having real email addresses used for signing up and only allowing one account per email address. |
| **User Stories Covered:** 2, 11, 15 |

| **Allauth: Sign In** |
| ----- |
| **Page: /accounts/login** |
| <details><summary>Sign In</summary><img src="/documentation/features/allauth_sign_in.png"></details> |
| **Details:** The AllAuth sign in form handles all user authentication and allows the user to sign in with google. |
| **User Stories Covered:** 2, 11, 14, 16 |

| **Allauth: Log out** |
| ----- |
| **Page: /accounts/logout** |
| <details><summary>Log out</summary><img src="/documentation/features/allauth_log_out.png"></details> |
| **Details:** The AllAuth log out page allows the user to log out of their account and be redirected to the home screen. |
| **User Stories Covered:** 2, 11, 16 |

| **Allauth: Reauthenticate** |
| ----- |
| **Page: /accounts/reauthenticate** |
| <details><summary>Account Reauthenticate</summary><img src="/documentation/features/allauth_reauthenticate.png"></details> |
| **Details:** The AllAuth reauthenticate page allows users to keep their accounts secure. |
| **User Stories Covered:** 2, 11 |

| **Allauth: Multiple Emails** |
| ----- |
| **Page: /accounts/email** |
| <details><summary>Account Emails</summary><img src="/documentation/features/allauth_emails.png"></details> |
| **Details:** The AllAuth emails page allows users to add and remove emails from their account. |
| **User Stories Covered:** 2, 11 |

| **Allauth: Change Password** |
| ----- |
| **Page: /accounts/password/change** |
| <details><summary>Change password</summary><img src="/documentation/features/allauth_change_password.png"></details> |
| **Details:** The AllAuth change password page allows users change their password to continue keeping their account secure or to access the forgotten password page. |
| **User Stories Covered:** 2, 11, 17, 18 |

| **Allauth: Reset Password** |
| ----- |
| **Page: /accounts/password/reset** |
| <details><summary>Reset password</summary><img src="/documentation/features/allauth_password_reset.png"></details> |
| **Details:** The AllAuth reset password page allows users to reset their password if they have forgotten it by enetering their email addresses and receiving a link to reset their password. |
| **User Stories Covered:** 2, 11, 18 |

| **Allauth: Google Login** |
| ----- |
| **Page: /accounts/google/login** |
| <details><summary>Google Login</summary><img src="/documentation/features/allauth_google.png"></details> |
| **Details:** The AllAuth Google login allows users to sign up or log in with their Google accounts. This is good for security, as it is a validated email address. |
| **User Stories Covered:** 2, 11, 14 |

| **Homepage: Header** |
| ----- |
| **Page: /** |
| <details><summary>Homepage Header</summary><img src="/documentation/features/homepage_header.png"></details> |
| **Details:** The homepage header allows the user to easily navigate the home page, going to different sections at a click of a button. When scrolling the homepage, the header stays at the top of the page and on smaller screens becomes a burger menu. |
| **User Stories Covered:** 2 |

| **Homepage: About Us** |
| ----- |
| **Page: /** |
| <details><summary>About Us</summary><img src="/documentation/features/homepage_about_us.png"></details> |
| **Details:** The about us feature contains a carousel of images of the hotel area and information about the Hotel. |
| **User Stories Covered:** 2, 3 |

| **Homepage: Services** |
| ----- |
| **Page: /** |
| <details><summary>Services</summary><img src="/documentation/features/homepage_services.png"></details> |
| **Details:** The services section contains cards in a carousel of each service provided and information about them. |
| **User Stories Covered:** 2, 4 |

| **Homepage: Location** |
| ----- |
| **Page: /** |
| <details><summary>Location</summary><img src="/documentation/features/homepage_services.png"></details> |
| **Details:** The location section provides travel information and an interactive Google map of the location. |
| **User Stories Covered:** 2, 6 |

| **Homepage: FAQs** |
| ----- |
| **Page: /** |
| <details><summary>FAQs</summary><img src="/documentation/features/homepage_faqs.png"></details> |
| **Details:** The FAQs section provides the user with answers to frequently asked question. |
| **User Stories Covered:** 2, 5 |