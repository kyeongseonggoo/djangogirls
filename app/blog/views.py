from django.http import HttpResponse
from datetime import timezone

from django.shortcuts import render

def post_list(request):
    current_time = timezone.now()

    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post list</h1>'
        '<p>{}</p>'
        '</body>'
        '</html>'.format(
            # 날짜 & 시간 객체가 가진 정보를 문자열로 변환
            current_time.strftime('%Y, %m, %d<br>%H:%M:%S')
        )
    )