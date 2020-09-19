
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
User = apps.get_model('UserActivity', 'User')
ActivityPeriod = apps.get_model('UserActivity','ActivityPeriod')


class UserList(APIView):
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        response = {
            'ok':True,
            'members':serializer.data
        }
        return Response(response)
