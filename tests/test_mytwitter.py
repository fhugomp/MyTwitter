import pytest

from exceptions.mfp_exception import MFPException
from exceptions.pd_exception import PDException
from exceptions.pe_exception import PEException
from exceptions.pi_exception import PIException
from exceptions.si_exception import SIException
from main.mytwitter import MyTwitter
from main.perfil import Perfil


@pytest.fixture
def mytwitter_teste():
    my_twitter = MyTwitter()
    perfil = Perfil("@usuario_teste")
    my_twitter.criar_perfil(perfil)
    return my_twitter


def test_criar_perfil_valido(mytwitter_teste):
    perfil = Perfil("@novo_usuario")

    # Criar o perfil sem exceções
    mytwitter_teste.criar_perfil(perfil)

    # Verificar se o perfil foi criado e é possível buscar o usuário
    usuario_buscado = mytwitter_teste._MyTwitter__repositorio.buscar(
        perfil.get_usuario()
    )  # Acessa repositório internamente
    assert usuario_buscado.get_usuario() == perfil.get_usuario()


def test_criar_perfil_duplicado(mytwitter_teste):
    perfil1 = Perfil("@usuario_duplicado")
    perfil2 = Perfil("@usuario_duplicado")

    # Criar o primeiro perfil
    mytwitter_teste.criar_perfil(perfil1)

    # Tentar criar o perfil duplicado, o que deve gerar uma exceção PEException
    with pytest.raises(PEException):
        mytwitter_teste.criar_perfil(perfil2)


def test_cancelar_perfil_sucesso(mytwitter_teste):
    """Testa se um perfil ativo pode ser cancelado corretamente."""
    mytwitter_teste.cancelar_perfil("@usuario_teste")

    usuario_buscado = mytwitter_teste._MyTwitter__repositorio.buscar("@usuario_teste")
    assert not usuario_buscado.get_ativo()  # O perfil deve estar desativado


def test_cancelar_perfil_ja_desativado(mytwitter_teste):
    """Testa se tentar cancelar um perfil já desativado levanta PDException."""
    mytwitter_teste.cancelar_perfil("@usuario_teste")  # Primeiro, desativa o perfil

    with pytest.raises(PDException):
        mytwitter_teste.cancelar_perfil(
            "@usuario_teste"
        )  # Segunda tentativa deve falhar


def test_cancelar_perfil_inexistente(mytwitter_teste):
    """Testa se tentar cancelar um perfil inexistente levanta PIException."""
    with pytest.raises(PIException):
        mytwitter_teste.cancelar_perfil("@nao_existe")


def test_tweetar_sucesso(mytwitter_teste):
    """Testa se um tweet válido pode ser postado corretamente."""
    usuario = "@usuario_teste"
    mensagem = "Este é um tweet de teste."

    mytwitter_teste.tweetar(usuario, mensagem)
    perfil = mytwitter_teste._MyTwitter__repositorio.buscar(usuario)

    assert any(tweet.get_mensagem() == mensagem for tweet in perfil.get_tweets())


def test_tweetar_usuario_inexistente(mytwitter_teste):
    """Testa se tentar tweetar com um usuário inexistente levanta PIException."""
    with pytest.raises(PIException):
        mytwitter_teste.tweetar("@nao_existe", "Teste de mensagem")


def test_tweetar_perfil_desativado(mytwitter_teste):
    """Testa se tentar tweetar com um perfil desativado levanta PIException."""
    usuario = "@usuario_teste"
    mytwitter_teste.cancelar_perfil(usuario)

    with pytest.raises(PDException):
        mytwitter_teste.tweetar(usuario, "Teste de mensagem")


def test_tweetar_mensagem_curta(mytwitter_teste):
    """Testa se uma mensagem vazia ou muito curta levanta MFPException."""
    usuario = "@usuario_teste"

    with pytest.raises(MFPException):
        mytwitter_teste.tweetar(usuario, "")


