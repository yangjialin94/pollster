from django.contrib import admin

# bring in our models
from .models import Question, Choice

# change admin header
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"


class ChoiceInline(admin.TabularInline):  # want to show choices under questions
    model = Choice
    extra = 3       # how many extra field do we want


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# register models
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
