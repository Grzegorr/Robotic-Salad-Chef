import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Extracted from matlab code
batch1_before_markov = [
    [379, 0, 0, 0, 0, 0, 5],
    [9, 22, 0, 0, 0, 0, 0],
    [15, 0, 54, 0, 9, 0, 0],
    [12, 0, 0, 37, 0, 0, 0],
    [27, 0, 0, 0, 17, 0, 0],
    [44, 0, 0, 0, 0, 43, 0],
   [202, 1, 1, 0, 0, 0, 609]
]

batch1_after_markov = [
    [379, 0, 0, 0, 0, 0, 5],
    [2, 26, 0, 0, 0, 0, 3],
    [3, 0, 65, 0, 0, 0, 10],
    [7, 0, 0, 40, 0, 0, 2],
    [10, 0, 0, 0, 34, 0, 0],
    [30, 0, 0, 0, 0, 57, 0],
    [30, 1, 0, 0, 2, 11, 769]
]

batch2_before_markov = [
    [243, 0, 0, 0, 0, 0, 5],
    [9, 22, 0, 0, 0, 0, 0],
    [7, 0, 46, 0, 1, 0, 0],
    [12, 0, 0, 37, 0, 0, 0],
    [27, 0, 0, 0, 17, 0, 0],
    [20, 0, 0, 0, 0, 43, 0],
    [162, 1, 1, 0, 0, 0, 401]
]

batch2_after_markov = [
    [243, 0, 0, 0, 0, 0, 5],
    [2, 26, 0, 0, 0, 0, 3],
    [4, 0, 50, 0, 0, 0, 0],
    [7, 0, 0, 40, 0, 0, 2],
    [10, 0, 0, 0, 34, 0, 0],
    [6, 0, 0, 0, 0, 49, 8],
    [22, 1, 6, 0, 2, 0, 534]
]

before_markov = np.add(np.array(batch1_before_markov), np.array(batch2_before_markov))
after_markov = np.add(np.array(batch1_after_markov), np.array(batch2_after_markov))





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

labels = ["Nothing", "Broccoli", "Carrot", "Apple", "Banana", "Orange", "Knife"]
plt.figure(figsize=(12, 8))
plt.title("Handled Object Identification Confusion Matrix after Pearsons Correlation")
sns.heatmap(before_markov, fmt = "d", vmax = 100, annot = True, xticklabels = labels, yticklabels = labels)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False, labeltop=True)
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
plt.figure(figsize=(12, 8))
plt.title("Handled Object Identification Confusion Matrix - HMM filtered")
sns.heatmap(after_markov, fmt = "d", vmax = 100, annot = True, xticklabels = labels, yticklabels = labels)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False, labeltop=True)
plt.show()
