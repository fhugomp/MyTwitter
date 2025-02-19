class PEException(Exception):
    """Exceção lançada quando um perfil já está cadastrado."""
    def __init__(self, message="Perfil já cadastrado"):
        self.message = message
        super().__init__(self.message)