def filterSeries(arr, sd_filter=3):
    """
    Takes in a NumPy series and filters out outliers based on standard deviations.
    """
    
    mean = np.mean(arr, axis=0)
    print(mean)
    sd = np.std(arr, axis=0)
    print(sd)
    
    final_list = [x for x in arr if (x > mean - (sd_filter * sd))]
    final_list = [x for x in final_list if (x < mean + (sd_filter * sd))]
    print(final_list)
    
    return pd.Series(final_list)
