from django.db import models

class Faculty(models.Model):
    acronym = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=62)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.acronym

class Career(models.Model):
    name = models.CharField(max_length=38, primary_key=True)
    id_faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Organization(models.Model):
    abbreviation = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=38)
    description = models.CharField(max_length=100)
    id_tutor = models.OneToOneField('user.Professor', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class SubOrganization(models.Model):
    sub_org_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=38)
    description = models.CharField(max_length=100)
    id_organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    id_member_in_charge = models.OneToOneField('user.Member', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
