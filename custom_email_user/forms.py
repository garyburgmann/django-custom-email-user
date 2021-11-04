from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm
)


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        # model = AbstractUser
        fields = BaseUserCreationForm.Meta.fields + ('email',)


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        pass
