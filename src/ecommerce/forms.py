from django import forms


class Contact_form(forms.Form):
    Fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"fom_full_name","placeholder":"Enter FullName"}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","id":"fom_Email","placeholder":"Enter Email Id"}))
    Content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","id":"fom_Email","placeholder":"Enter Message"}))


    def clean_email(self):
        email = self.cleaned_data.get('Email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email