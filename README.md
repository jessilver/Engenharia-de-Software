# Projeto - Criação de Certificado pdf

Este projeto foi desenvolvido utilizando Django 5.1, HTML, CSS, BOOTSTRAP 5, Git, e GitHub. O objetivo é criar uma aplicação web simples, seguindo boas práticas de versionamento de código e organização de projetos.

## Tecnologias Utilizadas

- **[Django 5.1](https://www.djangoproject.com/start/):** Para o backend e lógica da aplicação.
- **HTML:** Estruturação do conteúdo e das páginas web.
- **CSS:** Estilização das páginas web para uma melhor experiência do usuário.
- **[BOOTSTRAP 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/):** Estilização das páginas web para uma melhor experiência do usuário.
- **Git:** Controle de versão do código.
- **GitHub:** Hospedagem do repositório remoto.
- **Gitflow:** Modelo de ramificação para organização do desenvolvimento.

## Padrão de Nomes para Features

As features e correções devem seguir o padrão abaixo para facilitar o entendimento e rastreamento no projeto:
- Feat/issue-numero-da-issue-descricao-da-issue


### Exemplo

`Feat/issue-01-correcao-de-bugs`

**Observação:** Não utilizar caracteres especiais. O mesmo padrão aplicado na criação de nomes de variáveis.

## Como Iniciar o Projeto

1. **Certifique-se que tem o Python instalado:**

   - No seu cmd execute o seguinte coamndo:
   ```bash
     python --version
   ```
   - Se não estiver instaldo: [Python](https://www.python.org/downloads/)

2. **Instalando o Django:**

   - No seu cmd execute o seguinte coamndo:
   ```bash
     pip install django
   ```

3. **Criando a Máquina virtual:**

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

   - Dentro do projeto (geradoPdf/) execute o seguinte coamndo:
   ```bash
     py manage.py runserver 
   ```
   - Em seguida va para: http://127.0.0.1:8000/

## Criar uma Nova Branch para uma Feature

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
