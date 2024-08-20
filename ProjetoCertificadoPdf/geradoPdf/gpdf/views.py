from urllib import request
from django.shortcuts import render
from django.views.generic import View
from PIL import Image #pip install pillow
import os


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):

        nomeAluno = request.POST.get('nomeAluno')

        print(nomeAluno)

        #transforma uma imagem em um arquivo pdf
        outputDir = 'C:/Users/arthu/Desktop/Engenharia de Software/Engenharia-de-Software/ProjetoCertificadoPdf/geradoPdf/gpdf/static/PDFs' #pasta na qual será salvo o pdf
        sourceDir = 'C:/Users/arthu/Desktop/Engenharia de Software/Engenharia-de-Software/ProjetoCertificadoPdf/geradoPdf/gpdf/static/img' #pasta de origem da imagem

        #busca no diretório de origem imagens e a converte para formato pdf
        for arquivo in os.listdir(sourceDir):
            if arquivo.split('.')[-1] in ('png', 'jpg', 'jpeg'):   #checa a extensão para ver se é imagem
                caminhoImagem = os.path.join(sourceDir, arquivo)
                imagem = Image.open(caminhoImagem)  
                imagemConvertida = imagem.convert('RGB')
                imagemConvertida.save(os.path.join(outputDir, '{0}.pdf'.format(arquivo.split('.')[-2])))

        return render(request, "index.html")


