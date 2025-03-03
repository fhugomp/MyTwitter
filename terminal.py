from main.mytwitter import MyTwitter
from main.perfil import Perfil
from main.pessoa_juridica import PessoaJuridica

def terminal_interativo():
    twitter = MyTwitter()

    while True:
        print("\n--- MyTwitter Terminal ---")
        print("1. Criar Perfil")
        print("2. Cancelar Perfil")
        print("3. Tweetar")
        print("4. Ver Timeline")
        print("5. Ver Tweets de um Usuário")
        print("6. Seguir Usuário")
        print("7. Ver Número de Seguidores")
        print("8. Ver Seguidores")
        print("9. Ver Seguidos")
        print("10. Sair")

        escolha = input("Escolha uma opção: ")

        try:
            if escolha == "1":
                usuario = input("Digite o nome de usuário: ")
                tipo_perfil = input("É uma pessoa jurídica? (s/n): ").lower()
                if tipo_perfil == "s":
                    cnpj = input("Digite o CNPJ: ")
                    perfil = PessoaJuridica(usuario, cnpj)
                else:
                    perfil = Perfil(usuario)
                twitter.criar_perfil(perfil)
                print(f"Perfil '{usuario}' criado com sucesso!")

            elif escolha == "2":
                usuario = input("Digite o nome de usuário a ser cancelado: ")
                twitter.cancelar_perfil(usuario)
                print(f"Perfil '{usuario}' cancelado com sucesso!")

            elif escolha == "3":
                usuario = input("Digite o nome de usuário: ")
                mensagem = input("Digite a mensagem do tweet: ")
                twitter.tweetar(usuario, mensagem)
                print(f"Tweet de '{usuario}' publicado com sucesso!")

            elif escolha == "4":
                usuario = input("Digite o nome de usuário: ")
                timeline = twitter.timeline(usuario)
                print(f"Timeline de '{usuario}':")
                for tweet in timeline:
                    print(f"\n@{tweet.get_usuario()} ----------- ({tweet.get_data_postagem()}) \n{tweet.get_mensagem()}")

            elif escolha == "5":
                usuario = input("Digite o nome de usuário: ")
                tweets = twitter.tweets(usuario)
                print(f"Tweets de '{usuario}':")
                for tweet in tweets:
                    print(f"{tweet.get_usuario()} ({tweet.get_data_postagem()}): {tweet.get_mensagem()}")

            elif escolha == "6":
                seguidor = input("Digite o nome de quem vai seguir: ")
                seguido = input("Digite o nome de quem será seguido: ")
                twitter.seguir(seguidor, seguido)
                print(f"'{seguidor}' começou a seguir '{seguido}'!")

            elif escolha == "7":
                usuario = input("Digite o nome de usuário: ")
                num_seguidores = twitter.numero_seguidores(usuario)
                print(f"'{usuario}' tem {num_seguidores} seguidores.")

            elif escolha == "8":
                usuario = input("Digite o nome de usuário: ")
                seguidores = twitter.seguidores(usuario)
                print(f"Seguidores de '{usuario}':")
                for seguidor in seguidores:
                    print(seguidor.get_usuario())

            elif escolha == "9":
                usuario = input("Digite o nome de usuário: ")
                seguidos = twitter.seguidos(usuario)
                print(f"'{usuario}' segue:")
                for seguido in seguidos:
                    print(seguido.get_usuario())

            elif escolha == "10":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Erro: {e}")

# Iniciar o terminal interativo
if __name__ == "__main__":
    terminal_interativo()