import numpy as np
import pandas as pd
np.random.seed(0)
# transactions
left_df = pd.DataFrame({'transaction_id': ['A', 'B', 'C', 'D'], 'user_id': ['Peter', 'John', 'John', 'Anna'],'value': np.random.randn(4),})
# users
right_df = pd.DataFrame({'user_id': ['Paul', 'Mary', 'John','Anna'],'favorite_color': ['blue', 'blue', 'red', np.NaN],})


#left join example
left_df.merge(right_df, on='user_id', how='left')


#drop column
df.drop(columns=['B', 'C'])
