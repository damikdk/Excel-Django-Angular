from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from .models import OfficeFile

class OfficeFileResource(ModelResource):
    """
    API Facet
    """
    class Meta:
        queryset = OfficeFile.objects.all()
        resource_name = 'officefile'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True