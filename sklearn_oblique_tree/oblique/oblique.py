from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted, check_random_state
from sklearn.utils.multiclass import unique_labels
from ._oblique import Tree

class ObliqueTree(BaseEstimator, ClassifierMixin):


    def __init__(self, splitter="oc1", random_state=None):
        self.random_state = random_state
        self.splitter = splitter



    def fit(self, X, y):
        """
        Grows an Oblique Decision Tree
        :param X:
        :param y:
        :return:
        """
        X, y = check_X_y(X, y)
        random_state = check_random_state(self.random_state)
        self.classes_ = unique_labels(y)
        Tree.fit(X,y)



    def predict(self, X):
        pass

