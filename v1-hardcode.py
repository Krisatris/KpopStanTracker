import numpy as np
import matplotlib.pyplot as plt

groups = np.array(["Hello Venus", "U-Kiss", "Shinee", "Infinite", "f(x)", "Vixx", "Block B", "Exo", "Mamamoo", "Loona", "Pixy", "OnlyOneOf"])
start_year = np.array([2013, 2013, 2013, 2013, 2013, 2013, 2013, 2013, 2014, 2016, 2022, 2023])
years_stanned = np.array([1, 2, 10, 10, 3, 6, 2, 2, 4, 6, 1, 1])
colors = np.array(['#99cc00', '#fe3391', '#01beb2', '#f5db8e', '#a4a6fc', '#082954', '#000000', '#c9cac5', '#ffffff', '#ffffff', '#ffffff', '#ffffff'])

barlist = plt.barh(groups, years_stanned, left=start_year, color=colors, edgecolor='black')
plt.title("Krisatris' Stan Hell")
plt.xlabel("Years")
plt.ylabel("Groups")
plt.xlim(2013, 2023)
plt.show()