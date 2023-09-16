#%%
import pandas as pd
import json
import ydata_profiling

#%%
results_path = r'C:\Users\jjuua\Downloads\response_1694821905684.json'

with open(results_path, 'r') as json_file:
    data = json.load(json_file)

# Extract the "results" key from the parsed data
results_data = data["results"]

# Create an empty list to store individual records
records = []

# Iterate through the results and extract inputs and output
for result in results_data:
    for key, value in result.items():
        inputs = value.get("inputs", {})
        output = value.get("output", {})
        record = {**inputs, **output}
        records.append(record)

# Create a DataFrame from the list of records
df = pd.DataFrame(records)

# Print the DataFrame
df.head()
#%%
df['Predicted Label'] = df['Predicted Label'].replace({'Sepsis status is Negative':0,'Sepsis status is Positive':1})
df = df.rename(columns={'Predicted Label': 'Sepsiss Pred'})

df.head()
#%%
path_export = r'C:\Users\jjuua\VSCode\huawei_talleres\fastapi\DeployFastAPI\dev\notebooks\Profile_Sepsis_results.html'
profile = ydata_profiling.ProfileReport(df, title="Profiling Report - Sepsiss Results" , minimal=False)
profile.to_file(output_file=path_export)
# %%
