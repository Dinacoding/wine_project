| Task | Status | Notes |
|------|--------|-------|
| Git initialized | Yes | Project under version control |
| Virtual environment created | Yes | Python environment isolated |
| Django installed | Yes | Confirmed via `pip freeze` |
| Project structure created | Yes | Models: `UserProject`, `WinePost` |
| Deployed to Heroku | Yes| Live version available |
| Models registered in admin | Yes | Accessible via Django Admin |
| Views created and mapped | Yes | Handles requests/responses |
| Assign valid User as author | Yes | Create a `User` via admin or shell, then assign as `author` when creating a `WinePost` | `WinePost` is saved and linked to the correct `User` |
| Cascade delete behavior | Delete the `User` linked to a `WinePost` | The `WinePost` is also deleted (due to `on_delete=models.CASCADE`) |
| Access related posts from User | Use `user.wine_posts.all()` in Django shell | Returns queryset of all posts by that user |
| Required field validation | Try to save a `WinePost` without setting `author` | Validation error is raised |





## Lighthouse Testing



### Mobile
