# Wine Project

**Wine Project** is a modern, community-driven wine blogging platform that serves as both a personal tasting journal and a social sharing space for wine enthusiasts. It combines the functionality of a traditional blog with wine-specific features to create a specialised platform for the wine community. The key characteristics of Wine project are centered around the detailed wine reviews and tasting experiences. Each post grabs a specific wine detail [name, vintage year and tasting notes]. This community driven web application uplifts user profiles to share their discoveries, branding and exhibit their expertise. It is built with the wine sophistication and the aesthetics needed for the appealing user experience and the community it serves. **Cheers!**

### find my app deployment link: [https://wineproject-7fef38f6bd48.herokuapp.com/](https://wineproject-7fef38f6bd48.herokuapp.com/)


## Target Audience 

Wine Project Target audience ranges from anyone eager to explore, learn, and connect within a vibrant, sophisticated wine community. The primary target audience for the Wine Project includes:

- ***Wine Enthusiasts*** : They are passionate about wine, eager to learn more, and keen to share their experiences and discoveries;

- ***Aspiring Sommeliers and Wine Professional*** : They work in the industry, or looking to deepen their professional knowledge would find the detailed tasting notes and community expertise invaluable for learning;

- ***Home Entertainers and Foodies*** : They would appreciate a resource for finding perfect wine matches and learning about different flavor profiles;

- ***Wine Bloggers and Content Creators*** : The platform could attract existing wine bloggers looking for a more specialised and community-focused space to publish their reviews and connect with an engaged audience.

To sum up, anybody with interest in wine would find beneficial and valuable the Wine Project.


## User Experience (UX) 

### User Goals

Wine Project primary goal is to serve a diverse community of wine lovers and connoisseurs. Through posts the user will be exposed to expert knowledge and a fine appreciation to dive deeper into the wine world. Understanding the following user goals is fundamental to creating a sucessful wine orientated social platform that brings in genuine value to its community. 

1) **Wine Enthusiasts**
- Document personal wine tasting experiences for future reference
- Learn from other wine lovers' experiences and recommendations
- Develop their palate and wine knowledge through community engagement

2) **Sommeliers, Industry Workers**
- Share professional knowledge and educate wine enthusiasts
- Wine purchasing decisions through trusted reviews

3) **Wine Collectors**
- Share valuable wine experiences with the community
- Value of insights shared with community

4) **Social Wine Drinkers**
- Get social validation and engagement on their wine posts
- Discover wines for group events and celebrations

## User Stories

To understand how to build the application, the Agile development method was used. This involved prioritizing user stories and their acceptance criteria with each story labeled using the MoSCoW method.

**User Story 1** (Must Have)

*As a new visitor*, *I want* to create an account with my email and password so that *I can* start posting about wines.

**Acceptance Criteria**

-  Given I am on the registration page, when I enter a valid email and a password (meeting complexity requirements), and click "Register," then my account is created successfully.
- Given I am on the registration page, when I enter an email that is already registered, then I receive an error message indicating the email is taken.
- Given my account is created, then I am automatically logged in or redirected to a login page.

**User Story 2** (Must Have)

**As a logged-in user**, **I want** to log out of my account **so that** my session is secure when I'm done.

**Acceptance Criteria**

- Given I am logged in, when I click the "Logout" button, then my session is terminated.
- Given I have logged out, then I am redirected to the home page or login page.
- Given I have logged out, when I try to access a protected page, then I am redirected to the login page.

**User Story 3** (Must Have)

**As a registered user**, **I want** to create a new wine post with a title, wine name, vintage year, and detailed content so that **I can** share my wine experiences with others.

**Acceptance Criteria**

- Given I am logged in, when I navigate to the "Create Post" page, then I see input fields for Title, Wine Name, Vintage Year, and Content.
- Given I have filled all required fields, when I click "Submit," then the post is successfully created and visible on my profile and the main Browse page.
- Given I omit a required field, when I click "Submit," then I receive an error message indicating which field is missing.
- Given I enter an invalid vintage year (e.g., future year), then I receive an error message.


**User Story 4** (Could have)

**As a registered user**, **I want** to edit my existing wine posts so that **I can** update or correct information I've shared

