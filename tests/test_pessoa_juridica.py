import pytest

from main.pessoa_juridica import PessoaJuridica


@pytest.fixture
def PessoaJuridica_teste():
    perfil = PessoaJuridica("@user_teste", "56.275.377/0001-08")

    return perfil


def test_get_usuario(PessoaJuridica_teste):
    perfil = PessoaJuridica_teste

    usuario = "@user_teste"

    # A classe está puxando o construtor da classe pai?
    assert usuario == perfil.get_usuario()

    # O usuário é do tipo string?
    assert isinstance(perfil.get_usuario(), str)


def test_get_cnpj(PessoaJuridica_teste):
    perfil = PessoaJuridica_teste
    cnpj = "56.275.377/0001-08"

    # O CNPJ devolvido é correspondente ao enviado?
    assert cnpj == perfil.get_cnpj()

    # O CNPJ é do tipo string?
    assert isinstance(perfil.get_cnpj(), str)


def test_cnpj_invalido():
    # O CNPJ é vazio?
    with pytest.raises(ValueError):
        PessoaJuridica("@user_teste", "")


def test_usuario_invalido():
    # O usuario é vazio?
    with pytest.raises(ValueError):
        PessoaJuridica("", "56.275.377/0001-08")
