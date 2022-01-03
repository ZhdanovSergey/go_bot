import numpy as np
from matplotlib import pyplot as plt
from dlgo.nn.load_mnist import load_data
from dlgo.nn.layers import sigmoid_double


def average_digit(data, digit):
	filtered_data = [x[0] for x in data if np.argmax(x[1]) == digit]
	return np.average(filtered_data, axis=0)

train, test = load_data()
avg_eight = average_digit(train, 8)

# img = (np.reshape(avg_eight, (28, 28)))
# plt.imshow(img)
# plt.show()

W = np.transpose(avg_eight)
b = -3 * 10**6

def predict(x, W, b):
	return sigmoid_double(np.dot(W, x) + b)

x_2 = train[2][0]
x_17 = train[17][0]

# print(predict(x_2, W, b))
# print(predict(x_17, W, b))

def evaluate(data, digit, treshold, W, b):
	total_samples = 1.0 * len(data)
	correct_predictions = 0

	for x in data:
		prediction = predict(x[0], W, b)
		is_label_equal = np.argmax(x[1]) == digit

		if prediction >= treshold and is_label_equal\
			or prediction < treshold and not is_label_equal:
			correct_predictions += 1

	return correct_predictions / total_samples

eight_test = [x for x in test if np.argmax(x[1]) == 8]
print('train_eval', evaluate(train, 8, 0.5, W, b))
print('test_eval', evaluate(test, 8, 0.5, W, b))
print('test_eight_eval', evaluate(eight_test, 8, 0.5, W, b))