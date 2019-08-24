# Django Custom Email User

Replacing the username with the email as the unique identifier is so common, that I simply decided to create a package to prevent this tedium again.

Used to replace default Django User model with email, instead of the username, as the unique identifer. The username is changed to optional and will not be requested as part of createsuperuser.

The Django admin panel is customised to accommodate these changes, along with the User forms custom_email_user.forms.CustomUserCreationForm and custom_email_user.forms.CustomUserChangeForm

Simply add custom_email_user to your installed apps, configure the AUTH_USER_MODEL, and run the migrations

```
INSTALLED_APPS = [
    ...
    'custom_email_user'
]

AUTH_USER_MODEL = 'custom_email_user.User'
```
