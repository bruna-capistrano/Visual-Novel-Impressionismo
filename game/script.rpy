# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define protagonist = Character("Você")
define monet = Character("Monet")
define cezanne = Character("Cézanne")
define marie = Character("Marie")
define rochefort = Character("Rochefort")
define pissarro = Character("Pissarro")

default pista_rochefort = False
default pista_galeria = False
default pista_obra_despedida = False
default pista_jardim = False
default pista_presenca_pissarro = False
default pista_bilhete_jardim = False
default pista_envelope_galeria = False
default pista_quadro_oculto = False
default pista_rochefort2 = False


label start:

    scene bg_paris_morning with fade
    play music "ambiente_paris.ogg" fadein 1.5

    window hide
    pause 1.0
    window show

    "Paris, outubro de 1890. Uma névoa leve cobre a cidade como um véu translúcido, dissolvendo os contornos das ruas e edifícios, suavizando as formas até que pareçam traços borrados de uma aquarela recém-pintada."

    "O ar frio e úmido roça a pele do rosto como seda gelada, trazendo consigo o aroma levemente adocicado das castanhas assadas vendidas nas esquinas."

    "Ao longe, ouvem-se o tilintar de sinos de bicicleta, o ranger das rodas das charretes sobre o empedrado e o murmúrio arrastado de conversas abafadas pelos cachecóis."

    "Há um gosto quase mineral no ar, como se a cidade respirasse pelas grades de seus bueiros fumegantes."

    show protagonista at center with fade

    "Você, Louise Michel, exilada e sobrevivente da Comuna de Paris, retorna discretamente a Paris."
    "Agora dedicada às artes e às ideias, uma carta misteriosa sobre o desaparecimento de Camille Pissarro a leva de volta aos bastidores de uma cidade que ainda guarda feridas — e segredos."

    protagonist "É aqui que começa minha busca. Se Pissarro realmente sumiu, alguém precisa encontrar respostas."

    "Seu primeiro destino é o famoso Café Les Deux Magots. À medida que se aproxima, o aroma quente e adocicado do café recém-passado mistura-se ao leve perfume de charutos franceses."
    scene bg_frente_cafe with fade
    show protagonista at left with moveinleft
    "A fachada elegante, com toldos verde-musgo e letreiros dourados, reluz suavemente sob a neblina da manhã."

    "Pelas janelas embaçadas, você distingue vultos animados gesticulando, pincéis nas mãos e bocas entreabertas em discussões acaloradas sobre arte."
    
    "O tilintar de xícaras de porcelana se mistura ao murmúrio constante de vozes — uma sinfonia boêmia que parece aquecer o ar úmido de Paris."

    "É neste lugar, dizem os moradores, que os artistas se reúnem para compartilhar ideias, rascunhos e sonhos — como se cada mesa guardasse os esboços de um novo movimento."


    jump cena_cafe

label cena_cafe:

    scene bg_cafe_les_deux_magots with fade
    play music "cafe_ambiente.ogg" fadeout 2.0 fadein 1.5    
    pause 1.0

    "O aroma encorpado do café fresco envolve o ambiente como um convite caloroso logo à entrada." with dissolve

    "O som das conversas animadas — risos leves, frases entrecortadas por entusiasmo e sotaques diversos — preenche o ar como uma melodia espontânea." with dissolve

    "Entre uma palavra e outra, o tilintar ritmado das xícaras de porcelana contra os pires ecoa como pequenos acentos musicais." with dissolve

    "Tudo isso cria uma atmosfera viva e pulsante, onde cada detalhe parece respirar a energia criativa daquele lugar." with dissolve


    "Ao fundo, você reconhece Claude Monet, envolto por uma névoa tênue de fumaça de cigarro, gesticulando com vivacidade enquanto conversa com outros pintores." with dissolve

    "Seus olhos brilham sob a luz suave que entra pelas janelas do café, refletindo a intensidade de quem enxerga o mundo em cores que poucos conseguem captar." with dissolve

    "Uma cadeira vazia ao lado do grupo parece quase lhe esperar, como se aquele pequeno espaço carregasse o convite silencioso para entrar em um universo de ideias, telas e pigmentos." with dissolve

    
    jump menu_cafe

