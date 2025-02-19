from datetime import datetime

import pytest

from MyTwitter.tweet import Tweet


@pytest.fixture
def test_tweet():
    """Cria um objeto tweet de teste

    Returns:
        Objeto : Retorna um objeto da classe Tweet
    """

    return Tweet("@usuario_teste", "Mensagem de teste")


def test_get_id(test_tweet):
    id_gerado = test_tweet.get_id()

    # ID é string?
    assert isinstance(id_gerado, str)

    # ID é vazio?
    assert len(id_gerado) > 0


def test_unicidade_dos_ids(test_tweet):
    novo_tweet = Tweet("@novo_usuario_teste", "Nova mensagem de teste")

    novo_id = novo_tweet.get_id()

    assert novo_id != test_tweet.get_id()


def test_get_usuario():
    usuario = "@novo_usuario_teste"
    novo_tweet = Tweet(usuario, "Nova mensagem de teste")

    # O usuario retornado é igual ao passodo na classe?
    assert novo_tweet.get_usuario() == usuario

    # O usuario é valida?
    assert len(novo_tweet.get_usuario()) > 0

    # O usuario retornado é uma string?
    assert isinstance(novo_tweet.get_usuario(), str)


def test_mensagem():
    mensagem = "Nova mensagem de teste"
    novo_tweet = Tweet("@novo_usuario_teste", mensagem)

    # A mensagem retornada é igual a enviada?
    assert mensagem == novo_tweet.get_mensagem()

    # A mensagem é valida?
    assert len(novo_tweet.get_mensagem()) > 0

    # O mensagem retornado é uma string?
    assert isinstance(novo_tweet.get_mensagem(), str)


def test_data_postagem():
    novo_tweet = Tweet("@novo_usuario_teste", "Nova mensagem de teste")

    # A data retornada é um datetime?
    assert isinstance(novo_tweet.get_data_postagem(), datetime)

    # A data é valida?
    data_postagem = novo_tweet.get_data_postagem()
    data_atual = datetime.today()
    assert data_postagem <= data_atual
