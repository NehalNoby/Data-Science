import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.DataFrame({
    'Category':['A','B','C','D'],
    'Values':[4,7,2,9]})
sns.barplot(x='Category',y='Values',data=data)
plt.title("Normal Bar Plot(Seaborn)")
plt.show()