label menu_cafe:
    while True:
        menu:
            "Ver pistas coletadas":
                call mostrar_pistas from _call_mostrar_pistas
            "Aproximar-se de Monet e cumprimentá-lo" if not pista_rochefort:
                jump falar_com_monet
            "Observar o café em silêncio primeiro" if not pista_galeria:
                jump observar_cafe
            
            "Sair do café":
                jump sair_cafe

label falar_com_monet:

    show monet at left with moveinleft

    "Monet, com um sorriso tranquilo, ajeita o chapéu enquanto observa seu entorno. Ao notar sua presença, ele se volta para você e diz:"

    monet "Bonjour. Vejo que é nova por aqui. Está procurando alguém?"  with dissolve

    show protagonista inverso at right with moveinright

    protagonist "Na verdade, sim. Estou atrás de informações sobre Camille Pissarro. Soube que desapareceu."

    "O pintor, então, faz uma pausa, franzindo levemente a testa."

    monet "Camille..."
    pause
    
    "Monet olha para o horizonte, com olhar paralisado e com ar pensativo, como se tentasse resgatar uma memoria desimportante."
    monet "...não o vejo há dias. A última vez que nos falamos, ele parecia nervoso. Mencionou o nome de um crítico. Rochefort."

    $ pista_rochefort = True

    "Você anota mentalmente o nome. Talvez seja o começo de algo."  with dissolve

    jump menu_monet

label menu_monet:

    menu:
        "Ver pistas coletadas":
            call mostrar_pistas from _call_mostrar_pistas_1
        "Perguntar mais sobre Rochefort" if not pista_rochefort2:
            jump perguntar_rochefort
        "Observar o café em silêncio agora" if not pista_galeria:
            hide monet with dissolve
            jump observar_cafe
        "Agradecer e sair discretamente":
            hide monet with dissolve
            jump sair_cafe

label observar_cafe:

    "Você observa os artistas e intelectuais se movimentando pelo salão, suas vozes se misturando em risos e discussões animadas."

    "Ao longe, uma conversa chama sua atenção: dois pintores comentam com preocupação sobre uma galeria que rejeitou uma obra de Pissarro poucos dias antes do seu desaparecimento."

    $ pista_galeria = True

    "Você faz uma anotação mental para visitar essa galeria."

    if pista_rochefort:
        jump menu_monet  # Já falou com Monet, então pode voltar ao menu dele
    else:
        jump menu_cafe  # Ainda não falou com Monet — volta ao menu geral do café

label perguntar_rochefort:

    "O pintor olha para você e, com expressão séria, diz:"
    
    monet "Um crítico influente... e cruel. Disse que os trabalhos recentes de Pissarro estavam decadentes. Camille ficou devastado."  with dissolve
    
    "Neste momento, seu olhar fica distante, ele continua a conversa, mas baixa o tom de voz, quase sussurrando"

    monet "Se alguém o empurrou para o silêncio, foi aquele homem."  with dissolve
    
    $ pista_rochefort2 = True

    pause 1.0

    jump menu_monet 

label sair_cafe:

    scene bg_rua_com_nevoa with fade
    play music "cafe_ambiente2.ogg" fadeout 2.0 fadein 1.5

    jump cena_duvida
    # Monet mencionou Rochefort → leva ao ateliê

    # observação da conversa → leva à galeria

