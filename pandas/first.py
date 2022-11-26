# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[22, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)

c = list(df)

for i in c:
    # printing the third element of the column
    print (df[i])