from django.contrib import admin
from .models import (User, 
                     Organization, 
                     PreferredContact, 
                     Member
                     )

admin.site.register(User)
admin.site.register(Member)
admin.site.register(Organization)
admin.site.register(PreferredContact)

