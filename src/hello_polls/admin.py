'''
Created on Jan 24, 2013

@author: KenD
'''
from hello_polls.models import MyPoll
from django.contrib import admin
from hello_polls.models import MyChoice


class MyChoiceInline(admin.TabularInline):
    model = MyChoice
    extra = 3

class MyPollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [MyChoiceInline]

admin.site.register(MyPoll, MyPollAdmin)