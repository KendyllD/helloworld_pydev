# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from hello_polls.models import MyPoll, MyChoice
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse


def index(request):
    latest_mypoll_list = MyPoll.objects.all().order_by('-pub_date')[:3]
    return render_to_response('hello_polls/index.html', {'latest_mypoll_list': latest_mypoll_list})

def detail(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    return render_to_response('hello_polls/detail.html', {'mypoll': p},
                               context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    return render_to_response('hello_polls/results.html', {'mypoll': p})

def vote(request, poll_id):
    p = get_object_or_404(MyPoll, pk=poll_id)
    try:
        selected_mychoice = p.mychoice_set.get(pk=request.POST['mychoice'])
    except (KeyError, MyChoice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('hello_polls/detail.html', {
            'mypoll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_mychoice.votes += 1
        selected_mychoice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mypoll_results', args=(p.id,)))