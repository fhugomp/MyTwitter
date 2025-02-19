from MyTwitter.repositorio import RepositorioUsuarios
from MyTwitter.perfil import Perfil
from exceptions.pe_exception import PEException
from exceptions.unc_exception import UNCException

class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()
        
    def criar_perfil(self, perfil:Perfil) -> None:
        if not isinstance(perfil, Perfil):
            raise ValueError
        
        try:
            # Se o usuário já existir, lança PEException
            self.__repositorio.buscar(perfil.get_usuario())
            raise PEException(f"O usuário '{perfil.get_usuario()}' já está cadastrado.")
        except UNCException:
            # Se não existir, cadastra o perfil
            self.__repositorio.cadastrar(perfil)
    
    def cancelar_perfil(self, usuario:str) -> None:
        pass
    
    def tweetar(self, usuario:str, mensagem:str) -> None:
        pass

    def timeline(self, usuario:str) -> None:
        pass
    
    def tweets(self, usuario:str) -> None:
        pass
    
    def seguir(self, seguidor:str, seguido:str) -> None:
        pass
    
    def numero_seguidores(self, usuario:str) -> int:
        pass
    
    def seguidores(self, usuario:str) -> list:
        pass
    
    def seguidos(self, usuario:str) -> list:
        pass