**Acceptance Criteria**

- Given I am viewing one of my own posts, when I click the "Edit" button, then I am taken to an edit form pre-populated with the post's current data.
- Given I am on the edit form, when I make changes and click "Save," then the post is updated successfully and the changes are reflected on the post view.
- Given I am on the edit form, when I try to edit a post that does not belong to me, then I receive an unauthorized error or the edit option is not visible.


**User Story 5** (Should have)

**As a registered** user, **I want** to delete my wine posts so that **I can** remove content I no longer want to share.

**Acceptance Criteria**

- Given I am logged in, when I navigate to the "Create Post" page, then I see input fields for Title, Wine Name, Vintage Year, and Content.
- Given I have filled all required fields, when I click "Submit," then the post is successfully created and visible on my profile and the main Browse page.
- Given I omit a required field, when I click "Submit," then I receive an error message indicating which field is missing.
- Given I enter an invalid vintage year (e.g., future year), then I receive an error message.


## Planning

Wine Project is established by developing a technical architecture. This involves implementing a Django based core platform integrated with a PostgreSQL relational database to ensure data management and security. Key functionalities will include a secure user authentication system, encompassing registration, login, and comprehensive profile management.A wine post creation and editing system will be developed, featuring a rich text editor and a draft/publish workflow. The front-end will utilize responsive Bootstrap templates, having in mind mobile-first design paradigm and incorporating a wine-themed aesthetic with a complete navigation structure. This phase aims to deliver a fully operational authentication system, content management capabilities, and responsive user interface templates.

**Phase 1**

1) Create the User Stories using Agile approach
2) Set up the project for the Django and PostgreSQL, by creating a Python project and setting up a .venv virtual environment.
3) Install all the dependencies 
4) Deploy to Heroku

**Phase 2**

1) Design the Wireframes
2) Create the Apps
3) Create a Post Entity Relationship Diagram 
4) Create the models for the WinePost and UserProfile
5) Add the Urls
6) Deploy to Heroku

**Phase 3**

1) Code the templates 
2) Migrate all the changes
3) Test the Application 
4) Deploy to Heroku

**Phase 4**

1) Deploy the app on Heroku
2) Complete the README.md file



### ERD (Entity Relationship Diagram)

This database schema outlines relationships between User, WinePost, and UserProfile models. A User can author multiple WinePosts (one-to-many), with each post linked to a single author via a foreign key. The WinePost model includes details like wine_name and vintage_year. Each User also has a unique UserProfile (one-to-one), extending user information with fields like bio. This structure uses Django's built-in User model and clearly defines foreign key relationships for data integrity. WinePost also utilizes an integer status field (0 for Draft, 1 for Published).

![Find the diagram here](documentation/relationship_diagram.png)

## Wireframes

### Phone 

- [Home](documentation/phone_wireframes/home.png)

- [Menu Dropdown](documentation/phone_wireframes/menu_dropdown.png)

- [Login](documentation/phone_wireframes/login.png)

- [Register](documentation/phone_wireframes/register.png)

- [Main Menu](documentation/phone_wireframes/main_page.png)

- [Create a Post](documentation/phone_wireframes/create_post.png)

- [Posted](documentation/phone_wireframes/posted.png)

- [Logout](documentation/phone_wireframes/logout.png)

### Tablet

- [Home](documentation/tablet_wireframes/home.png)

- [Menu Dropdown](documentation/tablet_wireframes/dropdown.png)

- [Login](documentation/tablet_wireframes/login.png)

- [Register](documentation/tablet_wireframes/register.png)

- [Main Menu](documentation/tablet_wireframes/blog.png)

- [Create a Post](documentation/tablet_wireframes/create_post.png)

- [Posted](documentation/tablet_wireframes/posted.png)

- [Logout](documentation/tablet_wireframes/logout.png)

### Desktop


- [Home](documentation/desktop_wireframes/home.png)

- [Login](documentation/desktop_wireframes/login.png)

- [Register](documentation/desktop_wireframes/register.png)

- [Main Menu](documentation/desktop_wireframes/blog.png)

- [Create a Post](documentation/desktop_wireframes/create_post.png)

