import os
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from PIL import Image, ImageDraw, ImageFont
from geradoPdf import settings
from fpdf import FPDF


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        # Caminho da imagem base
        image_path = os.path.join(settings.BASE_DIR, 'gpdf', 'static', 'image', 'certificado_base.jpg')
        certificado = Image.open(image_path)

        # Carregar as fontes (certifica-te de que o caminho está correto)
        try:
            fonteNome = ImageFont.truetype("arial.ttf", 175)
            fontePadrao = ImageFont.truetype("arial.ttf", 120)
        except IOError:
            return render(request, 'index.html', {'error': 'Fonte não encontrada!'})

        # Captura os dados do POST
        nomeAluno = request.POST.get('nomeAluno', "")
        cpfAluno = request.POST.get('cpfAluno', "")
        rgAluno = request.POST.get('rgAluno', "")
        nomeCurso = request.POST.get('nomeCurso', "")
        inicioCurso = request.POST.get('inicioCurso', "")
        fimCurso = request.POST.get('fimCurso', "")
        cargaHoraria = request.POST.get('cargaHoraria', "")
        instituicao = request.POST.get('instituicao', "")
        diretor = request.POST.get('diretor', "")

        print(nomeAluno)
        print(cpfAluno)
        print(rgAluno)
        print(nomeCurso)
        print(inicioCurso)
        print(fimCurso)
        print(cargaHoraria)
        print(instituicao)
        print(diretor)

        inicioCurso = str(inicioCurso).split('-')
        inicioCurso = inicioCurso[-1]+'/'+inicioCurso[-2]+'/'+inicioCurso[-3]
        fimCurso = str(fimCurso).split('-')
        fimCurso = fimCurso[-1]+'/'+fimCurso[-2]+'/'+fimCurso[-3]

        # Desenhar texto na imagem
        desenho = ImageDraw.Draw(certificado)
        desenho.text((2030, 2070), nomeAluno, font=fonteNome, fill="black")
        desenho.text((2540, 2380), cpfAluno, font=fontePadrao, fill="black")
        desenho.text((3850, 2380), rgAluno, font=fontePadrao, fill="black")
        desenho.text((680, 2575), nomeCurso, font=fontePadrao, fill="black")
        desenho.text((2970, 2575), inicioCurso, font=fontePadrao, fill="black")
        desenho.text((3850, 2575), fimCurso, font=fontePadrao, fill="black")
        desenho.text((1650, 2770), cargaHoraria, font=fontePadrao, fill="black")
        desenho.text((3220, 2770), instituicao, font=fontePadrao, fill="black")
        desenho.text((510, 3320), diretor, font=fontePadrao, fill="black")

        # Salvar a imagem final com o texto sobreposto
        finalPath = os.path.join(settings.BASE_DIR, 'gpdf', 'static', 'image', 'certificado_final.jpg')
        certificado.save(finalPath)

        # Obter as dimensões da imagem em pixels
        largura_px, altura_px = certificado.size

        # Converter as dimensões de pixels para milímetros
        largura_mm = largura_px * 25.4 / 72
        altura_mm = altura_px * 25.4 / 72

        # Criar o PDF com o tamanho exato da imagem
        outputDir = os.path.join(settings.BASE_DIR, 'gpdf', 'static', 'pdf')
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)

        pdf_filename = f'certificado_{nomeAluno}.pdf'
        pdf_path = os.path.join(outputDir, pdf_filename.replace(" ","-"))

        pdf = FPDF(unit="mm", format=[largura_mm, altura_mm])
        pdf.add_page()
        pdf.image(finalPath, x=0, y=0, w=largura_mm, h=altura_mm)
        pdf.output(pdf_path)

        # Retornar a resposta com o caminho do PDF
        return render(request, "index.html", {'success': 'Certificado gerado com sucesso!', 'pdf_url': f'/static/pdf/{pdf_filename.replace(" ","-")}'})
