from uuid import uuid4


def gerador_id():
    """Gere um id utilizando o lib uuid

    Yields:
        str: a cada nova chamada um novo id é gerado.
    """

    while True:
        yield str(uuid4())
