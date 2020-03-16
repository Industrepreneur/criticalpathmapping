# from django.contrib.auth.tests.utils import skipIfCustomUser
# from django.contrib.auth.tests.custom_user import CustomUser, ExtensionUser
# from django.test import TestCase, override_settings
from django.test import TestCase


class ApplicationTestCase(TestCase):
    pass
    # @override_settings(AUTH_USER_MODEL='auth.CustomUser')
    # def test_custom_user(self):
    #     "Run tests for a custom user model with email-based authentication."
    #     self.assertFalse(True)


# from django.test import TestCase

# from .models import

# from .models import Company


# class CompanyCreationTestCase(TestCase):
#     def setUp(self):
#         Company.objects.create(
#             id=1,
#             name='Some funky company',
#             is_active=True,)
#         Company.objects.create(
#             id=2,
#             name='Another company',
#             is_active=False,)
#         Company.objects.create(
#             id=3,
#             is_active=True,)

#     def test_companies_have_names(self):
#         """Companies must have a valid name."""
#         company_one = Company.objects.get(id=1)
#         company_two = Company.objects.get(id=2)
#         # company_three = Company.objects.get(id=3)
#         self.assertEqual(company_one.name, 'Some funky company')
#         self.assertEqual(company_two.name, 'Another company')
#         # self.assertNone(company_three)
