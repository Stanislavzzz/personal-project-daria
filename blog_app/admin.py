from django.contrib import admin

from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'created_at', 'tag_list')
    ordering = ('-rating', 'created_at')
    list_filter = ('rating', 'author')
    search_fields = ('title', 'content')
    search_help_text = 'Введите часть заголовка или текста поста'

    # fields = ('title', 'author', 'content', 'rating', 'tags')
    # readonly_fields = ('rating', )

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'author')
        }),
        ('Дополнительная информация', {
            'fields': ('content', 'rating', 'tags'),
            'classes': ('collapse',)
        }),
    )

    @admin.action(description="Увеличить рейтинг")
    def inc_rating(self, request, queryset):
        for post in queryset:
            post.rating = post.rating + 1
            post.save()
        self.message_user(request, f"{queryset.count()} постов обновлено")

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    actions = (inc_rating, )

    tag_list.short_description = "Тэги"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    pass