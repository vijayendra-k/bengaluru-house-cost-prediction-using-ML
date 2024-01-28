from django import forms
class RegistrationForm(forms):
    gender = [('Male', 'Male'),
                   ('Female', 'Female'),
                   ('Other', 'Other')
                   ]
    
    name = StringField('Name')
    phone = StringField('Phone')
    address= StringField('Address')
    email= StringField('email')
    gender = SelectField('Gender', choices=gender)
    