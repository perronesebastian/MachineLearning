from sklearn.preprocessing import LabelEncoder
import ParserService as parserService

def search_correlation(data_path):
    #Obtenemos una copia y parseo del dataset
    df = parserService.getDataSet(data_path)
    # Transformamos los valores del atributo class de categoricos a numéricos
    labelencoder = LabelEncoder()
    df["class"] = labelencoder.fit_transform(df["class"])
    # Transformamos los valores de los atributos categóricos a numéricos: class = 0 -> anomaly
    df["protocol_type"] = labelencoder.fit_transform(df["protocol_type"])
    df["service"] = labelencoder.fit_transform(df["service"])
    df["flag"] = labelencoder.fit_transform(df["flag"])
    # Mostrar correlación lineal entre todos los atributos del conjunto de datos
    return df


