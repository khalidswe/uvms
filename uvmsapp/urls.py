from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("homepage",views.Homepage,name="homepage"),
    path("busdetails/",views.DetailsPage,name="busdetails"),
    path("signuppage/",views.SignUpPage,name="signuppage"),
    #path("loginpage/",views.LogInPage,name="loginpage"),
    path("s&c/",views.SugAndCompPage,name="s&c"),
    path("rent/",views.RentPage,name="rent"),
    path("book/",views.BookPage,name="book"),
    path("signup/",views.SignUp,name="signup"),
    path("login/",views.LogIn,name="login"),
    path("profile/<int:pk>",views.Profile,name="profile"),
    path("updateprofilepage/<int:pk>",views.UpdateProfilePage,name="updateprofilepage"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("searchresult/",views.SearchResultPage,name="searchresult"),
    path("searchbus/",views.SearchBus,name="searchbus"),
    path("logout/",views.LogOut,name="logout"),


]