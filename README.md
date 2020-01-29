# Django Custom Email User

Replacing the username with the email as the unique identifier is so common, that I simply decided to create a package to prevent this tedium again.

Used to replace default Django User model with email, instead of the username, as the unique identifer. The username is changed to optional and will not be requested as part of createsuperuser.

The Django admin panel is customised to accommodate these changes, along with the User forms custom_email_user.forms.CustomUserCreationForm and custom_email_user.forms.CustomUserChangeForm

Simply:
* add custom_email_user to your installed apps
* subclass the abstracted class 
* configure the AUTH_USER_MODEL
* run the migrations
* register your user model with the admin site

```python
INSTALLED_APPS = [
    ...
    'custom_email_user'
]

AUTH_USER_MODEL = 'my_model_module.User'
```

```python
from django.db import models
from custom_email_user.models import User as BaseUser


class User(BaseUser):
    pass
```

```python
from django.contrib import admin
from custom_email_user.admin import CustomUserAdmin

from .models import User

admin.site.register(User, CustomUserAdmin)
```
