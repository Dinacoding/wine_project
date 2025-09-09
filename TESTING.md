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
|






## Lighthouse Testing



### Mobile
