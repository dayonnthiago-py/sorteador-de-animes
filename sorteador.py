import random

print("--------------------SORTEADOR DE ANIMES--------------------")
print("Está com dificuldades de escolher um bom anime para assistir? Aqui resolvemos o seu problema." \
" Temos uma lista com vários nomes famosos e também menos conhecidos de animes de vários gêneros." \
" Primeiro, escolha seu gênero de anime.")

acao = {"Attack on Titan" : "A humanidade luta pela sobrevivência em cidades cercadas por muralhas gigantes contra gigantes devoradores.", 
        "Demon Slayer": "Um jovem se torna um caçador de demônios para curar sua irmã e vingar a família massacrada.",
        "One Punch Man": "Um herói ridiculamente forte busca um oponente à altura após se entediar por derrotar todos com apenas um soco.",
        "Bleach": "Um estudante ganha poderes de Ceifador de Almas e precisa proteger os vivos e guiar os mortos para o além.",
        "Fullmetal Alchemist": "Dois irmãos usam a alquimia na tentativa de recuperar seus corpos após um ritual proibido dar errado.",
        "Jujutsu Kaisen": "Um estudante engole um objeto amaldiçoado e entra para uma escola de feiticeiros para combater maldições.",
        "Solo Leveling": "O caçador mais fraco da humanidade ganha uma habilidade única de evoluir de nível como em um jogo.",
        "Hunter X Hunter": "Um garoto decide se tornar um caçador profissional para encontrar seu pai e explorar um mundo repleto de perigos.",
        "Chainsaw Man": "Um jovem garoto faz um pacto com um demônio motosserra e passa a caçar outras criaturas para a segurança pública.",
        "Dragon Ball Z": "Goku e os Guerreiros Z defendem a Terra e o universo contra ameaças alienígenas e vilões extremamente poderosos."
}

romance = {"Kaguya-sama: Love Is War": "Dois gênios do conselho estudantil travam uma batalha mental para forçar o outro a confessar seu amor primeiro.",
    "Toradora!": "Dois estudantes com personalidades opostas se ajudam mutuamente a tentar conquistar os melhores amigos um do outro.",
    "Horimiya": "Duas pessoas com vidas secretas bem diferentes na escola se aproximam e mostram suas verdadeiras identidades.",
    "Your Lie in April": "Um prodígio do piano traumatizado recupera a paixão pela música ao conhecer uma violinista de espírito livre.",
    "Fruits Basket": "Uma garota órfã vai morar com uma família misteriosa cujos membros se transformam nos animais do zodíaco ao serem abraçados.",
    "Clannad": "Um jovem desacreditado da vida encontra uma garota com o sonho de reabrir o clube de teatro e muda sua visão do mundo.",
    "Tomo-chan Is a Girl!": "Uma garota lutadora de tomboy tenta fazer com que seu amigo de infância finalmente a veja como uma garota.",
    "My Dress-Up Darling": "Um jovem artesão de bonecas tradicionais aceita ajudar uma colega popular a confeccionar roupas para cosplay.",
    "Kimi ni Todoke: From Me to You": "Uma garota mal interpretada por sua aparência tímida tenta se conectar com os outros ao se aproximar do garoto mais popular da turma.",
    "A Sign of Affection": "Uma estudante universitária surda descobre novas emoções e horizontes ao se apaixonar por um colega itinerante e poliglota."
}

comedia = {
    "Gintama": "Um samurai com alma de moleque faz bicos num Japão feudal invadido por alienígenas.",
    "Konosuba": "Um jovem morre de forma ridícula e vai parar num mundo de fantasia com uma deusa inútil e uma equipe caótica.",
    "The Disastrous Life of Saiki K.": "Um estudante com poderes psíquicos surreais só quer ter uma vida comum, mas seus colegas bizarras não deixam.",
    "Nichijou": "A rotina absurda e exagerada de estudantes, um robô e um gato falante em uma cidade nada normal.",
    "Great Teacher Onizuka": "Um ex-membro de gangue se torna professor e usa métodos nada convencionais para lidar com alunos difíceis.",
    "Asobi Asobase": "Três garotas formam um clube na escola para passar o tempo com jogos, resultando em situações totalmente insanas.",
    "Grand Blue Dreaming": "Um universitário busca uma vida calma no litoral, mas é arrastado para um clube de mergulho focado em festas loucas.",
    "Colégio Ouran Host Club": "Uma garota humilde quebra um vaso caríssimo e precisa trabalhar disfarçada num clube de acompanhantes elite da escola.",
    "The 100 Girlfriends Who Really, Really, Really, Really, Really Love You": "Um garoto descobre que tem 100 almas gêmeas destinadas a morrer se ele não namorar todas ao mesmo tempo.",
    "Mashle: Magic and Muscles": "Num mundo onde a magia é tudo, um jovem sem poderes decide resolver qualquer feitiço na base do soco e da musculação."
}

