from MyTwitter.perfil import Perfil


class PessoaJuridica(Perfil):
    def __init__(self, usuario: str, cnpj: str) -> None:
        if not isinstance(usuario, str):
            raise TypeError("O usuário deve ser uma string.")

        if not usuario.strip():
            raise ValueError("O usuário deve ser uma string não vazia.")

        if not isinstance(cnpj, str):
            raise TypeError("O CNPJ deve ser uma string.")

        if not cnpj.strip():
            raise ValueError("O CNPJ deve ser uma string não vazia.")

        super().__init__(usuario)
        self.__cnpj = cnpj

    def get_cnpj(self) -> str:
        return self.__cnpj
