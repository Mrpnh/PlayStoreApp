from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import AppSerializer
from playstore.models import AppAdmin

# api only works for get requests
# And permission is only available if authenticated
# here authentication is Token Authentication
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def apiAppView(request):
    try:
        # Gets the app
        apps=AppAdmin.objects.all()
    except AppAdmin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        # passes it to our serialiser 
        # many=True will tell the serialiser that it is 
        serializer=AppSerializer(apps,many=True)
        # sends the json data
        return Response(serializer.data)