label cena_duvida:

    scene bg_rua_com_nevoa
    play music "descoberta_suave.ogg" fadein 1.5
    show protagonista at left with moveinleft

    "Você caminha pelas ruas enevoadas de Paris. As luzes douradas dos lampiões tremeluzem através da névoa espessa, lançando sombras dançantes sobre a calçada irregular de paralelepípedos."

    "O som abafado de cascos de cavalos e rodas de carruagens ecoa entre os prédios de pedra, misturando-se aos murmúrios distantes de conversas em cafés."

    "O frio úmido penetra pelas suas roupas, e o cheiro de carvão queimado se mistura ao aroma de pão recém-saído do forno vindo de uma padaria próxima."

    "Há um leve gosto metálico no ar, talvez da neblina carregada ou das lembranças que pesam na boca do estômago."

    "Apesar das pistas obtidas, algo em você hesita. E se tudo isso não passar de uma paranoia? Uma viagem sem volta?"

    protagonist "Camille era excêntrico, mas... desaparecer assim?"

    "Você para na calçada, sentindo o vento fresco brincar com as folhas ao redor."

    "De repente, o canto do seu caderno de notas se levanta com uma brisa súbita. Um pedaço de papel escorrega para o chão — um bilhete, parte da carta original."

    "Você pega o bilhete que caiu e lê as palavras cuidadosamente escritas: 'Só quem busca a verdade com a alma inteira pode vê-la sob a névoa.'"

    "Fecha os olhos por um instante, sentindo o peso da mensagem. Ao abrir, uma determinação silenciosa cresce dentro de você — sabe que precisa continuar."

    if pista_rochefort:
        jump cena_atelier
    elif pista_galeria:
        jump cena_galeria
    else:
        jump final_neutro

label proximo_destino:

    if pista_rochefort:
        jump cena_atelier
    elif pista_galeria:
        jump cena_galeria
    else:
        jump cena_atelier

label cena_atelier:

    scene bg_atelier_pissarro with dissolve
    play music "atelier_silencio.ogg" fadeout 2.0 fadein 1.5    
    pause 1.0

    "O ateliê de Camille Pissarro está silencioso. A luz suave da manhã atravessa as janelas altas, iluminando telas inacabadas e pincéis manchados de tinta com um brilho tranquilo." with dissolve

    show cezanne at right with moveinright  

    "Você vê Paul Cézanne parado diante de uma das obras de Pissarro. Seu olhar está distante, como se mergulhado em pensamentos profundos."

    show protagonista at left with moveinleft
    protagonist "Paul..."

    cezanne "Louise?"

    "Ele se vira, surpreso, mas com um sorriso contido nos lábios."

    cezanne "Nunca imaginei te ver por aqui novamente. Não depois de tudo..."

    protagonist "O desaparecimento de Camille me trouxe de volta. Alguém precisava vir. E você... parece saber mais do que deixa transparecer."

    cezanne "Ele confiava em mim. Em você também, embora nunca admitisse — dizia que sua visão era mais nítida do que a de qualquer crítico."

    protagonist "E mesmo assim, se foi em silêncio."

    cezanne "Ele estava... perturbado. Falava de uma obra que ninguém jamais poderia ver. Uma despedida."

    menu:
        "Ver pistas coletadas":
            call mostrar_pistas from _call_mostrar_pistas_2
        
        "Perguntar sobre essa obra de despedida":
            jump obra_despedida

        "Pedir para olhar o ateliê":
            jump vasculhar_atelier

label obra_despedida:

    cezanne "Era algo diferente. Abstrato, quase invisível. Ele dizia que só quem entendesse a luz verdadeira poderia decifrá-lo."

    "Você anota essa descrição, sentindo que talvez essa obra esteja escondida em algum lugar, esperando para ser encontrada."
    $ pista_obra_despedida = True

    jump vasculhar_atelier

label vasculhar_atelier:

    "Você caminha pelo ateliê silencioso. Entre pincéis espalhados, esboços amarelados e cartas antigas, seus olhos se fixam em um envelope esquecido. Na capa, uma anotação intrigante:
'Jardins ao entardecer. Lá tudo será revelado.'"

    $ pista_jardim = True

    cezanne "Se ele for a algum lugar, será lá. O Jardim das Tulherias sempre foi onde ele pintava quando queria desaparecer do mundo."

    jump reflexao_atelier 

