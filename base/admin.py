from django.contrib import admin
from parler.admin import TranslatableAdmin


from .models import Base, MenuLevOne, MenuLevTwo
from .models import ContentBody

# Base classes. All pages
admin.site.register(Base, TranslatableAdmin)
admin.site.register(MenuLevOne, TranslatableAdmin)
admin.site.register(MenuLevTwo, TranslatableAdmin)

# For body page. One entry basedata to one page
admin.site.register(ContentBody, TranslatableAdmin)


