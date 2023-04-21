from django.db import models

# Create your models here.

class Phones(models.Model):

    name = models.CharField('Phone name',max_length=100)
    price = models.PositiveIntegerField('Phone price')
    about = models.TextField('Phone about')
    image = models.ImageField('Phone img',upload_to='Phone') #mediai mej sarquma phone u nkary qcuma phone papki mej

    def __str__(self):
        return self.name