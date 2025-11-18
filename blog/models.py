from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # gera data automática
    updated_at = models.DateTimeField(auto_now=True)      # atualiza sempre que salvar

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)  # ex: "Python, Django, Bash"
    repo_url = models.URLField(blank=True, null=True)  # link do GitHub
    demo_url = models.URLField(blank=True, null=True)  # link do site (opcional)
    created_at = models.DateField()  # você define a data do projeto

    def __str__(self):
        return self.name

# Create your models here.
