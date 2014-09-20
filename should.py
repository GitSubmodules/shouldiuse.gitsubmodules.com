from os import path
import random
import rivr
from rivr.wsgi import WSGIHandler

# Loaded into global space so they're always in memory

with open('messages.txt') as fp:
    global messages
    messages = fp.readlines()

with open('gifs.txt') as fp:
    global gifs
    gifs = fp.readlines()


class ShouldView(rivr.views.TemplateView):
    template_name = 'should.html'

    def get_context_data(request, **kwargs):
        return {
            'message': random.choice(messages).strip(),
            'gif': random.choice(gifs).strip(),
            'params': kwargs,
        }

template_dir = path.dirname(path.realpath(__file__))
app = rivr.MiddlewareController.wrap(ShouldView.as_view(),
    rivr.TemplateMiddleware(template_dirs=template_dir),
)
wsgi = WSGIHandler(app)

if __name__ == '__main__':
    rivr.serve(app)