label decidir_proxima_acao:

    scene bg_rua_com_nevoa with fade
    stop music fadeout 2.0

    "Com novas pistas em mãos, você precisa decidir seu próximo passo."
    while True:
        
        if pista_galeria:
            menu:
                "Ver pistas coletadas":
                    call mostrar_pistas from _call_mostrar_pistas_3
                "Ir ao Jardim das Tulherias":
                    jump cena_jardim
                "Visitar a galeria que recusou a obra de Pissarro" if not pista_envelope_galeria:
                    jump cena_galeria
        else:
            menu:
                "Ver pistas coletadas":
                    call mostrar_pistas from _call_mostrar_pistas_4
                "Ir ao Jardim das Tulherias":
                    jump cena_jardim

label reflexao_atelier:

    scene bg_atelier_pissarro 
    play music "descoberta_suave.ogg" fadeout 2.0 fadein 1.5

    show protagonista at left      

    "Você para diante de uma pintura inacabada no canto mais escuro do ateliê. Os traços saltam aos seus olhos — familiares, mas com algo diferente."

    "As cores parecem mais densas, quase vibrando na luz fraca; as pinceladas, ásperas e rápidas, parecem quase sussurrar um chamado urgente."

    "Você sente um peso silencioso no ar, uma mistura estranha de pressa e calma que toca sua pele como uma brisa fria."

    protagonist "Essa... não é uma paisagem. É um grito contido."

    "No canto inferior da tela, há uma anotação rabiscada:"

    "\"A arte não suplica por aplauso. Ela exige coragem.\""

    "Você sente um arrepio. Essa não é mais uma investigação — é um chamado pessoal."

    $ pista_obra_despedida = True

    "Com olhos mais atentos e alma inquieta, você guarda o caderno de notas. Está pronta para o que vier."

    jump decidir_proxima_acao

label cena_jardim:

    scene bg_jardim_tulherias_entardecer with dissolve
    play music "jardim_suave.ogg" fadeout 2.0 fadein 1.5
    show protagonista at left with moveinleft

    "O sol começa a se pôr quando você chega ao Jardim das Tulherias. A luz dourada da tarde envolve as folhas, tingindo-as com tons quentes de fogo."

    "Você caminha lentamente entre as estátuas silenciosas e as árvores, sentindo o chão firme sob os pés."

    "Então, perto de um banco, algo chama sua atenção: uma paleta de tintas meio enterrada na terra, as cores ainda vibrantes sob a luz suave." 

    $ pista_presenca_pissarro = True

    "A paleta tem as iniciais C.P. gravadas discretamente em madeira."

    menu:
        "Ver pistas coletadas":
            call mostrar_pistas from _call_mostrar_pistas_5
        "Vasculhar mais ao redor":
            jump explorar_jardim

        "Sentar no banco e esperar":
            jump esperar_jardim

label explorar_jardim:

    "Você encontra, entre as raízes de uma árvore próxima, um pedaço de tela rasgada com pinceladas familiares, ainda vibrantes sob a luz tênue."

    "Escondido ao lado, um bilhete amarelado chama sua atenção: 'A luz muda tudo. Não confie no que dizem.'"

    $ pista_bilhete_jardim = True

    "Enquanto lê, você percebe passos distantes se aproximando, ecoando pelo jardim."
    "Mas, por um instante, tudo silencia ao seu redor — o ar parece parar, e uma sensação estranha percorre sua pele, como se algo estivesse prestes a acontecer."

    scene bg_jardim_miragem with fade
    play music "atelier_silencio.ogg" fadeout 2.0 fadein 1.5

    "A luz da lua atravessa as copas das árvores, formando uma clareira difusa à sua frente."

    "Ali, entre sombras e folhas, uma figura parece se formar por instantes... não é real, mas também não é apenas imaginação."
    show pissarro miragem at right with dissolve 
    "Camille Pissarro — ou algo como a memória dele — está de pé diante de uma tela invisível, pintando com gestos lentos e etéreos."

    protagonist "Isso é... impossível."

    "Pissarro ergue o olhar e, sem falar, apenas sorri. Ele aponta para o bilhete em sua mão."

    "Você ouve sua própria voz em pensamento:"

    show protagonista at left with dissolve

    protagonist "A luz muda tudo. Não confie no que dizem..."

    "A figura se desfaz com o vento. A brisa agora é fria. E os passos voltam, firmes, reais, determinados."

    $ pista_bilhete_jardim = True

    "Você se levanta. Algo está vindo — e agora, você está pronta."

    jump final_confronto

