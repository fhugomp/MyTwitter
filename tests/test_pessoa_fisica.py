import pytest
from MyTwitter.pessoa_fisica import PessoaFisica

@pytest.fixture
def pessoa_teste():
    perfil = PessoaFisica('@usuario_teste', '123456789-12')
    
    return perfil

def test_get_usuario(pessoa_teste):
    perfil = pessoa_teste
    usuario = '@usuario_teste'
    
    # A classe está puxando o construtor da classe pai?
    assert usuario == perfil.get_usuario()
    
    # O usuário é do tipo string?
    assert isinstance(perfil.get_usuario(), str)

def test_get_cpf(pessoa_teste):
    perfil = pessoa_teste
    cpf = '123456789-12'
    
    # O CPF devolvido é correspondente ao enviado?
    assert cpf == perfil.get_cpf()
    
    # O CPF é do tipo string?
    assert isinstance(perfil.get_cpf(), str)
