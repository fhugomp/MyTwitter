import pytest

from exceptions.unc_exception import UNCException
from main.perfil import Perfil
from main.repositorio import RepositorioUsuarios


@pytest.fixture
def repositorio_teste():
    repo = RepositorioUsuarios()
    p1 = Perfil("@User_1")
    p2 = Perfil("@User_2")

    repo.cadastrar(p1)
    repo.cadastrar(p2)

    return repo


def test_cadastrar(repositorio_teste):
    repo = repositorio_teste
    perfil_teste = Perfil("@usuario_teste")
    repo.cadastrar(perfil_teste)

    usuario_buscado = repo.buscar(perfil_teste.get_usuario())

    # O usuario foi cadastrado?
    assert usuario_buscado == perfil_teste


def test_buscar(repositorio_teste):
    repo = repositorio_teste

    # O usuário buscado existe?
    usuario_buscado = repo.buscar("@User_1")
    assert usuario_buscado.get_usuario() == "@User_1"

    # A busca por usuário inexistente funciona?
    with pytest.raises(UNCException):
        repo.buscar("@nao_existe")


def test_atualizar(repositorio_teste):
    repo = repositorio_teste

    perfil_atualizado = Perfil("@User_1")

    repo.atualizar(perfil_atualizado)
    usuario_buscado = repo.buscar("@User_1")

    # O usuário buscado existe?
    assert usuario_buscado == perfil_atualizado

    # É possível atualizar um usuário inexistente?
    perfil_inexistente = Perfil("@nao_existe")
    with pytest.raises(UNCException):
        repo.atualizar(perfil_inexistente)
