from django.test import TestCase
from account.views import showmybooks
# Create your tests here.

class User:
    id=0

class Request:
    user = User()








class ProfilpageTest(TestCase):

    def setUp(self):
        self.req = Request()
        self.req.user.id = 3
        self.answer = showmybooks(self.req)

    def test_profillow(self):
        assert (self.answer is not None)

        #self.assertEqual(lion.speak(), 'The lion says "roar"')
        #self.assertEqual(cat.speak(), 'The cat says "meow"')
