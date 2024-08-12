from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Itemserializer
from .models import qbank
from django.http import JsonResponse
class api(APIView):

    serializer_class=Itemserializer
    def post(self,request):

        print("HELLO")
        ser_data=self.serializer_class(data=request.data)
        print("HELLO",type(request.data['image']))
        if ser_data.is_valid(raise_exception=True):
            ser_data.save()
            print("Svaed")
        return Response({"status":"done"})


    def get(self,request):
        
        obj=qbank.objects.all()
        val=list(obj.values())
        return JsonResponse(val,safe=False)
