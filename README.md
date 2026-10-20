https://www.djangoproject.com/

pip install django
django-admin --version

django-admin startproject config .

python manage.py runserver

python manage.py startapp blog_app


https://sqlitebrowser.org/

python manage.py migrate
python manage.py createsuperuser

python manage.py makemigrations


>>> from blog_app.models import Post
>>> post = Post(title="Первый пост", content="Привет, Мир!", author="Bob")
>>> post.save()
>>> post1 = Post(title="Второй пост", content="Пока, Мир!", author="Mary")
>>> post1.save()
>>> all_post = Post.objects.all()
>>> all_post
<QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>
>>> all_post[1].author
'Mary'
>>> all_post[0].title
'Первый пост'
> 
> Один ко многим
> 
>>> post = Post.objects.create(title="Важный пост", content="Завтра выходит новая версия Django!", author="Mary")
>>> comment1 = Comment.objects.create(text="Отличная новость", author="Bob", post=post)
>>> comment2 = Comment.objects.create(text="Супер!", author="Ivan", post=post)
>>> post.comments.all()
<QuerySet [<Comment: Author by Bob>, <Comment: Author by Ivan>]>
>>> post.comments.all()[0].text
'Отличная новость'
>>> comment1.post.title
'Важный пост'
> 
> Один к одному
> 
> >>> author = Author.objects.create(name="Sara")
>>> profile = AuthorProfile.objects.create(author=author, bio="Любитель программировать на Python", website="http://google.com")
>>> author.profile.bio
'Любитель программировать на Python'
>>> profile.author.name
'Sara'
> 
> 
> Многие ко многим
> 
> >>> post = Post.objects.all()[1]
>>> post
<Post: Второй пост>
>>> tag1 = Tag.objects.create(name="Django")
>>> tag2 = Tag.objects.create(name="Python")
>>> post.tags.add(tag1, tag2)
>>> post.tags.all()
<QuerySet [<Tag: Django>, <Tag: Python>]>
>>> tag1.posts.all()
<QuerySet [<Post: Второй пост>]>
>>> exit()
now exiting InteractiveConsole...
> 
> 

# fixtures
python manage.py loaddata blog_fixtures.json

python manage.py dumpdata blog_app
python manage.py dumpdata blog_app > blog_app_export.json
python manage.py dumpdata blog_app --indent 4 > blog_app_export.json
python manage.py dumpdata blog_app.Post --indent 4 > blog_app_post_export.json

