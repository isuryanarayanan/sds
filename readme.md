# Social Distancing Service

- Author [DevDooDan](https://www.instagram.com/devdoodan/)
- backend `Django`
- frontend `Vue js`

## An Event

`Event is an action taken by the customer on the vendor which is managed by the administrator`

For example, imagine you have to go to the bank. You're account needs to be freezed as you have noticed it has been subjected to online scamming. as the socially responsible and smart being you are you chose to go to the bank when there is the least amount of people there. So you pick a time between 10am and 4pm and you went to the bank expecting the least amount of interaction, but for your suprise the bank was packed.

So in the scenario the event is you going to the bank and obviously you become the customer in this system, the bank will be the vendor.

You can pick a time slot from the vendor page and make sure there is only a certain number of people there at the time.

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
