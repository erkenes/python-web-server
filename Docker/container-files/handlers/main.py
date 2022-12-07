from response.templateHandler import TemplateHandler
from response.jsonTemplateHandler import JsonTemplateHandler
from response.staticHandler import StaticHandler

handlers = {
    'html' : TemplateHandler(),
    'json': JsonTemplateHandler(),
    'js': StaticHandler(),
    'css': StaticHandler(),
    'jpg': StaticHandler(),
    'png': StaticHandler(),
    'ico': StaticHandler(),
    'notfound': StaticHandler(),
}