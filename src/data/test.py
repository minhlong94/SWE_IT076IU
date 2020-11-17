import datetime

import pandas as pd

# transactions = pd.read_csv("sales_train.csv")
# new = transactions['date'].str.split('.', expand = True)
# transactions['day'] = new[0]
# transactions['month'] = new[1]
# transactions['year'] = new[2]
# transactions = transactions.drop("date", axis=1)
# transactions.to_csv("sales_train_defrag.csv", index=False)
#
# df = pd.read_csv("sales_train.csv")
# new = df['date'].str.split('.', expand = True)
# df['day'] = new[0]
# df['month'] = new[1]
# df['year'] = new[2]
# df = df.astype({"day" : "int32", "month": "int32", "year": "int32"})
# df = df.drop("date", axis=1)
# df.to_csv("sales_train_defrag.csv", index=False)

transactions = pd.read_csv("sales_train.csv")
new = transactions['date'].str.split('.', expand=True)
res = []
for d, m, y in zip(new[0].tolist(), new[1].tolist(), new[2].tolist()):
    res.append(datetime.date(int(d) - 1, int(m), int(y)))
transactions["date"] = res
transactions.to_csv("trans_datefor.csv", index=False)
