from django.shortcuts import render
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import OfficeFileForm


def onepage(request):
    c = {}
    if request.method == 'POST':
        form = OfficeFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = OfficeFileForm()

    c = RequestContext(request, {'form': form})

    return render_to_response('web/base.html', c)