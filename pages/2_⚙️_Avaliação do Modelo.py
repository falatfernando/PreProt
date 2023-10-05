import streamlit as st
import joblib
import functions.model as nb
import numpy as np
import matplotlib.pyplot as plt

######################################################### CONFIGURAÇÃO ###############################################################
# Declarando configurações da página
st.set_page_config(
                layout = 'wide', 
                initial_sidebar_state = 'expanded',      
                page_title = "PreProt Modelo",
                page_icon= "🧬",
                )
######################################################################################################################################

# Carregando o modelo de Naive Bayes
nb_model = joblib.load("trained_model.pkl")

# Load and preprocess the data using your existing functions from model.py
file_path = "datasets/Escherichia coli str. K-12 substr. MG1655/proteome.fasta"
df = nb.load_dataset(file_path)
X_train, X_test, y_train, y_test = nb.split_dataset(df)
vectorizer, X_train_encoded, X_test_encoded = nb.preprocess_data(X_train, X_test, k=1)
train_accuracy, train_precision, train_recall, train_f1 = nb.evaluate_model(nb_model, X_train_encoded, y_train)

train_accuracy_percent, train_precision_percent, train_recall_percent, train_f1_percent = train_accuracy * 100 , train_precision * 100, train_recall * 100, train_f1 * 100 
# Display evaluation metrics

st.markdown('''<h1 style="text-align: center; color: white; font-size: 48px"><b>Avaliação do Modelo de Naive Bayes ⚙️</b></h1>''', unsafe_allow_html = True)

col1, col2 = st.columns([1, 2])

with col1:
    st.warning('k-mers: 1')
    st.warning('Vetorizador: CountVectorizer')
    st.info(f'Acurácia: {train_accuracy_percent:.2f} %')
    st.info(f'Recall: {train_recall_percent:.2f} %')
    st.info(f'F1 Score: {train_f1_percent:.2f} %')
    st.info(f'Precisão: {train_precision_percent:.2f} %')


with col2:
    # Your data
    metricas = ['Acurácia', 'Precisão', 'Recall', 'F1-Score']
    valores = [train_accuracy, train_precision, train_recall, train_f1]
    valores_percentuais = [value * 100 for value in valores]

    # Create a figure and plot
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(metricas, valores_percentuais, color='#325ea8', width=0.4)
    ax.set_xlabel('Métricas')
    ax.set_ylabel('Valores')
    ax.set_ylim([0, 100])
    ax.set_yticks(np.linspace(0, 100, 11))
    ax.set_yticklabels(['{}%'.format(int(val)) for val in np.linspace(0, 100, 11)])
    ax.bar_label(ax.containers[0])
    ax.set_title('Métricas de Desempenho do Modelo')

    # Add background color
    ax.set_facecolor('#d5d7db')

    # Use different style of bars
    ax.bar_style = 'bar'

    # Use different font for the labels
    ax.set_xticklabels(metricas)
    ax.set_yticklabels(['{}%'.format(int(val)) for val in np.linspace(0, 100, 11)])

    # Display the plot in Streamlit
    st.pyplot(fig)

# Sidebar
st.sidebar.markdown('''
<body>
<p style = "text-align: justify;" >O classificador de Naive Bayes é um algoritmo de aprendizado de máquina que usa o teorema de Bayes para prever a probabilidade de uma amostra pertencer a uma determinada classe. Ele se baseia na hipótese de que as características de uma amostra são independentes entre si, o que significa que a presença de uma característica não afeta a probabilidade de outra característica estar presente.</p>
<p style = "text-align: justify;" >O modelo de machine learning pode ser aplicado à classificação de sequências de aminoácidos para proteínas devido à sua capacidade de lidar com dados de alta dimensionalidade e à suposição de independência entre as características. Isso permite que o algoritmo avalie a probabilidade de uma sequência pertencer a uma classe específica com base nas frequências dos aminoácidos individuais, mesmo que existam muitas combinações possíveis..</p>
<p style = "text-align: justify;" >Apesar de ser um algoritmo simples é muito eficiente, e ele tem sido usado com sucesso em uma variedade de aplicações, incluindo classificação de texto, classificação de imagens e classificação de proteínas.</p>

</body>
                    ''',  unsafe_allow_html=True)
# Linha separadora CSS
st.sidebar.markdown('<hr>', unsafe_allow_html=True)