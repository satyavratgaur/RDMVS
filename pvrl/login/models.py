from django.db import models

# Create your models here.
class UserCredentials(models.Model):
    """Class for saving user login details"""

    # Fields
    uname = models.CharField(max_length=50, help_text='User name')
    psw = models.CharField(max_length=50, help_text='Password')

    # Metadata
    class Meta: 
        ordering = ['-uname','-psw']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of username."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Username object (in Admin site)."""
        return self.uname
