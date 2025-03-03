class UJCException(Exception):
    """Exceção lançada quando um usuário já está cadastrado."""

    def __init__(self, message: str="Usuário já cadastrado"):
        self.message = message
        super().__init__(self.message)
