# User Backend

The social distancing service should have a three layer user system which include custom permission groups like customers, vendors and admins. Customers can book time slots for a specific vendor and admin users are there for managing the site.

User system in django is done by extending the base user model into a custom user with booleans defining the user role.

```python
is_customer = False
is_vendor = True
is_admin = False
```

This configuration tells us that the given user is a vendor. Each user will then have a profile attached to the type of user they are, like if a user is a customer then the user will have a profile which will be made specifically for collecting data from the customer side of things and nothing else.

### `Every user have their own profile`

```python
class customer_profile(models.Model):
    user = models.OneToOneField(ExtendedUserModel)
```

Here the user will be linked to a customer profile model as the user variable, indicating the model is in a one to one relationship with the extended user, and this model can have data which will suit the customer.

```python
    user = models.OneToOneField(ExtendedUserModel)

    first_name = models.CharField()
    last_name = models.CharField()
    phone = models.CharField()
    address = models.CharField()
    .
    .
    .
```

these fields in the profile will only be available for the customer users. Customers have permission to create or change certain models like the profile and event registration model, they will not have permission to edit or interfere with other models for admins and vendors.

Since the vendors does not need information like first and last name they will have a different profile with fields more specific to them.The linking process will be the same only the fields will change, there will be a model called `vendor_profile` just like the customers.

```python
    user = models.OneToOneField(ExtendedUserModel)

    vendor_addr = models.TextField()
    phone = models.CharField()
    zipcode = models.CharField()
    .
    .
    .
```

Whereas admins dont require detailed information they just have to be authorized so the `admin_profile` will store the admin previlages available to the user.

```python
    user = models.OneToOneField(ExtendedUserModel)

    is_god = models.BooleanField(default=True)
    can_edit_vendor = models.BooleanField(default=True)
    can_edit_customer = models.BooleanField(default=True)
    .
    .
    .
```
