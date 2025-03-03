from exceptions.ujc_exception import UJCException
from exceptions.unc_exception import UNCException
from main.perfil import Perfil


class RepositorioUsuarios:
    def __init__(self):
        self.__usuarios: list[Perfil] = []

    def cadastrar(self, usuario: Perfil) -> None:
        """
        Cadastra um novo usuário no repositório.

        Args:
            usuario (Perfil): O perfil do usuário a ser cadastrado.

        Raises:
            ValueError: Se o objeto passado não for uma instância de Perfil.
            UJCException: Se o usuário já estiver cadastrado.
        """

        try:
            self.buscar(usuario.get_usuario())
            raise UJCException(
                f"O usuário '{usuario.get_usuario()}' já está cadastrado."
            )
        except UNCException:
            self.__usuarios.append(usuario)

    def buscar(self, usuario: str) -> Perfil | None:
        """
        Busca um usuário pelo nome de usuário.

        Args:
            usuario (str): O nome do usuário a ser buscado.

        Returns:
            Perfil | None: O perfil do usuário se encontrado, ou None se não existir.

        Raises:
            UNCException: Se o usuário não for encontrado.
        """
        for perfil in self.__usuarios:
            if perfil.get_usuario() == usuario:
                return perfil
        raise UNCException(f"O usuário '{usuario}' não foi encontrado.")

    def atualizar(self, novo_usuario: Perfil) -> None:
        """
        Atualiza um perfil de usuário existente no repositório.

        Args:
            usuario_atualizado (Perfil): O perfil atualizado do usuário.

        Raises:
            ValueError: Se o objeto passado não for uma instância de Perfil.
            UNCException: Se o usuário não estiver cadastrado.
        """

        for pos, perfil in enumerate(self.__usuarios):
            if perfil.get_usuario() == novo_usuario.get_usuario():
                self.__usuarios[pos] = novo_usuario
                return

        raise UNCException(
            f"O usuário '{novo_usuario.get_usuario()}' não está cadastrado."
        )
