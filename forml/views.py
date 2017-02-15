from django.shortcuts import render, get_object_or_404, render_to_response
import forml

static_context = {
    'images': 'static/images/',
    'scripts': 'static/scripts/',
}

def home(request):
    context = dict(static_context)
    f1 = forml.form()
    f1.input('text', "field1", value="please enter some shite")
    f1.text("enter stuff:")
    f1.input('text', "field2", placeholder="please enter some mo shite")
    f1.br()
    f1.text("gender stuff:")
    f1.br()
    f1.input('radio', "gender", "male")
    f1.input('radio', "gender", "female")
    f1.input('radio', "gender", "other")
    f1.br(2)
    f1.submit("OKPRESSME")
    context['form1'] = f1.html()
    return render(request, 'forml/templates/index.html', context)
