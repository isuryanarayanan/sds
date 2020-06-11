from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    The User model has a custom manager that has the following helper
    methods (in addition to the methods provided by BaseUserManager)
    """
    use_in_migrations = True

    def sudo_create_user(self, email, password, **extra_fields):
        """
        Saves a user with the passed arguments
        """
        if not email:
            raise ValueError('Email required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates a user without any privilages
        """
        extra_fields.setdefault('is_staff', False)

        return self.sudo_create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        print("super")
        """
        Creates a user with staff privilages
        """
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.sudo_create_user(email, password, **extra_fields)
