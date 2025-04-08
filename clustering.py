import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import SpectralClustering
import config

def run_clustering():
    df = pd.read_csv(config.CLUSTER_DATA_PATH)
    X = df[['Annual Surface Solar Radiation (Kwh/m2)', 'Rooftop Area (km2)', 'Grid Emission Factor (gCO2/Kwh)']].values

    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)

    spectral = SpectralClustering(n_clusters=4, affinity='rbf', assign_labels='kmeans', random_state=1212)
    labels = spectral.fit_predict(X_std)

    df['cluster'] = labels
    df.to_csv("./spectral_cluster_results.csv", index=False)

    # 可视化
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_std)

    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='tab10', s=40, alpha=0.8)
    plt.title("Spectral Clustering")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.grid(True)
    plt.savefig("./spectral_cluster_visual.png")
    plt.close()
