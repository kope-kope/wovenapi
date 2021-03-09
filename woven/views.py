from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .models import MandateId, APIRequest
from woven.wovenapi import verify_mandate
import re
from backend.schedulers import get_status
# Create your views here.


class GetOTP(APIView):

    def post(self, request):
        body = request.data.get('body_plain')
        otp = re.search("token: \d{6}", body).group().split(': ')[1]
        mandate_ref = MandateId.objects.last()
        status_code, response, start_time, end_time = verify_mandate(otp, mandate_ref.mandate_id)
        APIRequest.objects.create(
            call_type='verify_mandate',
            start_time=start_time,
            end_time=end_time,
            status=get_status(status_code),
            status_message=json.dumps(response)
        )
        return Response({'hello': 'world'})