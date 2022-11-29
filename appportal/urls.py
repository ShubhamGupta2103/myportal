from django.urls import path,include
from.import views#used . for current directory
urlpatterns = [
  path("",views.home,name="home"),  
  path("bloodgroup",views.bloodgroup,name="bloodgroup"),
  path("diseases",views.diseases,name="diseases"),
  path("donationtype",views.donationtype,name="donationtype"),
  path("contactus/",views.contactus,name="contactus"),
  path("feedback/",views.feedback,name="feedback"),
  path("donorlist/",views.donorlist,name="donorlist"),
  path('member_registration/',views.member_registration,name="member_registration"),
  path('member_login/',views.member_login,name="member_login"),
  path('member_edit_profile/',views.member_edit_profile,name="member_edit_profile"),
  path('member_logout/',views.member_logout,name="member_logout"),
  path('member_view_profile/',views.member_view_profile,name="member_view_profile"),
  path("AboutUs/",views.AboutUs,name="AboutUs"),
  path("member_experience/",views.member_experience,name="member_experience"),
  path("experience/",views.experience,name="experience"),
]