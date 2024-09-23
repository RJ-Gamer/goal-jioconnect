from rest_framework.response import Response
from .utils import send_sms, CELEBRITY_INQUIRY_SMS
from rest_framework import generics, status
from decouple import config

key = config('TEXT_LOCAL_API_KEY')


class TestMsgAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        number = request.data.get('number')
        message = CELEBRITY_INQUIRY_SMS.format('Rajat Jog')

        if not number or not message:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        print(send_sms(key, number, 'OPPVNZ', message))
        return Response({'message': 'SMS sent successfully'}, status=status.HTTP_200_OK)