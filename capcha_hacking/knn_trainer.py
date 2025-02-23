import os
import cv2
import numpy as np

file_names = list(range(0, 13))
train = []
train_labels = []

for file_name in file_names:
    path = '../training_data/' + str(file_name) + '/'
    file_count = len(next(os.walk(path))[2])
    for i in range(1, file_count + 1):
        img = cv2.imread(path + str(i) + '.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        train.append(gray)
        train_labels.append(file_name)
x = np.array(train)
train = x[:, :].reshape(-1, 400).astype(np.float32)
train_labels = np.array(train_labels)[:, np.newaxis]

np.savez("trained.npz", train=train, train_labels=train_labels)