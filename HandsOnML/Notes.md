# Preface

* Most problems can be solved quite well using random forest and ensemble
* DL is best when you have enough data, computing power and patience
* https://github.com/ageron/handson-ml 

# Chapter 1 The ML landscape

* What is ML: programming computer so they can learn from data.
    * Another one: task T (filter spam email), experience E (training data), performance P (accuracy)
* Why is ML 
    * Consider email filter, program will become long list of rules.
    * ML based approach, short, easy to maintain, can be updated without your intervention
    * For problems that is too hard for traditional approach.
    * ML can help human to learn, reveal new trends and lead to better understanding.
* ML is great for:
    * require a lot of hand tuning and long lists of rules
    * complex problems
    * adapt to new data
    * getting insight to complex problems and large amount of data.

## Different types

* Whether with human supervision (supervised/unsupervised/semisupervised/reinforcement)
* Whether On the fly 
* Instance or model - based

* Important supervised method: KNN, linear/logistic regression, SVM, Decision tree and random forest, NN
* unsupervised method: clustering, visulization and dimension reduction (PCA, kernel PCA etc.)
    * visualization, input unlabeled data and output 2-D or 3-D easy to plot, easy to understand how data organized and
      identify suspicious patterns
* dimension reduction: often good to use before sending to another ML algorithm. Run faster, less disk/memory, sometimes better results
* anomaly detection, also unsupervised
* association rule learning: customer buy barbecue source and potato chips tend to by steak
* semisupervised learning, a lot of unlabeled data + some labeled data. 
    * photo service: unsupervised part, identify which person in which photos. supervised part, ask you to label them.
    * deep belief network + restricted boltzmann network
* reinforcement learning:
    * Observe environment, perform actions, get rewards (AlphaGo)

### Batch learning and online learning

* batch learning
    * unable to learn incrementally, if retrain, take long time and lots of computing resources
* online learning
    * still done offline, use mini-batch data
    * Learning rate, how fast it adapts to new data
    * bad data feed into system, then performance degrades  

### Instance based and Model based

* Instance based: remember the instance and use the most similar instance to make prediction
* Model based: like linear regression.

# Chapter 9 Up and Running with TF 

* First define a python graph of computation to perform
* Possible to run them in different CPU and GPUs
* Millions of parameters + Billions of training data + Millions of features
* clean, scalable, flexible, production-ready
* Big commnunity:
    * Great projects on top of it: https://www.tensorflow.org/ , https://github.com/jtoy/awesome-tensorflow
    * Question: http://stackoverflow.com/ with tag tensorflow
    * bugs and features: github
    * General discussion: google group
* First example (`firstex.py`):
    * build the graph
    * open a tensorflow session, `sess = tf.Session()`, which place operations on devices like CPU/GPU
    * Initialize `x, y`, run the graph `f`.
    * Can also use `with tf.Session() as sess`
    * To Initialize, define a init node `init = tf.global_variables_initializer()`
    * In Ipython or Jupyter, you can do `tf.InteractiveSession()`
* Two phases:
    * Construction phase builds computation graph
    * Execution phase

## Managing Graph

* create graph `graph = Graph()`
* Set graph as default graph: `with graph.as_default()`, `tf.get_default_graph()`
* `tf.reset_default_graph()`

## Lifecycle

* All nodes value dropped between different graph run
* if want to save the common computation, needs to run 2 graphs at the sanme time: `y_val, z_val = sess.run([y, z])`

## LR with TF

* TF operations (ops)
* Variable and constants without inputs : source op
* Inputs/outputs multi-dimension: tensors

## Implementing gradient descent

* The key step in manual updating is to update theta: `training_op = tf.assign(theta, theta - learning_rate * gradients)`
* If use autodiff, then gradient becomes `gradients = tf.gradients(mse, [theta])[0]`
* If use optimizer:
    * `optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)`
    * `training_op = optimizer.minimize(mse)`

## Feeding data to training algorithm

* If we need to create a placeholder node, we need to call `tf.placehoder(type, shape)`, ``
* can be used for mini batch `house_gd_minibatch.py`
    * `X = tf.placeholder(dtype=tf.float32, shape=(None, n+1), name='X')`
    * `y = tf.placeholder(dtype=tf.float32, shape=(None, 1), name='y')`
    * `X_batch, y_batch = fetch_batch(epoch, batch_index, batch_size)`
    * `sess.run(training_op, feed_dict={X: X_batch, y: y_batch})`

## Saving and restoring Models

* use it in another program
* save it every other iterations in case computer crashes
* create a node: `saver = tf.train.Saver()`
* save the model: `save_path = saver.save(sess, "/tmp/my_model_final.ckpt")`
* restore it: `saver.restore(sess, "/tmp/my_model_final.ckpt")`
* only save one variable: `saver = tf.train.Saver({"weights": theta})`

## Visualization

* `house_gd_tensorboard.py`
* only safari shows the graph
* At the end Construction phase
    * `mse_summary = tf.summary.scalar('MSE', mse)`
    * `file_writer = tf.summary.FileWriter(log_dir, tf.get_default_graph())`, creates the dir/writes the graph definition
* When you need to dump the data
    * `summary_str = mse_summary.eval()`
    * `file_writer.add_summary(summary_str, epoch)`
* Then in the terminal, do `tensorboard --logdir tf_logs`
* In Jupyter, you can also do `show_graph()` to show the graph structure

##  Name scopes

* `house_gd_namescope.py`
* `with tf.name_scope('loss') as scope:`
* `print(error.op.name)`
* `print(mse.op.name)`
* Then in the tensorboard, we can see the nodes of error and mse are grouped together.

## Modularity

* `relu_mod.py` 
* We can define the function
* `tf.add_n` is useful to add a list of nodes
* When creating a node, tensorflow will add `_1`, `_2` if a variable name is already there.
* So can be combined with name_scope to make graph much clearer.

## Sharing Variables

* Approach 1: Add the variable as an argument for the function (`sharing_func.py`)
    * Note if you need to change the variable threshold, you need to do `assign_op = threshold.assign(5)`
    * https://stackoverflow.com/questions/34220532/how-to-assign-a-value-to-a-tensorflow-variable
* Similar approach, python dictionary and class
* Tensorflow's approach: `sharing_get_variable.py`, `sharing_get_variable_2.py`
    * create a threshold variable with `tf.get_variable()` within `with tf.variable_scope()`
    * get the variable again with `tf.get_variable('threshold')` in the `relu` function
    * The reason I cannot get this code work because I defined the `threshold` too late in the script
      after the `add_n`
    * A similar way to define threshold inside `relu` function can be found in `sharing_get_variable_2.py`.

