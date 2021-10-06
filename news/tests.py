from django.test import TestCase
from .models import Editor, Article, tags

# Create your tests here.
class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.sharry=Editor(first_name='Sharry', last_name='Cherop', email='sharry@moringaschool.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharry,Editor))
    
    #Testing Save method
    def test_save_method(self):
        self.sharry.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)> 0)