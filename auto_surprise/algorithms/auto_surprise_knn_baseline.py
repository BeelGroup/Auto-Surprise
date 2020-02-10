from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from surprise import KNNBaseline
from surprise.model_selection import cross_validate
from auto_surprise.constants import DEFAULT_MAX_EVALS, ACCURACY_METRICS
from auto_surprise.algorithms.spaces import KNN_DEFAULT_SPACE
from auto_surprise.algorithms.base import AlgorithmBase

class AutoSurpriseKNNBaseline(AlgorithmBase):
    def _hyperopt(self, params):
        algo = KNNBaseline(**params)
        return cross_validate(algo, self._data, measures=ACCURACY_METRICS, cv=self._cv, n_jobs=self._cv_n_jobs, verbose=self._debug)[self._metric].mean()

    def _objective(self, params):
        loss = self._hyperopt(params)
        return {'loss': loss, 'status': STATUS_OK}

    def best_hyperparams(self, max_evals=DEFAULT_MAX_EVALS):
        trials = Trials()
        best = fmin(self._objective, KNN_DEFAULT_SPACE, algo=tpe.suggest, max_evals=max_evals, trials=trials)
        return best, trials
