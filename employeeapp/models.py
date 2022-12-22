from django.db import models
from django.utils import timezone

class Employee( models.Model ):
    '''
    Employee model created with fields: name, email, date joined and the annual salary

    Name is a character field
    Email is a email field
    Date joined is a date field
    Annual salary is an integer field
    '''
    name = models.CharField( max_length=350 )
    email = models.EmailField( max_length=254, null=True )
    date_joined = models.DateField( default=timezone.now )
    annual_salary = models.IntegerField( default=0 )

    def __str__( self ):
        '''If the model were to be referenced it will be represented via the employee name'''
        return self.name

    def to_dict( self ):
        ''' Converts the model to a dictionary or JSON '''
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'date_joined': self.date_joined,
            'annual_salary': self.annual_salary,
        }

