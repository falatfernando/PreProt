import streamlit as st
from PIL import Image

######################################################### CONFIGURAÇÃO ###############################################################
# Declarando configurações da página
st.set_page_config(
                layout = 'wide', 
                initial_sidebar_state = 'expanded',      
                page_title = "PreProt Métrica",
                page_icon= "🧬",
                )
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

st.markdown('<link href="https://use.fontawesome.com/d178376847.css" rel="stylesheet">', unsafe_allow_html=True)
st.markdown('<script src="https://use.fontawesome.com/d178376847.js"></script>', unsafe_allow_html=True)

######################################################### SIDE BAR ####################################################################

# Título da Sidebar e Descrição
st.sidebar.markdown('''<h1 style="text-align: center; color: white; font-size: 36px"><b>PreProt 🧬</b></h1>''', unsafe_allow_html = True)
st.sidebar.markdown('''<p style="text-align: justify; color: white; font-size: 16px">Modelo de Machine Learning para predição de proteínas da <i>Escherichia coli.</i></p>''', unsafe_allow_html = True)
st.sidebar.markdown('''<p style="text-align: justify; color: white; font-size: 16px"> Projeto de conclusão do MBA em <b>Data Science & analytics</b> pela <b> USP/ESALQ </b> </p>
                       <p style="text-align: justify; color: white; font-size: 16px"> Desenvolvido por Fernando Falat Rangel, orientado por Miriam Martin. </p>''', unsafe_allow_html = True)
# Linha separadora CSS
st.sidebar.markdown('<hr>', unsafe_allow_html=True)
# Footer

# Icones

