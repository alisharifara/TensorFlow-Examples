import tensorflow as tf

# W = Wx + b
W = tf.Variable([2.5, 4.0], tf.float32, name='var_W')
x = tf.placeholder(tf.float32, name='x')
b = tf.Variable([5.0, 10.0], tf.float32, name='var_b')

y = W * x + b

# initialize all variables defined
# it initializes all the variables that we have defined
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    print('Final Result :', sess.run(fetches=y, feed_dict={x: [10, 100]}))

# s= Wx
s = W * x

# initialize only variables that you might need
init = tf.variables_initializer([W])

with tf.Session() as sess:
    sess.run(init)

    # print('will this work? Wx+b ', sess.run(y, feed_dict={x: [10, 100]}))
    print(' result Wx', sess.run(s, feed_dict={x: [10, 100]}))

# update values
number = tf.Variable(2)
multiplier = tf.Variable(1)

init = tf.global_variables_initializer()

# assign new value to number variable
result = number.assign(tf.multiply(number, multiplier))

with tf.Session() as sess:
    sess.run(init)

    for i in range(10):
        print('the result of multiplication is:', sess.run(result))
        print('increment multiplier, new value', sess.run(multiplier.assign_add(1)))


writer = tf.summary.FileWriter('./m3_example4', sess.graph)
writer.close()

# then, we run in the terminal: tensorboard --logdir="m3_example4"
