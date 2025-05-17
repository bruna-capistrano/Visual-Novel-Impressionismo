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
        "Perguntar mais sobre Rochefort" if not pista_rochefort2:
            jump perguntar_rochefort
        "Observar o café em silêncio agora" if not pista_galeria:
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

    if pista_rochefort:
        jump menu_monet  # Já falou com Monet, então pode voltar ao menu dele
    else:
        jump menu_cafe  # Ainda não falou com Monet — volta ao menu geral do café

label perguntar_rochefort:

    monet "Um crítico influente... e cruel. Disse que os trabalhos recentes de Pissarro estavam decadentes. Camille ficou devastado."  with dissolve

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

    scene bg_rua_com_nevoa with fade
    play music "descoberta_suave.ogg" fadein 1.5
    show protagonista at left with moveinleft

    "Você caminha pelas ruas enevoadas de Paris, com o som abafado de carruagens e passos ao fundo."

    "Apesar das pistas obtidas, algo em você hesita. E se tudo isso não passar de uma paranoia? Uma viagem sem volta?"

    protagonist "Camille era excêntrico, mas... desaparecer assim?"

    "Você para na calçada. O vento levanta o canto do seu caderno de esboços. Dentro, um bilhete cai — era parte da carta original."

    "Bilhete: 'Só quem busca a verdade com a alma inteira pode vê-la sob a névoa.'"

    "Você fecha os olhos por um instante. Quando os abre, sente que precisa continuar."
    if pista_rochefort:
        jump cena_atelier
    elif pista_galeria:
        jump cena_galeria
    else:
        jump cena_atelier

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

    "O ateliê de Camille Pissarro está silencioso. A luz suave da manhã atravessa as janelas altas, iluminando telas inacabadas e pincéis manchados de tinta." with dissolve

    show cezanne at right with moveinright  

    "Você vê Paul Cézanne observando uma das obras de Pissarro. Ele parece perdido em pensamentos."

    show protagonista at left with moveinleft
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
                "Visitar a galeria que recusou a obra de Pissarro":
                    jump cena_galeria
        else:
            menu:
                "Ver pistas coletadas":
                    call mostrar_pistas from _call_mostrar_pistas_4
                "Ir ao Jardim das Tulherias":
                    jump cena_jardim

label reflexao_atelier:

    scene bg_atelier_pissarro with fade
    play music "descoberta_suave.ogg" fadeout 2.0 fadein 1.5

    show protagonista at left with moveinleft     

    "Você se detém diante de uma pintura inacabada encostada no canto mais escuro do ateliê."

    "Ao se aproximar, reconhece traços familiares... mas há algo diferente."

    "Cores mais densas, pinceladas mais bruscas. A tela parece pulsar com urgência e silêncio ao mesmo tempo."

    protagonist "Essa... não é uma paisagem. É um grito contido."

    "No canto inferior da tela, há uma anotação rabiscada:"

    "\"A arte não suplica por aplauso. Ela exige coragem.\""

    "Você sente um arrepio. Essa não é mais uma investigação — é um chamado pessoal."

    $ pista_obra_despedida = True

    "Com olhos mais atentos e alma inquieta, você guarda o caderno de esboços. Está pronto para o que vier."

    jump decidir_proxima_acao

label cena_jardim:

    scene bg_jardim_tulherias_entardecer with dissolve
    play music "jardim_suave.ogg" fadeout 2.0 fadein 1.5
    show protagonista at left with moveinleft

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
    "Mas, por um instante, tudo silencia — e algo acontece."

    scene bg_jardim_miragem with fade
    play music "atelier_silencio.ogg" fadeout 2.0 fadein 1.5

    "A luz da lua atravessa as copas das árvores, formando uma clareira difusa à sua frente."

    "Ali, entre sombras e folhas, uma figura parece se formar por instantes... não é real, mas também não é apenas imaginação."
    show pissarro miragem at left with dissolve 
    "Camille Pissarro — ou algo como a memória dele — está de pé diante de uma tela invisível, pintando com gestos lentos e etéreos."

    protagonist "Isso é... impossível."

    "Pissarro ergue o olhar e, sem falar, apenas sorri. Ele aponta para o bilhete em sua mão."

    "Você ouve sua própria voz em pensamento:"

    show protagonista at right with dissolve

    protagonist "A luz muda tudo. Não confie no que dizem..."

    "A figura se desfaz com o vento. A brisa agora é fria. E os passos voltam, firmes, reais, determinados."

    $ pista_bilhete_jardim = True

    "Você se levanta. Algo está vindo — e agora, você está pronto."

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
    show rochefort at right 
    show protagonista at left 

    "Você apresenta todas as pistas. Rochefort, pressionado, confessa: manipulou a crítica para destruir a reputação de Pissarro."

    "Mas Camille escapou. Fingiu seu desaparecimento e está agora escondido, pintando sua obra final."

    scene bg_atelier_pissarro with fade
    play music "epilogo_feliz.ogg" fadeout 2.0 fadein 1.5
    show pissarro at center

    "Dias depois, você recebe um convite secreto. Ao chegar ao ateliê, encontra Camille Pissarro em silêncio, diante de uma tela imensa, pincel na mão."

    pissarro "Você seguiu os sinais. Não esperava por isso."

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

    scene bg_atelier_pissarro with fade
    play music "epilogo_reflexivo1.ogg" fadeout 2.0 fadein 1.5

    "Você decide que o mundo precisa conhecer a última obra de Pissarro — uma peça que transcende a pintura e se torna manifesto."

    "A notícia do reaparecimento do mestre abala Paris. A exposição secreta lota. A obra divide opiniões, mas reacende o espírito do impressionismo."

    "Pissarro, relutante, aceita a nova fama. Você é lembrado como o responsável por trazer à luz um dos maiores enigmas da arte moderna."

    scene black with fade
    centered "Fim — A Luz da Verdade"
    return


label final_guardado:

    "Camille sorri, volta-se para a tela e continua a pintar."

    "Você sai do ateliê com a certeza de que a verdade, às vezes, deve permanecer entre artistas."

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
