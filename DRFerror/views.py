from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from .models import Startup
from .serializers import StartupSerializer

from collections import OrderedDict

# Create your views here.
class StartupViewSet( mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet ):
    """ViewSet for managing Startup objects"""
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

    def update(self, request, *args, **kwargs):

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        # print(serializer.initial_data)
        # assert serializer.initial_data['logo']
        
        serializer.is_valid(raise_exception=True)
        
        # print(serializer.validated_data)
        # assert serializer.validated_data['logo']

        # Assert fails, because validated data is
        # OrderedDict([('admin', OrderedDict()), ('logo', <InMemoryUploadedFile: ...>)])
        assert serializer.validated_data['admin'] != OrderedDict()

        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)