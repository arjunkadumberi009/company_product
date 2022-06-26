from cProfile import label
from django import forms
from .models import user_reg,product_details

#create consumer form
class ConsumerForm(forms.ModelForm):
	"""Customer form"""

	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password again'}))
	
	class Meta:
		"""meta"""
		model=user_reg
		fields = "__all__"
		widgets ={
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email Number'}),
			'phone_number': forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Number'}),
			'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),
		}

		error_messages = {
            'first_name': {'required': 'Name is required'},
            'Last_Name': {'required': 'Last Name is required'},
            'email': {'required': 'Email is required'},
			'phone_number': {'required': 'Number is required'},
			'password': {'required': 'Password is required'},
			
        }


class loginForm(forms.ModelForm):
	class Meta:
		model=user_reg
		fields=['first_name','password'] 
		widgets ={
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Email/number'}),
			'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),
		}
		error_messages = {
            'first_name': {'required': 'Field is required'},
			'password': {'required': 'Password is required'},
        }

class productForm(forms.ModelForm):
	class Meta:
		model=product_details
		fields = "__all__"
		widgets ={
			'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Product Name'}),
			'product_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Product Rate'}),
			'product_description': forms.Textarea(attrs={'rows': 3,'class': 'form-control', 'placeholder':'Product Specification ..'}),
			'product_status': forms.Select(attrs={'class': 'form-control'}),
		}
		error_messages = {
            'product_name': {'required': 'Product Name is required'},
            'product_rate': {'required': 'Product rate is required'},
			'product_description': {'required': 'Product specification is required'},
			'product_status': {'required': 'Product status is required'},
		}