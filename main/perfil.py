from datetime import datetime

from main.tweet import Tweet


class Perfil:
    def __init__(self, usuario: str) -> None:
        self.__usuario = usuario
        self.__seguidos = []
        self.__seguidores = []
        self.__tweets = []
        self.__ativo = True

    def add_seguidor(self, perfil: "Perfil") -> None:
        """Adiciona o perfil enviado na lista de seguidores

        Args:
            perfil (Perfil): Perfil enviado
        """
        self.__seguidores.append(perfil)

    def add_seguidos(self, perfil: "Perfil") -> None:
        """Adiciona o perfil enviado a lista de seguidos

        Args:
            perfil (Perfil): Perfil enviado
        """
        self.__seguidos.append(perfil)

    def add_tweet(self, mensagem: str) -> None:
        """Adiciona um novo tweet na lista de tweets

        Args:
            mensagem (str): Mensagem do tweet adicionado
        """
        self.__tweets.append(Tweet(self.__usuario, mensagem))

    def get_tweets(self) -> list:
        """Recupera todos os tweets ordenados pela data de postagem

        Returns:
            list: Lista de tweets ordenados pela data de postagem
        """

        # Retornando os tweets ordenados do ultimo enviado pro primeiro como uma pilha.
        return sorted(
            self.__tweets, key=lambda tweet: tweet.get_data_postagem(), reverse=True
        )

    def get_seguidores(self) -> list:
        """Retorna a lista de perfils seguidores

        Returns:
            list: Lista de perfis pertecentes aos seguidores
        """
        return self.__seguidores

    def get_seguidos(self) -> list:
        """Recupera a lista de perfis seguidos

        Returns:
            list: Lista de perfis seguidos
        """
        return self.__seguidos

    def get_tweet(self, id: str) -> Tweet:
        """Pega um tweet especifico pelo id

        Args:
            id (str): ID do tweet que sera recuperado

        Returns:
            Tweet: Tweet retornado correspondete ao id
        """
        for tweet in self.get_tweets():
            if id == tweet.get_id():
                return tweet

    def get_timeline(self) -> list:
        """Retorna a lista de tweets incluindo os do perfil como os dos seguidos

        Returns:
            list: Lista de tweets ordenados
        """
        timeline = []
        timeline.extend(self.__tweets)  # Adiciona os tweets do perfil atual

        # Adiciona os tweets dos perfis seguidos
        for perfil in self.__seguidos:
            timeline.extend(perfil.get_tweets())

        return sorted(
            timeline, key=lambda tweet: tweet.get_data_postagem(), reverse=True
        )

    def set_usuario(self, novo_usuario: str) -> None:
        """Define o novo nome de usuario

        Args:
            novo_usuario (str): Novo nome de usuario
        """
        self.__usuario = novo_usuario

    def get_usuario(self) -> str:
        """Retorna o usuario

        Returns:
            str: Usuario retornado
        """
        return self.__usuario

    def set_ativo(self, estado: bool) -> None:
        """Define o estado do perfil

        Args:
            estado (bool): Estado do perfil se esta ativo ou inativo
        """
        self.__ativo = estado

    def get_ativo(self) -> bool:
        """Retorna o estado do perfil

        Returns:
            bool: Se o estado esta ativo oy inativo
        """
        return self.__ativo
