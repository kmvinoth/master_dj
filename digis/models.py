from django.db import models


# When the project admin adds the members, it should be added automatically to the users table in the database
# with particular permissions  (to a particular group based on their role)
class Members(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    email      = models.EmailField()


class AdminstrativeMetaData(models.Model):
    SubmittingOrganization    = models.CharField(max_length=80)
    OrganizationIdentifier   = models.CharField(max_length=80)
    ContractNumber           = models.CharField(max_length=80)
    Contact                  = models.CharField(max_length=80)
    ContactEmail             = models.EmailField()

    # Below fields may vary for each deposit
    TransferCurator          = models.CharField(max_length=80)
    TransferCuratorEMail     = models.EmailField()
    SubmissionName           = models.CharField(max_length=80)
    SubmissionDescription    = models.TextField()
    RightsDescription        = models.TextField()
    AccessRights             = models.CharField(max_length=80)
    License                  = models.CharField(max_length=80)
    DataSourceSystem         = models.CharField(max_length=80)
    MetadataFile             = models.CharField(max_length=80)
    MetadataFileFormat       = models.CharField(max_length=80)


class DataUpload(models.Model):
    Title_dataset    = models.CharField(max_length=80)
    Author           = models.CharField(max_length=30)
    CreationDate     = models.DateField()
    Department       = models.CharField(max_length=30)
    Funder           = models.CharField(max_length=30)
    Project          = models.CharField(max_length=30)
    Abstract_dataset = models.TextField()
    Methodology      = models.TextField()




