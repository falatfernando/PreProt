import streamlit as st
import functions.funcoes_aux as aux
import functions.model as nb
import joblib
import pandas as pd
from streamlit.components.v1 import html

### CONFIGURAÇÕES DA PÁGINA ###

# Carregando o modelo de Naive Bayes
nb_model = joblib.load("C:/Users/ferna/Documents/GitHub/PreProt/trained_model.pkl")

# Load and preprocess the data using your existing functions from model.py
file_path = "C:/Users/ferna/Documents/GitHub/PreProt/datasets/Escherichia coli str. K-12 substr. MG1655/proteome.fasta"
df = nb.load_dataset(file_path)
X_train, X_test, y_train, y_test = nb.split_dataset(df)
vectorizer, X_train_encoded, X_test_encoded = nb.preprocess_data(X_train, X_test, k=1)

# Carrengando dataset contendo mais informações sobre as proteínas preditas
df_interactors = pd.read_csv("C:/Users/ferna/Documents/GitHub/PreProt/datasets/MG1655_Chaperone_Interactors.csv")

##################################### Configuração da interação da página com a janela ###############################################
st.set_page_config(layout = 'wide', 
                   initial_sidebar_state = 'expanded',
                   page_title = "PreProt Dashboard",
                   page_icon= "🧬")

# Declarando CSS do app
#with open('C:/Users/ferna/Documents/GitHub/PreProt/style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

##################################################### SIDEBAR ########################################################################
# Título da Sidebar e Descrição
st.sidebar.markdown('''<h1 style="text-align: center; color: white; font-size: 36px"><b>PreProt 🧬</b></h1>''', unsafe_allow_html = True)
st.sidebar.markdown('''<p style="text-align: justify; color: white; font-size: 14.7px">Modelo de Machine Learning para predição de proteínas da <i>E. Coli</i></p>''', unsafe_allow_html = True)

# Sequência padrão INSA9_ECOLI
seq_default = "MASVSISCPSCSATDGVVRNGKSTAGHQRYLCSHCRKTWQLQFTYTASQPGTHQKIIDMAMNGVGCRATARIMGVGLNTILRHLKNSGRSR"

# Botão de Seleção:

options = ["DNA", "AA", "mRNA", "tRNA"]
st.sidebar.write('<style> div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
option = st.sidebar.radio("Tipo de Input", options)

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

# Declarando função do botão (enviando pra API do ESM FOLD)

pdb_string, b_value = aux.update(txt)
pdb_string, b_value, predicted_class = nb.predict_protein_structure(txt, nb_model, vectorizer)

# Usando o output do modelo de Naive Bayes para buscar mais informações no df de chaperone interactors
protein_match = df_interactors[df_interactors["Protein_ID_STEPdb_2.0"].str.contains(predicted_class, case = False)]

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

col1, col2 = st.columns([2, 1])

# Coluna da esquerda

with col1:
        # Output ESM Fold 
        st.markdown("<h3 style='color: #333333; text-align: center;'>Estrutura Molecular</h3>", unsafe_allow_html=True)
        aux.render_mol(pdb_string)

        # Declarando colunas para separação
        col1_a, col1_b = st.columns([1,1])

        with col1_a:
            st.download_button(
                label="Baixar PDB",
                data=pdb_string,
                file_name='predicted.pdb',
                mime='text/plain',
            )

        with col1_b:
        ## Output plDDT ESM Fold 
         st.write(f"Valor do plDDT: {b_value}")
        st.markdown("<p style='color: #333333;'>plDDT é uma estimativa por resíduo da confidencia na predição da estrutura de 0 a 1. </p>", unsafe_allow_html=True)


with col2:
    container = st.container()
    container.markdown("<h3 style='color: #333333; text-align: center;'>Caracterização</h3>", unsafe_allow_html=True)
    
    # Naive Bayes output
    container.info(f"Classe Predita: {predicted_class}")
    if not protein_match.empty:
        st.info(f"Foram encontrados {len(protein_match)} matches para a proteína.")

        df_display = protein_match
        desired_column_order = ['Protein_ID_STEPdb_2.0', 
                                'Accession_STEPdb_2.0', 
                                'Uniprot_Protein_Name',
                                'STEPdb_Universal_Name',
                                '1ary_Gene_Name',
                                'STEPdb_Sub-cellular_Location_Letter Code',
                                'STEPdb_Sub-cellular_Location_Full Name',
                                'sub-cellular_topology_group',
                                ]




        renamed_columns = {'Accession_STEPdb_2.0': 'Accession STEPdb 2.0', 
                           'Protein_ID_STEPdb_2.0': 'ID da Proteína STEPdb 2.0', 
                           '1ary_Gene_Name': 'Nome do Gene Primário',
                           'STEPdb_Universal_Name': 'Nome Universal',
                           'Uniprot_Protein_Name': 'Nome da Proteína UNIPROT',
                           'STEPdb_Sub-cellular_Location_Full Name': 'Localidade Subcelular',
                           'STEPdb_Sub-cellular_Location_Letter Code': 'Código da Localidade',
                           'sub-cellular_topology_group': 'Grupo de Topologia'
                           }
        df_display = df_display[desired_column_order].rename(columns=renamed_columns)

        df_display = df_display.transpose().reset_index()

        df_display.columns = df_display.iloc[0]
        df_display = df_display.iloc[1:8].reset_index(drop=True)


        st.table(df_display)

    else:
        st.warning("Sem matches.")