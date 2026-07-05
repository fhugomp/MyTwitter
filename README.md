# MyTwitter

Este repositório contém a implementação do **MyTwitter**, uma aplicação baseada no serviço de microblogging Twitter, desenvolvida como projeto prático para a disciplina *CK0442 - Técnicas de Programação para Ciência de Dados* na Universidade Federal do Ceará (UFC). O sistema adota os pilares de Programação Orientada a Objetos (POO) para simular o gerenciamento de perfis, publicações, conexões de rede social e distribuição de feeds de conteúdo.

## 1. Arquitetura e Engenharia de Software

A arquitetura do sistema é estruturada em módulos independentes que segmentam a lógica de domínio, persistência em memória, validações de integridade e interfaces de execução:

### 1.1. Modelagem de Domínio e Abstrações (POO)
* **Estrutura de Perfis:** Implementação de herança onde as classes concretas `PessoaFisica` e `PessoaJuridica` herdam da classe base abstrata `Perfil`. O modelo encapsula atributos restritos como identificadores únicos, listas de seguidores/seguidos, vetor de tweets publicados e estado de ativação da conta.
* **Componente de Publicação (`Tweet`):** Abstração que encapsula a mensagem (respeitando o limite de tamanho estabelecido), o carimbo identificador e o vínculo estrito com o perfil autor da postagem.

### 1.2. Camada de Persistência e Controle
* **Módulo de Repositório (`repositorio.py`):** Responsável pelo armazenamento e gerenciamento das entidades em memória estruturada. Fornece métodos padronizados para inserção, busca e atualização de perfis e tweets, atuando como uma camada de abstração de dados.
* **Orquestrador Central (`mytwitter.py`):** Atua como a fachada (*Facade*) do sistema, centralizando o fluxo de chamadas das regras de negócio como a validação de unicidade de identificadores, gerenciamento de relacionamentos de rede (seguir/deixar de seguir) e a composição algorítmica da *timeline*.

### 1.3. Matriz de Tratamento de Sinais e Exceções (`exceptions/`)
O sistema rejeita estados inválidos de execução por meio de um sistema de exceções customizadas fortemente tipadas, mapeando falhas de pré-condições de negócio sem interrupções abruptas do fluxo:
* `PIException` (Perfil Inexistente)
* `PDException` (Perfil Desativado)
* `PEException` (Perfil Já Existente)
* `SIException` (Seguidor Inválido)
* `UJCException` (Usuário Já Cadastrado)
* `UNCException` (Usuário Não Cadastrado)
* Outras exceções auxiliares de validação de payload (`mfp_exception.py`).

## 2. Regras de Negócio e Restrições de Sistema

* **Restrição de Identidade:** O identificador numérico ou literal associado a cada perfil deve possuir propriedades de unicidade global na base do repositório.
* **Sanitização de Entradas:** Publicações textuais (`Tweets`) possuem validação estrutural rígida no tamanho do payload, delimitadas na faixa de 1 a 140 caracteres.
* **Integridade de Estado:** Perfis marcados com estado inativo (`cancelado`) perdem a capacidade operacional no sistema, bloqueando operações de postagem, estabelecimento de novos vínculos de monitoramento (seguir) ou consultas ativas de feed.

## 3. Requisitos de Ambiente

A execução está condicionada às seguintes dependências de ambiente:
* Python 3.10 ou superior
* Poetry (Gerenciador de dependências, empacotamento e ambientes virtuais)

## 4. Instruções de Instalação e Execução

1. Clonar o repositório localmente:
```bash
 git clone https://github.com/fhugomp/MyTwitter.git
```

2. Navegar até o diretório raiz do projeto:
```bash
cd MyTwitter
```

3. Realizar a instalação das dependências e isolamento de ambiente via Poetry:
```bash
poetry install
```

4. Executar os scripts de demonstração ou a interface em modo terminal:
```bash
poetry run python demo.py
```
ou
```bash
poetry run python terminal.py
```

## 5. Validação e Testes Unitários

A confiabilidade das regras de negócio, consistência do repositório e os gatilhos de exceções são validados por uma suíte de testes automatizados estruturada sob o framework `pytest`.

Para disparar os testes lógicos e validar a integridade da base de código:
```bash
poetry run pytest
```

## 6. Estrutura Estrutural do Repositório

```text
MyTwitter/
├── exceptions/
│   ├── __init__.py
│   ├── mfp_exception.py
│   ├── pd_exception.py
│   ├── pe_exception.py
│   ├── pi_exception.py
│   ├── si_exception.py
│   ├── ujc_exception.py
│   └── unc_exception.py
├── MyTwitter/
│   ├── __init__.py
│   ├── mytwitter.py
│   ├── perfil.py
│   ├── pessoa_fisica.py
│   ├── pessoa_juridica.py
│   ├── repositorio.py
│   └── tweet.py
├── tests/
│   ├── __init__.py
│   ├── test_mytwitter.py
│   ├── test_perfil.py
│   ├── test_pessoa_fisica.py
│   ├── test_pessoa_juridica.py
│   ├── test_repositorio.py
│   └── test_tweet.py
├── utils/
│   ├── __init__.py
│   └── gerador_id.py
├── demo.py
├── pyproject.toml
└── terminal.py
```
