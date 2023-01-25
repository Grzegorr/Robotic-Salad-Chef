import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Extracted from matlab code
batch1_before_markov = [
    [243,     0,     0,     0,     0,     0,     5],
    [27,   17,     0,     0,     0,     0,     0],
    [20,     0,    43,     0,     0,    0,     0],
    [7,     1,     0,    46,     0,     0,     0],
    [9,     0,     0,     0,    22,    0,     0],
    [12,     0,     0,     0,     0,    37,     0],
    [162,     0,     0,     1,     1,     0,   401]
]

batch1_after_markov = [
    [243,     0,     0,     0,     0,     0,     5],
    [10,    34,    0,     0,     0,     0,     0],
    [6,     0,    49,     0,     0,     0,     8],
    [4,     0,     0,    50,     0,     0,     0],
    [2,     0,     0,     0,    26,     0,     3],
    [7,     0,     0,     0,     0,   40,     2],
    [22,     2,     0,     6,     1,     0,   534]
]

batch2_before_markov = [
    [379,     0,     0,    0,     0,     0,     5],
    [27,    17,     0,     0,     0,     0,     0],
    [44,     0,    43,     0,     0,     0,    0],
    [15,     9,     0,    54,     0,     0,     0],
    [9,     0,     0,     0,    22,     0,     0],
    [12,     0,     0,     0,     0,    37,     0],
    [202,     0,     0,     1,     1,     0,   609]
]

batch2_after_markov = [
    [379,     0,     0,     0,     0,     0,     5],
    [10,    34,     0,     0,     0,     0,     0],
    [30,     0,    57,     0,     0,     0,     0],
    [3,     0,     0,    65,     0,     0,    10],
    [2,     0,     0,     0,    26,     0,     3],
    [7,     0,     0,     0,    0,    40,    2],
    [30,     2,    11,     0,     1,     0,   769]
]

before_markov = np.add(np.array(batch1_before_markov), np.array(batch2_before_markov))
after_markov = np.add(np.array(batch1_after_markov), np.array(batch2_after_markov))

before_markov = before_markov.transpose()
after_markov = after_markov.transpose()





#confusion_matrix_before = [
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7]
#]
#print(confusion_matrix)


sns.set(font_scale=2.2)

labels = ["Nothing", "Broccoli", "Carrot", "Apple", "Banana", "Orange", "Knife"]
plt.figure(figsize=(14, 10))
plt.title("Handled Object Identification Confusion Matrix before HMM filtering", fontsize = 24, y = 1.1)
heat = sns.heatmap(before_markov, fmt = "d", vmax = 100, annot = True, xticklabels = labels, yticklabels = labels)
heat.set_xlabel("Ground Truth for Item Handled", fontsize = 20)
heat.set_ylabel("Prediction for Item Handled before HMM", fontsize = 20)
heat.xaxis.set_label_position('top')
plt.tick_params(axis='both', which='major', labelsize=20, labelbottom=False, bottom=False, top=False, labeltop=True)
plt.show()




#confusion_matrix = [
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7],
#[1, 2, 3, 4, 5, 6, 7]
#]
#print(confusion_matrix)


labels = ["Nothing", "Broccoli", "Carrot", "Apple", "Banana", "Orange", "Knife"]
plt.figure(figsize=(14, 10))
plt.title("Handled Object Identification Confusion Matrix - HMM filtered", fontsize = 22, y = 1.1)
heat = sns.heatmap(after_markov, fmt = "d", vmax = 100, annot = True, xticklabels = labels, yticklabels = labels)
heat.set_xlabel("Ground Truth for Item Handled", fontsize = 20)
heat.set_ylabel("Prediction for Item Handled after HMM", fontsize = 20)
heat.xaxis.set_label_position('top')
plt.tick_params(axis='both', which='major', labelsize=20, labelbottom=False, bottom=False, top=False, labeltop=True)
plt.show()