# E-mail
# Hyperlinks do LinkedIn, GitHub, and Email
st.sidebar.markdown(
    """
    <style>
        .icon-link a {
            text-decoration: none;
        }

        .icon-link a:hover {
            opacity: 0.75;
        }
    </style>
    <div class="icon-link" style='text-align: center; margin-bottom: 20px;'>
        <a href="mailto:fernandofalat@proton.me" target="_blank" style='margin: 10px;'>
            <img src="https://img.icons8.com/fluent/48/000000/gmail.png"/>
        </a>
        <a href="https://www.linkedin.com/in/fernandofalat/" target="_blank" style='margin: 10px;'>
            <img src="https://img.icons8.com/color/48/000000/linkedin.png"/>
        </a>
        <a href="https://github.com/falatfernando" target="_blank" style='margin: 10px;'>
            <img src="https://img.icons8.com/fluent/48/000000/github.png"/>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
# CSS para alterar a cor do texto
custom_css = """
<style>
    body {
        color: #333333;
    }

    p, ol, h3 {
        color: #333333;
        text-align: justify;
        font-size: 14px !important;
    }

    a {
        color: #333333;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Título
st.markdown("<b style='font-size: 24px'>O que é o PreProt?</b>", unsafe_allow_html=True)
st.markdown("<p>PreProt é um projeto de implementação de Machine Learning, mais especificamente o modelo de Naive Bayes, para avaliar a eficácia e acurácia do mesmo dentro do campo da bioinformática, através de testes de eficácia encontrados na aba 'Avaliação do Modelo'. Mais informações do projeto podem ser encontradas na <a href='readme.txt'>documentação</a> e na <a href='https://docs.google.com/document/d/1evF9-wIk1tZ6xFhq2hgq4nII7toi9ARP/edit)'>monografia</a>.</p>", unsafe_allow_html=True)

# Introdução
st.markdown("<h3><b style='font-size: 24px'>Introdução</b></h3>", unsafe_allow_html=True)
st.markdown("""
    <div>
        <p align='justify'>A fim de que ocorra a formação de uma proteína, é necessário percorrer um conjunto de etapas. Iniciando-se pelos ácidos nucleicos, que constituem a base do DNA (ATCG):
            <ol type='1'>
                <li><b>Transcrição:</b> O DNA é transcrito em RNA mensageiro (mRNA) através da RNA polimerase.</li>
                <br></br>
                <li><b>Tradução:</b> O mRNA é lido pelos ribossomos, decodificando os códons (sequência de 3 ácidos nucleicos), então entram os tRNAs e transportam os aminoácidos correspondentes para formar a cadeia polipeptídica. Um peptídeo é composto por dois ou mais aminoácidos, sendo classificados em dipeptídeos (2); tri; tetra; oligo e polipeptídeos; quando a cadeia de aminoácidos passa de 70, classifica-se em proteína.</li>
                <br></br>
                <li><b>Desdobramento e pós-tradução:</b> Após a síntese da cadeia polipeptídica, a proteína pode passar por um processo de dobramento ou enovelamento para adquirir sua estrutura tridimensional funcional. Após o dobramento, a proteína pode sofrer modificações pós-traducionais, como a adição de grupos químicos ou a clivagem de segmentos adicionais.</li>
            </ol>
        </p>
        <br></br>
        <p>A imagem abaixo exemplifica o processo da tradução da fita de mRNA até a leitura pela fita de tRNA:</p>
        <p style='text-align:center;'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Aminoacids_table.svg/609px-Aminoacids_table.svg.png?20210405175054' alt='Tabela de conversão de aminoácidos' width='500' height='500' align=center> </img>
        </p>
    </div>
""", unsafe_allow_html=True)

# Machine Learning
st.markdown("<h3><b style='font-size: 24px'>Machine Learning</b></h3>", unsafe_allow_html=True)
st.markdown("<div><p>Como citado anteriormente, uma proteína é composta por uma cadeia polipeptídica que pode conter mais de 70 aminoácidos. Como existem 20 tipos diferentes de aminoácidos que podem ser usados para construir uma proteína, e esses aminoácidos podem ser combinados em qualquer ordem, o número de sequências possíveis é virtualmente infinito. Portanto, as proteínas possuem combinações quase infinitas de aminoácidos.</p>", unsafe_allow_html=True)
st.markdown("<p>Logo um algoritmo de machine learning pode aprender a partir de dados experimentais como o DNA é transcrito em RNA e depois traduzido em proteínas, quais são os fatores que influenciam essa transformação e quais são as consequências de mutações ou alterações na expressão gênica.</p>", unsafe_allow_html=True)
st.markdown("<p>Com o objetivo de facilitar o processo de tradução de uma sequência de DNA em uma proteína, o PreProt treina um modelo de aprendizado de máquina, e analisa os resultados, com uma base de dados contendo o proteoma da <i>Escherichia coli</i> K-12 substr. MG1655, que é uma das bactérias melhor caracterizada atualmente.</p></div>", unsafe_allow_html=True)

# Integração com ESMFold
st.markdown("<h3><b style='font-size: 24px'>ESM Fold</b></h3>", unsafe_allow_html=True)
st.markdown("<p>O output do modelo de machine learning é enviado para a API do ESM Fold, algorítimo de predição de estruturas 3D de proteínas desenvolvido pela Meta AI em 2023, retornando um dataset com dados nescessários para plotar a estrutura 3D da proteína através do módulo py3Dmol. Para saber mais sobre o ESM Fold acesse o <a href = 'https://ai.meta.com/blog/protein-folding-esmfold-metagenomics/'> artigo publicado no blog da Meta AI.</a> </p>", unsafe_allow_html=True)

# Arquitetura do aplicativo
st.markdown("<h3> <b style='font-size: 24px'> Arquitetura do Aplicativo </b> </h3>", unsafe_allow_html=True)
st.markdown("<p>A interface gráfica do PreProt apresenta a proposta de aprimorar a acessibilidade à informação para todos aqueles que desejam interagir com um modelo treinado, viabilizando a exploração de diferentes sequências de proteínas não nescessariamente sabendo programar.</p>", unsafe_allow_html=True)
st.markdown("<p>O aplicativo opera por meio do encaminhamento da entrada da sequência fornecida pelo usuário por dois percursos distintos, após ser submetida ao processo de pré-processamento adequado: a API do ESMFold e o modelo treinado de Naive Bayes. O diagrama a seguir ilustra de forma esquemática o fluxo dos dados até o usuário:</p>"
            , unsafe_allow_html= True)

# Local path to the image
image_path = r'images/Fluxograma APP.png'

# Open the image using PIL
image = Image.open(image_path)

# Display the image
st.image(image, use_column_width=True)