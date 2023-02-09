from django.contrib import admin
from parler.admin import TranslatableAdmin


from .models import Base, MenuLevOne, MenuLevTwo

admin.site.register(Base, TranslatableAdmin)
admin.site.register(MenuLevOne, TranslatableAdmin)
admin.site.register(MenuLevTwo, TranslatableAdmin)

