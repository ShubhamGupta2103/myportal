from django.contrib import admin
from .models import BloodDonor,Experience,Health_Campaign,Contact,FeedBack

# Register your models here.


# class Admin_Coach(admin.ModelAdmin):
#     list_display=('Name','Email','phone','Experience')
#     search_fields=('Name',)


class Admin_BloodDonor(admin.ModelAdmin):
    list_display=('Name','Email','Address','Gender','Bloodgroup')
    search_fields=('Bloodgroup',)#it used for searching


class Admin_BloodDonor(admin.ModelAdmin):
    list_display=('Name','Phone','CityName','Bloodgroup')
    search_fields=('CityName',)
    list_filter=['CityName','Bloodgroup','Phone']

# admin.site.register(sport_detail,Admin_sport)
# admin.site.register(Membership_plan)
# admin.site.register(Coach_Detail,Admin_Coach)#it will show data in tabular formate
# admin.site.register(Member_Feedback)
# admin.site.register(Event)
# admin.site.register(Member_Detail,Admin_Member)
admin.site.register(BloodDonor,Admin_BloodDonor)
admin.site.register(Experience)
admin.site.register(Health_Campaign)
admin.site.register(Contact)
admin.site.register(FeedBack)



admin.site.site_header="Life Line Portal"
admin.site.site_title="Life Line Admin Dashboard"
admin.site.index_title="Welcome to Our Portal"

