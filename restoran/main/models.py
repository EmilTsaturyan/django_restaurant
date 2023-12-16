from django.db import models

# Create your models here.

class Contact(models.Model):

    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('Message')


    def __str__(self) -> str:
        return self.email


class Booking(models.Model):
    
    COUNT_CHOICE = (
        ('People 1', 'People 1'),
        ('People 2', 'People 2'),
        ('People 3', 'People 3'),
    )

    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    date = models.CharField('Date', max_length=60)
    count = models.CharField('Number of people', choices=COUNT_CHOICE, max_length=30)
    special = models.TextField('Special Request')


    def __str__(self) -> str:
        return self.email
    

class Index(models.Model):

    first_line = models.CharField('First line', max_length=50)
    second_line = models.CharField('Second line', max_length=50)
    description = models.TextField('Description')
    button = models.CharField('Button', max_length=50)
    image = models.ImageField('Image', upload_to='index')

    def __str__(self) -> str:
        return 'Index'

class Service(models.Model):

    icon_name = models.CharField('Icon name', max_length=50)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description')

    def __str__(self) -> str:
        return self.name
    

class Menu(models.Model):

    TYPE_CHOICE = (
        ('Breakfast', 'Breakfast'),
        ('Launch', 'Launch'),
        ('Dinner', 'Dinner')
    )

    name = models.CharField('Food name', max_length=50)
    image = models.ImageField('Food image')
    description = models.TextField('Description')
    price = models.PositiveIntegerField('Price')
    type = models.CharField('Type', choices=TYPE_CHOICE, max_length=30)

    def __str__(self) -> str:
        return self.name
    

class Team(models.Model):

    name = models.CharField('Name', max_length=50)
    image = models.ImageField('Image')
    description = models.TextField('Description')

    def __str__(self) -> str:
        return self.name
    

class Testimonial(models.Model):

    name = models.CharField('Name', max_length=50)
    profession = models.CharField('Profession', max_length=50)
    image = models.ImageField('Image')
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.name
    

class About(models.Model):

    experience = models.PositiveIntegerField('Years Of Experience')
    master_chefs = models.PositiveIntegerField('Popular Master Chefs')
    description = models.TextField('Description')
    image_1 = models.ImageField('Image 1')
    image_2 = models.ImageField('Image 2')
    image_3 = models.ImageField('Image 3')
    image_4 = models.ImageField('Image 4')

    def __str__(self) -> str:
        return 'About'