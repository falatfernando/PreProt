import streamlit as st
import functions.funcoes_aux as aux

### CONFIGURAÇÕES DA PÁGINA ###

##################################### Configuração da interação da página com a janela ###############################################
st.set_page_config(layout = 'wide', 
                   initial_sidebar_state = 'expanded',
                   page_title = "PreProt Dashboard",
                   page_icon= "🧬")

# Declarando CSS do app
with open('C:/Users/ferna/Documents/GitHub/PreProt/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

##################################################### SIDEBAR ########################################################################
# Título da Sidebar e Descrição
st.sidebar.markdown('''<h1 style="text-align: center; color: white; font-size: 36px"><b>PreProt 🧬</b></h1>''', unsafe_allow_html = True)
st.sidebar.markdown('''<p style="text-align: justify; color: white; font-size: 14.7px">Modelo de Machine Learning para predição de proteínas da <i>E. Coli</i></p>''', unsafe_allow_html = True)

# Sequência padrão INSA9_ECOLI
seq_default = "MASVSISCPSCSATDGVVRNGKSTAGHQRYLCSHCRKTWQLQFTYTASQPGTHQKIIDMAMNGVGCRATARIMGVGLNTILRHLKNSGRSR"

# Caixa de Input
txt = st.sidebar.text_area('Input da sequência', seq_default, height=230)

# Botão de previsão de proteína
predict = st.sidebar.button('Prever Proteína')
st.sidebar.markdown(
    """
    <style>
    hr {
        margin-top: -5px;
        margin-bottom: -10px;
    }
    .stButton button {
        margin-top: 0px;
        margin-bottom: -10px;
        margin-left: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Declarando função do botão
pdb_string, b_value = aux.update(txt)

# Linha separadora CSS
st.sidebar.markdown('<hr>', unsafe_allow_html=True)

# Footer
st.sidebar.markdown(''' <p style = "text-align: left; 
                                    color: white; 
                                    font-size: 12px;"
                                    margin-top: 10px;
                                    margin-bottom: 0px;>
                                    Contato: fernandofalat@proton.me
                    </p>''', unsafe_allow_html = True)

######################################################################################################################################
######################################################################################################################################
################################################### MAIN PAGE ########################################################################

# Título do Dashboard
st.markdown("<h1 style='color: #333333; text-align: center; margin-top: -80px;'>Caracterização da Proteína</h1>", unsafe_allow_html=True)

# Flexbox

col1, col2 = st.columns([2, 2])

# Coluna da esquerda

with col1:
        st.markdown("<h3 style='color: #333333;'>Estrutura Molecular</h3>", unsafe_allow_html=True)
        aux.render_mol(pdb_string)

with col2:
    container = st.container()
    container.markdown("<h3 style='color: #333333;'>Parâmetros</h3>", unsafe_allow_html=True)
    container.info(f'plDDT: {b_value}')


    '''
    container.markdown("<p style='color: #333333;'>plDDT é uma estimativa por resíduo da confidencia na predição da estrutura de 0 à 100</p>", unsafe_allow_html=True)
    container.download_button(
    label="Download PDB",
    data=pdb_string,
    file_name='predicted.pdb',
    mime='text/plain',
)
'''

if not predict:
    st.warning('👈 Enter protein sequence data!')