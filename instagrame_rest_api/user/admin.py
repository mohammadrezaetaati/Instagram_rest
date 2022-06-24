from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import User,Follow


admin.site.register(User)
admin.site.register(Follow)

