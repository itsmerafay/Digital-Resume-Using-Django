from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

#  In Django, a "slug" is a short label that contains only letters, numbers, hyphens, or underscores. It is commonly used to create human-readable and SEO-friendly URLs. Slugs are often derived from the title of an object, such as a blog post or product, to create a URL that is easy to understand.
# slug used automatically generated
# These built-in functions and the Meta class are part of Django's model definition and customization features. They help you control how your models are displayed, saved, and interacted with in your Django application.
# meta class : Specifies the human-readable names for the model in plural and singular forms.
# save(self, *args, **kwargs): Customizes the save behavior to set slug using slugify when creating a new portfolio entry.
# get_absolute_url(self): Returns the absolute URL for the portfolio entry.
#  for :

# def save(self, *args, **kwargs):
    # if not self.id:
    #     self.slug = slugify(self.name)
    # super(Blog, self).save(*args, **kwargs)

#  this explains above :
# If it's a new object (no ID assigned), it generates a slug based on the name.
# Then, it calls the save method of the parent class to perform the standard saving process.


# Create your models here.


class Skill(models.Model):
    class Meta: # data about data
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null= True)
    image = models.FileField(blank=True, null = True, upload_to = "skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank= True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ['timestamp']

# purpose :
# Without Customization:
# It might display as "Contactprofile" or something similar based on default inflections.

# With Customization:
# It will specifically display as "Contact Profile" in the singular form.


    timestamp = models.DateTimeField(auto_now_add = True)
    name = models.CharField(verbose_name="Name", max_length = 100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name = "Message")


    def __str__(self):
        return f"{self.name}"
    
class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = "Testimonials"
        verbose_name = "Testimonial"
        #  The ordering option takes a list of field names or expressions by which the results should be sorted.
        ordering = ["name"]
    
    thumbnail = models.ImageField(blank=True, null=True, upload_to = "testimonials")
    name = models.CharField(max_length = 200, blank = True, null=True)
    role = models.CharField(max_length = 200, blank = True, null=True)
    quote = models.CharField(max_length = 200, blank = True, null=True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    

class Media(models.Model):
    class Meta:
        verbose_name_plural = "Media Files"
        verbose_name = "Media File"
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

        def __str__(self):
            return self.name
        
class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio Profile'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length = 200, blank= True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True) 
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name) # rafay-atiq
        super(Portfolio, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 200 , blank= True, null=True)
    name = models.CharField(max_length=500, blank = True, null=True)
    description = models.CharField(max_length = 500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        f"/portfolio/{self.slug}"

class Certificate(models.Model):
    class Meta :
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length = 50, blank = True, null = True)
    title = models.CharField(max_length = 200, blank=True, null=True)
    description = models.CharField(max_length = 500, blank=True, null=True)
    is_active = models.BooleanField(default = True)

    def __str__(self) :
        return self.name