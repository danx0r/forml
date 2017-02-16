from django.shortcuts import render, get_object_or_404, render_to_response
import forml

static_context = {
    'images': 'static/images/',
    'scripts': 'static/scripts/',
}

def home(request):
    context = dict(static_context)
    from testform import form as testform
    context['form1'] = testform.html()
    return render(request, 'forml/templates/index.html', context)
