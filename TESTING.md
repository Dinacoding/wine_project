

## Functionality Testing


### Webpage functionality 

| Task | Status | Notes |
|------|--------|-------|
| Git initialized | Yes | Project under version control |
| Virtual environment created | Yes | Python environment isolated |
| Django installed | Yes | Confirmed via `pip freeze` |
| Project structure created | Yes | Models: `UserProject`, `WinePost` |
| Deployed to Heroku | Yes| Live version available |
| Models registered in admin | Yes | Accessible via Django Admin |
| Views created and mapped | Yes | Handles requests/responses |
| User can create an account | Yes | Mandatory fields need to be filled|
| User can log in to the account | Yes | Using the username and required password|
| User can post | Yes | After logged in the user can post, edit , delete and view all the posts|
| User can logout | Yes | User can logout and the page is directed to the home page |
| Visitor can view posts | Yes | User can navigate throught the page and view all posts and individual posts|
| Assign valid User as author | Yes | Create a `User` via admin or shell, then assign as `author` when creating a `WinePost` | `WinePost` is saved and linked to the correct `User` |
| Cascade delete behaviour | Delete the `Wine_post` linked to a `User` | The `WinePost` is also deleted (due to `on_delete=models.CASCADE`) |
| Access related posts from User | Use `user.wine_posts.all()` in Django shell | Returns queryset of all posts by that user |
| Required field validation | Try to save a `WinePost` without setting `author` | Validation error is raised |
| Cascade edit behaviour | Edit the `Wine_post` linked to a `User` | The logged in user can edit the post ( duet to the EditWinePost.view and respective url)|
| Footer contains social links and direct you to an external tab| Yes | It results as expected|


### Login and log out testing 

| Categotry | Test Case | Notes | Result|
|------|--------|-------| -------|
| User | Visit the login page while logged in| | Ensures proper redirection and a good user experience for authenticated users. |
| User |Visit the login page while logged out | | Verifies the initial state for new or logged-out visitors. |
| Functionality| Submit the form with valid credentials | | Tests the form.non_field_errors display for authentication failures |
| Form Validation | Submit the form with an empty username or password field | Page reloads, and specific validation errors ("This field is required") are displayed below the respective fields | Verifies field-level error handling using form.username.errors and form.password.errors |
| Navigation | Click the "Create Account" button. | | Ensures the link is correctly configured and working |
| Form Validation | Submit the form with an invalid username and/or password. | Page reloads with a general error message, example, "Please enter a correct username and password." | Tests the form.non_field_errors display for authentication failures. |



### Blog 

| Category           | Action / Scenario                                         | Expected Result                                                                 | Status |
|--------------------|-----------------------------------------------------------|---------------------------------------------------------------------------------|--------|
| User State         | Visit home page while logged out                          | "Welcome to Wine Project" displayed; links for "Login" and "Register" visible    | Pass   |
| User State         | Visit home page after logging in                          | "Hello, {{ user.username }}!" displayed; "Create New Post" and "Logout" buttons visible | Pass   |
| Navigation         | Click "Login" link while logged out                       | Browser navigates to login page (`/login/`)                                     | Pass   |
| Navigation         | Click "Register" link while logged out                    | Browser navigates to registration page (`/register/`)                           | Pass   |
| Navigation         | Click "Create New Post" while logged in                   | Browser navigates to post creation page (`/create_post/`)                       | Pass   |
| Functionality      | Click "Logout" button while logged in                     | User is logged out, redirected, and home page reverts to logged-out view        | Pass   |
| Content Display    | Visit page when `wine_posts` list is empty                | Message displayed: "No wine posts available yet. Be the first to share a review!" | Pass   |
| Content Display    | Visit page with multiple wine posts                       | Cards displayed for each post: title, wine name, vintage, content preview, author, date | Pass   |
| Functionality      | Click "Read Full Review" as post author                   | Browser navigates to detail page for that specific post                         | Pass   |
| Functionality      | Click "Delete" button as post author                      | "Confirm Delete" modal displayed with correct post title                        | Pass   |
| Functionality      | In delete modal, click "Delete Post"                      | Post is deleted, user redirected, and post no longer visible on home page       | Pass   |


### Post Form

| Test Category       | Test Case                                                         | Expected Result                                                                                          | Result | Notes                                                                |
|---------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------|
| Form Display (Create) | Navigate to the create post page (`/create_post/`).               | Title = "Create Wine Post". Main button = "Create Wine Post". Cancel → `/blog/`.                         | Pass   | Verifies correct initial state for a new post.                       |
| Form Display (Edit)   | Navigate to the edit page for an existing post (`/edit_post/my-post-slug/`). | Title = "Edit Wine Post". Fields pre-populated. Main button = "Update Wine Post". Cancel → post detail.   | Pass   | Confirms form loads correctly for editing.                           |
| Form Validation       | Submit with a required field left blank.                         | Error alert displayed below the empty field.                                                             | Pass   | Tests field-level error handling.                                    |
| Form Validation       | Submit with invalid data (e.g., wrong date format).              | Validation error displayed below the field.                                                              | Pass   | Checks error messages on invalid input.                              |
| Form Validation       | Submit with non-field errors (e.g., server-side validation).     | Error alert displayed at top of the form.                                                                | Pass   | Verifies general form errors handled correctly.                      |
| Form Submission (Create) | Fill in valid data and click "Create Wine Post".                 | Post created. Success message shown. Redirected to new post’s detail page.                                | Pass   | Ensures creation + redirection flow works.                           |
| Form Submission (Edit)   | Modify post data and click "Update Wine Post".                   | Post updated. Success message shown. Redirected to updated post’s detail page.                            | Pass   | Verifies updates saved + correct redirect.                           |
| Navigation            | Click "Cancel" on create form.                                   | Redirected to `/blog/` without creating a post.                                                          | Pass   | Confirms cancel works for new post.                                  |
| Navigation            | Click "Cancel" on edit form.                                     | Redirected to the post’s detail page without saving changes.                                              | Pass   | Confirms cancel works for editing.                                   |
| Messaging             | Submit form with success outcome.                                | Green success alert displayed at top of form.                                                            | Pass   | Verifies Django messages framework success display.                  |
| Messaging             | Submit form with error outcome.                                  | Red error alert displayed at top of form or near the field.                                               | Pass   | Verifies Django messages framework error display.                    |


