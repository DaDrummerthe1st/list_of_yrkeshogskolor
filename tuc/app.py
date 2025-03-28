# %%
import pandas as pd
import json


json_file = "dump_fixed.json"
#dump_columns = ["name","title","responsabilities","work_placement","email_adress"]
with open(json_file) as f:
    json_dump = json.load(f)


# %%

print(json.dumps(json_dump,indent=4))


# %%
df = pd.read_json(json_file)
df

# %%
df.fillna("", inplace=True)


# %%
df.loc[:, "work_placement_2"] = df["work_placement"].copy() # copy för att inte arbeta med en virtuel kopia, utan en som faktiskt existerar

# %%
df.work_placement

# %%
df.loc[:, "work_placement_2"] = df.groupby("email_adress")["work_placement"].transform(lambda x: ", ".join(x))

# %%
# display(df[df.duplicated(subset=['email_adress'], keep=False)])
# display(df.drop_duplicates(subset=['email_adress'], keep=False))
# display(result = df.concat)
df.drop_duplicates(subset=['email_adress'], inplace=True)


# %%
df.drop(labels=['work_placement'], axis=1, inplace=True)

# %%
import streamlit as st

st.header("Kontakter att höra av sig till")
st.dataframe(df)


