
from django.shortcuts import render
from django.http import HttpResponse,response,JsonResponse
from weasyprint import HTML
from django.conf import settings
import wikipediaapi
import requests



class Wikki_Aricles:
    @staticmethod
    def wikki_search_artcles(article):
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )
        search_article = wiki_wiki.page(article)
        return search_article.text
    @classmethod
    def download(cls,request):
        article = request.GET.get('res')
        result= Wikki_Aricles.wikki_search_artcles(article)
        if not result:
            return HttpResponse(article+' '+ 'Not Found!!!')
        #it takes time depends on content which convert into a pdf
        HTML(string=result).write_pdf(settings.MEDIA_ROOT+"remark.pdf")
        fileobj = open(settings.MEDIA_ROOT+"remark.pdf",'rb')
        response = HttpResponse(fileobj.read(),content_type='application/pdf')
        filename = article+'.pdf'
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response

    def search_list(request):
        article = request.GET.get('ress')
        res = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search="+article+"&namespace=0&limit=10&suggest=true")
        ss=eval(res.content.decode("utf-8"))[1]
        return JsonResponse(ss,safe=False)

def main(request):
    return render(request,'wikki.html')

def search_list_values(request):
    return render(request,'search_list.html')


