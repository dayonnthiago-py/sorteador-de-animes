import random

print("--------------------SORTEADOR DE ANIMES--------------------")
print("Está com dificuldades de escolher um bom anime para assistir? Aqui resolvemos o seu problema." \
"Temos uma lista com vários nomes famosos e também menos conhecidos de animes de vários gêneros." \
"Primeiro, escolha seu gênero de anime.")

acao = ["Attack on Titan", "Demon Slayer", "One Punch Man", "Bleach", "Fullmetal Alchemist", "Jujutsu Kaisen", "Solo Leveling",
        "Hunter X Hunter", "Chainsaw Man", "Dragon Ball Z"]

romance = ["Kaguya-sama: Love Is War", "Toradora!", "Horimiya", "Your Lie in April", "Fruits Basket", "Clannad",
           "Tomo-chan Is a Girl!", "My Dress-Up Darling", "Kimi ni Todoke: From Me to You", "A sign of Affection"]

comedia = ["Gintama", "Konosuba", "The Disastrous Life of Saiki K.", "Nichijou", "Great Teacher Onizuka", "Asobi Asobase", "Grand Blue Dreaming",
           "Colégio Ouran Host Club", "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You", "Mashle: Magic and Muscles"]

suspense = ["Death Note", "Monster", "A Ilha das Sombras", "Erased", "The Promised Neverland", "Psycho-Pass", "Another", "Pluto", "Parasyte: The Maxim",
            "Serial Experiments Lain"]

terror = ["Higurashi: When They Cry", "Corpse Party: Tortured Souls", "Junji Ito Collection", "Devilman Crybaby", "Yamishibai: Japanese Ghost Stories",
          "Dark Gathering", "O Verão em que Hikaru Morreu", "Perfect Blue", "Shiki", "Mononoke"]

ficcao = ["Cowboy Bebop", "Evangelion", "Code Geass: Lelouch of the Rebellion", "Steins;Gate", "Ghost in the Shell: Stand Alone Complex", "Cyberpunk: Edgerunners",
          "Tengen Toppa Gurren Lagann", "Mobile Suit Gundam", "Ergo Proxy", "Planetes"]

print("Mas antes, vamos ver todo o nosso catálogo.")
print(f"Animes de ação: {acao}")
print(f"Animes de romance: {romance}")
print(f"Animes de comédia: {comedia}")
print(f"Animes de suspense: {suspense}")
print(f"Animes de terror: {terror}")
print(f"Animes de ficção: {ficcao}")

validacao = str(input("Você quer que escolhemos um nome aleatório? (Sim ou não)")).lower().strip()

if validacao == "sim" or validacao == "s":

    while True:
        escolha = str(input("Digite o gênero que quer assistir, e nós vamos dizer um nome aleatório da lista: (Acão, Romance, Comédia, Suspense, Terror, Ficção)")).lower().strip()

        if escolha == "ação" or escolha == "acao" or escolha == "açao" or escolha == "acão":
            anime_para_assistir = random.choice(acao)
            print(f"O anime escolhido foi: {anime_para_assistir}. Boa maratona!")
            break
        elif escolha == "romance":
            anime_para_assistir = random.choice(romance)
            print(f"O anime escolhido foi: {anime_para_assistir}. Boa maratona!")
            break
        elif escolha == "comedia" or escolha == "comédia":
            anime_para_assistir = random.choice(comedia)
            print(f"O anime escolhido foi: {anime_para_assistir}. Boa maratona!")
            break
        elif escolha == "suspense":
            print("Mas se lembre, esse gênero pode conter animes com conteúdo muito sensível para alguns públicos. Esteja ciente de que o que"
            " for selecionado aqui, talvez não seja muito agradável de se assistir. Obrigado pela compreensão.")
            anime_para_assistir = random.choice(suspense)
            print(f"O anime escolhido foi: {anime_para_assistir}. Boa maratona!")
            break
        elif escolha == "terror":
            print("Mas se lembre, esse gênero pode conter animes com conteúdo muito sensível para alguns públicos. Esteja ciente de que o que"
                " for selecionado aqui, talvez não seja muito agradável de se assistir. Obrigado pela compreensão.")
            anime_para_assistir = random.choice(terror)
            print(f"O anime escolhido foi: {anime_para_assistir}. Boa maratona!")
            break
        elif escolha == "ficção" or escolha == "ficcao" or escolha == "ficçao" or escolha == "ficcão":
            anime_para_assistir = random.choice(ficcao)
            print(f"O anime escolhido foi: {anime_para_assistir}. Boa maratona!")
            break
        else:
            print("Você não digitou um gênero válido de nosso programa. Digite novamente.")
elif validacao == "não" or validacao == "nao" or validacao == "n":
    print("Sem problemas! Então você pode procurar em nosso catálogo um nome que chame sua atenção.")