from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.tag(name='admin_edit')
def render_admin_url(parser, token):
    try:
        tag_name, model = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('tag requires model instance as argument')
    return LinkInAdmin(model)

class LinkInAdmin(template.Node):

    def __init__(self, obj):
        self.obj = template.Variable(obj)

    def render(self, context):
        model = self.obj.resolve(context)
        name = '_'.join((model._meta.app_label,model._meta.module_name))
        try:
            url = reverse('admin:{}_change'.format(name), args=(model.pk,))
        except Exception:
            return ''
        return '<a href="{0}">change {1} in admin</a>'.format(url, model._meta.module_name)