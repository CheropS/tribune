from django.db import models

class Editor(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    def update_first_name(self,value):
        self.first_name=value
        self.save_editor()
        
    def update_last_name(self,value):
        self.last_name=value
        self.save_editor()

    @staticmethod
    def show_all_editors():
        return Editor.objects.all()

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=60)
    post=models.TextField()
    editor=models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags=models.ManyToManyField(tags)
    pub_date=models.DateTimeField(auto_now_add=True)