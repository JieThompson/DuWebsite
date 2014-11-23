from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.
def home(request):
    
    return render_to_response("home.html",
                              locals(),
                              context_instance=RequestContext(request))

def people(request):
    
    return render_to_response("people.html",
                              locals(),
                              context_instance=RequestContext(request))

def publication(request):
    
    return render_to_response("publication.html",
                              locals(),
                              context_instance=RequestContext(request))

def research(request):
    
    return render_to_response("research.html",
                              locals(),
                              context_instance=RequestContext(request))

def exciton(request):
    
    return render_to_response("exciton.html",
                              locals(),
                              context_instance=RequestContext(request))

def fqhe(request):
    
    return render_to_response("fqhe.html",
                              locals(),
                              context_instance=RequestContext(request))

def magnetotransport(request):
    
    return render_to_response("magneto-transport.html",
                              locals(),
                              context_instance=RequestContext(request))

def manyparticle(request):
    
    return render_to_response("many-particle.html",
                              locals(),
                              context_instance=RequestContext(request))

def microwave(request):
    
    return render_to_response("microwave.html",
                              locals(),
                              context_instance=RequestContext(request))

def nanoelectronics(request):
    
    return render_to_response("nano-electronics.html",
                              locals(),
                              context_instance=RequestContext(request))

def qshe(request):
    
    return render_to_response("qshe.html",
                              locals(),
                              context_instance=RequestContext(request))

def quantumwell(request):
    
    return render_to_response("quantum-well.html",
                              locals(),
                              context_instance=RequestContext(request))

def shpm(request):
    
    return render_to_response("shpm.html",
                              locals(),
                              context_instance=RequestContext(request))