import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


X_corr = [
[ 1 , 0.68  , 0.042  , 0.1  ],
[ 0.68 ,  1 ,  0.17 , 0.26  ],
[ 0.042 , 0.17  ,  1 ,  0.39 ],
[ 0.1 ,  0.26  , 0.39  ,  1 ]
]

Y_corr = [
[ 1 , 0.61  , -0.022  , 0.41  ],
[ 0.61 ,  1 ,-0.028   , 0.46  ],
[ -0.022 , -0.028  ,  1 ,  0.12 ],
[ 0.41 ,  0.46 , 0.12  ,  1 ]
]

XY_corr = [
[ 1 , 0.42  ,  0 , 0.042  ],
[ 0.42 ,  1 , 0  , 0.12  ],
[ 0 ,  0 ,  1 , 0.047  ],
[ 0.042 ,0.12,0.047 ,  1 ]
]


sns.set(font_scale=2.2)

labels = ["Cup", "Right Hand", "Chair", "Left Hand"]
plt.figure(figsize=(12, 11))
plt.title("Correlations between Items' Paths\n(X direction)", fontsize = 28, y = 1.055)
heat = sns.heatmap(X_corr,vmin = 0, vmax = 1, annot = True, xticklabels = labels, yticklabels = labels)
heat.xaxis.set_label_position('top')
plt.tick_params(axis='both', which='major', labelsize=22, labelbottom=False, bottom=False, top=False, labeltop=True)
plt.show()

labels = ["Cup", "Right Hand", "Chair", "Left Hand"]
plt.figure(figsize=(12, 11))
plt.title("Correlations between Items' Paths\n(Y direction)", fontsize = 28, y = 1.055)
heat = sns.heatmap(Y_corr,vmin = 0, vmax = 1, annot = True, xticklabels = labels, yticklabels = labels)
heat.xaxis.set_label_position('top')
plt.tick_params(axis='both', which='major', labelsize=22, labelbottom=False, bottom=False, top=False, labeltop=True)
plt.show()

labels = ["Cup", "Right Hand", "Chair", "Left Hand"]
plt.figure(figsize=(12, 11))
plt.title("Correlations between Items' Paths\n(multiplied)", fontsize = 28, y = 1.055)
heat = sns.heatmap(XY_corr,vmin = 0, vmax = 1, annot = True, xticklabels = labels, yticklabels = labels)
heat.xaxis.set_label_position('top')
plt.tick_params(axis='both', which='major', labelsize=22, labelbottom=False, bottom=False, top=False, labeltop=True)
plt.show()