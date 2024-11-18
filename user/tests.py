from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from student.models import User  # Adjust the import according to your structure

class UserModelTest(TestCase):
    # Test case for the User model
    def setUp(self):
        # Create a valid user instance to use in tests
        self.valid_user = User.objects.create(
            first_name="John",
            last_name="Doe",
            user_name="johndoe",
            password="mypassword",
            role=User.STUDENT  # Assigning a role
        )

    # 1. Test Missing Required Field (first_name)
    def test_missing_first_name(self):
        user = User(
            last_name="Doe",
            user_name="johndoe",
            password="mypassword",
            role=User.STUDENT
        )
        with self.assertRaises(IntegrityError):
            user.save()  # Attempt to save should raise an error

    # 2. Test Missing Required Field (last_name)
    def test_missing_last_name(self):
        user = User(
            first_name="John",
            user_name="johndoe",
            password="mypassword",
            role=User.STUDENT
        )
        with self.assertRaises(IntegrityError):
            user.save()

    # 3. Test Missing Required Field (user_name)
    def test_missing_user_name(self):
        user = User(
            first_name="John",
            last_name="Doe",
            password="mypassword",
            role=User.STUDENT
        )
        with self.assertRaises(IntegrityError):
            user.save()

    # 4. Test Missing Required Field (password)
    def test_missing_password(self):
        user = User(
            first_name="John",
            last_name="Doe",
            user_name="johndoe",
            role=User.STUDENT
        )
        with self.assertRaises(IntegrityError):
            user.save()

    # 5. Test Exceeding Max Length for first_name
    def test_first_name_too_long(self):
        user = User(
            first_name="x" * 21,  # Exceeds max length
            last_name="Doe",
            user_name="johndoe",
            password="mypassword",
            role=User.STUDENT
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  # Validate the model

    # 6. Test Exceeding Max Length for last_name
    def test_last_name_too_long(self):
        user = User(
            first_name="John",
            last_name="x" * 21,  # Exceeds max length
            user_name="johndoe",
            password="mypassword",
            role=User.STUDENT
        )
        with self.assertRaises(ValidationError):
            user.full_clean()

    # 7. Test Duplicate Usernames
    def test_duplicate_user_name(self):
        # Create the first user
        User.objects.create(
            first_name="Alice",
            last_name="Smith",
            user_name="johndoe",
            password="password123",
            role=User.STUDENT
        )
        # Attempt to create a second user with the same username
        user = User(
            first_name="Bob",
            last_name="Brown",
            user_name="johndoe",  # Duplicate username
            password="mypassword",
            role=User.TEACHER
        )
        with self.assertRaises(IntegrityError):
            user.save()  # This should fail

    # 8. Test Invalid Role Assignment
    def test_invalid_role_assignment(self):
        user = User(
            first_name="John",
            last_name="Doe",
            user_name="johndoe",
            password="mypassword",
            role="invalid_role"  # Invalid role
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  # Validate the model


# Create your tests here.
