from relevanceai.operations_new.cluster.models.sklearn.base import SklearnModelBase
from sklearn.cluster import KMeans
from typing import Optional


class KMeansModel(SklearnModelBase):
    def __init__(self, model_kwargs: Optional[dict] = None):
        if model_kwargs is None:
            model_kwargs = {}
        self.model = KMeans(**model_kwargs)

    @property
    def name(self):
        return "kmeans"

    @property
    def cluster_centers_(self):
        return self.model.cluster_centers_

    @property
    def alias(self):
        return "kmeans-" + str(self.model.n_clusters)
