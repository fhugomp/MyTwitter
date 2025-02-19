from MyTwitter.perfil import Perfil

class PessoaFisica(Perfil):
    def __init__(self, usuario, cpf):
        super().__init__(usuario)
        self.__cpf = cpf
        
    def get_cpf(self) -> str:
        return self.__cpf