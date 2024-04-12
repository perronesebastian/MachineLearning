import matplotlib.pyplot as plt
import CorrelationDataService as correlationService
from pandas.plotting import scatter_matrix

# Representar gráficamente la matriz de correlación
# corr = correlationService.search_correlation('datasets/NSL-KDD/KDDTrain+.arff').corr()
# fig, ax = plt.subplots(figsize=(8, 8))
# ax.matshow(corr)
# plt.xticks(range(len(corr.columns)), corr.columns);
# plt.yticks(range(len(corr.columns)), corr.columns);


# Representar gráficamente las correlaciones
df = correlationService.search_correlation('datasets/NSL-KDD/KDDTrain+.arff')
attributes = ["same_srv_rate", "dst_host_srv_count", "class", "dst_host_same_srv_rate"]

scatter_matrix(df[attributes], figsize=(12,8))
plt.show()