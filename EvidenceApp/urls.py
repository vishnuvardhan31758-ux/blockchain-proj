from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='home'),
    	   path("index.html", views.index, name="index"),
	       path('AdminLogin.html', views.AdminLogin, name="AdminLogin"), 
	       path('OfficerLoginAction', views.OfficerLoginAction, name="OfficerLoginAction"),
	       path('OfficerLogin.html', views.OfficerLogin, name="OfficerLogin"), 
	       path('AdminLoginAction', views.AdminLoginAction, name="AdminLoginAction"),
	       path('AddOfficer.html', views.AddOfficer, name="AddOfficer"),
	       path('AddOfficerAction', views.AddOfficerAction, name="AddOfficerAction"),
	       path('ViewOfficer', views.ViewOfficer, name="ViewOfficer"),
	       path('ViewEvidence', views.ViewEvidence, name="ViewEvidence"),
	       path('AddEvidences.html', views.AddEvidences, name="AddEvidences"),
	       path('AddEvidencesAction', views.AddEvidencesAction, name="AddEvidencesAction"),
	       path('AccessEvidence', views.AccessEvidence, name="AccessEvidence"),
	       path('AccessEvidenceAction', views.AccessEvidenceAction, name="AccessEvidenceAction"),	  	       
]