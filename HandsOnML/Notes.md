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

* If we need to create a placeholder node, we need to call `tf.placeholder(type, shape)`, ``
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

# Chapter 10 Introduction to Artificial Neural Networks

## 10.1 From Biological to Artificial Neurons

* Reasons to believe this wave of ANN will be different: Huge data/computing power/small tweak of algorithm/local optima close to global optima/more money
* Most used activation functions:
    * logistic functions
    * hyperbolic tangent functions: tanh
    * Relu functions: fast to compute/doesn't have maximum output value

## 10.3 Training a DNN Using Plain TensorFlow

* `plain.ipynb`

1. construction phase
    1. The dimension of each layer, input layer, multiple hidden layers and output layer.
    2. `tf.placeholder` for `X` and `y`
    3. The actual network will be in a function
        * Initialize `W` to a truncated normal distribution so to converge faster
	* Initialize `b` to all zero
    4. But usually, don't need to define manully, there are many handy functions like: `fully_connected` 
    5. `tensorflow.contrib` package is experimental code, so might move in the future
    6. The next step is to define cost function.
       `tf.nn.sparse_softmax_cross_entropy_with_logits` and `tf.nn.softmax_cross_entropy_with_logits` takes care of softmax functions
       So we don't need to code them. The difference is the 1st takes in the label from 0 to number of classes - 1. The second takes one hot vector
    7. Next is define the optimizer.
    8. Last define the evaluation function.
    9. As usual, define initialier and saver.
2. execution phase
    1. Run initialier
    2. for each epoch and mini-batch, run `sess.run(training_op)`.
    3. Print accuracy after every epoch

## 10.4 Fine-Tuning Neural Network Hyperparameters

* Things you can change:
    * Network topology
    * # of layers
    * # of neurons
    * type of activation functions
    * weight initilization logic

## number of layers

* Training a large NN on huge dataset takes long time
* The benefits of multiple layers: parameter efficiency.
    * Can model the same complex functions with exponential less neurons.
* Lower level neurons model lower level structure
* Intermedia level neurons model Intermedia level structure
* High level neurons model High level structure
* The lower level can be reused for another problem
* Can reuse parts of a pretrained network.

## number of Neurons per hidden layer

* previous, people use size like a funnel
* Now, people tend to use the same neurons for each layer
* More layers are more important

## Activation Functions

* Hidden layer, relu is generally good
* output layer, none for regression, softmax for classification

# Chapter 11 Training Deep Neural Nets

## 11.0 Introduction

* 3 problems we are facing:
    * Vanishing gradients or exploding gradients which makes lower levels very hard to train.
    * Training will be very slow with large Networks.
    * Overfitting the training data.

## 11.1 Vanishing/Exploding Gradients Problems

* Gradients often get smaller and smaller as the algorithm progresses down to the lower layer.
* lower layer weight virtually unchanged.
* When opposite happens, it's exploding, usually happens in RNN.
* Xavier and Yoshua found the combination of sigmoid activation function and weight initilization be the problem
* The output layer variance is much bigger than the input layer

### Xavier and He initialization

* Xavier proposes the variance of ouput should be similar to that of input
* He propose Different initilization for different activation functions
* Default initialier for `fully_connected` layer in Xavier, if you want to change to
  He, you can do the 2 steps:
    * `he_init = tf.contrib.layers.variance_scaling_initializer()`, use `mode="FAN_AVG"`
    * `hidden1 = fully_connected(X, n_hidden1, weights_initializer=he_init, scope="h1")`

### Nonsaturating Activation Functions

* sigmoid -> ReLU -> Leaky ReLU, typically `alpha = 0.01` in leaky
* Problems with ReLU, dying ReLU:
    * When the neuron only output 0, because the weighted sum of inputs is negative.
* Exponential ReLU is also good (ELU):
    * Alleviate vanishing grad.
    * Avoid dying units issue
    * Smooth everywhere
* It's drawback is slow in computing gradients but faster in convergence.
  At test time, it's slower.
* General advice: ELU > leakyRelu > ReLu, but if cares more runtime, use leaky reLU.
* Tensor flow provide `elu()`, to use it:
    * `hidden1 = fully_connected(X, n_hidden1, activation_fn=tf.nn.elu)`
    * Have to define leaky relu ourself: `hidden1 = fully_connected(X, n_hidden1, activation_fn=leaky_relu)`

### Batch Normalization

* The technique consists of adding an operation in the model just before the activation function of each layer,
  simply zero-centering and normalizing the inputs, then scaling and shifting the result using two new parameters per layer (one for scaling, the other for shifting).
* Equation 11-3 for the details
* Four parameters are learned for each batch layer: gamma/beta/mu/sigma.
* Pro: Significantly improve training time. Also acts like a regulizer.
* Run-time penalty for each layer. If needs lightning-fast, then use ELU + He
* Implementation: `batch_norm.ipynb`
* Things to Note:
    * `is_training`: use the current mini-batch’s mean and standard deviation (during training),
      or the running averages that it keeps track of (during testing).
    * Since all layers needs `normalizer_fn`, we can put them in `tf.contrib.framework.arg_scope`
    * In the execution phase, we need to add `is_training`

### gradient clip

* Just limit the gradients to prevent from exploding
* `optimizer.minimize` will do 2 steps, compute the gradients and then apply them
* So we will clip the gradients before apply them:	
    * `grads_and_vars = optimizer.compute_gradients(loss)`
    * `capped_gvs = [(tf.clip_by_value(grad, -threshold, threshold), var) for grad, var in grads_and_vars]`
    * 
* example: `gradient_clip.ipynb`