label esperar_jardim:

    "Você decide sentar e aguardar. O céu escurece lentamente, tingindo tudo de um azul profundo. Nada acontece — apenas o sussurrar do vento e o farfalhar das folhas ao seu redor."

    "Depois de um tempo, uma figura distante surge entre as sombras, movendo-se rapidamente. Antes que você possa reagir, ela desaparece. Era tarde demais."

    jump final_neutro

label final_confronto:

    scene bg_jardim_noite with fade
    play music "tensao_final.ogg" fadeout 2.0 fadein 1.5


    "Uma figura surge da escuridão — o crítico Rochefort. Ele está tenso, visivelmente abalado." with dissolve

    show rochefort at right with moveinright
    show protagonista at left with dissolve

    rochefort "Louise...? Você aqui?"
    rochefort "Nunca imaginei que nos encontraríamos novamente... e muito menos sob essa névoa."
    rochefort "Você não devia estar aqui. Isso não lhe diz respeito."

    if pista_rochefort:
        protagonist "Você sabia que eu viria. Você sabia que, se alguém pudesse seguir os rastros deixados por Camille, seria eu."

        protagonist "E agora você está encurralado. Todas as pistas apontam para você, Rochefort."

        menu:
            "Ver pistas coletadas":
                call mostrar_pistas from _call_mostrar_pistas_6
            "Confrontar Rochefort com as provas":
                jump final_bom

            "Tentar convencê-lo a contar a verdade":
                jump final_medio

    else:
        "Você encara o homem à sua frente, algo nele provoca memórias desconfortáveis."

        rochefort "Não esperava vê-la outra vez, Louise. Muito menos aqui, neste jardim."

        menu:
            "Ver pistas coletadas":
                call mostrar_pistas from _call_mostrar_pistas_7
            "Pedir explicações ao desconhecido":
                jump final_medio

label final_bom:

    scene bg_jardim_noite with fade
    play music "tensao_final.ogg" fadeout 2.0 fadein 1.5
    show rochefort at right 
    show protagonista at left 

    "Você encara Rochefort com firmeza, revelando todas as pistas. Ele hesita, depois suspira."

    rochefort "Louise... nunca imaginei que seria você. Sempre tão idealista. Mas sempre tão... perspicaz."

    "Ele confessa que manipulou a crítica, não apenas por vaidade, mas por convicção de que Pissarro colocava em risco os fundamentos da arte — e, talvez, da sociedade."

    rochefort "Camille fugiu. Fingiu o desaparecimento para escapar da pressão e terminar sua obra. Mas nunca esperei que fosse você a encontrá-lo."

    scene bg_atelier_pissarro with fade
    play music "epilogo_feliz.ogg" fadeout 2.0 fadein 1.5
    show pissarro at center with dissolve

    "Dias depois, você recebe uma carta em papel grosso. Sem assinatura. Só um endereço. No ateliê silencioso, encontra Pissarro, mais velho, mais contido."
    
    show protagonista at left 
    
    pissarro "Louise Michel... se soubesse que era você, teria deixado outro caminho."
    
    
    protagonist "Camille... por que esconder tudo?"

    pissarro "A arte é meu protesto agora. Mas não esperava que alguém como você — alguém que lutou com armas — viesse atrás de pincéis e sombras."
 
    "Você observa a obra em silêncio. Não é só pintura. É memória, é manifesto, é confissão."

    protagonist "A arte merece ser protegida. Mesmo da própria sociedade."

    pissarro "Então entenderá por que tudo isso foi necessário."

    show protagonista at left 
    "Você observa a obra em silêncio. Agora, cabe a você decidir o destino dessa verdade."

    menu:
        "Revelar a verdade ao mundo":
            jump final_revelado

        "Proteger o segredo de Pissarro":
            jump final_guardado
