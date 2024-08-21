import os
from urllib import request
from django.shortcuts import render
from django.views.generic import View
from PIL import Image, ImageDraw, ImageFont
from geradoPdf import settings
from PIL import Image #pip install pillow
import os


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):

        image_path = os.path.join(settings.BASE_DIR, 'gpdf', 'static', 'image', 'certificado_base.jpg')
        certificado = Image.open(image_path)

        fonte = ImageFont.truetype("arial.ttf", 75)
        nomeAluno = request.POST.get('nomeAluno')
        cpfAluno = request.POST.get('cpfAluno')
        nomeCurso = request.POST.get('nomeCurso')
        inicioCurso = request.POST.get('inicioCurso')
        fimCurso = request.POST.get('fimCurso')
        cargaHoraria = request.POST.get('cargaHoraria')
        
        desenho = ImageDraw.Draw(certificado)

        fonte = ImageFont.truetype("arial.ttf", 75)

        posicaoNome = (1330, 1050)
        posicaoCurso = (2200, 1250)
        posicaoCinicio = (975, 1345)
        posicaoCfim = (1355, 1345)
        posicaoCargahoraria = (2580, 1345)
        posicaoCpf = (570, 1250)

        desenho.text(posicaoNome, nomeAluno, font=fonte, fill="black")
        desenho.text(posicaoCurso, nomeCurso, font=fonte, fill="black")
        desenho.text(posicaoCinicio, inicioCurso, font=fonte, fill="black")
        desenho.text(posicaoCfim, fimCurso, font=fonte, fill="black")
        desenho.text(posicaoCargahoraria, cargaHoraria, font=fonte, fill="black")
        desenho.text(posicaoCpf, cpfAluno, font=fonte, fill="black")

        # Salvar a imagem com o texto adicionado como JPG
        final_path = os.path.join(settings.BASE_DIR, 'gpdf', 'static', 'image', 'certificado_final.jpg')
        certificado.save(final_path)


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
    


