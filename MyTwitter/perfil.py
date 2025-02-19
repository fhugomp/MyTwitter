from datetime import datetime

from MyTwitter.tweet import Tweet


class Perfil:
    def __init__(self, usuario: str) -> None:
        self.__usuario = usuario
        self.__seguidos = []
        self.__seguidores = []
        self.__tweets = []
        self.__ativo = True

    def add_seguidor(self, perfil: "Perfil") -> None:
        self.__seguidores.append(perfil)

    def add_seguidos(self, perfil: "Perfil") -> None:
        self.__seguidos.append(perfil)

    def add_tweet(self, mensagem: str) -> None:
        self.__tweets.append(Tweet(self.__usuario, mensagem))

    def get_tweets(self) -> list:
        # Retornando os tweets ordenados do ultimo enviado pro primeiro como uma pilha.
        return sorted(
            self.__tweets, key=lambda tweet: tweet.get_data_postagem(), reverse=True
        )

    def get_seguidores(self) -> list:
        return self.__seguidores

    def get_seguidos(self) -> list:
        return self.__seguidos

    def get_tweet(self, id: str) -> Tweet:
        for tweet in self.get_tweets():
            if id == tweet.get_id():
                return tweet

    def get_timeline(self) -> list:
        timeline = []
        timeline.extend(self.__tweets)  # Adiciona os tweets do perfil atual

        # Adiciona os tweets dos perfis seguidos
        for perfil in self.__seguidos:
            timeline.extend(perfil.get_tweets())

        return sorted(
            timeline, key=lambda tweet: tweet.get_data_postagem(), reverse=True
        )

    def set_usuario(self, novo_usuario: str) -> None:
        self.__usuario = novo_usuario

    def get_usuario(self) -> str:
        return self.__usuario

    def set_ativo(self, estado: bool) -> None:
        self.__ativo = estado

    def get_ativo(self) -> bool:
        return self.__ativo
