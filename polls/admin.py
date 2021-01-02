from django.contrib import admin
from .models import Question, Choice


# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
