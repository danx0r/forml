from django.shortcuts import render, get_object_or_404, render_to_response
import forml

static_context = {
    'images': 'static/images/',
    'scripts': 'static/scripts/',
}

def form1(request):
    context = dict(static_context)
    from forms import form1
    context['form1'] = form1.html()
    return render(request, 'forml/templates/index.html', context)

def form2(request):
    context = dict(static_context)
    from forms import form2
    context['form1'] = form2.html()
    return render(request, 'forml/templates/index.html', context)
