from django.db import models

class Category(models.Model):
    """models.Model은 DB 테이블로 자동 변환해줌, blog_category에 key(자동 생성) - value(name)으로 데이터 저장"""
    name = models.CharField(max_length=30)

class Post(models.Model):
    """blog_post에 id(integer, primary_key) 그리고 manytomany를 이용하여, blog_post_categories라는 중간 연결 테이블을 만든다 id / post_id / category_id가 저장됨 """
    title = models.CharField(max_length=255) # VARCHAR로 저장
    body= models.TextField() # TEXT로 저장 됨
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)