from exceptions.mfp_exception import MFPException
from exceptions.pd_exception import PDException
from exceptions.pe_exception import PEException
from exceptions.pi_exception import PIException
from exceptions.si_exception import SIException
from exceptions.unc_exception import UNCException
from MyTwitter.perfil import Perfil
from MyTwitter.repositorio import RepositorioUsuarios
from MyTwitter.tweet import Tweet


class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()

    def criar_perfil(self, perfil: Perfil) -> None:
        """Cria o perfil e o cadastra no repositorio de perfis

        Args:
            perfil (Perfil): Obj da classe Perfil ja criado

        Raises:
            ValueError: Caso o perfil enviado não foi instacia de Perfil
            PEException: Quando o perfil ja existe
        """
        if not isinstance(perfil, Perfil):
            raise ValueError

        try:
            # Se o usuário já existir, lança PEException
            self.__repositorio.buscar(perfil.get_usuario())
            raise PEException(f"O usuário '{perfil.get_usuario()}' já está cadastrado.")
        except UNCException:
            # Se não existir, cadastra o perfil
            self.__repositorio.cadastrar(perfil)

    def cancelar_perfil(self, usuario: str) -> None:
        """
        Cancela (desativa) o perfil de um usuário.

        Args:
            usuario (str): O nome de usuário a ser cancelado.

        Raises:
            ValueError: Se o nome de usuário não for uma string.
            PIException: Se o perfil não for encontrado.
            PDException: Se o perfil já estiver desativado.
        """
        if not isinstance(usuario, str):
            raise ValueError("O nome de usuário deve ser uma string.")

        try:
            perfil = self.__repositorio.buscar(usuario)
        except UNCException:
            # Se o usuário não for encontrado
            raise PIException(f"O perfil '{usuario}' não existe.")

        if not perfil.get_ativo():
            raise PDException(f"O perfil '{usuario}' já está desativado.")

        perfil.set_ativo(False)

    def tweetar(self, usuario: str, mensagem: str) -> None:
        """
        Permite que um usuário publique um tweet.

        Args:
            usuario (str): Nome do usuário que deseja tweetar.
            mensagem (str): Conteúdo do tweet.

        Raises:
            ValueError: Se o nome de usuário não for uma string.
            PIException: Se o perfil não existir.
            PDException: Se o perfil estiver desativado.
            MFPException: Se a mensagem não estiver entre 1 e 140 caracteres.
        """
        if not isinstance(usuario, str):
            raise ValueError("O nome de usuário deve ser uma string.")

        if not (1 <= len(mensagem) <= 140):
            raise MFPException("A mensagem deve ter entre 1 e 140 caracteres.")

        try:
            usuario_buscado = self.__repositorio.buscar(usuario)
        except UNCException:
            raise PIException("O perfil não existe.")

        if not usuario_buscado.get_ativo():
            raise PDException("O perfil está desativado.")

        novo_tweet = Tweet(usuario, mensagem)
        usuario_buscado.add_tweet(novo_tweet.get_mensagem())

    def timeline(self, usuario: str) -> list:
        """
        Recupera todos os tweets da timeline do perfil do usuário informado.

        Args:
            usuario (str): Nome do usuário cuja timeline será recuperada.

        Returns:
            list: Lista de tweets da timeline do usuário.

        Raises:
            ValueError: Se o nome de usuário não for uma string.
            PIException: Se o perfil não existir.
            PDException: Se o perfil estiver desativado.
        """
        if not isinstance(usuario, str):
            raise ValueError("O nome de usuário deve ser uma string.")

        try:
            usuario_buscado = self.__repositorio.buscar(usuario)
        except UNCException:
            raise PIException("O perfil não existe.")

        if not usuario_buscado.get_ativo():
            raise PDException("O perfil está desativado.")

        return usuario_buscado.get_timeline()

    def tweets(self, usuario: str) -> list:
        """Retorna os tweets do usuario enviado.

        Args:
            usuario (str): Nome do usuario que deve retornar os tweets

        Raises:
            ValueError: Caso o usuario não seja do tipo str
            PIException: Caso o perfil não exista
            PDException: Caso o perfil estaja com o estado False

        Returns:
            list: Lista de tweets
        """
        if not isinstance(usuario, str):
            raise ValueError("O nome de usuário deve ser uma string.")

        try:
            usuario_buscado = self.__repositorio.buscar(usuario)
        except UNCException:
            raise PIException("O perfil não existe.")

        if not usuario_buscado.get_ativo():
            raise PDException("O perfil está desativado.")

        return usuario_buscado.get_tweets()

    def seguir(self, seguidor: str, seguido: str) -> None:
        """
        Permite que um usuário siga outro.

        Args:
            seguidor (str): Nome do usuário que deseja seguir.
            seguido (str): Nome do usuário a ser seguido.

        Raises:
            ValueError: Se os nomes de usuário não forem strings.
            PIException: Se o perfil do seguidor ou seguido não existir.
            PDException: Se o perfil do seguidor ou seguido estiver desativado.
            SIException: Se o seguidor tentar seguir a si mesmo.
        """
        if not isinstance(seguidor, str) or not isinstance(seguido, str):
            raise ValueError("Os nomes de usuário devem ser strings.")

        if seguidor == seguido:
            raise SIException("Um usuário não pode seguir a si mesmo.")

        try:
            perfil_seguidor = self.__repositorio.buscar(seguidor)
            perfil_seguido = self.__repositorio.buscar(seguido)
        except UNCException:
            raise PIException("Um dos perfis não existe.")

        if not perfil_seguidor.get_ativo() or not perfil_seguido.get_ativo():
            raise PDException("Um dos perfis está desativado.")

        # Adiciona o seguido à lista de seguidos do seguidor
        perfil_seguidor.add_seguidos(perfil_seguido)

        # Adiciona o seguidor à lista de seguidores do seguido
        perfil_seguido.add_seguidor(perfil_seguidor)

    def numero_seguidores(self, usuario: str) -> int:
        """
        Retorna o número de seguidores do perfil do usuário informado.

        Args:
            usuario (str): Nome do usuário cujo número de seguidores será retornado.

        Returns:
            int: Número de seguidores ativos do usuário.

        Raises:
            ValueError: Se o nome de usuário não for uma string.
            PIException: Se o perfil não existir.
            PDException: Se o perfil estiver desativado.
        """
        if not isinstance(usuario, str):
            raise ValueError("O nome de usuário deve ser uma string.")

        try:
            perfil = self.__repositorio.buscar(usuario)
        except UNCException:
            raise PIException("O perfil não existe.")

        if not perfil.get_ativo():
            raise PDException("O perfil está desativado.")

        # Filtra os seguidores ativos
        seguidores_ativos = [
            seguidor for seguidor in perfil.get_seguidores() if seguidor.get_ativo()
        ]

        return len(seguidores_ativos)

    def seguidores(self, usuario: str) -> list:
        """
        Retorna a lista de seguidores do perfil do usuário informado.

        Args:
            usuario (str): Nome do usuário cuja lista de seguidores será retornada.

        Returns:
            list: Lista de seguidores ativos do usuário.

        Raises:
            ValueError: Se o nome de usuário não for uma string.
            PIException: Se o perfil não existir.
            PDException: Se o perfil estiver desativado.
        """
        if not isinstance(usuario, str):
            raise ValueError("O nome de usuário deve ser uma string.")

        try:
            perfil = self.__repositorio.buscar(usuario)
        except UNCException:
            raise PIException("O perfil não existe.")

        if not perfil.get_ativo():
            raise PDException("O perfil está desativado.")

        # Filtra os seguidores ativos
        seguidores_ativos = [
            seguidor for seguidor in perfil.get_seguidores() if seguidor.get_ativo()
        ]

        return seguidores_ativos

    def seguidos(self, usuario: str) -> list:
        """
        Retorna a lista de perfis seguidos pelo usuário informado.

        Args:
            usuario (str): Nome do usuário cuja lista de seguidos será retornada.

        Returns:
            list: Lista de perfis seguidos que estão ativos.

        Raises:
            ValueError: Se o nome de usuário não for uma string.
            PIException: Se o perfil não existir.
            PDException: Se o perfil estiver desativado.
        """
        if not isinstance(usuario, str):
            raise ValueError("O nome de usuário deve ser uma string.")

        try:
            perfil = self.__repositorio.buscar(usuario)
        except UNCException:
            raise PIException("O perfil não existe.")

        if not perfil.get_ativo():
            raise PDException("O perfil está desativado.")

        # Filtra apenas os perfis seguidos que estão ativos
        seguidos_ativos = [
            seguido for seguido in perfil.get_seguidos() if seguido.get_ativo()
        ]

        return seguidos_ativos
