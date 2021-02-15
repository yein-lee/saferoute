from django.shortcuts import render
from django.views import View
import json
# Create your views here.
class RequestView(View):
    template_name='request.html'
    def get(self, request):
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode) #json.loads JSON 문자열을 python 객체로 변환
        data_value =data['key'] #json.dumps python 객체를 JSON 문자열로 변환
        return render(request, self.template_name, {'content':data_value})
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        data_value = data['key']
        return render(request, self.template_name, {'content': data_value})