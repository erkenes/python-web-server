from response.requestHandler import RequestHandler

class JsonTemplateHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'application/json'

    def find(self, route_data, query_params):
        try:
            template_file = open('templates/{}'.format(route_data['template']))
            self.contents = template_file
            self.setStatus(200)
            return True
        except:
            self.setStatus(404)
            return False