import os
from urllib import request
from django.shortcuts import render
from django.views.generic import View
from PIL import Image, ImageDraw, ImageFont
from geradoPdf import settings

class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):

        image_path = os.path.join(settings.BASE_DIR, 'gpdf', 'static', 'image', 'certificado_base.jpg')
        certificado = Image.open(image_path)

        
        fonteNome = ImageFont.truetype("arial.ttf", 175)
        fontePadrao = ImageFont.truetype("arial.ttf", 110)

        
        nomeAluno = request.POST.get('nomeAluno') or ""
        cpfAluno = request.POST.get('cpfAluno') or ""
        rgAluno = request.POST.get('rgAluno') or ""
        nomeCurso = request.POST.get('nomeCurso') or ""
        inicioCurso = request.POST.get('inicioCurso') or ""
        fimCurso = request.POST.get('fimCurso') or ""
        cargaHoraria = request.POST.get('cargaHoraria') or ""
        instituicao = request.POST.get('instituicao') or ""
        diretor = request.POST.get('diretor') or ""
        
        desenho = ImageDraw.Draw(certificado)

        
        posicaoNome = (2030, 2080)
        posicaoCpf = (2540, 2400)
        posicaoRg = (3850, 2400)
        posicaoCurso = (730, 2590)
        posicaoInicio = (2970, 2590)
        posicaoFim = (3850, 2590)
        posicaoCargaHoraria = (1650, 2790)
        posicaoInstituicao = (1650, 2790)
        posicaodiretor = (510, 3345)
        

        
        desenho.text(posicaoNome, nomeAluno, font=fonteNome, fill="black")
        desenho.text(posicaoCpf, cpfAluno, font=fontePadrao, fill="black")
        desenho.text(posicaoRg, rgAluno, font=fontePadrao, fill="black")
        desenho.text(posicaoCurso, nomeCurso, font=fontePadrao, fill="black")
        desenho.text(posicaoInicio, inicioCurso, font=fontePadrao, fill="black")
        desenho.text(posicaoFim, fimCurso, font=fontePadrao, fill="black")
        desenho.text(posicaoCargaHoraria, cargaHoraria, font=fontePadrao, fill="black")
        desenho.text(posicaoInstituicao, instituicao, font=fontePadrao, fill="black")
        desenho.text(posicaodiretor, diretor, font=fontePadrao, fill="black")
        

        
        finalPath = os.path.join(settings.BASE_DIR, 'gpdf', 'static', 'image', 'certificado_final.jpg')
        certificado.save(finalPath)

        return render(request, "index.html")
    


