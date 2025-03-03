import numpy as np
import pandas as pd
import sklearn.preprocessing
import sklearn.impute

f = pd.read_csv(
    "data/example_data.csv",
    dtype={
        "target": object,
        "checking_account_status": "category",
        "duration": np.float64,
        "credit_history": "category",
        "credit_amount": np.float64,
        "other_installment_plans": "category",
        "job": "category",
        "foreign_worker": "category",
        "interest_rate": np.float64,
        "city": "category",
    },
)


def preprocess_data(data: pd.DataFrame):
    d = data.copy()

    cat_idx = d.select_dtypes(include=['category']).columns
    for idx in cat_idx:
        mfv = d[idx].mode().values[0]
        d[idx].fillna(mfv, inplace=True)

        dmy = pd.get_dummies(d[idx], prefix=idx, prefix_sep='_', drop_first=True)
        d = pd.concat([d, dmy], axis=1)

    d.drop(cat_idx, axis=1, inplace=True)

    num_idx = d.select_dtypes(include=['float64']).columns
    for idx in num_idx:
        mdv = d[idx].median()
        d[idx].fillna(mdv, inplace=True)

        ss = sklearn.preprocessing.StandardScaler()
        v = d[idx].values.reshape(-1, 1)
        ss_v = ss.fit_transform(v)
        d[idx] = ss_v

    target = d.select_dtypes(include=['object']).columns[0]
    target_a = [i for i in d[target].unique()]
    target_a.sort()
    target_m = {value: i for i, value in enumerate(target_a)}
    d[target] = d[target].map(target_m)

    X = d.drop(target, axis=1)
    y = d[target].tolist()

    return X, y


x, y = preprocess_data(f)

print(y)
x.to_csv(
    'data/processed.csv'
)