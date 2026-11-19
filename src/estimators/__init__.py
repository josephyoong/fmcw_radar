def getEstimator(estimator):
    if estimator == "estimator1":
        from estimators.estimator1 import estimateDisplacement
        return estimateDisplacement
    raise ValueError(f"unknown estimator: {estimator}")