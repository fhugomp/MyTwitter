# MyTwitter

**Desenvolvido para a disciplina CK0442 - Técnicas de Programação para Ciência de Dados (UFC).** 🎓

---

## 📌 Descrição
O **MyTwitter** é uma versão simplificada do popular serviço de microblogging Twitter. Ele permite que usuários (pessoas ou empresas) criem perfis, publiquem tweets, sigam outros usuários e visualizem uma timeline personalizada.

## 📋 Funcionalidades
- 📌 **Criar perfil** (Pessoa Física ou Pessoa Jurídica)
- 📝 **Tweetar** (com limite de 140 caracteres)
- 👥 **Seguir outros perfis**
- 📃 **Visualizar timeline** (tweets próprios e de perfis seguidos)
- 🔍 **Buscar perfis**
- ❌ **Cancelar perfil** (desativar conta)
- 📊 **Número de seguidores e lista de seguidores**
- ✅ **Testes unitários obrigatórios**

## 🚀 Tecnologias Utilizadas
- **Python 3** 🐍
- **Poetry** 📦 (gerenciamento de dependências)
- **Pytest** 🧪 (testes unitários)

## 📂 Estrutura do Projeto
```
exceptions/
│── __init__.py
│── mfp_exception.py
│── pd_exception.py
│── pe_exception.py
│── pi_exception.py
│── si_exception.py
│── ujc_exception.py
│── unc_exception.py
MyTwitter/
│── __init__.py
│── mytwitter.py
│── perfil.py
│── pessoa_fisica.py
│── pessoa_juridica.py
│── repositorio.py
│── tweet.py
tests/
│── __init__.py
│── test_mytwitter.py
│── test_perfil.py
│── test_pessoa_fisica.py
│── test_pessoa_juridica.py
│── test_repositorio.py
│── test_tweet.py
utils/
│── __init__.py
│── gerador_id.py
demo.py
terminal.py

```

## 🛠️ Configuração e Instalação
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/MyTwitter.git
cd MyTwitter
```
### 2️⃣ Instalar dependências com Poetry
```bash
poetry install
```
### 3️⃣ Rodar testes
```bash
poetry run pytest
```
### 4️⃣ Executar o projeto
```bash
poetry run python demo.py
```

## 📜 Regras e Restrições
- O nome de usuário deve ser único.
- Tweets podem ter no mínimo 1 e no máximo 140 caracteres.
- Perfis desativados não podem tweetar, seguir ou ser seguidos.
- Erros geram exceções específicas (`PIException`, `PDException`, etc.).
