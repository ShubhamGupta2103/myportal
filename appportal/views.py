from email import message
from django.shortcuts import render,HttpResponse,redirect
from .models import BloodDonor,Experience,Health_Campaign,Contact,FeedBack
from django.contrib import messages

# Create your views here.
def home(request):
    compaign_objects=Health_Campaign.objects.all()
    compaign_dict={
        "compaign_key":compaign_objects
    }
    return render(request,'index.html',compaign_dict)



def bloodgroup(request):
    return render(request,'bloodgroup.html')

def AboutUs(request):
    return render(request,'aboutus.html')

def donationtype(request):
    return render(request,'donationtype.html')

def diseases(request):
    return render(request,'diseases.html')

def member_login(request):
    if request.method=="GET":
      return render(request,'login.html')

    if request.method=="POST":
        donor_id=request.POST["donorid"]
        donor_password=request.POST["donorpass"]

        donor_query_set=BloodDonor.objects.filter(Donerid=donor_id,Password=donor_password)
        print(len(donor_query_set))
        if len(donor_query_set)>0:
            request.session["donor_session"]=donor_id#builtin dictionary 
            
            donor_object={"donor_data":donor_query_set}
            return render(request,'member/member_home.html',donor_object)
            

        else:
            messages.error(request,"Invalid Credential")
            return render(request,'login.html')

def member_registration(request):
    if request.method=="GET":
        plan_objects=BloodDonor.objects.all()
        plan_dict={"plan_key":plan_objects}
        return render(request,'registration.html',plan_dict)

    if request.method=="POST":
        member_id=request.POST["txtdonorid"]
        member_pass=request.POST["txtdonorpass"]
        member_name=request.POST["txtname"]
        member_phone=request.POST["txtphone"]
        member_address=request.POST["txtaddress"]
        member_city=request.POST["cmbcity"]
        member_gender=request.POST["gender"]
        member_age=request.POST["txtage"]
        member_group=request.POST["cmbgrp"]
        member_email=request.POST["txtemail"]
       
       
        # len(member_age)>2 or int(member_age)<0:
        if int(member_age)<18 or int(member_age)>60:
             messages.success(request,"You are not eligible for Blood Donation")
             return render(request,'registration.html')

        elif len(member_phone)>10 or int(member_phone)<10 or int(member_phone)<0:
             messages.success(request,"Please enter a valid phone number")
             return render(request,'registration.html')


        else:
            new_member=BloodDonor(Donerid=member_id,Password=member_pass,Name=member_name,Age=member_age,Phone=member_phone,CityName=member_city,Address=member_address,Gender=member_gender,Bloodgroup=member_group,Email=member_email)
            new_member.save()
            print("Member registered successfully")
            messages.error(request,"Thank you for being a Member")
            return render(request,'registration.html')


def member_edit_profile(request):
    if "donor_session" not in request.session.keys():
        return redirect("member_login")

    if request.method=="GET":
        loggedIn_member_Id=request.session["donor_session"]
        member_object=BloodDonor.objects.get(Donerid=loggedIn_member_Id)
        member_dict={
            "donor_data":member_object
        }

        return render(request,'member/member_editprofile.html',member_dict)

    if request.method=='POST':
        ph=request.POST["Phone"]
        add=request.POST["Address"]
        loggedIn_member_Id=request.session["donor_session"]
        member_object=BloodDonor.objects.get(Donerid=loggedIn_member_Id)
        
        member_object.Phone=ph
        member_object.Address=add
        member_object.save()
        member_dict={
            "donor_data":member_object
        }

        messages.success(request,"Profile updated successfully")

        return render(request,'member/member_editprofile.html',member_dict)


def member_logout(request):
    if "donor_session" not in request.session.keys():
        return redirect("member_login")


    del request.session["donor_session"]#it is used to destroy the session
    return redirect("member_login")

##view profile##
def member_view_profile(request):

    if "donor_session" not in request.session.keys():
        return redirect("member_login")
        
    if request.method=="GET":
        loggedIn_member_Id=request.session["donor_session"]#fetch
        member_object=BloodDonor.objects.get(Donerid=loggedIn_member_Id)

        member_dict={
            "donor_data":member_object
        }

        return render(request,'member/member_view_profile.html',member_dict)
        

def feedback(request):
    if request.method=="GET":
        return render(request,'feedback.html')
    if request.method=="POST": #request.POST is dictionary and control names are keys here
        user_name=request.POST["txtname"]
        user_email=request.POST["txtemail"]
        user_rate=request.POST["txtrate"]
        user_feedback=request.POST["txtfeedback"]
        m=FeedBack(Name=user_name,Email=user_email,Rating=user_rate,Feedbacktext=user_feedback)# object creation
        m.save()# object saving and it will store data into Contact table using ORM
        print("feedback saved successfully")
        return render(request,'feedback.html')

def contactus(request):
    if request.method=="GET":
        return render(request,'contactus.html')
    if request.method=="POST": #request.POST is dictionary and control names are keys here
        user_name=request.POST["txtname"]
        user_email=request.POST["txtemail"]
        user_phone=request.POST["txtphone"]
        user_query=request.POST["txtquestion"]
        c=Contact(Name=user_name,Email=user_email,Phone=user_phone,question=user_query)# object creation
        c.save()# object saving and it will store data into Contact table using ORM
        print("Contact saved successfully")
        messages.success(request,"Thank you for contacting us ")
        return render(request,'contactus.html')

def member_experience(request):
    if request.method=="GET":
        return render(request,'member_experience.html')

    if request.method=="POST": #request.POST is dictionary and control names are keys here
        user_name=request.POST["txtdonorid"]
        user_subject=request.POST["txtsubject"]
        user_remarks=request.POST["txtremarks"]
        
        c=Experience(Doner_id=user_name,Subject=user_subject,Remarks=user_remarks)# object creation
        c.save()# object saving and it will store data into Contact table using ORM
        print("Experience saved successfully")
        messages.success(request,"Thank you for sharing your experience ")
        return render(request,'member_experience.html')

def donorlist(request):
    donor_objects=BloodDonor.objects.all()#it returns queryset
    
#How to send data on an html template from view
    donor_dict={
        "donor_data":donor_objects
    }

    return render(request,'donorlist.html',donor_dict)

def experience(request):
    donor_objects=Experience.objects.all()#it returns queryset
    
#How to send data on an html template from view
    donor_dict={
        "donor_data":donor_objects
    }

    return render(request,'experience.html',donor_dict)


def member_edit_profile(request):
    if "donor_session" not in request.session.keys():
        return redirect("member_login")

    if request.method=="GET":
        loggedIn_member_Id=request.session["donor_session"]
        member_object=BloodDonor.objects.get(Donerid=loggedIn_member_Id)
        member_dict={
            "donor_data":member_object
        }

        return render(request,'member/member_editprofile.html',member_dict)

    




