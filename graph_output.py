import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

url = 'tabl.csv'

df = pd.read_csv(url, names=['iks', 'igrek'], decimal=',')
#df = pd.read_csv(url, names=['iks', 'igrek'], sep=';', decimal=',')
# df = pd.read_csv(url, names=['val','date'], index_col=[1], decimal=',')
#df.plot()
df.plot.scatter(x='iks', y='igrek');
plt.show()
