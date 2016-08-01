from django.shortcuts import render
from video.models import tags as Tags
from video.models import video as Video
from django.http import HttpResponse
import json
from django.template import RequestContext, loader
from django.template import Context, Template

# Create your views here.

def ajaxresponse(ret):
    return HttpResponse(content=json.dumps(ret), content_type="application/json")

def home(request):
    choicetags=request.GET.get('tag',0)
    tags=Tags.objects.all().order_by("-count")
    tagsdata=[]
    for son in tags:
        tagsdata.append({"id":son.id,"value":son.name})
    if choicetags==0:
        choicetags=tags[0].id
    else:
        choicetags=int(choicetags[4:])
    OBJ=Video.objects.filter(tags__id=choicetags)
    videos=[]
    for son in OBJ:
        temp={}
        temp['name']=son.name
        temp['id']=son.id
        temp['videourl']=son.videourl
        temp['paperurl']=son.paperurl
        temp['tags']=[]
        for i in son.tags.all():
            temp['tags'].append(i.name)
        temp['tags'].append('+')
        videos.append(temp)

    return render(request,'home.html',{'tags':tagsdata,'videos':videos,'choicetagname':choicetags})


def addtag(request):
    tag=request.GET.get('tag','')
    videoid=int(request.GET.get('id',0))
    OBJ=Video.objects.get(id=videoid)
    try:
        OBJT=Tags.objects.get(name=tag)
    except:
        OBJT=Tags()
        OBJT.name=tag
        OBJT.count=1
        OBJT.save()
    OBJ.tags.add(OBJT)
    OBJ.save()
    tags=Tags.objects.all()
    tagsdata=[]
    for son in tags:
        tagsdata.append({"id":son.id,"value":son.name})
    OBJ=Video.objects.get(id=id)
    videotags=[]
    for i in OBJ.tags.all():
       videotags.append(i.name)

    tagshtml="""<ul class='nav nav-pills' style='margin-left:10px;margin-top:10px;'>"""
    for son in tagsdata:
        if son.id==OBJT.id:
            tagshtml+="""<li id="tags%s"  onclick="onclick1('tags%s')" role="presentation" class="tag" style="margin:10px;background-color:#2A906B;color:#fff;">%s</li>"""%(son['id'],son['id'],son['value'])
        else:
            tagshtml+="""<li id="tags%s"  onclick="onclick1('tags%s')" role="presentation" class="tag" style="margin:10px;">%s</li>"""%(son['id'],son['id'],son['value'])
    tagshtml+="</ul>"

    videotaghtml='''<ul class="nav nav-pills" >'''
    for son in videotags:
        videotaghtml+="""<li  role="presentation" class="tag1" style="margin:5px;">%s</li>"""%son
    videotaghtml+="""<li id="add" onclick="addfunc()"  role="presentation" class="tag1" style="margin:5px;">+</li><input id="addinput" type="text" onblur="addtag(%d)" style="display:none;margin-top:5px;width:60px;"></ul>"""%OBJ.id

    return ajaxresponse({'tags':tagshtml,"videotags":videotaghtml,"id":OBJ.id})
