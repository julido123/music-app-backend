from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import Account


class AccountCreationForm(forms.ModelForm):
    """Formulario para crear usuarios desde el admin, con set_password."""

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'username', 'nombre', 'apellido', 'cedula')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    """Formulario para actualizar usuarios (sin cambiar la contraseña en texto plano)."""

    class Meta:
        model = Account
        fields = ('email', 'username', 'nombre', 'apellido', 'cedula', 'is_active', 'is_staff', 'is_admin')


class CustomAccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ('username', 'email', 'nombre', 'apellido', 'is_staff', 'is_admin')
    list_filter = ('is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellido', 'cedula')}),
        ('Permisos', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombre', 'apellido', 'cedula', 'password1', 'password2', 'is_staff', 'is_admin', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(Account, CustomAccountAdmin)