label final_revelado:

    scene bg_exposicao_final with fade
    play music "epilogo_reflexivo1.ogg" fadeout 2.0 fadein 1.5

    "Você decide que o mundo precisa conhecer a última obra de Pissarro — não apenas como arte, mas como um grito silencioso contra o esquecimento."

    "A notícia explode em Paris. O reaparecimento do mestre é manchete. A obra é exposta em uma galeria neutra, longe das críticas venenosas de Rochefort."

    "Pissarro, surpreso, observa a multidão dividir-se entre veneração e escárnio. Mas você sabe que era necessário."

    "Você — Louise Michel — que já havia acendido revoluções com palavras e pólvora, agora reacende com luz e cor uma nova forma de resistência."
    
    "Pissarro, relutante, aceita a nova fama. Você é lembrado como o responsável por trazer à luz um dos maiores enigmas da arte moderna."

    scene black with fade
    centered "Fim — A Luz da Verdade"
    return


label final_guardado:

    scene bg_atelier_final with fade
    play music "epilogo_reflexivo1.ogg" fadeout 2.0 fadein 1.5

    "Camille sorri, volta-se para a tela e continua a pintar, como se o peso da verdade recém-compartilhada se dissolvesse em cor e luz."

    show protagonista at left with dissolve
    "Você observa em silêncio. A paleta de Pissarro agora parece mais viva — como se cada pincelada carregasse não apenas pigmento, mas também memória e resistência."

    "— Guardar um segredo, por vezes, é também um ato de luta — você diz, rompendo o silêncio com a voz firme de quem conheceu o cárcere e a revolução."

    "Camille assente, sem desviar os olhos da tela."

    "Você sai do ateliê com a convicção de que nem todas as verdades precisam ser ditas para transformarem o mundo. Algumas apenas precisam sobreviver."


    scene black with fade
    centered "Fim — O Guardião da Verdade"
    return

label mostrar_pistas:

    $ pistas = []
    if pista_rochefort:
        $ pistas.append("Nome do crítico: Rochefort")
    if pista_galeria:
        $ pistas.append("Galeria recusou obra de Pissarro")
    if pista_obra_despedida:
        $ pistas.append("Pissarro mencionou uma obra de despedida")
    if pista_jardim:
        $ pistas.append("Mensagem indicando os Jardins ao entardecer")
    if pista_presenca_pissarro:
        $ pistas.append("Paleta com iniciais C.P. encontrada")
    if pista_bilhete_jardim:
        $ pistas.append("Bilhete misterioso sobre a verdade e a luz")
    if pista_envelope_galeria:
        $ pistas.append("Envelope lacrado deixado na galeria")
    if pista_quadro_oculto:
        $ pistas.append("Tela escondida na galeria com mensagem enigmática")

    if pistas:
        "Pistas coletadas até agora:"

        python:
            for item in pistas:
                renpy.say(None, "- " + item)
    else:
        "Você ainda não encontrou nenhuma pista."

    menu:
        "Voltar":
            return

label final_neutro:

    scene bg_jardim_noite with fade
    play music "epilogo_reflexivo.ogg" fadeout 2.0 fadein 1.5
    show protagonista at left with moveinleft

    "Você permaneceu em silêncio, e assim também a verdade."
    "O tempo passou e Camille nunca apareceu."

    scene black with fade
    centered "Fim — O Eco da Ausência"
    return

