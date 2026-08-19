import pandas as pd
df = pd.read_csv('d:/IIIT Hyderabad/Cogsci/dcmr/NSD/subj01_response.tsv', sep='\t')
df_s1 = df[df['SESSION'] == 1].copy()

print('=== ISOLD value counts (what human responds) ===')
print(df_s1['ISOLD'].value_counts())

print('\n=== presentation_number value counts ===')
print(df_s1['presentation_number'].value_counts())

print('\n=== ISOLDCURRENT value counts (ground truth) ===')
print(df_s1['ISOLDCURRENT'].value_counts())

# Critical check
first_pres = df_s1[df_s1['presentation_number'] == 1]
repeat_pres = df_s1[df_s1['presentation_number'] > 1]
print(f'\nFirst presentations: {len(first_pres)}')
print(f'  ISOLDCURRENT=0: {(first_pres["ISOLDCURRENT"]==0).sum()}')
print(f'  ISOLDCURRENT=1: {(first_pres["ISOLDCURRENT"]==1).sum()}')
print(f'\nRepeat presentations: {len(repeat_pres)}')
print(f'  ISOLDCURRENT=0: {(repeat_pres["ISOLDCURRENT"]==0).sum()}')
print(f'  ISOLDCURRENT=1: {(repeat_pres["ISOLDCURRENT"]==1).sum()}')

print('\n=== Cross-check: ISOLD vs ISOLDCURRENT ===')
print(pd.crosstab(df_s1['ISOLDCURRENT'], df_s1['ISOLD'], rownames=['Ground Truth (ISOLDCURRENT)'], colnames=['Human Response (ISOLD)']))