def test_tweetar_mensagem_longa(mytwitter_teste):
    """Testa se uma mensagem maior que 140 caracteres levanta MFPException."""
    usuario = "@usuario_teste"
    mensagem = "a" * 141  # 141 caracteres

    with pytest.raises(MFPException):
        mytwitter_teste.tweetar(usuario, mensagem)


def test_timeline_valida(mytwitter_teste):
    """Testa se a timeline de um perfil válido é retornada corretamente."""
    usuario = "@usuario_teste"
    mensagem = "Este é um tweet de teste."

    # Adiciona um tweet ao perfil
    mytwitter_teste.tweetar(usuario, mensagem)

    # Recupera a timeline
    timeline = mytwitter_teste.timeline(usuario)

    # Verifica se o tweet está na timeline
    assert any(tweet.get_mensagem() == mensagem for tweet in timeline)


def test_timeline_perfil_inexistente(mytwitter_teste):
    """Testa se tentar recuperar a timeline de um perfil inexistente levanta PIException."""
    with pytest.raises(PIException):
        mytwitter_teste.timeline("@nao_existe")


def test_timeline_perfil_desativado(mytwitter_teste):
    """Testa se tentar recuperar a timeline de um perfil desativado levanta PDException."""
    usuario = "@usuario_teste"
    mytwitter_teste.cancelar_perfil(usuario)  # Desativa o perfil

    with pytest.raises(PDException):
        mytwitter_teste.timeline(usuario)


def test_timeline_vazia(mytwitter_teste):
    """Testa se a timeline de um perfil sem tweets retorna uma lista vazia."""
    usuario = "@usuario_teste"

    # Recupera a timeline (sem tweets adicionados)
    timeline = mytwitter_teste.timeline(usuario)

    # Verifica se a timeline está vazia
    assert len(timeline) == 0


def test_tweets_validos(mytwitter_teste):
    """Testa se os tweets de um perfil válido são retornados corretamente."""
    usuario = "@usuario_teste"
    mensagem = "Este é um tweet de teste."

    # Adiciona um tweet ao perfil
    mytwitter_teste.tweetar(usuario, mensagem)

    # Recupera os tweets do perfil
    tweets = mytwitter_teste.tweets(usuario)

    # Verifica se o tweet está na lista de tweets
    assert any(tweet.get_mensagem() == mensagem for tweet in tweets)


def test_tweets_perfil_inexistente(mytwitter_teste):
    """Testa se tentar recuperar os tweets de um perfil inexistente levanta PIException."""
    with pytest.raises(PIException):
        mytwitter_teste.tweets("@nao_existe")


def test_tweets_perfil_desativado(mytwitter_teste):
    """Testa se tentar recuperar os tweets de um perfil desativado levanta PDException."""
    usuario = "@usuario_teste"
    mytwitter_teste.cancelar_perfil(usuario)  # Desativa o perfil

    with pytest.raises(PDException):
        mytwitter_teste.tweets(usuario)


def test_tweets_vazios(mytwitter_teste):
    """Testa se a lista de tweets de um perfil sem tweets retorna uma lista vazia."""
    usuario = "@usuario_teste"

    # Recupera os tweets do perfil (sem tweets adicionados)
    tweets = mytwitter_teste.tweets(usuario)

    # Verifica se a lista de tweets está vazia
    assert len(tweets) == 0


def test_seguir_valido(mytwitter_teste):
    """Testa se um usuário pode seguir outro corretamente."""
    seguidor = "@seguidor"
    seguido = "@seguido"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(seguidor))
    mytwitter_teste.criar_perfil(Perfil(seguido))

    # Segue o usuário
    mytwitter_teste.seguir(seguidor, seguido)

    # Verifica se o seguido foi adicionado à lista de seguidos do seguidor
    perfil_seguidor = mytwitter_teste._MyTwitter__repositorio.buscar(seguidor)
    assert seguido in [s.get_usuario() for s in perfil_seguidor.get_seguidos()]

    # Verifica se o seguidor foi adicionado à lista de seguidores do seguido
    perfil_seguido = mytwitter_teste._MyTwitter__repositorio.buscar(seguido)
    assert seguidor in [s.get_usuario() for s in perfil_seguido.get_seguidores()]


