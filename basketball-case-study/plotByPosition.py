def plotByPosition(var, positions="all", vlen=0.15, bins=50):
    """
    This function takings in the name of a variatble in the df_bball dataframe, 
    and creates a histogram with mean values for each.
    Optionally, you can pass the names of specific positions to plot.
    """
    shooting_guard = df_bball[df_bball['Position'] == 'Shooting Guard'][var]
    power_forward = df_bball[df_bball['Position'] == 'Power Forward'][var]
    center = df_bball[df_bball['Position'] == 'Center'][var]
    small_forward = df_bball[df_bball['Position'] == 'Small Forward'][var]
    point_guard = df_bball[df_bball['Position'] == 'Point Guard'][var]

    if positions == "all":
        positions = ["Shooting Guard", "Power Forward", "Center", "Small Forward", "Point Guard"]
        
    # Plot the distributions
    fig = plt.figure(figsize=(12, 5))
    
    if "Shooting Guard" in positions:
        ax = shooting_guard.hist(bins=bins, label="Shooting Guard", normed=True, color='r')
        ax.vlines(np.mean(shooting_guard),-.01,vlen, colors="r")
    if "Power Forward" in positions:  
        ax2 = power_forward.hist(bins=bins, label="Power Forward", normed=True, color='y')
        ax2.vlines(np.mean(power_forward),-.01,vlen, colors="y")
    if "Center" in positions:
        ax3 = center.hist(bins=bins, label="Center", normed=True, color='b')
        ax3.vlines(np.mean(center),-.01,vlen, colors="b")
    if "Small Forward" in positions:
        ax4 = small_forward.hist(bins=bins, label="Small Forward", normed=True, color='g')
        ax4.vlines(np.mean(small_forward),-.01,vlen, colors="g")
    if "Point Guard" in positions:
        ax5 = point_guard.hist(bins=bins, label="Point Guard", normed=True, color='grey')
        ax5.vlines(np.mean(point_guard),-.01,vlen, colors="k")

    
    plt.xlabel(var, fontsize=14, fontweight='bold')
    plt.legend()
    plt.show
