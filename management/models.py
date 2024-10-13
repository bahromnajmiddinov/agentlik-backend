from django.db import models

from core.models import TimeStamps
# from labeler.models import SubCategory


# class AgencyCategory(models.Model):
#     sub_category = models.OneToOneField('labeler.SubCategory', on_delete=models.SET_NULL, null=True, 
#                                         related_name='agencies')
#     staffs = models.ManyToManyField('Staff', blank=True, related_name='agency_categories', 
#                                     through='AgencyCategoryThrouh')
#     created_at = models.DateField(auto_now_add=True)


# class AgencyCategoryThrouh(models.Model):
#     staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
#     agency_category_name = models.CharField(max_length=300)
#     agency_category = models.ForeignKey('AgencyCategory', on_delete=models.CASCADE)


class Role(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description


class Staff(TimeStamps):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    role = models.OneToOneField(Role, on_delete=models.SET_NULL, null=True)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    website_url = models.URLField()
    address = models.CharField(max_length=200)

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

    def __str__(self):
        return self.get_full_name
