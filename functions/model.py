from Bio import SeqIO
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from functions.funcoes_aux import update
import joblib

def ler_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append({"Sequencia_AA": str(record.seq), "ID_Proteina": record.id})
    return sequences

def load_dataset(file_path):
    sequencias = ler_fasta(file_path)
    df = pd.DataFrame(sequencias)
    df['ID_Proteina'] = df['ID_Proteina'].str.rsplit('|', n=1).str[-1]
    return df

def split_dataset(df, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        df["Sequencia_AA"], df["ID_Proteina"], test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test

def preprocess_data(X_train, X_test, k=1):
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(k, k))
    X_train_encoded = vectorizer.fit_transform(X_train)
    X_test_encoded = vectorizer.transform(X_test)
    return vectorizer, X_train_encoded, X_test_encoded

def predict_protein_structure(input_sequence, nb_model, vectorizer):
    pdb_string, b_value = update(input_sequence)

    # Preprocess the input for Naive Bayes prediction
    txt_encoded = vectorizer.transform([input_sequence])

    # Perform prediction using Naive Bayes model
    predicted_class = nb_model.predict(txt_encoded)[0]

    return pdb_string, b_value, predicted_class

def train_naive_bayes(X_train_encoded, y_train):
    naive_bayes_model = MultinomialNB()
    naive_bayes_model.fit(X_train_encoded, y_train)
    return naive_bayes_model

def evaluate_model(model, X_train_encoded, y_train):
    y_pred_train = model.predict(X_train_encoded)
    train_accuracy = accuracy_score(y_train, y_pred_train)
    train_precision = precision_score(y_train, y_pred_train, average='weighted')
    train_recall = recall_score(y_train, y_pred_train, average='weighted')
    train_f1 = f1_score(y_train, y_pred_train, average='weighted')
    return train_accuracy, train_precision, train_recall, train_f1

def save_model(model, filename="trained_model.pkl"):
    joblib.dump(model, filename)


if __name__ == "__main__":
    # Inputs
    file_path = "datasets/Escherichia coli str. K-12 substr. MG1655/proteome.fasta"
    df = load_dataset(file_path)
    X_train, X_test, y_train, y_test = split_dataset(df)
    X_train_encoded, X_test_encoded = preprocess_data(X_train, X_test, k=1)
    model = train_naive_bayes(X_train_encoded, y_train)
    train_accuracy, train_precision, train_recall, train_f1 = evaluate_model(model, X_train_encoded, y_train)
    save_model(model)
