from django.db import models

## 자동으로 증가하는 primary key setting
# class CustomAutoField(models.AutoField):
    
#     def db_type(self, connection):
#             return 'mediumint(8) UNSIGNED AUTO_INCREMENT'
#     def rel_db_type(self, connection):
#         return 'mediumint(8) UNSIGNED'


## 사용자 테이블 
class UserInfo(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    registration_date = models.DateTimeField()


class TutorInfo(models.Model):
    tutor_id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=50)
    tutor_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    registration_date = models.DateTimeField()

class LectureInfo(models.Model):
	lecture_id = models.BigAutoField(primary_key=True)
	lecture_name = models.CharField(max_length=100)
	tutor_id = models.ForeignKey(TutorInfo, on_delete=models.CASCADE)
	recommended = models.FloatField()
	lecture_url = models.CharField(max_length=250)
	lecture_length = models.IntegerField()
	registration_date = models.DateTimeField() 

class ResultInfo(models.Model):
    result_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(LectureInfo, on_delete=models.CASCADE)
    capture_start = models.TimeField()
    capture_end = models.TimeField()
    start_log = models.TimeField()
    end_log = models.TimeField()
    registration_date = models.DateTimeField() 

class EventInfo(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    result_id = models.ForeignKey(ResultInfo, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(LectureInfo, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    continued_time = models.IntegerField()
    registration_date = models.DateTimeField() 

