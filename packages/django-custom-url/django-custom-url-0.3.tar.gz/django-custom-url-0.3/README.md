[![](https://img.shields.io/pypi/pyversions/django-custom-url?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-custom-url?color=0C4B33&label=django&logo=django&logoColor=white)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-custom-url?color=3776AB&logo=pypi&logoColor=white)](https://pypi.org/project/django-custom-url/)
[![](https://img.shields.io/pypi/l/django-custom-url?color=3776AB)](https://github.com/luciano-im/django-custom-url/blob/main/LICENSE)


# django-custom-url
django-custom-url is a Django app to **easily manage custom url linked to static files**.

Django is a great framework, but if you want to create URLs linked to static files, you have 
to create a view for that purpose. And if you have to manage not just one but severals of these URLs, you'll end up
with a bunch of dummy views.

This app allows you to create a custom URL and upload a file linked to that URL, so that when a user requests
the URL, they can view or download the related file (depending on whether it is a valid format for viewing from the browser).

---


## Supported file types
* Plain Text
* CSV
* MS Excel
* MS Word
* MS PowerPoint
* GIF
* JPEG
* PNG
* TIFF
* SVG
* PDF


## How it works
There is possible to use this app in two ways:
1. Use a fallback view that will check for a custom URL if all other URL patterns fails.
   This options doesn't require restarting your application server, just adding the custom URLs in the admin site, and it will work.
2. Execute an administrative command after creating the custom URLs in the admin, which will harcode URLs in a urls.py file.
   This option require restarting you application server each time a URL is added or modified.


## Installation
1. Run `pip install django-custom-url`
2. Add `custom_url` to `settings.INSTALLED_APPS` like this:
```python
    INSTALLED_APPS = [
        ...
        'custom_url',
    ]
```
3. Run `python manage.py migrate`


## Setup
If you want to use the fallback view (option 1 of the "How it works" section):

1. Include the Custom URL view in your project urls.py. Include it at the end of the path list like this:
```python
    from custom_url.views import CustomUrlView

    urlpatterns = [
        ...
        path('<path:url>', CustomUrlView.as_view())
    ]
```


If you want to opt for the hardcoded URLs (option 2 of the "How it works" section):

1. Include the Custom URL URLconf in your project urls.py like this:
```python
    from django.urls import include
    urlpatterns = [
        ...
        path('', include('custom_url.urls'))
    ]
```
2. Create your custom URLs in the admin site.
3. Run `python .\manage.py  update_urls` to update the Custom URL urls.py file.



## License
Released under [MIT License](LICENSE).



## Support
If you are having issues, please let me know through raising an issue, or just sending me a DM to [@luciano_dev](https://twitter.com/luciano_dev).