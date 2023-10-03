from django.contrib import admin
from .models import Sector , Studet, Teacher, Schedule, Room, News, Feedback,SectorMessage
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class TeachearAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'middle_name', 'phone_no')
    search_fields=('first_name',)

class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    list_display= ('first_name', 'middle_name', 'phone_number', 'sex', 'email' ,'status', 'sector','type' , 'date')
    list_filter= ('type','status', 'sector', 'sex')
    search_fields=('first_name',)


class SectorsAdmin(admin.ModelAdmin):
    list_display = ( 'title','type')

class SectorMessageAdmin(admin.ModelAdmin):
    list_display = ( 'title','type')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'time', 'room', 'sector', 'teacher')
    ordering =('-day',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'campaus')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('header', 'message' )

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message')






admin.site.register(Sector, SectorsAdmin)
admin.site.register(SectorMessage, SectorMessageAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Studet, StudentAdmin)
admin.site.register(Teacher, TeachearAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
