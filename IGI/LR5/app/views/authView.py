from django.shortcuts import render, redirect
from django.views import View
from django import forms
from app.models_app.customerModel import Customer
from app.security.security import validate_password_format, check_phone_number, check_auth
from app.services.authService import AuthService


class LoginForm(forms.ModelForm):
    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Customer
        fields = ['email', 'password']
        widgets = {'password': forms.PasswordInput()}


class SignUpForm(forms.ModelForm):
    age_confirmation = forms.BooleanField(required=True, help_text='I confirm that I am at least 18 years old')

    def clean(self):
        check_phone_number(self.cleaned_data['phone'], self)
        validate_password_format(self.cleaned_data['password'], self)
        return self.cleaned_data

    class Meta:
        model = Customer
        exclude = ['id', 'createdAt', 'lastUpdate']
        widgets = {'password': forms.PasswordInput()}


class LoginView(View):
    def get(self, request):
        return render(request, "authWindow.html",
                      {'form': LoginForm(), 'action': 'Login', 'role': request.session['role']})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user, role = AuthService.login(form.data['email'], form.data['password'])
                if user is None:
                    form.add_error(None, "Check the data you entered!")
                request.session['role'] = role
                request.session['id'] = user.id
                return redirect('home')
            except:
                form.add_error(None, "Error while logging in!")
        return render(request, 'authWindow.html',
                      {'form': form, 'action': 'Login', 'role': request.session['role']})


class SignUpView(View):
    def get(self, request):
        check_auth(request.session)
        return render(request, 'authWindow.html',
                      {'form': SignUpForm(initial={'phone': '+37529'}), 'action': 'Sign Up',
                       'role': request.session['role']})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = AuthService.sign_up(form.data['email'], form.data['name'],
                                           form.data['phone'], form.data['password'])
                if user is None:
                    form.add_error(None, "Error while trying to sign up!")
                request.session['role'] = 'user'
                request.session['id'] = user.id
                return redirect('home')
            except:
                form.add_error(None, "Error while trying to sign up!")

        return render(request, 'authWindow.html',
                      {'form': form, 'action': 'Sign Up', 'role': request.session['role']})


class LogoutView(View):
    @staticmethod
    def get(request):
        request.session.clear()
        check_auth(request.session)
        return redirect('home')