### Post Detail

| Test Category          | Test Case                                        | Expected Result                                                                 | Result | Notes                                                        |
|------------------------|--------------------------------------------------|---------------------------------------------------------------------------------|--------|--------------------------------------------------------------|
| Content Display        | Visit a specific post's detail page.             | Post title, wine name, vintage year, author, and content are displayed. Title also appears in the page title. | Pass   | Verifies content is correctly rendered from the post object. |
| Navigation             | Click the "Back to All Posts" button.            | Browser navigates to `/blog/`.                                                  | Pass   | Confirms navigation link works.                             |
| User State (Not Author)| View a post not authored by the logged-in user.  | "Delete" and "Edit" buttons are not visible.                                    | Pass   | Ensures only the author sees edit/delete actions.            |
| User State (Author)    | View a post authored by the logged-in user.      | "Delete" and "Edit" buttons are visible.                                        | Pass   | Confirms correct visibility of action buttons.               |
| Delete Modal           | Click "Delete" as the author.                    | "Confirm Delete" modal appears with the specific post title.                     | Pass   | Verifies modal triggers with correct content.                |
| Delete Action          | In delete modal, click "Delete Post".            | Post deleted, user redirected to `/blog/`, and post is no longer visible.        | Pass   | Confirms delete form submission works correctly.             |
| Edit Modal             | Click "Edit" as the author.                      | "Edit Wine Post" modal appears with pre-populated fields.                        | Pass   | Checks modal loads correctly with current post data.         |
| Edit Action            | Modify field in edit modal and save changes.     | Post updated, success message shown, user remains on detail page with updates.   | Pass   | Verifies edit submission updates post successfully.          |
| Updated Timestamp      | Edit a post and reload detail page.              | Updated date is displayed next to published date.                                | Pass   | Confirms modified date field is correctly rendered.          |


### Register Form

| Test Category                  | Test Case                                                     | Expected Result                                                                 | Result | Notes                                                                  |
|--------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------|--------|------------------------------------------------------------------------|
| Page Display (Logged Out)      | Navigate to `/register/` while logged out.                    | "Join Wine Project" heading, "Create your account!" subtitle, and full form visible. | Pass   | Verifies initial page state for a new user.                            |
| Page Display (Logged In)       | Navigate to registration page while logged in.                | Message: "You are already logged in as [username]." Form not visible.            | Pass   | Ensures logged-in users cannot access registration form.               |
| Form Fields                    | Inspect the form fields.                                      | Fields for First Name, Last Name, Username, Email, Password, Confirm Password.   | Pass   | Confirms all required fields for account creation exist.                |
| Form Validation (Required)     | Submit with one or more required fields blank.                | Error message shown for each blank field.                                       | Pass   | Tests validation for missing required data.                             |
| Form Validation (Password Mismatch) | Enter different values for Password and Confirm Password.       | Error: passwords do not match.                                                  | Pass   | Confirms password confirmation is enforced.                            |
| Form Validation (Existing User)| Try registering with an existing username or email.           | Error: username or email already taken.                                         | Pass   | Prevents duplicate accounts.                                           |
| Form Submission (Success)      | Fill all fields with valid, unique data and submit.           | User created, success message shown, redirected to login page (or next step).    | Pass   | Tests full successful registration flow.                               |
| Messaging                      | Submit form (success or error).                               | Bootstrap alert: green for success, red for error, dismissible.                  | Pass   | Verifies Django messages framework works properly.                     |
| Navigation                     | Click "Login Here" link at bottom of page.                    | Browser navigates to `/login/`.                                                 | Pass   | Ensures login navigation link works.                                   |





## Lighthouse Testing



### Mobile




### Desktop


## W3 HTML Validator 

HTML validation validator helped by providing the application’s pages to the validator, I was able to detect errors such as missing tags, incorrect attributes, or deprecated elements. This process helped improve browser compatibility, accessibility, and overall code quality. Using the validator throughout development ensured that the application remained clean, professional, and standards-compliant, reducing potential issues for users. 

### Index page

### Blog page

### Login

### Post_detail

### Post_form 

### Register


## W3 CSS Validator 


Css validation validator helped by providing the application’s pages to the validator, no errors were found


## Jshint testing

The code has been tested and successfully passes JSHint without any critical issues. It follows modern ES6+ standards, utilizing const and let for variable declarations, ensuring better scope management.


## Manual Testing

To performe a comprehensive manual evalutation of the Wine_Project web application, it is important to start assessing its functionalities and features. Firstly, ensure that the logo within the header redirects users to the homepage, secondly the toggle button should be tested to ensute it propertly expands and collapses the navigation links. To assess the website's responsiveness, its interface should be tested on different screen sizes and devices. This involves verifying that the layout adapts based on already defined CSS media query breakpoints. At last, a comprehensive review of the color scheme and design consistency is essential to ensure that background images, text colors, and other visual elements align with the intended design specifications.



To sum up, this manual testing will result in a fully operational website that provides a seamless user experience.


