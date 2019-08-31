from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    '''
    Ensures our static files are stored in 'static' directory in S3
    '''
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    '''
    Ensures our media files are stored in 'media' directory in S3
    '''
    location = settings.MEDIAFILES_LOCATION