def test_seguir_perfil_inexistente(mytwitter_teste):
    """Testa se tentar seguir um perfil inexistente levanta PIException."""
    seguidor = "@seguidor"
    seguido = "@nao_existe"

    # Cria o perfil do seguidor
    mytwitter_teste.criar_perfil(Perfil(seguidor))

    with pytest.raises(PIException):
        mytwitter_teste.seguir(seguidor, seguido)


def test_seguir_perfil_desativado(mytwitter_teste):
    """Testa se tentar seguir um perfil desativado levanta PDException."""
    seguidor = "@seguidor"
    seguido = "@seguido"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(seguidor))
    mytwitter_teste.criar_perfil(Perfil(seguido))

    # Desativa o perfil do seguido
    mytwitter_teste.cancelar_perfil(seguido)

    with pytest.raises(PDException):
        mytwitter_teste.seguir(seguidor, seguido)


def test_seguir_a_si_mesmo(mytwitter_teste):
    """Testa se tentar seguir a si mesmo levanta SIException."""
    usuario = "@usuario"

    # Cria o perfil
    mytwitter_teste.criar_perfil(Perfil(usuario))

    with pytest.raises(SIException):
        mytwitter_teste.seguir(usuario, usuario)


def test_numero_seguidores_valido(mytwitter_teste):
    """Testa se o número de seguidores de um perfil válido é retornado corretamente."""
    usuario = "@usuario"
    seguidor1 = "@seguidor1"
    seguidor2 = "@seguidor2"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.criar_perfil(Perfil(seguidor1))
    mytwitter_teste.criar_perfil(Perfil(seguidor2))

    # Segue o usuário
    mytwitter_teste.seguir(seguidor1, usuario)
    mytwitter_teste.seguir(seguidor2, usuario)

    # Verifica o número de seguidores
    assert mytwitter_teste.numero_seguidores(usuario) == 2


def test_numero_seguidores_perfil_inexistente(mytwitter_teste):
    """Testa se tentar obter o número de seguidores de um perfil inexistente levanta PIException."""
    with pytest.raises(PIException):
        mytwitter_teste.numero_seguidores("@nao_existe")


def test_numero_seguidores_perfil_desativado(mytwitter_teste):
    """Testa se tentar obter o número de seguidores de um perfil desativado levanta PDException."""
    usuario = "@usuario"

    # Cria o perfil e o desativa
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.cancelar_perfil(usuario)

    with pytest.raises(PDException):
        mytwitter_teste.numero_seguidores(usuario)


def test_numero_seguidores_seguidores_inativos(mytwitter_teste):
    """Testa se seguidores inativos não são contabilizados."""
    usuario = "@usuario"
    seguidor1 = "@seguidor1"
    seguidor2 = "@seguidor2"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.criar_perfil(Perfil(seguidor1))
    mytwitter_teste.criar_perfil(Perfil(seguidor2))

    # Segue o usuário
    mytwitter_teste.seguir(seguidor1, usuario)
    mytwitter_teste.seguir(seguidor2, usuario)

    # Desativa um seguidor
    mytwitter_teste.cancelar_perfil(seguidor1)

    # Verifica o número de seguidores (apenas seguidor2 deve ser contabilizado)
    assert mytwitter_teste.numero_seguidores(usuario) == 1


def test_seguidores_validos(mytwitter_teste):
    """Testa se a lista de seguidores de um perfil válido é retornada corretamente."""
    usuario = "@usuario"
    seguidor1 = "@seguidor1"
    seguidor2 = "@seguidor2"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.criar_perfil(Perfil(seguidor1))
    mytwitter_teste.criar_perfil(Perfil(seguidor2))

    # Segue o usuário
    mytwitter_teste.seguir(seguidor1, usuario)
    mytwitter_teste.seguir(seguidor2, usuario)

    # Recupera a lista de seguidores
    seguidores = mytwitter_teste.seguidores(usuario)

    # Verifica se os seguidores estão na lista
    assert seguidor1 in [s.get_usuario() for s in seguidores]
    assert seguidor2 in [s.get_usuario() for s in seguidores]


