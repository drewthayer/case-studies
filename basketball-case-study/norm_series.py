def norm_series(series):
    '''
    inputs: pandas series
    output: pandas series, normalized
    normalization: (x-mu)/sigma, mu = mean(series), sigma = stdev(series)
    '''
    norm = []
    for x in series:
        mu = series.mean()
        sigma = series.std()
        norm.append((x-mu)/sigma)
    return(pd.Series(norm))
