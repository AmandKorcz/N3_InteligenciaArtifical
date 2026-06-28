# N3_InteligenciaArtifical

## Instruções de execução

Este projeto foi desenvolvido em **Python** utilizando o framework **Streamlit** para construção da interface web. A aplicação implementa um sistema especialista baseado em regras para triagem e priorização de chamados de suporte.

### 1. Pré-requisitos

Antes de executar o projeto, é necessário ter instalado na máquina:

* Python 3.10 ou superior;
* Git;
* Pip, que normalmente já acompanha a instalação do Python.

Para verificar se o Python está instalado, execute:

```bash
python --version
```

Para verificar se o Git está instalado, execute:

```bash
git --version
```

---

### 2. Clonar o repositório

No terminal, execute o comando abaixo, substituindo a URL pelo link do repositório no GitHub:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Depois, acesse a pasta do projeto:

```bash
cd nome-do-repositorio
```

---

### 3. Criar o ambiente virtual

Dentro da pasta do projeto, crie um ambiente virtual com o comando:

```bash
python -m venv .venv
```

O ambiente virtual é utilizado para isolar as dependências do projeto, evitando conflitos com outras bibliotecas instaladas no computador.

---

### 4. Ativar o ambiente virtual

No Windows, utilizando o Prompt de Comando, execute:

```bash
.venv\Scripts\activate
```

No Windows, utilizando o PowerShell, execute:

```bash
.venv\Scripts\Activate.ps1
```

No Linux ou Mac, execute:

```bash
source .venv/bin/activate
```

Quando o ambiente virtual estiver ativo, o terminal deverá exibir algo parecido com:

```bash
(.venv) C:\caminho\do\projeto>
```

---

### 5. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

As principais dependências utilizadas são:

* streamlit;
* pandas.

---

### 6. Executar a aplicação

Após instalar as dependências, execute o projeto com o comando:

```bash
streamlit run app.py
```

Após a execução, o Streamlit abrirá automaticamente a aplicação no navegador. Caso isso não aconteça, acesse manualmente o endereço exibido no terminal, normalmente:

```bash
http://localhost:8501
```

---