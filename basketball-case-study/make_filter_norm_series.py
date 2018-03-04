positions = ['Shooting Guard', 'Power Forward', 'Center', 'Small Forward',
       'Point Guard']
field = 'Points' # not a list!!!

s_shtgrd = df_bball[df_bball['Position'] == positions[0]][field]
s_pwrfwd = df_bball[df_bball['Position'] == positions[1]][field]
s_center = df_bball[df_bball['Position'] == positions[2]][field]
s_smlfwd = df_bball[df_bball['Position'] == positions[3]][field]
s_pntgrd = df_bball[df_bball['Position'] == positions[4]][field]

ss = [s_shtgrd,s_pwrfwd,s_center,s_smlfwd,s_pntgrd]
names = ['s_shtgrd','s_pwrfwd','s_center','s_smlfwd','s_pntgrd']

out_df = pd.DataFrame()
for idx, series in enumerate(ss):
    filtered = filterSeries(series)
    normed = norm_series(filtered)
    out_df[names[idx]] = normed
