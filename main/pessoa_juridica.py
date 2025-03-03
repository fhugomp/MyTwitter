from main.perfil import Perfil


class PessoaJuridica(Perfil):
    def __init__(self, usuario: str, cnpj: str) -> None:

        if not usuario.strip():
            raise ValueError("O usuário deve ser uma string não vazia.")

        if not cnpj.strip():
            raise ValueError("O CNPJ deve ser uma string não vazia.")

        super().__init__(usuario)
        self.__cnpj = cnpj

    def get_cnpj(self) -> str:
        return self.__cnpj
