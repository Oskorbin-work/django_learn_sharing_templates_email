from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class MenuLevTwo(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=90),
        address=models.CharField(max_length=90, default="#"),
    )

    def __str__(self):
        return self.name



class MenuLevOne(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=90),
        menu_two=models.ManyToManyField(MenuLevTwo, blank=True),
        address=models.CharField(max_length=90, default="#"),
    )

    def __str__(self):
        return self.name

class Base(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=90),
        name_menu=models.CharField(max_length=90, blank=True),
        menu_one=models.ManyToManyField(MenuLevOne, blank=True),
    )

    def __str__(self):
        return self.title

class ContentBody(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=90),
        name=models.CharField(max_length=90),
    )

    def __str__(self):
        return self.title