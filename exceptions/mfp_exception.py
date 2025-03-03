class MFPException(Exception):
    """Exceção lançada quando a mensagem não esteja no limiar entre 1 e 140 caracteres."""

    def __init__(self, message: str="A mensagem não contém entre 1 e 140 caracteres."):
        self.message = message
        super().__init__(self.message)
