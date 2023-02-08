from modeltranslation.translator import translator, TranslationOptions

from core.models import Test


class ModelkaTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Modelka.
    """

    fields = ('name',)


translator.register(Test, ModelkaTranslationOptions)
