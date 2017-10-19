import  tensorflow as tf

hallo  = tf.constant('Hallo Schatze, ich bin Tensorflow!')


#start tf session
sess = tf.Session()

# Run the operation
print(sess.run(hallo))

