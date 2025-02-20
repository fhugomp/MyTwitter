class SIException(Exception):
    """Exceção lançada quando o nome de usuário do seguidor seja o mesmo do seguido."""

    def __init__(
        self, message="O nome de usuário do seguidor seja o mesmo do seguido."
    ):
        self.message = message
        super().__init__(self.message)
