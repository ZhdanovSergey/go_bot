import numpy as np
import os


def load_data():
	f = np.load('dlgo/nn/mnist.npz')
	train_data = (f['x_train'], f['y_train'])
	test_data = (f['x_test'], f['y_test'])
	f.close()
	return shape_data(train_data), shape_data(test_data)

def shape_data(data):
	features = [np.reshape(x, (784, 1)) for x in data[0]]
	labels = [encode_label(y) for y in data[1]]
	return list(zip(features, labels))

def encode_label(j):
	e = np.zeros((10, 1))
	e[j] = 1.0
	return e