from main.perfil import Perfil


class PessoaFisica(Perfil):
    def __init__(self, usuario: str, cpf: str):
        if not isinstance(usuario, str):
            raise TypeError("O usuário deve ser uma string.")

        if not usuario.strip():
            raise ValueError("O usuário deve ser uma string não vazia.")

        if not isinstance(cpf, str):
            raise TypeError("O CPF deve ser uma string.")

        if not cpf.strip():
            raise ValueError("O CPF deve ser uma string não vazia.")
        super().__init__(usuario)
        self.__cpf = cpf

    def get_cpf(self) -> str:
        return self.__cpf