suspense = {
    "Death Note": "Um estudante encontra um caderno capaz de matar quem tem o nome escrito nele e entra em um duelo mental contra um detetive gênio.",
    "Monster": "Um neurocirurgião salva a vida de um garoto que cresce para se tornar um psicopata perigoso, levando o médico a caçá-lo.",
    "A Ilha das Sombras": "Um jovem retorna à sua ilha natal para o funeral da amiga de infância e descobre uma conspiração envolvendo sombras assassinas.",
    "Erased": "Um homem com a habilidade involuntária de voltar no tempo é enviado 18 anos ao passado para impedir o assassinato de uma colega de classe.",
    "The Promised Neverland": "Crianças em um orfanato aparente perfeito descobrem a terrível verdade sobre o local e planejam uma fuga ousada.",
    "Psycho-Pass": "Num futuro onde a propensão ao crime é medida por sensores, inspetores caçam cidadãos antes mesmo de cometerem delitos.",
    "Another": "Um aluno novo entra em uma turma marcada por uma maldição mortal e tenta desvendar o segredo para parar as mortes trágicas.",
    "Pluto": "Um detetive robô investiga os assassinatos dos robôs mais avançados do mundo e dos humanos que defendem seus direitos.",
    "Parasyte: The Maxim": "Um jovem faz simbiose com um parasita alienígena no seu braço e juntos lutam contra outros parasitas que devoram humanos.",
    "Serial Experiments Lain": "Uma garota introvertida se conecta a uma rede virtual mundial e a linha entre a realidade e a internet começa a ruir."
}

terror = {
    "Higurashi: When They Cry": "Um jovem se muda para um vilarejo calmo, mas logo descobre um ciclo de assassinatos e paranoia ligado ao festival local.",
    "Corpse Party: Tortured Souls": "Estudantes realizam um ritual de amizade e são transportados para uma escola assombrada em outra dimensão repleta de espíritos vingativos.",
    "Junji Ito Collection": "Coletânea de histórias de horror psicológico e grotesco baseadas nos célebres mangás de Junji Ito.",
    "Devilman Crybaby": "Um jovem sensível se funde com um demônio para combater a invasão das criaturas e salvar a humanidade da ruína.",
    "Yamishibai: Japanese Ghost Stories": "Curtas de terror baseados em lendas urbanas e mitos do folclore japonês contados em estilo teatro de papel.",
    "Dark Gathering": "Um jovem capaz de atrair espíritos ajuda uma garota prodígio que caça fantasmas malignos para resgatar a alma da mãe.",
    "O Verão em que Hikaru Morreu": "Um garoto percebe que seu melhor amigo que voltou da montanha foi substituído por uma entidade sobrenatural idêntica.",
    "Perfect Blue": "Uma ex-ídolo pop tenta a carreira de atriz e começa a perder a noção da realidade enquanto é perseguida por um fã obsessivo.",
    "Shiki": "Uma pequena vila isolada é assolada por mortes misteriosas quando uma família estranha se muda para o topo da colina.",
    "Mononoke": "Um vendedor de remédios itinerante viaja pelo Japão feudal para investigar e exorcizar espíritos malignos que se alimentam de emoções humanas."
}

