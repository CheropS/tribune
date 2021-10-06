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

    #deleting 
    def test_delete_method(self):
        self.sharry.save_editor()
        self.sharry.delete_editor()
        editors=self.sharry.show_all_editors()
        self.assertTrue(len(editors) ==0)
    #updating first name
    def test_update_first_name(self):
        self.sharry.save_editor()
        self.sharry.update_first_name('test')
        self.assertTrue(self.sharry.first_name=='test')
        
    #updating last name
    def test_update_last_name(self):
        self.sharry.save_editor()
        self.sharry.update_last_name('cherop')
        self.assertTrue(self.sharry.last_name=='cherop')
