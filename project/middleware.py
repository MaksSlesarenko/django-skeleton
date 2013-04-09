from django.contrib import messages
from django.conf import settings
from django.db import connection

import json


class AjaxMessaging(object):
    def process_response(self, request, response):
        if request.is_ajax():
            if response['Content-Type'] in ["application/javascript", "application/json"]:
                try:
                    content = json.loads(response.content)
                except ValueError:
                    return response

                django_messages = []

                for message in messages.get_messages(request):
                    django_messages.append({
                        "level": message.level,
                        "message": message.message,
                        "extra_tags": message.tags,
                    })

                content['django_messages'] = django_messages

                response.content = json.dumps(content)
        return response


class SqlProfiler(object):
    def process_response(self, request, response):
        if False == request.is_ajax():
            if response.content.find("text/html"):
                sql = str(connection.queries)
                
                sql = sql.replace('{u', "\n").replace('},', "\n")
                
                #sql = "\n".join(['%s:: %s' % (key, value) for key, value in connection.queries])
                
                response.content = response.content.replace("</body>", '<pre>' + sql + '</pre></body>')
        return response