def test_seguidores_perfil_inexistente(mytwitter_teste):
    """Testa se tentar obter a lista de seguidores de um perfil inexistente levanta PIException."""
    with pytest.raises(PIException):
        mytwitter_teste.seguidores("@nao_existe")


def test_seguidores_perfil_desativado(mytwitter_teste):
    """Testa se tentar obter a lista de seguidores de um perfil desativado levanta PDException."""
    usuario = "@usuario"

    # Cria o perfil e o desativa
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.cancelar_perfil(usuario)

    with pytest.raises(PDException):
        mytwitter_teste.seguidores(usuario)


def test_seguidores_seguidores_inativos(mytwitter_teste):
    """Testa se seguidores inativos não são incluídos na lista."""
    usuario = "@usuario"
    seguidor1 = "@seguidor1"
    seguidor2 = "@seguidor2"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.criar_perfil(Perfil(seguidor1))
    mytwitter_teste.criar_perfil(Perfil(seguidor2))

    # Segue o usuário
    mytwitter_teste.seguir(seguidor1, usuario)
    mytwitter_teste.seguir(seguidor2, usuario)

    # Desativa um seguidor
    mytwitter_teste.cancelar_perfil(seguidor1)

    # Recupera a lista de seguidores
    seguidores = mytwitter_teste.seguidores(usuario)

    # Verifica se apenas o seguidor ativo está na lista
    assert seguidor2 in [s.get_usuario() for s in seguidores]
    assert seguidor1 not in [s.get_usuario() for s in seguidores]


def test_seguidos_validos(mytwitter_teste):
    """Testa se a lista de seguidos de um perfil válido é retornada corretamente."""
    usuario = "@usuario"
    seguido1 = "@seguido1"
    seguido2 = "@seguido2"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.criar_perfil(Perfil(seguido1))
    mytwitter_teste.criar_perfil(Perfil(seguido2))

    # Usuário segue os perfis criados
    mytwitter_teste.seguir(usuario, seguido1)
    mytwitter_teste.seguir(usuario, seguido2)

    # Recupera a lista de seguidos
    seguidos = mytwitter_teste.seguidos(usuario)

    # Verifica se os seguidos estão na lista
    assert seguido1 in [s.get_usuario() for s in seguidos]
    assert seguido2 in [s.get_usuario() for s in seguidos]


def test_seguidos_perfil_inexistente(mytwitter_teste):
    """Testa se tentar obter a lista de seguidos de um perfil inexistente levanta PIException."""
    with pytest.raises(PIException):
        mytwitter_teste.seguidos("@nao_existe")


def test_seguidos_perfil_desativado(mytwitter_teste):
    """Testa se tentar obter a lista de seguidos de um perfil desativado levanta PDException."""
    usuario = "@usuario"

    # Cria o perfil e o desativa
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.cancelar_perfil(usuario)

    with pytest.raises(PDException):
        mytwitter_teste.seguidos(usuario)


def test_seguidos_seguidos_inativos(mytwitter_teste):
    """Testa se seguidos inativos não são incluídos na lista."""
    usuario = "@usuario"
    seguido1 = "@seguido1"
    seguido2 = "@seguido2"

    # Cria os perfis
    mytwitter_teste.criar_perfil(Perfil(usuario))
    mytwitter_teste.criar_perfil(Perfil(seguido1))
    mytwitter_teste.criar_perfil(Perfil(seguido2))

    # Usuário segue os perfis criados
    mytwitter_teste.seguir(usuario, seguido1)
    mytwitter_teste.seguir(usuario, seguido2)

    # Desativa um seguido
    mytwitter_teste.cancelar_perfil(seguido1)

    # Recupera a lista de seguidos
    seguidos = mytwitter_teste.seguidos(usuario)

    # Verifica se apenas o seguido ativo está na lista
    assert seguido2 in [s.get_usuario() for s in seguidos]
    assert seguido1 not in [s.get_usuario() for s in seguidos]
