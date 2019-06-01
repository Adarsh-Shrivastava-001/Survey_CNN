from django.shortcuts import render
from django.views.generic import TemplateView
import numpy as np
import os
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.shortcuts import redirect
from .models import Results, MyUser



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

class End(TemplateView):
    template_name = "end.html"

class Que(TemplateView):
    template_name = "que.html"
    def get_context_data(self,**kwargs):

        global used, c
        context=super(TemplateView,self).get_context_data(**kwargs)
        print(context['mid'])
        context['img_url']=np.random.choice(images, 1)[0]
        while used.get(context['img_url'])!=None:
            context['img_url']=np.random.choice(images, 1)[0]
        used[context['img_url']]=1

        my_user=MyUser.objects.filter(mid=context['mid'])[0]
        my_user.part= my_user.part+context['img_url']
        my_user.save()
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


def start(req):
    name=req.POST.get('name')
    email=req.POST.get('e_mail')
    MyUser(name=name, e_mail=email, part='').save()
    mid=MyUser.objects.filter(e_mail=email)[0].mid
    print(mid)
    return redirect('Survey:que', mid=mid ,num=1)



def next_que(req,mid, num):

    ans=req.POST.get('ans')
    if ans!=None:
        my_user=MyUser.objects.filter(mid=mid)[0]
        my_user.part= my_user.part+'@'+ans+'#'
        my_user.save()
        res = Results.objects.all()[0]
        if ans=='fore':
            res.correct+=1
        elif ans=='back':
            res.incorrect+=1
        else:
            res.neither+=1
        res.save()
        if num==5:
            return redirect('Survey:end')
        else:
            return redirect('Survey:que', mid=mid,num=num+1)
    else:
        return redirect('Survey:que', mid=mid,num=num)