ficcao = {
    "Cowboy Bebop": "Um grupo variado de caçadores de recompensas viaja pelo espaço a bordo de uma espaçonave tentando fugir dos fantasmas do passado.",
    "Evangelion": "Adolescentes são pilotados para comandar robôs gigantes био-mecânicos na defesa da Terra contra seres misteriosos chamados Anjos.",
    "Code Geass: Lelouch of the Rebellion": "Um príncipe exilado ganha o poder de dar ordens absolutas e lidera uma rebelião contra o império que domina o mundo.",
    "Steins;Gate": "Um grupo de amigos descobre acidentalmente como enviar mensagens de texto para o passado usando um micro-ondas, alterando a linha do tempo.",
    "Ghost in the Shell: Stand Alone Complex": "Uma equipe especial de segurança cibernética investiga crimes tecnológicos e terrorismo num futuro cibernético.",
    "Cyberpunk: Edgerunners": "Um jovem de rua tenta sobreviver em uma metrópole futurista obcecada por tecnologia e modificações corporais se tornando um mercenário.",
    "Tengen Toppa Gurren Lagann": "Dois amigos saem de sua vila subterrânea e lideram a humanidade na luta pela liberdade a bordo de mechas gigantes.",
    "Mobile Suit Gundam": "Conflitos políticos e guerras espaciais travadas por jovens pilotos no comando de armaduras mecânicas móveis.",
    "Ergo Proxy": "Numa cidade domada sob uma domo num planeta pós-apocalíptico, um inspetor investiga assassinatos cometidos por robôs infectados por um vírus.",
    "Planetes": "Uma equipe de coletores de lixo espacial trabalha na órbita da Terra lidando com os perigos do vácuo e os sonhos de explorar o universo."
}

print("Mas antes, vamos ver todo o nosso catálogo.")
print(f"Animes de ação: {acao.keys()}")
print(f"Animes de romance: {romance.keys()}")
print(f"Animes de comédia: {comedia.keys()}")
print(f"Animes de suspense: {suspense.keys()}")
print(f"Animes de terror: {terror.keys()}")
print(f"Animes de ficção: {ficcao.keys()}")

validacao = str(input("Você quer que escolhemos um nome aleatório? (Sim ou não)")).lower().strip()

if validacao == "sim" or validacao == "s":

    while True:
        escolha = str(input("Digite o gênero que quer assistir, e nós vamos dizer um nome aleatório da lista: (Acão, Romance, Comédia, Suspense, Terror, Ficção)")).lower().strip()

        if escolha == "ação" or escolha == "acao" or escolha == "açao" or escolha == "acão":
            anime_para_assistir = random.choice(list(acao.keys()))
            print(f"O anime escolhido foi: {anime_para_assistir}.")
            print(f"Descrição: {acao[anime_para_assistir]}\n")
            break
        elif escolha == "romance":
            anime_para_assistir = random.choice(list(romance.keys()))
            print(f"O anime escolhido foi: {anime_para_assistir}.")
            print(f"Descrição: {romance[anime_para_assistir]}\n")
            break
        elif escolha == "comedia" or escolha == "comédia":
            anime_para_assistir = random.choice(list(comedia.keys()))
            print(f"O anime escolhido foi: {anime_para_assistir}.")
            print(f"Descrição: {comedia[anime_para_assistir]}\n")
            break
        elif escolha == "suspense":
            print("Mas se lembre, esse gênero pode conter animes com conteúdo muito sensível para alguns públicos. Esteja ciente de que o que"
            " for selecionado aqui, talvez não seja muito agradável de se assistir. Obrigado pela compreensão.")
            anime_para_assistir = random.choice(list(suspense.keys()))
            print(f"O anime escolhido foi: {anime_para_assistir}.")
            print(f"Descrição: {suspense[anime_para_assistir]}\n")
            break
        elif escolha == "terror":
            print("Mas se lembre, esse gênero pode conter animes com conteúdo muito sensível para alguns públicos. Esteja ciente de que o que"
                " for selecionado aqui, talvez não seja muito agradável de se assistir. Obrigado pela compreensão.")
            anime_para_assistir = random.choice(list(terror.keys()))
            print(f"O anime escolhido foi: {anime_para_assistir}.")
            print(f"Descrição: {terror[anime_para_assistir]}\n")
            break
        elif escolha == "ficção" or escolha == "ficcao" or escolha == "ficçao" or escolha == "ficcão":
            anime_para_assistir = random.choice(list(ficcao.keys()))
            print(f"O anime escolhido foi: {anime_para_assistir}.")
            print(f"Descrição: {ficcao[anime_para_assistir]}\n")
            break
        else:
            print("Você não digitou um gênero válido de nosso programa. Digite novamente.")
elif validacao == "não" or validacao == "nao" or validacao == "n":
    print("Sem problemas! Então você pode procurar em nosso catálogo um nome que chame sua atenção.")
