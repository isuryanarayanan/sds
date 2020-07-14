from accounts.models.profiles.customer import customer_profile
from accounts.models.profiles.vendor import vendor_profile
from accounts.models.profiles.administrator import administrator_profile
from django import forms


class CustomerProfileCreationForm(forms.ModelForm):
    """
    Creates the customer user profile.
    """
    class Meta:
        model = customer_profile
        fields = "__all__"


class VendorProfileCreationForm(forms.ModelForm):
    """
    Creates the vendor user profile.
    """
    class Meta:
        model = vendor_profile
        fields = "__all__"


class AdministratorProfileCreationForm(forms.ModelForm):
    """
    Creates the administrator user profile.
    """
    class Meta:
        model = administrator_profile
        fields = "__all__"
