import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


col1, col2, col3 = st.columns(3)

with col2:
    image = Image.open('logo.png')
    st.image(image)

st.title('Estilos de Aprendizagem - Matriz Essencial')
st.subheader('Teste de identificação do estilo de aprendizagem')
st.markdown('')
st.markdown('O questionário a seguir apresenta situações cotiadas e não há julgamento de valor em relação as '
            'respostas. O objetivo do exercício é identificar seu estilo pessoal de assimilação quanto as '
            'interações que vivencia.')
st.markdown('**Como responder: marque com o número 1 apenas na resposta que escolher, é permitido uma '
            'resposta por pergunta.**')
st.markdown('')

with st.container():
    st.markdown('**1. Diante de um(a) conhecido(a):**')

    id1a = st.number_input(label='A. Para saber se estão escutando, é essencial que ele(a) esteja olhando para você.',
                           min_value=0, max_value=1)
    id1b = st.number_input(label='B. Você entende que para ele(a) é importante o tom da sua voz.',
                           min_value=0, max_value=1)
    id1c = st.number_input(label='C. O que importa de fato é que ele(a) tenha algum sentimento por você.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**2. Em uma apresentação:**')

    id2a = st.number_input(label='A. É importante que existam figuras, gráficos e fluxos.',
                           min_value=0, max_value=1)
    id2b = st.number_input(label='B. As informações apresentadas nas projeções devem ser também verbalizadas.',
                           min_value=0, max_value=1)
    id2c = st.number_input(label='C. A temperatura adequada da sala é indispensável.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**3. Quando é apresentado a uma pessoa:**')

    id3a = st.number_input(label='A. Você acredita ser suficiente vê-la, para saber como ela é.',
                           min_value=0, max_value=1)
    id3b = st.number_input(label='B. Precisa falar com ela alguns minutos para saber como ela é.',
                           min_value=0, max_value=1)
    id3c = st.number_input(label='C. O aperto de mão é suficiente para saber com quem está lidando.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**4. Diante de uma entrevista de trabalho:**')

    id4a = st.number_input(label='A. Verifica o perfil do(a) entrevistador(a) nas redes sociais.',
                           min_value=0, max_value=1)
    id4b = st.number_input(label='B. Faz anotações e ensaia o discurso o que irá adotar durante a entrevista.',
                           min_value=0, max_value=1)
    id4c = st.number_input(label='C. O que realmente importa é o quão relaxado e tranquilo estará na ocasião.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**5. Quando está com um amigo(a):**')

    id5a = st.number_input(label='A. Presta atenção nas expressões faciais dele(a).',
                           min_value=0, max_value=1)
    id5b = st.number_input(label='B. Se concentra nas atitudes dele(a).',
                           min_value=0, max_value=1)
    id5c = st.number_input(label='C. O importante é o conteúdo do que ele(a) diz e a forma como fala.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**6. Em seus momentos de folga, você prefere:**')

    id6a = st.number_input(label='A. Assistir a algum programa de TV.',
                           min_value=0, max_value=1)
    id6b = st.number_input(label='B. Fazer alguma atividade física, ou se reunir com amigos e familiares.',
                           min_value=0, max_value=1)
    id6c = st.number_input(label='C. Ouvir sua playlist de músicas favorita.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**7. Quando quer comer em um restaurante:**')

    id7a = st.number_input(label='A. O importante é a apresentação do prato e diversidade de cores e texturas.',
                           min_value=0, max_value=1)
    id7b = st.number_input(label='B. Escolhe o local pela tranquilidade e silencio do ambientes.',
                           min_value=0, max_value=1)
    id7c = st.number_input(label='C. Opta pelo sabor e aroma da comida servida no lugar.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**8. Diante do seu superior hierárquico:**')

    id8a = st.number_input(label='A. Prefere receber orientações de uma tarefa por escrito.',
                           min_value=0, max_value=1)
    id8b = st.number_input(label='B. Pede que ele(a) explicar verbalmente o que se espera da tarefa.',
                           min_value=0, max_value=1)
    id8c = st.number_input(label='C. O que importa é como ele se comporta e se ambiente está pacífico.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**9. Em geral:**')

    id9a = st.number_input(label='A. Você prefere observar seu entorno e o comportamento das pessoas.',
                           min_value=0, max_value=1)
    id9b = st.number_input(label='B. Fica inquieto falando com você mesmo em voz alta,  faz algum contato telefônico.',
                           min_value=0, max_value=1)
    id9c = st.number_input(label='C. Presta atenção em seus pensamentos, relembra situações ou pensa no futuro.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**10. Quando está planejando uma viagem:**')

    id10a = st.number_input(label='A. Procura um local com vistas incríveis ou com alguma arquitetura típica.',
                           min_value=0, max_value=1)
    id10b = st.number_input(label='B. Espera a baixa temporada, para ficar em locais mais calmos e silenciosos.',
                           min_value=0, max_value=1)
    id10c = st.number_input(label='C. Busca locais que propiciem fortes emoções.',
                           min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**11. Na escolha por um novo carro:**')

    id11a = st.number_input(label='A. Você considera principamente o designe e a cor.',
                            min_value=0, max_value=1)
    id11b = st.number_input(label='B. O silêncio do motor é determinante.',
                            min_value=0, max_value=1)
    id11c = st.number_input(label='C. Busca um veículo confortável com sensação de bem estar.',
                            min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**12. Qual tipo de filme você prefere:**')

    id12a = st.number_input(label='A. Ficção com grandes efeitos especiais.',
                            min_value=0, max_value=1)
    id12b = st.number_input(label='B. Musical.',
                            min_value=0, max_value=1)
    id12c = st.number_input(label='C. Drama ou romance.',
                            min_value=0, max_value=1)

    st.markdown('')
    st.markdown('**13. Quais atitudes prefere que seu companheiro(a) tenha com você:**')

    id13a = st.number_input(label='A. Que lhe dê presentes.',
                            min_value=0, max_value=1)
    id13b = st.number_input(label='B. Diga seus sentimentos.',
                            min_value=0, max_value=1)
    id13c = st.number_input(label='C. Mantenha contatos físicos com frequência.',
                            min_value=0, max_value=1)

if st.button('Resultado'):
    soma_a = (id1a + id2a + id3a + id4a + id5a + id6a + id7a + id8a + id9a + id10a + id11a + id12a + id13a)
    soma_b = (id1b + id2b + id3b + id4b + id5b + id6b + id7b + id8b + id9b + id10b + id11b + id12b + id13b)
    soma_c = (id1c + id2c + id3c + id4c + id5c + id6c + id7c + id8c + id9c + id10c + id11c + id12c + id13c)

    lista = [
        {"Estilo": "Visual", "Pontos": soma_a},
        {"Estilo": "Auditivo", "Pontos": soma_b},
        {"Estilo": "Cinestésico", "Pontos": soma_c},
    ]
    st.markdown('')
    resultado = max(lista, key=lambda lista: lista["Pontos"])["Estilo"]
    score = max(lista, key=lambda lista: lista["Pontos"])["Pontos"]
    st.subheader(f"Seu estilo de aprendizagem é {resultado}, você obteve {score} pontos")

    st.markdown('')

    chart_soma = pd.DataFrame(np.array([[soma_a, 0, 0], [0, soma_b, 0], [0, 0, soma_c]]),
                              columns=['Visual', 'Auditivo', 'Cinestésico'])
    st.bar_chart(chart_soma)
    st.balloons()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Sobre", "Visual", "Auditivo", "Cinestésico", "Leitura/Escrita"])

    with tab1:
        st.header("História")
        st.subheader("**Neil Fleming**")
        st.markdown("O professor neozelandês Neil Fleming, 1992, após anos de estudo, identificou a existência de "
                    "diferentes estilos de aprendizagem, ou seja, cada indivíduo tem uma maneira própria para "
                    "assimilar o conhecimento de forma mais eficaz. Surgiu então o método VARK, que é o acrônimo "
                    "em inglês, que remete a cada um dos estilos de aprendizagem. São eles: V (visual), "
                    "Auditory (auditivo), Read/ Write (leirura/escrita) e Kinesthetic (cinestésico).")

    with tab2:
        st.header("Visual")
        st.markdown("No estilo visual, o indivíduo tem uma percepção essencialmente gráfica, ou seja, possue "
                    "maior facilidade para assimilar as informações quando são apresentadas de forma gráfica, "
                    "de imagens, mapas, listas, etc. Pessoas com esse estilo de aprendizagem “visualizam” o "
                    "conhecimento. É comum, pessoas com esse estilo de aprendizagem, utilizarem expressões "
                    "como “do modo como eu vejo isso...”.")

    with tab3:
        st.header("Auditivo")
        st.markdown("Quando falamos do estilo auditivo, nos referimos ao indivíduo que retém melhor a informação "
                    "utilizando meios sonoros como palestras, podcasts, entrevistas, uma vez que ele “memoriza "
                    "a conversa” e seu pensamento é estruturado por meio de palavras. Pessoas com o estilo de "
                    "aprendizagem auditivo, frequentemente usam a expressão “então, pelo que foi dito, "
                    "eu entendi que...”")

    with tab4:
        st.header("Cinestésico")
        st.markdown("Pessoas com estilo de aprendizagem cinestesico, precisa literalmente “por a mão na massa”. "
                    "O conhecimento é assimilado e retido quando o indivíduo exprerimenta na prática, como fazer "
                    "a atividade proposta. Seu senso de realidade é concreto, por isso precisam vivenciar o "
                    "conhecimento na prática.")

    with tab5:
        st.header("Leitura/Escrita")
        st.markdown("O indivíduo que tem maior facilidade com conteúdos escritos, ou seja, que assimilam as "
                    "informações expressas em forma de palavras. Também se caracteriza por fazerem resumos dos "
                    "temas abordados, ou mesmo por se sentirem mais seguros quando anotam as informações que "
                    "precisam assimilar o conteúdo.")
