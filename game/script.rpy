# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#define narrator = Character(None, kind=nvl)

#define slow_dissolve = Dissolve(1.5)
#define fade = Fade(1.0, 0.5, 0.5)
#define fade_out = Fade(0.5, 0.5, 0.5)
#define dissolve = Dissolve(0.5, 0.5, 0.5)


##bruuu
##########AQUI
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

label start:

    scene bg_paris_morning with fade
    play music "ambiente_paris.ogg" fadein 1.5

    window hide
    pause 1.0
    window show

    "Paris, outubro de 1890. Uma névoa leve cobre a cidade, tornando seus contornos mais suaves, quase como se tudo fosse parte de uma pintura."

    "Você acaba de chegar à capital francesa, trazendo apenas seu caderno de esboços e uma carta misteriosa que menciona o desaparecimento do mestre impressionista Camille Pissarro."

    show protagonista at center with fade

    protagonist "É aqui que começa minha busca. Se Pissarro realmente sumiu, alguém precisa encontrar respostas."

    "Seu primeiro destino é o famoso Café Les Deux Magots, onde dizem que os artistas costumam se reunir."

    jump cena_cafe

label cena_cafe:

    scene bg_cafe_les_deux_magots with fade
    play music "cafe_ambiente.ogg" fadeout 2.0 fadein 1.5    
    pause 1.0

    "O aroma de café fresco, o som das conversas animadas e o tilintar de xícaras criam uma atmosfera viva." with dissolve

    "Ao fundo, você reconhece Claude Monet sentado com outros pintores. Há uma cadeira vazia próxima." with dissolve

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

    monet "Bonjour. Vejo que é novo por aqui. Está procurando alguém?"  with dissolve

    protagonist "Na verdade, sim. Estou atrás de informações sobre Camille Pissarro. Soube que desapareceu."

    monet "Camille..."
    pause
    monet "...não o vejo há dias. A última vez que nos falamos, ele parecia nervoso. Mencionou o nome de um crítico. Rochefort."

    $ pista_rochefort = True

    "Você anota mentalmente o nome. Talvez seja o começo de algo."  with dissolve

    jump menu_monet

label menu_monet:

    menu:
        "Ver pistas coletadas":
            call mostrar_pistas from _call_mostrar_pistas_1
        "Perguntar mais sobre Rochefort":
            jump perguntar_rochefort
        "Observar o café em silêncio agora":
            hide monet with dissolve
            jump observar_cafe
        "Agradecer e sair discretamente":
            hide monet with dissolve
            jump sair_cafe

label observar_cafe:

    "Você observa os artistas e intelectuais se movimentando, discutindo, rindo. Uma conversa ao fundo chama sua atenção."

    "Dois pintores falam sobre uma galeria que recusou uma obra de Pissarro dias antes do sumiço."

    $ pista_galeria = True

    "Você faz uma anotação mental para visitar essa galeria."

    jump menu_monet #falar_com_monet #jump cena_cafe #jump sair_cafe

label perguntar_rochefort:

    monet "Um crítico influente... e cruel. Disse que os trabalhos recentes de Pissarro estavam decadentes. Camille ficou devastado."  with dissolve

    monet "Se alguém o empurrou para o silêncio, foi aquele homem."  with dissolve
    
    pause 1.0

    jump menu_monet #falar_com_monet #jump sair_cafe

label sair_cafe:

    scene bg_rua_com_nevoa with fade
    play music "cafe_ambiente2.ogg" fadeout 2.0 fadein 1.5
    #stop music fadeout 2.0
    if pista_rochefort:
        "Você sai do café com mais perguntas do que respostas... mas agora com um nome: Rochefort."
        jump cena_atelier  # Monet mencionou Rochefort → leva ao ateliê

    elif pista_galeria:
        "Você sai do café intrigado com a conversa sobre a galeria que recusou a obra de Pissarro."
        jump cena_galeria  # observação da conversa → leva à galeria

    else:
        "Você sai do café com uma sensação estranha — algo escapou por entre seus dedos."
        jump cena_atelier  # fallback padrão (pode ser ajustado)

#    "Você sai do café com mais perguntas do que respostas... mas agora com um nome: Rochefort."

#    jump cena_atelier

label cena_atelier:

    scene bg_atelier_pissarro with dissolve
    play music "atelier_silencio.ogg" fadeout 2.0 fadein 1.5    
    pause 1.0

    "O ateliê de Camille Pissarro está silencioso. A luz suave da manhã atravessa as janelas altas, iluminando telas inacabadas e pincéis manchados de tinta." with dissolve

    show cezanne at right with moveinright  

    "Você vê Paul Cézanne observando uma das obras de Pissarro. Ele parece perdido em pensamentos."

    protagonist "Paul Cézanne?"

    cezanne "Hm? Ah... você deve ser mais um dos curiosos. Está atrás de Camille também?"

    protagonist "Sim. Vim porque me disseram que ele desapareceu. E que você talvez soubesse de algo."

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

    "Você anota essa descrição. Talvez essa obra esteja escondida em algum lugar."
    $ pista_obra_despedida = True

    jump vasculhar_atelier