- [Posted](documentation/desktop_wireframes/posted.png)

- [Logout](documentation/desktop_wireframes/logout.png)


## Scenarios

![Flowchart](documentation/visitor_experience_diagram.png)


1. **The user has a login already**
- The user should login by giving the username and password that they register.
- They will be redirected to the blog post page and can view the posts previously created by another users.
- Will be given permission to create a new post by clicking the create post button.
- Will be able to delete the posts that they created.
- The user can logout.


2. **The user doesn't have a login and wants to register**
- The user will need to register their name, username and password.
- The user will be redirected to the login form.
- They will be redirected to the blog post page and can view the posts previously created by another users.
- Will be given permission to create a new post by clicking the create post button.
- Will be able to delete the posts that they created.
- The user can logout.

3. **The user wants to view the blogs only**
- The user can view the blogs by using the blog button
- It is not granted the delete function
- User can only post, delete or logout if follow the steps of a non register user

## Design Choises

Wine Project is design to sustain a visually appealing approach, emphasising a graceful choice of elegant tones that embrace the wine theme. The color palette consists of deep greens, richeness of the whites and seamless dark tones. Together the blend of colours brings of  ideal sophistication for a wine-related website. It also ensures that the layout stays resposive and is adaptable. It aims to cater the flexible layout ensures responsive adaptability, different screen sizes with well-structured media queries. The root variables allow for easy theme adjustments. Overall, the design effectively balances aesthetics, readability, and functionality, making it both user-friendly and visually immersive.

## Color pallete

![Palette](documentation/design/color_pallete.png)



## Technology used 


- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), for structure and content writting;
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), for styling and some visual effects;
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), for interactive elements, dynamic behavior, and enhancing user experience.
- [Django](https://www.djangoproject.com/),to handle the Web Request-Response Cycle and add logic
- [Python](https://www.python.org/), Use to build the backend of the app
- [Balsamiq](https://balsamiq.com/), used it to wireframe the webpages;
- [ChatGPT](https://chatgpt.com/), to use it to create content for the website and get me a color palette 
- [W3school](https://www.w3schools.com/) to review some concepts about code;
- [Gemini](https://gemini.google.com/app/a427d05ca7bf78c3) for correcting and questions code,website content
- [Claude](https://claude.ai/new), for project structuration and debugging.
- [Miro](https://miro.com/index/), Use for flowchart to build the user experience
- [Excel](https://excel.cloud.microsoft/), for building the ERD
- [PostgradeSQL](https://www.postgresql.org/), used to keep that database 
- [Heroku](https://heroku.com), use for deployment of the app online
- [Bootstrap](https://getbootstrap.com/), for responsivess and style of the web application
- [Coolors](https://coolors.co/262626-acbfa4-e2e8ce-ff7f11-ff1b1c), generate a color palette

## Pages 

To provide a comprehensive visual overview of the application, the following section contain screenshots of key pages as they appear across different devices. You will find dedicated subsections for phone, tablet, and desktop views, showcasing the responsive design and user experience on each platform. Click on the links below to view the respective page 

### Phone
- [Home](documentation/devices_screenshots/phone/phone_home.png)
- [Register](documentation/devices_screenshots/phone/phone_register.png)
- [Login](documentation/devices_screenshots/phone/phone_login.png)
- [Blog](documentation/devices_screenshots/phone/phone_blog.png)
- [Create Post](documentation/devices_screenshots/phone/phone_post_create.png)

### Tablet
- [Home](documentation/devices_screenshots/tablet/tablet_home.png)
- [Register](documentation/devices_screenshots/tablet/tablet_register.png)
- [Login](documentation/devices_screenshots/tablet/tablet_login.png)
- [Blog](documentation/devices_screenshots/tablet/tablet_blog.png)
- [Create Post](documentation/devices_screenshots/tablet/tablet_post_create.png)


### Desktop
- [Home](documentation/devices_screenshots/desktop/desktop_home.png)
- [Register](documentation/devices_screenshots/desktop/desktop_register.png)
- [Login](documentation/devices_screenshots/desktop/desktop_login.png)
- [Blog](documentation/devices_screenshots/desktop/desktop_blog.png)
- [Create Post](documentation/devices_screenshots/desktop/desktop_post_create.png)


## Features 

1. Navigation bar, responsive for different screen devices and it is position on the top of the webpage. 

* Features the logo on the left 
* Contains the links on the right.
* Navbar turns into a toggle button

2. Footer with social links
* Social media links on the left 

3. Call of Action Buttons in the hero section
* Register button
* Access the blog for visitor experience

3. Login form
* Inputs for username and password

4. Blog page not logged in 
* Full list of posts 
* Possible to full view a single post by click view more

5. Blog page logged in 
* Message welcoming the user
* Create Post button
* Log out button 

6. Create Post page
* Form with fields 
    - title
    - wine name 
    - wine year
    - content
    - post button
    - cancel

7. Single Post page
    - go back to all post butoon 
    - if logged in you can delete the post

8. Register Page
    - Register form 
    - Message if already register login button

## Testing 
Please follow this link [Click Here](TESTING.md) to view the full testing steps that were completed on every device and browser.

## Bugs

### Future Improvements 

1. Enhanced Typography for Elegance
- Adjust line height and letter spacing for better readability.
- Adjust Font and make the hierarchy 

2. Animations for Engagement
- Add a smooth fade-in effect when wine cards appear
- Animate the menu toggle for a more dynamic interaction

3. Wine Post Cards Enhancements
- Introduce a carousel or grid layout for wine cards, improving organisation.
- Make wine cards expandable.   

4. Change language button option
- To make your content more accessible to a global audience.
- Language Content Availability: Ensure that you have all necessary content translated and ready for the languages you support.

5. Improve testing and research
- introduce new features and functionalities to the project
- Add the screenshots of the steps of how to deploy in Heroku to the README.md

## How to deploy the app Heroku

1. Prepare Your Django Project for Heroku
    - Install Gunicorn locally on your project terminal with the command bash *pip install gunicorn*

2. Create a Procfile in your root directory at the same level that your manage.py and inside the file add the *web: gunicorn your_project_name.wsgi* inside.

3. Create a requirements.txt for necessary Python dependencies and freeze it with the command *pip freeze > requirements.txt* on your local terminal

4. Configure settings.py for Production:
- DEBUG = False: Crucial for production security.
- ALLOWED_HOSTS: Add your Heroku app's domain (e.g., your-app-name.herokuapp.com). You can also add * for initial testing, but narrow it down later.
 - Static Files: Configure STATIC_ROOT and STATIC_URL for serving static files in production. You'll often use whitenoise or Heroku's static file serving capabilities.
- Database: Heroku typically uses PostgreSQL. You'll need to install dj-database-url and psycopg2-binary and configure your database settings to use os.environ.get('DATABASE_URL').
- Secret Key: Store your SECRET_KEY in an environment variable, not directly in settings.py.

5. Install Whitenoise (for static files) using the command *pip install whitenoise* using your local terminal
and then modify your the *setting.py* to include the *Whitenoise*

6. Install dj-database-url and psycopg2-binary *pip install dj-database-url psycopg2-binary* in this project I used PostGradeSQL. You need to update your settings.


## How to run this project  locally 

1. Download the Git installer:

Windows:

Go to the official Git website: https://git-scm.com/
Click on the "Download for Windows" button.
Run the downloaded installer.
Follow the on-screen instructions. It's generally recommended to use the default options during installation.
macOS:

The easiest way is to use Homebrew:
Open Terminal.
Type brew install git and press Enter.
If you don't have Homebrew, install it first using the instructions on their website: https://brew.sh/
Linux:

Git is usually available through your distribution's package manager.
For Ubuntu/Debian, use sudo apt update and then sudo apt install git.
For Fedora/CentOS, use sudo dnf install git.
For Arch Linux, use pacman -S git.
2. Verify installation:

Open your terminal or command prompt.
Type git --version and press Enter.
If Git is installed correctly, you'll see the installed Git version displayed.


### To clone this project from GitHub:

1. Follow this link to the Project GitHub repository.
2. Under the repository name, click "Clone or download."
3. In the "Clone with HTTPS" section, copy the clone URL for the repository.
4. In your local IDE, open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.


