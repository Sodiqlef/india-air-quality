import pandas as pd

# Using LinearRegression Model, the mean absolute error are as follows (lag 1)
lr_baseline = round(25.17927308782788,2)
lr_train = round(5.103044019552854,2)
lr_test = round(3.516527657954878,2)


# Using AutoRegression Model, the mean absolute error are as follows (lag 26)
ar_baseline = round(25.338010670663973,2)
ar_train = round(4.356588174707222,2)
ar_test = round(3.351138752023845,2)


df_dict = {
    "baseline":[lr_baseline, ar_baseline ],
    "train":[lr_train, ar_train]
}

print(pd.DataFrame(df_dict, index=["LinearRegression", "AutoRegression"]))