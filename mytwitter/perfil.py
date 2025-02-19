from datetime import datetime

from tweet import Tweet


class Perfil:
    def __init__(self, usuario: str) -> None:
        self.__usuario = usuario
        self.__seguidos = None
        self.__seguidores = None
        self.__tweets = []
        self.__ativo = True

    def add_seguidor(self) -> None:
        self.__seguidores += 1

    def add_seguidos(self) -> None:
        self.__seguidos += 1

    def add_tweet(self, mensagem: str) -> None:
        self.__tweets.append(Tweet(self.__usuario, mensagem))

    def get_tweets(self) -> list:
        # Retornando os tweets ordenados do ultimo enviado pro primeiro como uma pilha.
        return sorted(
            self.__tweets, key=lambda tweet: tweet.get_data_postagem(), reverse=True
        )

    def get_tweet(self) -> Tweet:
        pass

    def get_date_time(self) -> datetime:
        pass

    def get_timeline(self):
        pass

    def set_usuario(self):
        pass

    def get_usuario(self):
        pass

    def set_ativo(self):
        pass

    def get_ativo(self):
        pass
