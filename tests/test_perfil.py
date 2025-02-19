import pytest

from MyTwitter.perfil import Perfil
from MyTwitter.tweet import Tweet


@pytest.fixture
def perfil_test():
    p1 = Perfil("@fhugo")
    p1.add_tweet("meu primeiro tweet")
    p1.add_tweet("meu segundo tweet")
    p1.add_tweet("meu terceiro tweet")

    return p1


def test_add_seguidor(perfil_test):
    perfil = perfil_test
    numero_seguidores = len(perfil.get_seguidores())
    novo_perfil = Perfil("@user_test")

    perfil.add_seguidor(novo_perfil)

    # O número de seguidores aumenta apos um novo seguidor?
    assert len(perfil.get_seguidores()) == numero_seguidores + 1


def test_add_seguido(perfil_test):
    perfil = perfil_test
    numero_seguidos = len(perfil.get_seguidos())
    novo_perfil = Perfil("@user_test")

    perfil.add_seguidos(novo_perfil)

    # O número de seguidos aumenta apos um novo seguidor?
    assert len(perfil.get_seguidos()) == numero_seguidos + 1


def test_add_tweet(perfil_test):
    perfil = perfil_test
    mensagem_teste = "novo tweet"

    perfil.add_tweet(mensagem_teste)

    # O ultimo tweet corresponde com a ultima mensagem enviada?
    assert perfil.get_tweets()[0].get_mensagem() == mensagem_teste


def test_get_tweets(perfil_test):
    perfil = perfil_test
    tweets = perfil.get_tweets()

    # O metodo get_tweets retorna uma lista?
    assert isinstance(tweets, list)

    # A lista está ordenada do mais recente para o mais antigo?
    assert tweets == sorted(
        tweets, key=lambda tweet: tweet.get_data_postagem(), reverse=True
    )


def test_get_seguidores(perfil_test):
    perfil = perfil_test
    novo_perfil = Perfil("@user_test")
    perfil.add_seguidor(novo_perfil)

    # O metodo retorna uma lista?
    assert isinstance(perfil.get_seguidores(), list)

    # O número de seguidores é igual a 1?
    assert len(perfil.get_seguidores()) == 1


def test_get_seguidos(perfil_test):
    perfil = perfil_test
    novo_perfil = Perfil("@user_test")
    perfil.add_seguidos(novo_perfil)

    # O metodo retorna uma lista?
    assert isinstance(perfil.get_seguidos(), list)

    # O número de seguidores é igual a 1?
    assert len(perfil.get_seguidos()) == 1


def test_get_tweet(perfil_test):
    perfil = perfil_test
    id_ultimo_tweet = perfil.get_tweets()[0].get_id()

    # O tweet retornado é um obj de Tweet?
    tweet_retornado = perfil.get_tweet(id_ultimo_tweet)
    assert isinstance(tweet_retornado, Tweet)

    # O método devolve o tweet correspondente ao id?
    tweet_esperado = perfil.get_tweets()[0]
    assert tweet_retornado.get_id() == tweet_esperado.get_id()

    # O método devolve a mensagem do tweet correspondente ao id?
    assert tweet_retornado.get_mensagem() == tweet_esperado.get_mensagem()

    # Teste para ID inválido
    id_invalido = -1
    tweet_invalido = perfil.get_tweet(id_invalido)
    assert tweet_invalido is None

    # Verifica se o método não levanta exceção para ID inválido
    try:
        perfil.get_tweet(id_invalido)
    except Exception as e:
        assert False


def test_get_timeline(perfil_test):
    perfil = perfil_test
    perfil.add_tweet("Tweet do perfil A")
    perfil.add_tweet("Tweet do perfil B")

    outro_perfil = Perfil("@outro_perfil")
    outro_perfil.add_tweet("Tweet do perfil B")

    perfil.add_seguidor(outro_perfil)
    timeline = perfil.get_timeline()

    # O retorno do metodo get_timeline é uma lista?
    assert isinstance(timeline, list)

    # A timeline contém o número de tweets esperados?
    assert len(timeline) == 5

    # A timeline está ordenada pela data de postagem?
    assert timeline[0].get_mensagem() == "Tweet do perfil B"


def test_set_usuario(perfil_test):
    perfil = perfil_test
    novo_usuario = "@novo_usuario"

    # Define o novo nome de usuário
    perfil.set_usuario(novo_usuario)

    # Verifica se o nome de usuário foi atualizado corretamente
    assert perfil.get_usuario() == novo_usuario


def test_get_usuario(perfil_test):
    perfil = perfil_test

    # O usuário retornado é uma string?
    assert isinstance(perfil.get_usuario(), str)

    # O nome de usuário é o esperado?
    nome_usuario_inicial = perfil.get_usuario()
    assert nome_usuario_inicial == perfil.get_usuario()

    novo_usuario = "@novo_usuario"
    perfil.set_usuario(novo_usuario)

    # O nome de usuário foi alterado corretamente?
    assert perfil.get_usuario() == novo_usuario


def test_set_ativo(perfil_test):
    perfil = perfil_test
    perfil.set_ativo(True)

    # O perfil esta ativo?
    assert perfil.get_ativo() == True

    perfil.set_ativo(False)

    # O perfil esta inativo?
    assert perfil.get_ativo() == False


def test_get_ativo(perfil_test):
    perfil = perfil_test

    # O estado do perfil retornado é do tipo bool?
    assert isinstance(perfil.get_ativo(), bool)

    # O perfil esta ativo ?
    perfil.set_ativo(True)
    assert perfil.get_ativo() == True

    # O perfil esta inativo?
    perfil.set_ativo(False)
    assert perfil.get_ativo() == False
