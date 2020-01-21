from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from surprise import NormalPredictor
from surprise.model_selection import cross_validate
from auto_surprise.constants import DEFAULT_MAX_EVALS, DEFAULT_TARGET_METRIC

class AutoSurpriseNormalPredictor(object):
    def __init__(self, cv=5, metric=DEFAULT_TARGET_METRIC, data=None, debug=False):
        self._cv = cv
        self._metric = metric
        self._data = data
        self._debug = debug

    def _hyperopt(self):
        algo = NormalPredictor()
        return cross_validate(algo, self._data, measures=['RMSE', 'MAE'], cv=self._cv, verbose=self._debug)[self._metric].mean()

    def _objective(self):
        loss = self._hyperopt()
        return { 'loss': loss, 'status': STATUS_OK }

    def best_hyperparams(self, max_evals=DEFAULT_MAX_EVALS):
        best = self._objective()
        return None, best
