from django.contrib import admin

from .models import *


admin.site.register(UserModel)
admin.site.register(StudentInfo)

admin.site.register(School)

admin.site.register(Grade)
admin.site.register(Exam)
admin.site.register(Board)



admin.site.register(Subjects_of_class)
admin.site.register(Course)


