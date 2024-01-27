# URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names
# In Django, the app_name variable is used to namespace the URL patterns of an app. It helps in avoiding naming conflicts between different apps in a project. 

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name = "home"),
    path('contact/', views.ContactView.as_view(), name = "contact"),
    path('portfolio', views.PortfolioView.as_view(), name = "portfolios"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name = "portfolio"),
    path('blog', views.BlogView.as_view(), name = "blogs"),
    path('blog<slug:slug>', views.BlogDetailView.as_view(), name = "blog"),
]
