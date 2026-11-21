def getEstimator(estimator):
    if estimator == "estimator1":
        from estimators.estimator1 import estimateDisplacement
        return estimateDisplacement
    if estimator == "estimator2":
        from estimators.estimator2 import estimateDisplacement
        return estimateDisplacement
    if estimator == "estimator3":
        from estimators.estimator3 import estimateDisplacement
        return estimateDisplacement
    raise ValueError(f"unknown estimator: {estimator}")