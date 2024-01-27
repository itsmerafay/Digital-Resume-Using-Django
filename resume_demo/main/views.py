from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib import messages # we have called messages here so that when it is saved we can make a pop up for it
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

# urls - view (from form) - templates - models


from django.views import generic # generic is used in views for tasks like displaying temalate, objects , performing crud
from .forms import ContactForm

# class base views 
# class base views provides more structure , reusability , good for large applications
# also provide built-in mixins 
class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    # This method is used for overriding when want to pass additional data with template when rendering
    # self refers to instance of this view 
    # kwargs allows to accept any additional keyword args
    def get_context_data(self, **kwargs):
        
        # context is a dictionary here and super is calling up the parent class which is template view
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active = True)
        blogs = Blog.objects.filter(is_active = True)
        portfolio = Portfolio.objects.filter(is_active = True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio

        # the above all will be added in context and we can reference them in templates and render them using lists
        return context


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm    # our custom contactform
    success_url = "/"           # user will be directed after successful submission

    # it's a built-in method , and we are overriding by mentioning it here too , so that we can add additional functionality
    def form_valid(self, form): # special method in django that is called whenever the form is successfully validated
        form.save() 
        messages.success(self.request, 'Thank you. We will be in touch soon')
        return super().form_valid(form)       # built-in form_valid # shows after successful sumission of form go to success url
    

class PortfolioDetailView(generic.DetailView): # show details about portfolio
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class PortfolioView(generic.ListView): # show details about portfolio
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)  # return True or return the data where active is set to True

class BlogView(generic.ListView): # it's a view for displaying a list of portfolios.
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self): # return only those query or object data 
        return super().get_queryset().filter(is_active = True)
    

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"

