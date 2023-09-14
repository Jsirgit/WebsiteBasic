from django.contrib import admin
from.models import Post


# Register your models here.
@admin.register(Post)

class PostModelAdmin(admin.ModelAdmin):

  # list_display = ['stuid','stuname','stuemail','stupass','comment'
  # ]

  list_display=['title','content','pub_date']