from __future__ import print_function

import tensorflow as tf

with tf.Session() as sess:
    # Create a simple computation graph to add two constants
    a = tf.constant([1.0, 1.0])
    b = tf.constant([2.0, 2.0])
    c = tf.add(a, b)

    # Evaluate and print the result
    result = c.eval()
    print("a+b = ", result)

    # Write summaries for tensorboard
    file_writer = tf.summary.FileWriter('logs', sess.graph)
