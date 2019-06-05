from django.shortcuts import render
from django.views.generic import TemplateView
import numpy as np
import os
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.shortcuts import redirect
from .models import Results, MyUser



# Create your views here.
images=os.listdir("./static/images")
images_test=os.listdir("./static/images_test")

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
        my_user=MyUser.objects.filter(mid=context['mid'])[0]

        rel_test_score=my_user.rel_corr+my_user.rel_wrong
        if rel_test_score<=5:
            ch=np.random.choice([0,1],1,[0.6,0.4])
        else:
            ch=np.random.choice([0,1],1, [0.4,0.6])

        if ch==1:
            context['img_url']=np.random.choice(images, 1)[0]
            while used.get(context['img_url'])!=None:
                context['img_url']=np.random.choice(images, 1)[0]
            used[context['img_url']]=1
            context['test']='normal'
            dec = context['img_url'].split('_')
            context['img_url']='images/'+context['img_url']

        else:
            context['img_url']=np.random.choice(images_test, 1)[0]

            context['test']='test'
            dec = context['img_url'].split('_')[1:]
            context['img_url']='images_test/'+context['img_url']



        my_user.part= my_user.part+context['img_url'].split('/')[1]
        my_user.save()
        context['fore']=classes[int(dec[0])]
        context['back']=classes[int(dec[1])]
        context['w1']=classes[int(dec[2])]
        context['w2']=classes[int(dec[3])]
        context['w3']=classes[int(dec[4][:-4])]
        c+=1
        if c==20:
            c=0
            used={}
        #context['post_list']=Posts.objects.filter(group=self.object)
        return context



def start(req):
    name=req.POST.get('name')
    email=req.POST.get('e_mail')
    MyUser(name=name, e_mail=email, part='', correct=0, incorrect= 0, neither=0,rel_corr=0,rel_wrong=0).save()
    mid=MyUser.objects.filter(e_mail=email)[0].mid
    print(mid)
    return redirect('Survey:que', mid=mid ,num=1)



def next_que(req,mid, num):

    ans=req.POST.get('ans')
    if ans!=None:




        my_user=MyUser.objects.filter(mid=mid)[0]
        my_user.part= my_user.part+'@'+ans+'#'

        if req.POST.get('test')=='test':
            if ans=='back':
                my_user.rel_corr +=1
            else:
                my_user.rel_wrong +=1

        else:


            if ans=='fore':
                my_user.incorrect +=1
            elif ans=='back':
                my_user.correct +=1
            else:
                my_user.neither +=1
        my_user.save()
        return redirect('Survey:que', mid=mid,num=num+1)
    else:
        return redirect('Survey:que', mid=mid,num=num)





def result(req):
    users=MyUser.objects.all()
    cor=0
    incor=0
    nei=0
    for user in users:
        cor=cor+user.correct
        incor=incor+user.incorrect
        nei=nei+user.neither
    context= {'cor':cor, 'incor':incor, 'nei':nei }

    return render(req, 'res.html', context)
