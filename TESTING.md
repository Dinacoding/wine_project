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

Our application has undergone a comprehensive audit using Google Lighthouse, a powerful open-source tool that evaluates web page quality. This testing provides valuable insights into key areas impacting user experience and search engine ranking. The audit focuses on four critical parameters, all of which achieved high scores in our recent assessment: Performance (98), which measures how quickly and smoothly the page loads and becomes interactive; Accessibility (96), ensuring the site is usable by people with disabilities; Best Practices (96), which checks for modern web development standards and code health; and SEO (100), evaluating how well the page is optimized for search engine crawling and indexing. These strong scores indicate a highly optimized, user-friendly, and discoverable web application.

