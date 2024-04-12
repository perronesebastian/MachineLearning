import arff, pandas as pd

def load_kdd_dataset(data_path):
    """Lectura del conjunto de datos NSL-KDD."""
    with open(data_path, 'r') as train_set:
        dataset = arff.load(train_set)
    attributes = [attr[0] for attr in dataset["attributes"]]
    return pd.DataFrame(dataset["data"], columns=attributes)

def getDataSet(data_path):
    df_orig = load_kdd_dataset(data_path)
    df = df_orig.copy()
    return df
