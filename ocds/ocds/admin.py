from django.contrib import admin
from .models import UserInfo, TutorInfo, LectureInfo, ResultInfo, EventInfo


# Register your models here.
admin.site.register(UserInfo)
admin.site.register(TutorInfo)
admin.site.register(LectureInfo) 
admin.site.register(ResultInfo) 
admin.site.register(EventInfo) 
##//, LectureInfo, ResultInfo, EventInfo)

