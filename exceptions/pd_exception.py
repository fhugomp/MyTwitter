class PDException(Exception):
    """Exceção lançada quando o perfil esta inativo."""
    def __init__(self, message="O perfil esta inativo."):
        self.message = message
        super().__init__(self.message)