label final_medio:

    play music "descoberta_intensa.ogg" fadeout 2.0 fadein 1.5
    show protagonista at left with moveinleft
    
    "Rochefort hesita ao ver você — há algo no seu olhar que o faz recuar."
    
    show rochefort at right with moveinright
    
    rochefort "Michel... jamais esperei vê-la aqui. Ainda causando problemas, como sempre."

    "Antes que você possa responder, ele desaparece pelas sombras da noite, levando seus segredos consigo."

    "Você reúne as pistas e procura as autoridades. Mas ao ouvir seu nome, os sussurros começam. Murmúrios sobre anarquistas, a Comuna, velhos fantasmas."

    "Nada é investigado. Nada é resolvido."

    "Camille continua desaparecido. A cidade esquece. Mas você não."

    scene black with fade
    centered "Fim — O Silêncio de Paris"
    return

label cena_galeria:

    scene bg_galeria_arte with dissolve
    play music "galeria_ambiente.ogg" fadeout 2.0 fadein 1.5

    "A galeria é silenciosa, quase solene. Obras de arte alinhadas nas paredes observam em silêncio sua entrada." with dissolve

    "Marie, a curadora da galeria, está organizando alguns papéis atrás de uma pequena mesa. Ela ergue os olhos ao ver você."

    show marie at right with moveinright
    show protagonista at left with dissolve

    marie "Ah, você deve ser Louise, ouvi falar de você pela cidade. Está aqui por causa de Pissarro, não é?"

    protagonist "Sim. Vim saber sobre a obra dele que foi recusada aqui."

    marie "Uma tela... ousada demais para os padrões da crítica atual. Camille parecia frustrado. Disse que era sua melhor pintura."

    pause 0.5

    "Marie parece hesitar, como se medisse suas palavras."

    menu:
        "Ver pistas coletadas":
            call mostrar_pistas from _call_mostrar_pistas_8
        "Questionar o motivo da recusa da galeria":
            jump duvidar_marie
        "Pedir informações sobre a obra de forma neutra":
            jump perguntar_tela
        "Olhar a sala de exposições":
            jump investigar_sala

label duvidar_marie:
    play music "descoberta_suave.ogg" fadeout 2.0 fadein 1.5
    show marie at right with moveinright
    show protagonista at left with dissolve

    protagonist "Marie... não entendo. Se era a melhor pintura dele, por que foi rejeitada?"

    marie "A crítica... é cega ao que desafia."

    "Ela olha para o chão por um momento, depois se recompõe."

    marie "Mas talvez nem todos aqui concordaram com a decisão. Talvez alguns tentaram proteger Camille do próprio sistema que o destruiu."

    "Você sente um calafrio — é possível que Marie tenha mais envolvimento do que diz."

    $ pista_envelope_galeria = True

    "Ainda assim, ela entrega um envelope selado com as iniciais 'C.P.'."

    protagonist "Obrigada, Marie. Isso pode ser importante."

    jump decidir_proxima_acao

label perguntar_tela:

    marie "A pintura foi devolvida a ele. Mas antes disso, Camille pediu que eu escondesse algo nos arquivos da galeria."

    marie "Ele disse que se algo lhe acontecesse, aquilo deveria ser entregue a quem fosse digno."

    "Marie entrega um envelope selado com as iniciais 'C.P.'."

    $ pista_envelope_galeria = True

    protagonist "Obrigada, Marie. Isso pode ser importante."

    jump decidir_proxima_acao

label investigar_sala:

    "Você caminha lentamente pela galeria. Em uma sala secundária, encontra um quadro coberto por um pano."

    "Ao retirá-lo, revela uma obra intensa, com cores e formas distorcidas. No canto inferior, a assinatura de Camille Pissarro."

    "Uma frase está escrita na borda da moldura: 'A verdade não se pinta com luz. Se revela com sombra.'"

    $ pista_quadro_oculto = True

    "Você anota o conteúdo e cobre a obra novamente."

    jump decidir_proxima_acao
