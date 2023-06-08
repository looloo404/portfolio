from django import forms
from .models import UserInfo, TutorInfo, LectureInfo, EventInfo, ResultInfo

class UserInfoForm(forms.ModelForm):
    # image -> imagefile 변경 
    class Meta:
        model = UserInfo
        fields = (
                'user_id',
                'password',
                'user_name',
                'email',
                'registrationDate'
        )  
   
class TutorInfoForm(forms.ModelForm):
    class Meta:
        model = TutorInfo
        fields = (
                'tutorId',
                'password' ,
                'tutorName',
                'email',
                'registrationDate'
        )  

class LectureInfoForm(forms.ModelForm):
    class Meta:
        model = LectureInfo
        fields = (
                'lectureId',
                'lectureName' ,
                'tutorId',
                'recommended',
                'lectureUrl',
                'lectureLength', 
                'registrationDate'
        )  

class ResultInfoForm(forms.ModelForm):
    class Meta:
        model = ResultInfo
        fields = (
                'resultId', 
                'userId', 
                'lectureId', 
                'captureStart', 
                'captureEnd', 
                'startLog', 
                'endLog',
                'registrationDate'
        )

class EventInfoForm(forms.ModelForm):
    class Meta:
        model = EventInfo
        fields = (
                'eventId', 
                'resultId', 
                'lectureId',
                'awake',
                'sleep',
                'stateNo',
                'continuedTime',
                'registrationDate'
        )
    