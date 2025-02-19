t = Perfil("@fhugo")
t.add_tweet("meu primeiro tweet")
t.add_tweet("meu segundo tweet")
t.add_tweet("meu terceiro tweet")
t.add_tweet("meu quarto tweet")

for tweet in t.get_tweets():
    print(f"{tweet.get_usuario()}, {tweet.get_mensagem()}")
