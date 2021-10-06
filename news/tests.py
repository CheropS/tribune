from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

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

class ArticleTestClass(TestCase):

    def setUp(self):
        #Creating a new editor and saving it
        self.sharry=Editor(first_name='Sharry', last_name='Cherop', email='sharry@moringaschool.com')
        self.sharry.save_editor()

        #creating a new tag and saving it
        self.new_tag=tags(name='testing')
        self.new_tag.save()

        self.new_article=Article(title='Test Article', post='This is a random test Post', editor=self.sharry)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        today_news=Article.todays_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):
        test_date='2017-03-17'
        date=dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)