from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test Api view"""

    def get(self ,request, format=None):
        """Return a list of  APIVIEW features"""
        an_apiview = [
            'Usee http methods as function (get , post ,patch, put, delete)',
            'is similar to a traditional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!' ,'an_apiview': an_apiview})