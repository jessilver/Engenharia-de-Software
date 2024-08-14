# Projeto - Criação de Certificado pdf

Este projeto foi desenvolvido utilizando PHP nativo, HTML, CSS, Git, e GitHub. O objetivo é criar uma aplicação web simples, seguindo boas práticas de versionamento de código e organização de projetos.

## Tecnologias Utilizadas

- **PHP Nativo:** Para o backend e lógica da aplicação.
- **HTML:** Estruturação do conteúdo e das páginas web.
- **CSS:** Estilização das páginas web para uma melhor experiência do usuário.
- **Git:** Controle de versão do código.
- **GitHub:** Hospedagem do repositório remoto.
- **Gitflow:** Modelo de ramificação para organização do desenvolvimento.

## Padrão de Nomes para Features

As features e correções devem seguir o padrão abaixo para facilitar o entendimento e rastreamento no projeto:

{Feat/issue-[numero-da-issue]-[descricao-da-issue]}


### Exemplo

`Feat/issue-01-correcao-de-bugs`

**Observação:** Não utilizar caracteres especiais. O mesmo padrão aplicado na criação de nomes de variáveis.

## Como Iniciar o Projeto

1. **Instalar o XAMPP:**

   - Faça o download e instale o [XAMPP](https://www.apachefriends.org/index.html).
   - Certifique-se de que o Apache está em execução.

2. **Configurar o Ambiente:**

   - Coloque o projeto na pasta `htdocs` do XAMPP.
   - ![image](https://github.com/user-attachments/assets/b5feba1a-f76f-42b5-be8a-87a9d0af342b)
   - ![image](https://github.com/user-attachments/assets/b96fec70-b9c4-4e63-ade6-12a3877181b0)
   - ![image](https://github.com/user-attachments/assets/4d8f206d-e50c-46bf-900c-12ac5556fe29)
   - Abra o terminal e clone o repositório:
     ```bash
     git clone https://github.com/teu-usuario/teu-projeto.git
     ```
   - 

4. **Iniciar o Servidor:**

   - Abra o XAMPP e inicie o Apache.
   - ![image](https://github.com/user-attachments/assets/cfa7ad11-259b-4118-8bea-1cdcafb99f18)
   - Acesse a aplicação através do navegador: `http://localhost/` ou `http://127.0.0.1`.

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
   git checkout -b Feat/issue-\[numero-da-issue\]-\[descricao-da-issue\]
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
   git push origin Feat/issue-\[numero-da-issue\]-\[descricao-da-issue\]
   ```
Exemplo:
   ```bash
   git push origin Feat/issue-01-correcao-de-bugs
   ```

## Fluxo de Trabalho com Gitflow

- **Main:** Contém a versão estável e em produção.
- **Develop:** Contém as últimas alterações que serão futuramente incluídas na Master.
- **Feature Branches:** Utilizadas para o desenvolvimento de novas funcionalidades (padrão `Feat/issue-[numero-da-issue]-[descricao-da-issue]`).
- **Release Branches:** Preparação das novas versões para produção.
- **Hotfix Branches:** Correções de bugs em produção.

## Contribuição

1. Crie uma branch a partir de `develop` para trabalhar em novas funcionalidades ou correções.
2. Faça commits regulares com mensagens claras.
3. Envie um Pull Request para a branch `develop`.
4. Aguarde a revisão do código antes de fazer o merge.