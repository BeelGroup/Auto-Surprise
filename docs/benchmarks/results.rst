.. benchmarks/_results
.. _results:

Results
=======

.. table:: Results for Movielens 100k Dataset

    +----------------------+--------+--------+----------+
    |       Algorithm      |  RMSE  |   MAE  |   Time   |
    +======================+========+========+==========+
    | Normal Predictor     | 1.5195 | 1.2200 | 00:00:01 |
    +----------------------+--------+--------+----------+
    | SVD                  | 0.9364 | 0.7385 | 00:00:23 |
    +----------------------+--------+--------+----------+
    | SVD++                | 0.9196 | 0.7216 | 00:14:23 |
    +----------------------+--------+--------+----------+
    | NMF                  | 0.9651 | 0.7592 | 00:00:25 |
    +----------------------+--------+--------+----------+
    | Slope One            | 0.9450 | 0.7425 | 00:00:15 |
    +----------------------+--------+--------+----------+
    | KNN Basic            | 0.9791 | 0.7738 | 00:00:18 |
    +----------------------+--------+--------+----------+
    | KNN with Means       | 0.9510 | 0.7490 | 00:00:19 |
    +----------------------+--------+--------+----------+
    | KNN with   Z-score   | 0.9517 | 0.7470 | 00:00:21 |
    +----------------------+--------+--------+----------+
    | KNN Baseline         | 0.9299 | 0.7329 | 00:00:22 |
    +----------------------+--------+--------+----------+
    | Co-clustering        | 0.9678 | 0.7581 | 00:00:08 |
    +----------------------+--------+--------+----------+
    | Baseline Only        | 0.9433 | 0.7479 | 00:00:01 |
    +----------------------+--------+--------+----------+
    | GridSearch           | 0.9139 | 0.7167 | 27:02:48 |
    +----------------------+--------+--------+----------+
    | Auto-Surprise (TPE)  | 0.9136 | 0.7280 | 02:00:01 |
    +----------------------+--------+--------+----------+
    | Auto-Surprise (ATPE) | 0.9116 | 0.7244 | 02:00:02 |
    +----------------------+--------+--------+----------+


.. table:: Results for Jester 2 Dataset (100k Random Sample)

    +----------------------+--------+--------+----------+
    |       Algorithm      |  RMSE  |  MAE   |   Time   |
    +======================+========+========+==========+
    | Normal Predictor     |  7.277 | 5.886  | 00:00:01 |
    +----------------------+--------+--------+----------+
    | SVD                  |  4.905 | 3.97   | 00:00:13 |
    +----------------------+--------+--------+----------+
    | SVD++                |  5.102 | 4.055  | 00:00:29 |
    +----------------------+--------+--------+----------+
    | NMF                  |   --   |   --   |    --    |
    +----------------------+--------+--------+----------+
    | Slope One            |  5.189 | 3.945  | 00:00:02 |
    +----------------------+--------+--------+----------+
    | KNN Basic            |  5.078 | 4.034  | 00:02:14 |
    +----------------------+--------+--------+----------+
    | KNN with Means       |  5.124 | 3.955  | 00:02:16 |
    +----------------------+--------+--------+----------+
    | KNN with   Z-score   |  5.219 | 3.955  | 00:02:20 |
    +----------------------+--------+--------+----------+
    | KNN Baseline         |  4.898 | 3.896  | 00:02:14 |
    +----------------------+--------+--------+----------+
    | Co-clustering        |  5.153 | 3.917  | 00:00:12 |
    +----------------------+--------+--------+----------+
    | Baseline Only        |  4.849 | 3.934  | 00:00:01 |
    +----------------------+--------+--------+----------+
    | GridSearch           | 4.7409 | 3.8147 | 80:52:35 |
    +----------------------+--------+--------+----------+
    | Auto-Surprise (TPE)  | 4.6489 | 3.6837 | 02:00:10 |
    +----------------------+--------+--------+----------+
    | Auto-Surprise (ATPE) | 4.6555 | 3.6906 | 02:00:01 |
    +----------------------+--------+--------+----------+


.. table:: Results for Book Crossing Dataset (100k Random Sample)

    +----------------------+--------+--------+----------+
    |       Algorithm      |  RMSE  |  MAE   |   Time   |
    +======================+========+========+==========+
    | Normal Predictor     | 4.8960 | 3.866  | 00:00:01 |
    +----------------------+--------+--------+----------+
    | SVD                  | 3.5586 | 3.013  | 00:00:11 |
    +----------------------+--------+--------+----------+
    | SVD++                | 3.5842 | 2.991  | 00:01:48 |
    +----------------------+--------+--------+----------+
    | NMF                  |   --   |   --   |    --    |
    +----------------------+--------+--------+----------+
    | Slope One            |   --   |   --   |    --    |
    +----------------------+--------+--------+----------+
    | KNN Basic            | 3.9108 | 3.562  | 00:00:38 |
    +----------------------+--------+--------+----------+
    | KNN with Means       | 3.8574 | 3.301  | 00:00:35 |
    +----------------------+--------+--------+----------+
    | KNN with   Z-score   | 3.8526 | 3.292  | 00:00:37 |
    +----------------------+--------+--------+----------+
    | KNN Baseline         | 3.6181 | 3.101  | 00:00:36 |
    +----------------------+--------+--------+----------+
    | Co-clustering        | 4.0168 | 3.409  | 00:00:19 |
    +----------------------+--------+--------+----------+
    | Baseline Only        | 3.5760 | 3.095  | 00:00:02 |
    +----------------------+--------+--------+----------+
    | GridSearch           | 3.5467 | 2.9554 | 48:29:46 |
    +----------------------+--------+--------+----------+
    | Auto-Surprise (TPE)  | 3.5221 | 2.8871 | 02:00:58 |
    +----------------------+--------+--------+----------+
    | Auto-Surprise (ATPE) | 3.5190 | 2.8739 | 02:00:06 |
    +----------------------+--------+--------+----------+


We see an improvement of anywhere from 0.8 - 4.0 % in RMSE using Auto-Surprise. The time taken to evaluate is also significantly less when compared to GridSearch.
