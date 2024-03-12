from django.contrib import admin
from .models import (User, 
                     Organization, 
                     PreferredContact, 
                     Member,
                     Product,
                     Cart,
                     CartItem
                     )

admin.site.register(User)
admin.site.register(Member)
admin.site.register(Organization)
admin.site.register(PreferredContact)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)


