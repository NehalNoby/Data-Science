import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
sns.countplot(x="day",data=df,palette="Set2")
plt.title("Count Plot") 
plt.show()

