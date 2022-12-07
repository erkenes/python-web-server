routes = {
    '/' : {
        'template' : 'index.html',
        'handler': 'html'
    },
    '/goodbye' : {
        'template' : 'goodbye.html',
        'handler': 'html'
    },
    '/status': {
        'template' : 'status.json',
        'handler': 'json'
    }
}