from django.contrib import admin
from main_app.models import Contact, FAQ
from main_app.models import Index, Services


# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['section', 'description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    def has_add_permission(self, request):
        # Имеет разрешение на добавление только 1-го поста
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    def has_add_permission(self, request):
        # Имеет разрешение на добавление только 1-го поста
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
