from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin
from apps.users.models import User

admin.site.register(User)
