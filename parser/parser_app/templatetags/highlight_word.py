import html

from django import template
from django.template.defaultfilters import stringfilter
from parser_app import views

register = template.Library()


# @register.filter
# @stringfilter
# def highlight_word(post):
#     word_input = views.get_word_input(word_input)
#     s = post.replace(word_input, "<h5><u>" + word_input + "</u></h5>")
#     return html.escape(s, quote=True)
