from django.shortcuts import render, get_object_or_404, render_to_response
import forml

static_context = {
    'images': 'static/images/',
    'scripts': 'static/scripts/',
}

def form1(request):
    context = dict(static_context)
    from forms import form1
    bugg = -1
    if len(request.GET):
        bugg=form1.do(**{k: (v[0] if len(v)==1 else v) for k, v in dict(request.GET).items()})
    context['form'] = form1.html(bugg)
    return render(request, 'forml/templates/index.html', context)

def form2(request):
    context = dict(static_context)
    from forms import form2
    if len(request.GET):
        form2.do(**{k: (v[0] if len(v)==1 else v) for k, v in dict(request.GET).items()})
    context['form'] = form2.html()
    return render(request, 'forml/templates/index.html', context)
