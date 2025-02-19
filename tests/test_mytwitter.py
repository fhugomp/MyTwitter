import pytest
from MyTwitter.mytwitter import MyTwitter
from MyTwitter.perfil import Perfil
from exceptions.pe_exception import PEException

@pytest.fixture
def mytwitter_teste():
    my_twitter = MyTwitter()
    
    return my_twitter

def test_criar_perfil_valido(mytwitter_teste):
    perfil = Perfil('@novo_usuario')
    
    # Criar o perfil sem exceções
    mytwitter_teste.criar_perfil(perfil)
    
    # Verificar se o perfil foi criado e é possível buscar o usuário
    usuario_buscado = mytwitter_teste._MyTwitter__repositorio.buscar(perfil.get_usuario())  # Acessa repositório internamente
    assert usuario_buscado.get_usuario() == perfil.get_usuario()

def test_criar_perfil_duplicado(mytwitter_teste):
    perfil1 = Perfil('@usuario_duplicado')
    perfil2 = Perfil('@usuario_duplicado')

    # Criar o primeiro perfil
    mytwitter_teste.criar_perfil(perfil1)
    
    # Tentar criar o perfil duplicado, o que deve gerar uma exceção PEException
    with pytest.raises(PEException):
        mytwitter_teste.criar_perfil(perfil2)

def test_criar_perfil_invalido(mytwitter_teste):
    # Passando um objeto que não é instância de Perfil
    with pytest.raises(ValueError):
        mytwitter_teste.criar_perfil("string_invalida")