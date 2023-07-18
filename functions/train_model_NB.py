import model

if __name__ == "__main__":
    # Inputs
    file_path = "datasets/Escherichia coli str. K-12 substr. MG1655/proteome.fasta"
    df = model.load_dataset(file_path)
    X_train, X_test, y_train, y_test = model.split_dataset(df)
    X_train_encoded, X_test_encoded = model.preprocess_data(X_train, X_test, k=1)
    trained_model = model.train_naive_bayes(X_train_encoded, y_train)
    model.save_model(trained_model, "trained_model.pkl")