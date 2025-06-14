# Wine Project

**Wine Project** is a modern, community-driven wine blogging platform that serves as both a personal tasting journal and a social sharing space for wine enthusiasts. It combines the functionality of a traditional blog with wine-specific features to create a specialised platform for the wine community. The key characteristics of Wine project are centered around the detailed wine reviews and tasting experiences. Each post grabs a specific wine detail [name, vintage year and tasting notes]. This community driven web application uplifts user profiles to share their discoveries, branding and exhibit their expertise. It is built with the wine sophistication and the aesthetics needed for the appealing user experience and the community it serves. **Cheers!**


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







## How to run this project locally 

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


