from os import path
import random
import rivr
from rivr.wsgi import WSGIHandler

messages = [
    'Yes, of course you should.',
    'No, you should write your own goddamn code.',
    'This is not even a valid question.',
]

class ShouldView(rivr.views.TemplateView):
    template_name = 'should.html'

    def get_context_data(request, **kwargs):
        return {
            'message': random.choice(messages),
            'params': kwargs,
        }

template_dir = path.dirname(path.realpath(__file__))
app = rivr.MiddlewareController.wrap(ShouldView.as_view(),
    rivr.TemplateMiddleware(template_dirs=template_dir),
)
wsgi = WSGIHandler(app)

if __name__ == '__main__':
    rivr.serve(app)

