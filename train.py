import pandas as pd
import wget
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

# Loading the file

url =  'https://raw.githubusercontent.com/Veranika23/endometriosis-prediction/refs/heads/main/data/structured_endometriosis_data.csv'
downloaded_file = wget.download(url)
df = pd.read_csv(downloaded_file)

#Data preparation

df.columns = df.columns.str.lower().str.replace(' ', '_')

numerical_columns = list(df.dtypes[(df.dtypes == 'int64') | (df.dtypes == 'float64')].index)

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical_columns:
    df[c] = df[c].replace("_", " ").str.lower()

del df['age']

numerical_columns = list(df.dtypes[(df.dtypes == 'int64') | (df.dtypes == 'float64')].index)

#Random Forest model

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)

y_full_train = df_full_train.diagnosis.values

del df_full_train['diagnosis']

full_train_dicts = df_full_train.to_dict(orient='records')

pipeline = make_pipeline(DictVectorizer(), RandomForestClassifier(n_estimators=80,
                            max_depth=10,
                            min_samples_leaf=50,
                            random_state=1))



pipeline.fit(full_train_dicts, y_full_train)

with open('model.bin', 'wb') as f_out: 
    pickle.dump(pipeline, f_out)

print('\n The model saved successfully')