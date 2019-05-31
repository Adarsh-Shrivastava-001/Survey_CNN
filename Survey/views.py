from django.shortcuts import render
from django.views.generic import TemplateView
import numpy as np
import os
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.shortcuts import redirect
from .models import Results



# Create your views here.
images=os.listdir("./static/images")
file_name ='./Survey/classes.txt'
classes = list()
with open(file_name) as class_file:
    for line in class_file:
        classes.append(line.strip().split(' ')[0][3:])
classes = tuple(classes)

used={}
c=0

class Home(TemplateView):
    template_name = "home.html"


class Que(TemplateView):
    template_name = "que.html"
    def get_context_data(self,**kwargs):

        global used, c
        context=super(TemplateView,self).get_context_data(**kwargs)
        print(context)
        context['img_url']=np.random.choice(images, 1)[0]
        while used.get(context['img_url'])!=None:
            context['img_url']=np.random.choice(images, 1)[0]
        used[context['img_url']]=1


        dec = context['img_url'].split('_')
        context['fore']=classes[int(dec[0])]
        context['back']=classes[int(dec[1])]
        context['w1']=classes[int(dec[2])]
        context['w2']=classes[int(dec[3])]
        context['w3']=classes[int(dec[4][:-4])]
        c+=1
        if c==7:
            c=0
            used={}
        #context['post_list']=Posts.objects.filter(group=self.object)
        return context

def next_que(req, num):
    ans=req.POST.get('ans')
    if ans!=None:
        res = Results.objects.all()[0]
        if ans=='fore':
            res.correct+=1
        elif ans=='back':
            res.incorrect+=1
        else:
            res.neither+=1
        res.save()
        return redirect('Survey:que', num=num+1)
    else:
        return redirect('Survey:que', num=num)
