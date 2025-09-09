import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
categories=['A','B','C']
values=[3,7,5]
plt.barh(categories,values,color=['blue','red','purple'])
plt.title("Horizontal Bar Plot")
plt.show()