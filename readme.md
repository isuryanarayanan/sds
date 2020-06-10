# Social Distancing Service

- Author [DevDooDan](https://www.instagram.com/devdoodan/)
- backend `Django`
- frontend `Vue js`

## Designing a user system

The social distancing service should have a three layer user system which include custom permission groups like customers, vendors and admins. Customers can book time slots for a specific vendor and admin users are there for managing the site.

User system in django is done by extending the base user model into a custom user with booleans defining the user role.

```python
is_customer = False
is_vendor = True
is_admin = False
```

This configuration tells us that the given user is a vendor. Each user will then have a profile attached to the type of user they are, like if a user is a customer then the user will have a profile which will be made specifically for collecting data from the customer side of things and nothing else.

that winds up the breif about user backend you can find more in `docs/backend`.
