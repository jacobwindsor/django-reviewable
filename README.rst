==========
Reviewable
==========
Reviewable provides simple reviews for any of your models and is easily customizable.

Quick Start
-----------
1. Add "Reviewable" to your INSTALLED_APPS setting:
    INSTALLED_APPS = [
        ...
        'Reviewable',
        ...
    ]

2. Include the Reviewable URLconf in your projects urls.py:

    url(r'^reviews/', include('Revieable.urls')),

3. Run `python manage.py migrate`

4. Add the mixin `Reviewable` to any model you want to be reviewable.

        ...
        from Reviewable.models import Reviewable
        ...

        class ReviewableModel(models.Model, Reviewable):
            ...

Custom Templates
----------------
Reviewable allows you to customise the templates for each reviewable model. Furthemore, the reviewable object is magically
made available in the template context.

For example:
    1. You have a model called `Hotel` in an app called `Hotel`
    2. You want a custom template for the review creation view
    3. You would add a template in `Hotel/templates/Hotel` called `hotel_review_create.html`
        * Note: This the template name has to be in camel case and all lower case
    4. The hotel object is made available in the template context by the usual `{{ hotel }}` tag
    5. This can be repeated for templates for all views: `hotel_review_list.html`, `hotel_review_update.html`,
    `hotel_review_confirm_delete.html` and `hotel_review_detail.html`