label vasculhar_atelier:

    "Você caminha pelo ateliê. Entre pincéis, esboços e cartas, encontra um envelope com uma anotação estranha: 'Jardins ao entardecer. Lá tudo será revelado.'"

    $ pista_jardim = True

    cezanne "Se ele for a algum lugar, será lá. O Jardim das Tulherias sempre foi onde ele pintava quando queria desaparecer do mundo."

    jump decidir_proxima_acao

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
                "Visitar a galeria que recusou a obra de Pissarro":
                    jump cena_galeria
        else:
            menu:
                "Ver pistas coletadas":
                    call mostrar_pistas from _call_mostrar_pistas_4
                "Ir ao Jardim das Tulherias":
                    jump cena_jardim
    # menu:
    #     "Ver pistas coletadas":
    #         call mostrar_pistas
    #     "Ir ao Jardim das Tulherias":
    #         jump cena_jardim

    #     "Visitar a galeria que recusou a obra de Pissarro":
    #         jump cena_galeria

label cena_jardim:

    scene bg_jardim_tulherias_entardecer with dissolve
    play music "jardim_suave.ogg"

    "O sol começa a se pôr quando você chega ao Jardim das Tulherias. A luz dourada da tarde pinta as folhas com tons de fogo."

    "Você anda entre as estátuas e árvores silenciosas, até encontrar uma paleta de tintas parcialmente enterrada próxima a um banco."

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

    "Você encontra um pedaço de tela rasgada com pinceladas familiares e um bilhete escondido entre as raízes de uma árvore próxima."

    "Bilhete: 'A luz muda tudo. Não confie no que dizem.'"

    $ pista_bilhete_jardim = True

    "Enquanto lê, você ouve passos ao longe..."

    jump final_confronto

label esperar_jardim:

    "Você decide sentar e aguardar. O céu escurece aos poucos, e nada acontece. Apenas o vento e o farfalhar das árvores."

    "Após algum tempo, percebe uma figura distante desaparecendo entre as sombras. Era tarde demais."

    jump final_neutro

label final_confronto:

    scene bg_jardim_noite with fade
    play music "tensao_final.ogg" fadeout 2.0 fadein 1.5


    "Uma figura surge da escuridão — o crítico Rochefort. Ele está tenso, visivelmente abalado." with dissolve

    show rochefort at right with moveinright
    show protagonista at left with dissolve

    rochefort "Você... não devia estar aqui. Isso não é da sua conta."

    if pista_rochefort:
        menu:
            "Ver pistas coletadas":
                call mostrar_pistas from _call_mostrar_pistas_6
            "Confrontar Rochefort com as provas":
                jump final_bom

            "Tentar convencê-lo a contar a verdade":
                jump final_medio

    else:
        "Você não reconhece o homem, mas sua presença te perturba."

        menu:
            "Ver pistas coletadas":
                call mostrar_pistas from _call_mostrar_pistas_7
            "Pedir explicações ao desconhecido":
                jump final_medio

label final_bom:

    scene bg_jardim_noite with fade
    play music "epilogo_reflexivo.ogg" fadeout 2.0 fadein 1.5

    "Você apresenta todas as pistas. Rochefort, pressionado, confessa: manipulou a crítica para destruir a reputação de Pissarro."

    "Mas Camille escapou. Fingiu seu desaparecimento e está agora escondido, pintando sua obra final."

    scene bg_atelier_pissarro with fade
    show pissarro at center

    "Dias depois, você recebe um convite secreto. Ao chegar ao ateliê, encontra Camille Pissarro em silêncio, diante de uma tela imensa, pincel na mão."

    pissarro "Você seguiu os sinais. Não esperava por isso."

    protagonist "A arte merece ser protegida. Mesmo da própria sociedade."

    pissarro "Então entenderá por que tudo isso foi necessário."

    "Camille sorri, volta-se para a tela e continua a pintar. Você sai do ateliê com a certeza de que a verdade, às vezes, deve permanecer entre artistas."

    scene black with fade
    centered "Fim — O Guardião da Verdade"
    return

#"Você apresenta todas as pistas. Rochefort, pressionado, confessa: manipulou a crítica para destruir a reputação de Pissarro."

# "Mas Camille escapou. Fingiu seu desaparecimento e está agora escondido, pintando sua obra final."

#"Você decide manter o segredo — a arte precisa de silêncio, às vezes."

#  scene black with fade
# centered "Fim — O Guardião da Verdade"
#return

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

    "Você permaneceu em silêncio, e assim também a verdade."
    "O tempo passou e Camille nunca apareceu."

    scene black with fade
    centered "Fim — O Eco da Ausência"
    return

label final_medio:

    "Rochefort hesita, mas foge sem revelar tudo. Você leva as pistas à polícia, que arquiva o caso por falta de provas."

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

    marie "Ah, você deve ser o investigador de quem ouvi falar. Está aqui por causa de Pissarro, não é?"

    protagonist "Sim. Vim saber sobre a obra dele que foi recusada aqui."

    marie "Uma tela... ousada demais para os padrões da crítica atual. Camille parecia frustrado. Disse que era sua melhor pintura."

    menu:
        "Ver pistas coletadas":
            call mostrar_pistas from _call_mostrar_pistas_8
        "Perguntar sobre a tela recusada":
            jump perguntar_tela

        "Investigar a sala de exposições":
            jump investigar_sala

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
