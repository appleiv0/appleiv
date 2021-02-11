import csv
import numpy as np
import tensorflow as tf


# csv 불러오기
f = open('pcpdtsbt-oc.csv', 'r')
pcpdsbt = csv.reader(f)
headers=next(pcpdsbt)
#print(len(headers))
#print(headers)
new_data = []
for n, line in enumerate(pcpdsbt):
    new_data.append(line)
f.close()
#print(type(new_data))
data_set=np.array(new_data,dtype=np.float32)

#for n, line in enumerate(data_set):
#    X=np.array(line[:,:-1])
X=data_set[:,:-1]
Y=data_set[:,[-1]]
#print(Y)

W=tf.Variable(tf.random.normal([3,1]))
b=tf.Variable(tf.random.normal([1]))

learning_rate=0.0000001

def predict(X):
    return tf.matmul(X, W) + b

n_epochs = 50000
for i in range(n_epochs+1):
    # tf.GradientTape() to record the gradient of the cost function
    with tf.GradientTape() as tape:
        cost = tf.reduce_mean((tf.square(predict(X) - Y)))
        # calculates the gradients of the loss
        W_grad, b_grad = tape.gradient(cost, [W, b])
        # updates parameters (W and b)
        W.assign_sub(learning_rate * W_grad)
        b.assign_sub(learning_rate * b_grad)
    if i % 100 == 0:
       print("{:5} | {:10.4f}".format(i, cost.numpy()))
W.numpy()
b.numpy()
print(predict([[50,205.93,28.8]]).numpy())

