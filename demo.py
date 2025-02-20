from exceptions.mfp_exception import MFPException
from exceptions.pd_exception import PDException
from exceptions.pe_exception import PEException
from exceptions.pi_exception import PIException
from exceptions.si_exception import SIException
from MyTwitter.mytwitter import MyTwitter
from MyTwitter.perfil import Perfil
from MyTwitter.pessoa_fisica import PessoaFisica
from MyTwitter.pessoa_juridica import PessoaJuridica
import time

# Criando instância do sistema
twitter = MyTwitter()
time.sleep(1)

# Criando perfis
try:
    pf = PessoaFisica("@joao", "123.456.789-00")
    pj = PessoaJuridica("@empresaX", "12.345.678/0001-99")
    twitter.criar_perfil(pf)
    twitter.criar_perfil(pj)
    print("✅ Perfis criados com sucesso!")
except PEException as e:
    print(f"⚠️ Erro ao criar perfil: {e}")
time.sleep(1)

# Tweetando
try:
    twitter.tweetar("@joao", "Meu primeiro tweet!")
    twitter.tweetar("@empresaX", "Promoção especial!")
    print("✅ Tweets postados com sucesso!")
except (PIException, PDException, MFPException) as e:
    print(f"⚠️ Erro ao tweetar: {e}")
time.sleep(1)

# Seguindo usuários
try:
    twitter.seguir("@joao", "@empresaX")
    print("✅ @joao agora segue @empresaX!")
except (PIException, PDException, SIException) as e:
    print(f"⚠️ Erro ao seguir: {e}")
time.sleep(1)

# Exibindo timeline de João
try:
    print("📃 Timeline de @joao:")
    for tweet in twitter.timeline("@joao"):
        print(f"{tweet.get_usuario()}: {tweet.get_mensagem()}")
except (PIException, PDException) as e:
    print(f"⚠️ Erro ao carregar timeline: {e}")
time.sleep(1)

# Listando seguidores
try:
    num_seguidores = twitter.numero_seguidores("@empresaX")
    print(f"👥 Seguidores de @empresaX: {num_seguidores}")
except (PIException, PDException) as e:
    print(f"⚠️ Erro ao contar seguidores: {e}")
time.sleep(1)

# Listando seguidos
try:
    seguidos = twitter.seguidos("@joao")
    print(f"📌 @joao segue: {[p.get_usuario() for p in seguidos]}")
except (PIException, PDException) as e:
    print(f"⚠️ Erro ao listar seguidos: {e}")
time.sleep(1)

# Cancelando perfil
try:
    twitter.cancelar_perfil("@joao")
    print("❌ @joao foi desativado!")
except (PIException, PDException) as e:
    print(f"⚠️ Erro ao cancelar perfil: {e}")
time.sleep(1)