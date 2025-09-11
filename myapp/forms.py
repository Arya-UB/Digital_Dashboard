from django import forms

from myapp.models import Dashboard,User,Announcements

class AdminRegistrationForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username','password']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mx-auto','placeholder':'enter your username','style':'border:2px solid black;width:300px'}),
            'password':forms.PasswordInput(attrs={'class':'form-control mx-auto','placeholder':'enter your password','style':'border:2px solid black;width:300px'})
                                                  
            }

# class LoginForm(forms.Form):

#     username = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class':'form-control mx-auto','placeholder':'enter your username','style':'border:2px solid black;width:300px'}))
           

#     password = forms.CharField(max_length=50, widget = forms.PasswordInput(attrs={'class':'form-control mx-auto','placeholder':'enter your username','style':'border:2px solid black;width:300px'}))
           


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control mx-auto',
            'id': 'floatingUsername',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        max_length=50,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingPassword',
            'placeholder': 'Password',
            'autocomplete': 'new-password' 
        })
    )
   

class UploadForm(forms.ModelForm):

    class Meta:

        model = Dashboard

        fields = ['Filetype','File','link']

        widgets = {
            'Filetype': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Select file type'
                }
            ),
            'File': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'link' : forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'paste any youtube or videolink'
                }
            )
        }
    
    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get("File")
        link = cleaned_data.get("link")

        if video and link:
            raise forms.ValidationError("Please upload a video or add a link, not both.")

class AnnouncementForm(forms.ModelForm):

    class Meta:

        model = Announcements

        fields = ['title','message']

