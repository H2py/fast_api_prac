from django.db import models

class Category(models.Model):
    """models.Model은 DB 테이블로 자동 변환해줌, blog_category에 key(자동 생성) - value(name)으로 데이터 저장"""
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"  # admin 페이지에서 복수형 이름 설정
    
    def __str__(self):
        return self.name


class Post(models.Model):
    """
    blog_post에 id(integer, primary_key) 그리고 manytomany를 이용하여, blog_post_categories라는 중간 연결 테이블을 만든다 
    id / post_id / category_id가 저장됨, 많은 post / category를 연결하기 위해서 사용함
    ManyToManyField의 첫 인자는 연결할 model을 설정한 뒤, related_name을 이용해서 반대편 모델에서 이 관계를 역으로 참조할 수 있게 만든다
    """
    
    title = models.CharField(max_length=255) # VARCHAR로 저장
    body= models.TextField() # TEXT로 저장 됨
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    """on_delete=models.CASCADE는 폭포처럼, POST라는 부모가 사라지면, comment도 사라지게 만든다는 의미를 담고 있음 Foreign key는 one to many 관계를 담음"""
    author = models.CharField(max_length=60)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"