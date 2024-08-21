# Projeto - Criação de Certificado pdf

## Sumario

- [Informações Acadêmicas](#informacoes-academicas)
- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Video onde mostra o projeto funcionando](#video-onde-mostra-o-projeto-funcionando)
- [Requisitos Implementados](#requisitos-implementados)
- [Padrão de Nomes para Features](#padrao-de-nomes-para-features)
- [Padrão de Nomes de Variáveis](#padrao-de-nomes-variaveis)
- [Como Iniciar o Projeto](#como-iniciar-o-projeto)
- [Criar uma Nova Branch para uma Feature](#criar-uma-nova-branch-para-uma-feature)
- [Realizar um Push](#realizar-um-push)
- [Fazendo o Pull Request](#fazendo-o-pull-request)

## Informacoes Academicas
<small>[voltar para o Sumário](#sumario)</small><br>

- Universidade Federal do Tocantins
- Curso de Bacharelado em Ciência da Computação
- Disciplina de Engenharia de Software
- Turma 2024/2
- Professor Dr. Edeilson Milhomem da Silva

### Integrantes
- Arthur Lima Duarte
- Gabriel Fernades Zamora
- Jessé Eliseu Nunes da Silva
- Jonatas de Sousa Madeira

## Sobre o Projeto
<small>[voltar para o Sumário](#sumario)</small><br>

Este projeto foi desenvolvido utilizando Django 5.1, HTML, CSS, BOOTSTRAP 4, Git, e GitHub. O objetivo é criar uma aplicação web simples cuja funcionalidade é gerar um certificado com base nas estradas que o usuário fornecer, seguindo boas práticas de versionamento de código e organização de projetos.

## Tecnologias Utilizadas
<small>[voltar para o Sumário](#sumario)</small><br>

- **[Django 5.1](https://www.djangoproject.com/start/):** Para o backend e lógica da aplicação.
- **HTML:** Estruturação do conteúdo e das páginas web.
- **CSS:** Estilização das páginas web para uma melhor experiência do usuário.
- **[BOOTSTRAP 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/):** Estilização das páginas web para uma melhor experiência do usuário.
- **Git:** Controle de versão do código.
- **GitHub:** Hospedagem do repositório remoto.
- **Gitflow:** Modelo de ramificação para organização do desenvolvimento.

## Apresentação do projeto:

https://github.com/user-attachments/assets/ad74d0ad-5ee1-4b3d-b91f-f2085a82a84b

## Video onde mostra o projeto funcionando
<small>[voltar para o Sumário](#sumario)</small><br>

https://github.com/user-attachments/assets/e9141e28-ed95-42d7-a736-ea0562fd2d1a

## Requisitos Implementados
<small>[voltar para o Sumário](#sumario)</small><br>

### Requisitos Funcionais

1. **Coleta de Dados dos Alunos:**

   - O sistema deve permitir que o usuário insira o nome do aluno.
   - O sistema deve permitir que o usuário insira o CPF do aluno.
   - O sistema deve permitir que o usuário insira o RG do aluno.
   - O sistema deve permitir que o usuário insira as datas de início e fim do curso no formato dd/mm/aaaa.
   - O sistema deve permitir que o usuário insira a carga horária do curso em horas.
   - O sistema deve permitir que o usuário insira o nome da instituição do curso.
   - O sistema deve permitir que o usuário insira o nome do responsável pelo curso.

2. Validação dos Dados:

   - O sistema deve validar se o CPF e RG inseridos estão no formato correto.

3. Geração de PDF:

   - O sistema deve gerar um documento PDF contendo todas as informações inseridas.
   - O sistema deve permitir que o usuário faça o download do PDF gerado.

### Requisitos Não-Funcionais

1. Desempenho:

   - O sistema deve gerar o PDF em até 2 segundos após a solicitação.

2. Usabilidade:

   - O sistema deve ter uma interface de utilizador intuitiva e fácil de usar, com campos de entrada claramente identificados e instruções claras.

## Padrao de Nomes para Features
<small>[voltar para o Sumário](#sumario)</small><br>

As features e correções devem seguir o padrão abaixo para facilitar o entendimento e rastreamento no projeto:
- Feat/issue-numero-da-issue-descricao-da-issue

### Exemplo

`Feat/issue-01-correcao-de-bugs`

**Observação:** Não utilizar caracteres especiais. O mesmo padrão aplicado na criação de nomes de variáveis.

## Padrao de Nomes de Variaveis
<small>[voltar para o Sumário](#sumario)</small><br>

- camelCase

# Como Iniciar o Projeto
<small>[voltar para o Sumário](#sumario)</small><br>

**Lembrando que tem um vídeo no final para melhor visualização: [Ir para o vídeo](#video-para-melhor-visualizacao)**

## Configurando o Ambiente

1. **Certifique-se que tem o Python e o Git instalado:**

   - **Python:**
   - No seu cmd execute o seguinte coamndo:
   ```bash
     python --version
   ```
   - Se não estiver instaldo: [Python](https://www.python.org/downloads/)
   - **Git:**
   - No seu cmd execute o seguinte coamndo:
   ```bash
     git --version
   ```
   - Se não estiver instaldo: [Git](https://git-scm.com/downloads)

2. **Importando repositório**

   - Em um local de sua preferência cria uma nova parte com o nome que preferir
   - Abra essa pasta com o VS Code (Ou outro editor, mas este tutorial é usando o vs)
   - Abra o Git Bash do vs code e digite o seguinte codigo:
   ```bash
     git clone https://github.com/jessilver/Engenharia-de-Software.git
   ```

3. **Criando a Máquina virtual:**

   - No próprio terminal do VS execute o seguinte comando:
   ```bash
     cd Engenharia-de-Software/ProjetoCertificadoPdf/geradoPdf
   ```
   - mude de branch com o seguinte comando:
   ```bash
     git checkout develop
   ```
   - Dentro do projeto (geradoPdf/) execute o seguinte coamndo:
   ```bash
     py -m venv venv
   ```
   - Para iniciar a maquina virtual execute os seguintes comandos:
   ```bash
     cd venv/Scripts
   ```
   ```bash
     activate  
   ```
   - Para voltar para o projeto execute os seguintes comandos:
   ```bash
     cd .. 
   ```
   ```bash
     cd .. 
   ```

4. **Instalando os requisitos na Máquina Virtual:**

   - No seu cmd execute o seguinte coamndo:
   ```bash
     pip install -r requirements.txt
   ```

5. **Iniciando o servidor:**

   - Mude para o terminal padrão e execute o seguinte comando:
   ```bash
     cd Engenharia-de-Software/ProjetoCertificadoPdf/geradoPdf
   ```
   - Dentro do projeto (geradoPdf/) execute o seguinte coamndo:
   ```bash
     py manage.py runserver 
   ```
   - Em seguida va para: http://127.0.0.1:8000/

## Video para Melhor visualizacao

https://github.com/user-attachments/assets/402acb87-6c74-4cb2-b04f-4b7944cba08a

## Criar uma Nova Branch para uma Feature
<small>[voltar para o Sumário](#sumario)</small><br>

### **OBSERVAÇÃO IMPORTANTE!:**

Sempre que mudar de branch, chegar em um novo dia para fazer suas modificações, ou antes de fazer um Pull Request, execute o seguinte comando:
```bash
git merge origin develop
```
Isso é **estremamente importante** para sempre manter seu codigo **atualizado** e **evitar problemas** futuros

Para criar uma nova branch para desenvolver uma feature, siga os passos abaixo:

1. Certifique-se de que está na branch `develop`:
   ```bash
   git checkout develop
   ```

2. Atualize a branch `develop` com as últimas mudanças:
   ```bash
   git pull origin develop
   ```

3. Crie uma nova branch para a `feature` utilizando o padrão de nomenclatura definido:
   ```bash
   git checkout -b Feat/issue-numero-da-issue-descricao-da-issue
   ```

## Realizar um Push
<small>[voltar para o Sumário](#sumario)</small><br>

Após ter realizado as alterações na sua branch, siga os passos para enviar as mudanças ao repositório remoto:

1. Adicione as mudanças ao staging:
   ```bash
   git add .
   ```

2. Faça um commit com uma mensagem clara e descritiva:
   ```bash
   git commit -m "Descrição clara das alterações realizadas"
   ```

3. Envie (push) as mudanças para a sua branch no GitHub:
   ```bash
   git push origin Feat/issue-numero-da-issue-descricao-da-issue
   ```
Exemplo:
   ```bash
   git push origin Feat/issue-01-correcao-de-bugs
   ```

## Fazendo o Pull Request
<small>[voltar para o Sumário](#sumario)</small><br>

1. Na pagina inicial do projeto no Git Hub: [Engenharia-de-Software](https://github.com/jessilver/Engenharia-de-Software)
   - Clique em `Pull requests`

![pullrequest1](https://github.com/user-attachments/assets/42c50623-87b8-470c-8499-68dbb560b337)

2. Na pagina de Pull requests:
   - Clique em `New pull request`

![pullrequest2](https://github.com/user-attachments/assets/eda6e914-b3c1-4e84-8cc6-05a53888cd6a)

3. Selecione a base e troque para `develop`:

![pullrequest3](https://github.com/user-attachments/assets/c8b169d9-326b-4df4-830d-3845154e5623)

4. No campo de pesquisa escreva `develop`:

![pullrequest4](https://github.com/user-attachments/assets/69d101f4-e0fa-420f-9eb2-a4e64c02466d)

5. Clique em `develop`:

![pullrequest5](https://github.com/user-attachments/assets/7a6c62aa-ecfb-4e06-8c6d-d9d7295257cf)

6. Selecione a compare e troque para `sua branch`:

![pullrequest6](https://github.com/user-attachments/assets/7b3d9542-8933-46b4-b8fb-89ebf919d906)

7. No campo de pesquisa procure pela sua branch:

![pullrequest7](https://github.com/user-attachments/assets/cabbf824-e0f0-4dd8-8cb6-ed4d0f1b9397)

8. Clique nela:

![pullrequest8](https://github.com/user-attachments/assets/2b1de95a-e294-418c-bde0-59e1ae37a783)

9. Clique em `Create pull request`:

![pullrequest9](https://github.com/user-attachments/assets/6953ddba-a433-4c9f-a002-6c87046e0ccb)

10. Clique na engrenagem para selecionar um `reviewer`:
   - Essa é a pessoa que vai revisar ser código.

![pullrequest10](https://github.com/user-attachments/assets/98774ed2-a9dc-4b2b-8c5f-dd7c6e6f1e9a)

11. Selecione um reviewer e dps clique fora da caixa de seleção:

![pullrequest11](https://github.com/user-attachments/assets/82ea5234-77cc-4609-9945-da41028ba2be)

12. Por fim, clique em `Create pull request`:

![pullrequest12](https://github.com/user-attachments/assets/46005297-34ac-4a9b-9e7d-4f162403c23b)

## Fluxo de Trabalho com Gitflow

- **Main:** Contém a versão estável e em produção.
- **Develop:** Contém as últimas alterações que serão futuramente incluídas na Master.
- **Feature Branches:** Utilizadas para o desenvolvimento de novas funcionalidades (padrão `Feat/issue-numero-da-issue-descricao-da-issue`).
- **Release Branches:** Preparação das novas versões para produção.
- **Hotfix Branches:** Correções de bugs em produção.

## Contribuição

1. Crie uma branch a partir de `develop` para trabalhar em novas funcionalidades ou correções.
2. Faça commits regulares com mensagens claras.
3. Envie um Pull Request para a branch `develop`.
4. Aguarde a revisão do código antes de fazer o merge.
