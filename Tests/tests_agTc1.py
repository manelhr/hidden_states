import scipy.spatial.distance as distance

from Tests.crossfoldcrf import cross_fold_ldcrf

__author__ = 'Manoel Ribeiro'

labels = 6
number_folds = 5
states = [6, 12, 18, 24, 30, 36]
n_jobs = 5


# -- Continuous

cross_fold_ldcrf(mat='../Dataset/ArmGesture/AG.mat', dist=distance.sqeuclidean,
                 labels=labels, number_folds=number_folds, states=states, n_jobs=n_jobs, c=1)
