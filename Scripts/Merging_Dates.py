import pandas as pd

# loading the CSV files
visual_observations = pd.read_csv('/ZTF_Observations.csv')
vlass_observations = pd.read_csv('/VLASS_Observations.csv')

visual_observations.head(), vlass_observations.head()

visual_observations[['name', 'visual_obs_date']] = visual_observations.iloc[:, 0].str.extract(r'(\S+) has a peak observation at (\d+\.\d+)')
visual_observations['visual_obs_date'] = visual_observations['visual_obs_date'].astype(float)
visual_observations['visual_obs_date'] = visual_observations['visual_obs_date'] + 57989.879
visual_observations = visual_observations.drop(columns=[visual_observations.columns[0]])

# processing VLASS observations dataframe
vlass_observations[['name_epoch', 'vlass_obs_date']] = vlass_observations.iloc[:, 0].str.extract(r'(\S+)\.png observed on (\d+\.\d+)')
vlass_observations['vlass_obs_date'] = vlass_observations['vlass_obs_date'].astype(float)
vlass_observations[['name', 'epoch']] = vlass_observations['name_epoch'].str.extract(r'(\S+)_(VLASS\d\.\d\w?)')
vlass_observations = vlass_observations.drop(columns=[vlass_observations.columns[0]])

# merging the datasets on the 'name' column
merged_data = pd.merge(visual_observations, vlass_observations, on='name', how='inner')

merged_data['visual_obs_date'] = pd.to_numeric(merged_data['visual_obs_date'], errors='coerce')
merged_data['days_diff'] = merged_data['vlass_obs_date'] - merged_data['visual_obs_date']

merged_file_path = '/Merged_Observations.csv'
merged_data.to_csv(merged_file_path, index=False)
print(f"Merged data saved to {merged_file_path}")
