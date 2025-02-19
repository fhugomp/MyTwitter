from datetime import datetime
# import sys
# sys.path.append('/home/hugomendes/Projetos/MyTwitter')


from utils.gerador_id import gerador_id

id_gerado = gerador_id()


class Tweet:
    def __init__(self, nome_usuario: str, mensagem: str):
        self.__id = next(id_gerado)
        self.__nome_usuario = nome_usuario
        self.__mensagem = mensagem
        self.__data_postagem = datetime.today()

    def get_id(self) -> str:
        return self.__id

    def get_usuario(self) -> str:
        return self.__nome_usuario

    def get_mensagem(self) -> str:
        return self.__mensagem

    def get_data_postagem(self) -> datetime:
        return self.__data_postagem
