from django.contrib import admin

from .models import Question, Choice, Eleitor

admin.site.site_header = "Administração Mesa de Voto"
admin.site.site_title = "Ola"
admin.site.index_title = "Bem vindo(a)"


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['question_text']}),
#                  ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
#     inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(Question, QuestionAdmin)
admin.site.register(Eleitor)