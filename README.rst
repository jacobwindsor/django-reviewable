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