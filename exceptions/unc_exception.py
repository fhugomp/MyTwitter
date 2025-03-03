class UNCException(Exception):
    """Exceção lançada quando um usuário não está cadastrado."""

    def __init__(self, message: str="Usuário não cadastrado"):
        self.message = message
        super().__init__(self.message)
