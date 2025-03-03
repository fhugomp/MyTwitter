class PIException(Exception):
    """Exceção lançada quando o perfil do nome de usuário informado não existe."""

    def __init__(self, message: str="O perfil do nome de usuário informado não existe."):
        self.message = message
        super().__init__(self.message)
