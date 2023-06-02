# Task 44


from sklearn.preprocessing import LabelBinarizer
import pandas as pd

df = pd.DataFrame({'Категория': ['A', 'B', 'C', 'A', 'B', 'C']})

binarizer = LabelBinarizer()

one_hot_encoded = pd.DataFrame(binarizer.fit_transform(df['Категория']), columns=binarizer.classes_)

df_encoded = pd.concat([df, one_hot_encoded], axis=1)

print(df_encoded)

