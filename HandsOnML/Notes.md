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
