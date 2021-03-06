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

# Chapter 2 End-to-End ML Project

## Working with real data

* List all the website with data

## Looking at the Big Picture

### Frame the problem

* Machine Learning Project checklist see Appendix B
* How does the company expect to use and benefit from this model?
    * Boss's Answer: will be used in next stage of the pipeline
* pipeline:
    * Each stage: pulls in data -> process it -> spits out
    * Self contained so robust
    * Interface is data store
    * Broken component needs to be monitored properly
* What the current solution looks like? (reference performance)
    * Boss's Answer: Manual and Not great (15% error)
* Frame the problem
    * Supervised/Unsupervised/Reinforcement?
    * Classification/Regression?
    * Batch/Online?

### Select a performance Measure

* For regression: Root mean squre error (RMSE)
* Can also use Mean absolute error (MAE)
* RMSE: l2 norm, MAE: l1 norm and general `l_k` norm
* The higher the norm, more sensitive to outliers. So RMSE is more sensitive that MAE.

### Check the assumption

* It's important to list assumption we have
  can help find problem in early stage
* For example, we assume the downstream needs just the price, but what if they actually need
  just cheap/expensive, 2 categorical Variables.

## Get the Data

* fetch data should be one function: `fetch_housing_data`
* load data should be another function: `load_housing_data`

### Take a quick look at the data

* `housing.head()`
* `housing.info()`: how many rows, the data type of each attributes and # of non-null value
* Then if we find some categorical variables, we can use `pd.value_counts()`
    * `housing.ocean_proximity.value_counts()`
    * `housing['ocean_proximity'].value_counts()`
* Then we use `data.describe()` to show the numerical variables
* Next step is to use `housing.hist(bins=50, figsize=(20,15))` to do histogram
* Analyze the data
    * Has the data been preprocessed, e.g. capped?
    * The data has very different scale?
    * Not bell shape?

### Create a Test Set

* Generally, test set is 20%
* `sklearn` has the available function:
    * `train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)`
* stratified sampling on most important feature, i.e. `median_income`
    * step 1: scale it to 0 ~ 10
    * step 2: discretize it by using `np.ceil()`
    * step 3: merge everything above 5 to 5, with `where`
    * step 4: Now do the real staff

```
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index]
    strat_test_set  = housing.loc[test_index]
```

## Discover and Visualize the Data to Gain Insights

### Scatter plot

* Scatter plot:
    * `housing.plot(kind="scatter", x='longitude', y='latitude')`
    * color for high density: `housing.plot(kind="scatter", x='longitude', y='latitude', alpha=0.1)`
    * Much sofisticated example:

```
strat_train_set_copy.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4,
                          s=strat_train_set_copy.population/100,
                          c=strat_train_set_copy.median_house_value,
                          cmap=plt.get_cmap("jet"),
                          label="population", figsize=(15, 15),
                          colorbar=True)
plt.legend()
```

### Looking for Correlation

* First way, find correlation matrix `corr_matrix = house.corr(); corr_matrix.median_house_value.sort_values(ascending=False)`
* Second way, Use `from pandas.tools.plotting import scatter_matrix`
    * Looks like, in later `pandas`, it changes to `from pandas.plotting import scatter_matrix`.
    * Zoom in to see the promising variables
    * If correlation is strong, we can see clear upward or downward trend and points are not too dispersed
      like `median_income` and the `median_house_value`

### Experimenting with Attribute Combinations 

* We found the following two new varaiables are more informative than some of existing variables.
    * `housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]`
    * `housing["population_per_household"]=housing["population"]/housing["households"]`
* This step doesn't have to be thorough, we can come back later

## 2.5 Prepare the Data for Machine Learning Algorithms

### 2.5.1 Data Cleaning

* Since most machine learning algorithm cannot work with `NA` value, so we have the following strategies:
    * Drop the row where `total_bedrooms` is `NA`: `housing.dropna(subset=['total_bedrooms']).info()`
    * Drop the `total_bedrooms` column: `housing.drop('total_bedrooms', axis=1)`
    * Filla the `NA` with the `median` value: `housing['total_bedrooms'].fillna(housing['total_bedrooms'].median())`

* `Imputer` flow for data Cleaning

```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
housing_num = housing.drop("ocean_proximity", axis=1)
imputer.fit(housing_num)
imputer.statistics_
X = imputer.transform(housing_num)
housing_tr = pd.DataFrame(X, columns=housing_num.columns)
```

* `sklearn` Design
    * Consistency 
        * `Estimator`: estimate some parameters based on a dataset, like `imputer`
          It has `fit()` function, takes one dataset or two dataset in case of supervised learning.
          Hyperparameters like `strategy` is instance variables and usually set in constructor.
        * `Transformers`, like `imputer`, which has a `transform` function. Use `fit_transform` might
          run faster.
        * `Predictor`: has a `predict()` function.
    * Inspection: like `imputer.statistics_` and `imputer.strategy` are all instance variables.

### 2.5.2 Handling Text and Categorical Attributes

* We met 3 encoders from `sklearn.preprocessing`
    * `LabelEncoder` : convert text to label, the result after `fit_transform` is `numpy.ndarray`
        * `encoder.classes_` to check the classes
    * `OneHotEncoder` : convert label to one hot array, note we need to convert the above `numpy.ndarray` to 2-d
      with `numpy.ndarray.reshape(-1, 1)`
        * The output is `scipy.sparse.csr.csr_matrix`
        * We can convert to `ndarray` with `toarray()` function
    * `LabelBinarizer` : combine the above two.
        * The output is dense `numpy.ndarray`, which is not memory efficient.
        * We can make the output sparse by `LabelBinarizer(sparse_output=True)`

### 2.5.3 Customer Transformer

* We just need to provide our own `fit`, `transform` and `fit_transform` function.
* We need to make our class inherited from `BaseEstimator, TransformerMinMax`
    * `BaseEstimator` gives you free `get_params` and `set_params`
    * `TransformerMinMax`: gives you free `fit_transform` if you have `fit` and `transform`.
* Note in this example, the author uses `X = housing.values` to convert a DataFrame to an `np.ndarray`
    * This is consistent with the `transform` function output.
    * If we want to play with `DataFrame`, we can use
      `housing.iloc[:, [rooms_ix, bedrooms_ix, households_ix, population_ix]]`

### 2.5.4 Feature Scaling

* One of the most important transformation.
    * To find if data has different scales: `housing.describe()`
* 2 common ways
    * min-max scaling: `MinMaxScalar` with `feature_range` hyperparameter
    * standardization: mean 0, with unit variance
        * `StandardScalar`
        * might not work well for some Neural Network algorithm which expect `[0, 1]`.
* Sample code using `MinMaxScaler/StandardScaler` is like below, note we have to use `values` and `reshape` to
  get it work.

```python
from sklearn.preprocessing import MinMaxScaler

scalar = MinMaxScaler()
scalar.fit(housing["total_rooms"].values.reshape(-1, 1))
pd.DataFrame(scalar.transform(housing["total_rooms"].values.reshape(-1, 1))).describe()

count    16512.000000
mean         0.066560
std          0.054394
min          0.000000
25%          0.036552
50%          0.053759
75%          0.079743
max          1.000000
Name: total_rooms, dtype: float64

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
scalar.fit(housing["total_rooms"].values.reshape(-1, 1))
pd.DataFrame(scalar.transform(housing["total_rooms"].values.reshape(-1, 1)), columns=["total_rooms"])["total_rooms"].describe()

count    1.651200e+04
mean     8.606884e-17
std      1.000030e+00
min     -1.223689e+00
25%     -5.516890e-01
50%     -2.353301e-01
75%      2.423650e-01
max      1.716114e+01
Name: total_rooms, dtype: float64
```

### 2.5.5 Transformation Pipeline

* `scikit-learn` provides `Pipeline` class to combine them together.
* To initialize a `Pipeline`, give it a list of transformers and one `Estimator` at the very end
* When you call `fit` method of the pipeline, it will call `fit_transform()` of the `n-1` stage
  and `fit()` on the last stage
* When you call `fit_transform()`, it will call `fit_transform()` on all stages.
* Sample code is like the following
    * Use `np.array_equal` to verify

```python
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('attr_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler())
])

# Verify the pipeline version is the same as the stand alone version
X_pipeline = num_pipeline_stage1.fit_transform(housing_num)
X = imputer.transform(housing_num)
np.array_equal(X, X_pipeline)
```

* The above works for numerical features, we need to do the same for the categorical
  features.
* `sklearn` provides `FeatureUnion` to combine them together
* Note the code defined in the book has some problem
    * See this [discussion](https://stackoverflow.com/questions/46162855/fit-transform-takes-2-positional-arguments-but-3-were-given-with-labelbinarize)
      and see my fix below
    * The reason is in newer `sklearn`, `LabelBinarizer.fit()` can only take `X`
      But the `Pipeline` still pass `X, y` to it.
    * This is the reason this code `LabelBinarizer().fit_transform(DataFrameSelector(cat_attribs).fit_transform(housing))`
      works.

```python
class CustomizedLabelBinarizer(BaseEstimator, TransformerMixin):
    def __init__(self, sparse_output=False):
        self.encode = LabelBinarizer(sparse_output = sparse_output)
    def fit(self, X, y=None):
        return self.encode.fit(X)
    def transform(self, X):
        return self.encode.transform(X)

cat_pipeline = Pipeline([
    ('selector', DataFrameSelector(cat_attribs)),
    ('label_binarizer', CustomizedLabelBinarizer()),
])
```

* The usage is like below
    * I don't understand why the transformed data has 17 features, mine only has 16	
    * Maybe it has `add_bedrooms_per_room`

```python
from sklearn.pipeline import FeatureUnion

full_pipeline = FeatureUnion(transformer_list=[
    ('num_pipeline', num_pipeline),
    ('cat_pipeline', cat_pipeline),
])

housing_prepared = full_pipeline.fit_transform(housing)
```

## 2.6 Select and Train a Model

### 2.6.1 Training and Evaluating on the Training Set

* The sample code to use a linear regressiong model is below:

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)
housing_prediction = lin_reg.predict(housing_prepared)

# compute the rooted mean_squared_error
lin_mse = mean_squared_error(housing_prediction, housing_labels)
lin_rmse = np.sqrt(lin_mse)

```

* The sample code to use a more powerful tree model is almost the same:

```python
from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)
tree_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(tree_predictions, housing_labels)
tree_rmse = np.sqrt(tree_mse)
```

### 2.6.2 Better Evaluation Using Cross-Validation

* Use cross validation is also very easy

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
```

* Use Random forest

```python
from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor()
forest_reg.fit(housing_prepared, housing_labels)
forest_scores = cross_val_score(forest_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
display_scores(forest_rmse_scores)
```

* What we saw is the training error is still much smaller than the
  cross-validation error, meaning we are still overfitting.
    * make the model simpler
    * regulation
    * more training data
* But first thing is to try many more other models.
* Save and load model for future use

```python
from sklearn.externals import joblib
joblib.dump(forest_reg, 'forest_reg.pkl')
forest_reg_loaded = joblib.load('forest_reg.pkl')
```

## 2.7 Fine Tune your models

### 2.7.1 Grid Search

* Sample code like below

```python
from sklearn.model_selection import GridSearchCV
param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2,4,6,8]},
    {'bootstrap': [False], 'n_estimators': [3, 10, 30], 'max_features': [2,4,6,8]}
]
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv=5, scoring="neg_mean_squared_error")
grid_search.fit(housing_prepared, housing_labels)
```

* If not sure what grid to use, power of 10 is a good start, or a more fine number
  like in the example.
* Useful variable can be accessed directly:
    * `grid_search.best_params_`
    * `grid_search.best_estimator_`
    * `grid_search.cv_results_`: a dictionary, `mean_test_score` and `params` are important keys
* Grid search can do if use a feature or not, see exercise 5.

### 2.7.2 Random Search

* `RandomizedSearchCV`
* Usually good when search space is large, benefits
    * Seems like we can just give the hyperparameter, and give how many iterations we want.
      Don't have to give list for each hyperparameter.
    * We can control computing budget by change # of iterations.

### 2.7.4 Analyze the best models and their errors

* `feature_importances = grid_search.best_estimator_.feature_importances_`

### 2.7.5 Evaluate Your System on the Test Set

* The sample code

```python
final_model = grid_search.best_estimator_
X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set.median_house_value.copy()
X_test_prepared = full_pipeline.transform(X_test)

final_predictions = final_model.predict(X_test_prepared)
final_mse = mean_squared_error(final_predictions, y_test)
final_rmse = np.sqrt(final_mse)
final_rmse
```

## 2.8 Exercise

### 2.8.1 `GridSearchCV` with `SVM`

```python
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

param_grid = [
    {'kernel': ['linear'], 'C': [0.1, 1.0, 10.0]},
    {'kernel': ['rbf'], 'C': [0.1, 1.0, 10.0], 'gamma': np.logspace(-2, 2, 5)},
]

svm_reg = SVR()
grid_search = GridSearchCV(svm_reg, param_grid, cv=5, scoring="neg_mean_squared_error")

grid_search.fit(housing_prepared, housing_labels)

cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)
```

### 2.8.2 `RandomizedSearchCV`

### 2.8.4 Add one pipeline to predict

* My solution

```python
full_pred_pipeline = Pipeline([
    ('full_pipeline', full_pipeline),
    ('pred_pipeline', RandomForestRegressor()),
])

full_pred_pipeline.fit(housing, housing_labels)
forest_prediction_pipeline = full_pred_pipeline.predict(housing)
forest_rmse_pipeline = np.sqrt(mean_squared_error(forest_prediction_pipeline, housing_labels))
forest_rmse_pipeline
```

* Author's solution, note he is use the best solution in random search
  to initialize the `SVR`

```python
prepare_select_and_predict_pipeline = Pipeline([
    ('preparation', full_pipeline),
    ('feature_selection', TopFeatureSelector(feature_importances, k)),
    ('svm_reg', SVR(**rnd_search.best_params_))
])
```
### 2.8.5

* My solution

```python
full_pred_pipeline = Pipeline([
    ('full_pipeline', full_pipeline),
    ('pred_pipeline', RandomForestRegressor()),
])

param_grid = [
    {   'full_pipeline__num_pipeline__attr_adder__add_bedrooms_per_room' : [False, True],
        'pred_pipeline__n_estimators': [3, 10, 30], 'pred_pipeline__max_features': [2,4,6,8]},
]
```

* Author's solution

```python
param_grid = [{
    'preparation__num__imputer__strategy': ['mean', 'median', 'most_frequent'],
    'feature_selection__k': list(range(1, len(feature_importances) + 1))
}]
```

# Chapter 3 Classification

## 3.1 MNIST

* The steps to load the image

```python
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

some_digit = X[36000]
some_digit_image = some_digit.reshape((28, 28))
plt.imshow(some_digit_image, cmap = matplotlib.cm.binary, interpolation="nearest")
plt.axis('off')
plt.show()
```

* Split the train/test data:
    * the dataset has been arranged in the way such that [0:60000] is training data
      [60000:] is the testing data
    * Since the data is ordered, we need to shuffle it:

```python
shuffle_index = np.random.permutation(len(X_train))
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
```

## 3.2 Training a binary classifier

* We first to convert it to a binary classification problem: 5 or not 5.
  We can see the ratio is 1:10, which makes sense.

```python
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)
pd.Series(y_train_5.reshape(len(y_train_5),)).value_counts()	
False    54579
True      5421
dtype: int64
```

* Use `SGDClassifier` to train and predict
    * Note that in `predict`, we need to make the data to `some_digit.reshape(1, -1)`
      or `[some_digit]`

```python
from sklearn.linear_model import SGDClassifier

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)
sgd_clf.predict([some_digit])
```

## 3.3 Performance Measure

### 3.3.1 Measuring Accuracy Using Cross-Validation

* Creating cross validation data with `StratifiedKFold` instead of `cross_val_score`
  It's pretty much similar as `StratifiedShuffleSplit`

```python
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone

skfolds = StratifiedKFold(n_splits=3, random_state=42)
for train_index, test_index in skfolds.split(X_train, y_train_5):
    pass
```

* Now use `cross_val_score`, note in this case, the `scoring` is `'accuracy'`
  instead of `neg_mean_squared_error`

```python
from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, X_train, y_train_5.reshape(len(y_train_5,)), cv=3, scoring="accuracy")
```

* Define a dummy estimator, it's subclassing `BaseEstimator` 
    * The accuracy is > 90%

```python
from sklearn.base import BaseEstimator

class Never5Classifier(BaseEstimator):
    def fit(self, X, y=None):
        pass
    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)
```

### 3.3.2 Confusion matrix

* First we want to have the actual prediction for the training set,
  instead of just score, but we want the clean prediction,
  meaning a prediction on a instance which is not seen in training
  so we use `cross_val_predict`, like the following

```python
from sklearn.model_selection import cross_val_predict
y_train_predict = cross_val_predict(sgd_clf, X_train, y_train_5.reshape(len(y_train_5,)), cv=3)
```

* The we use `sklearn.metrics.confusion_matrix` to get
    * `True Negtive`
    * `False Negtive`
    * `True Positive`
    * `False Positive`

```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y_train_5, y_train_predict)

array([[53409,  1170],
       [  976,  4445]])
```

* The row is a class, row 0 is `False` or row 1 is `True`
* The col is a prediction, col 0 is predicting `False`, col 1 is predicting `True`
* Precision: `TP/(TP+FP)`
* Recall: `TP/(TP+FN)`
* F1 score

```python
from sklearn.metrics import precision_score, recall_score, f1_score
```

* Select which one depends on application
    * Video safe for kids: It's OK to have large `FN` but must have almost 0 `FP`
      so it's high precision / low recall
    * Catch shoplift: It's OK to have large `FP`, but should have low FN
      so it's low precision / high recall

### 3.3.3 Precision Recall Tradeoff

* Instead of `predict` function, we can call the `decision_function` to get the actual score
  and the 2nd line clearly shows the `decision_function` are `predict` are equivalent if use
  0 as the `threshold`.

```python
y_scores = sgd_clf.decision_function([some_digit])
np.array_equal(np.where(sgd_clf.decision_function(X_train) < 0, False, True), sgd_clf.predict(X_train))
```

* So how to decide which `threshold` is best?
    * The first step is to get the actual score
    * The 2nd step is to use `sklearn.metrics.precision_recall_curve`
    * The 3rd step is to plot

```python
y_scores = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, method="decision_function")

from sklearn.metrics import precision_recall_curve
precisions, recalls, thresholds = precision_recall_curve(y_train_5, y_scores)
```

* We can see the precision might be bumpy and recall is smooth
    * `TP/(TP+FP) = 1/(1+FP/TP)`, when threshold increase, both `TP` and `FP` goes down, so might not be monotonic
    * `TP/(TP+FN) = 1/(1+FN/TP)`, when threshold increase, `FN` increase, `TP` decrease, so it's monotonic

* Assume our task is to find a threshold to achieve 90% precision
    * We use `np.argmax` to find the threshold

```python
threshold_90_precision = thresholds[np.argmax(precisions >= 0.9)]
y_train_pred_90 = (y_scores >= threshold_90_precision)

print(precision_score(y_train_5, y_train_pred_90))
print(recall_score(y_train_5, y_train_pred_90))

0.9001403180542563
0.710016602102933
```

### 3.3.4 The ROC Curve

* receiver operating characteristic (ROC) curve: true positive rate against false positive rate
    * `FPR`: ratio of negtive instance that are incorrectly predicted as positive
    * `TNR`: ratio of negtive instance that are correctly predicted as positive, A.K.A specificity
    * `FPR = 1 - TNR`

```python
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)
```

* Use area under curve (AUC)
    * Perfect prediction will have `AUC = 1`
    * Purely random prediction will have `AUC = 0.5`

```python
from sklearn.metrics import roc_auc_score
roc_auc_score(y_train_5, y_scores)
```

* When to choose `PR`:
    * positive class is rare
    * care more false positive (movie for children) than false negative (shoplift)
* When to choose `ROC`
    * otherwise

* To use `RandomForestClassifier` to make prediction
    * Note here we need to get probability first, and then use probability as score

```python
from sklearn.ensemble import RandomForestClassifier
forest_clf = RandomForestClassifier(random_state=42)
y_probas_forest = cross_val_predict(forest_clf, X_train, y_train_5, cv=3, method='predict_proba')
y_scores_froest = y_probas_forest[:, 1]
```

## 3.4 Multiclass Classication

* Multiclass: Random forest / naive Bayes classifiers
* Binary classification: SVM / Linear
    * Convert binary to multiclass: 
        * Get 10 classifiers
        * Get the highest score
        * One versus all (OVA) AKA One versus the rest
    * One V.S. One (OVO)
        * Get one classifier for every pair of lables: 0 v.s. 1, 1 v.s. 2, etc
        * (N-1)*N/2 classifiers
        * In classification, each classifier will vote, the class gets the most votes wins
        * Good for algorithm that doesn't scale well with big dataset, e.g. SVM
    * For other binary classifications, OVA
* `sklearn` automatically detects multiclass and will perform OVA underhood
    * The training time is much longer
    * `sgd_clf.decision_function()` outputs a vector of 10 instead of a single number.
    * `sgd_clf.classes_` to show the classes

```
sgd_clf.fit(X_train, y_train)
sgd_clf.decision_function([some_digit])
sgd_clf.classes_
```

* We can manully use `OneVsOneClassifier` or `OneVsRestClassifier`
    * `ovo_clf.estimators_` shows the number of estimators is 45

```python
from sklearn.multiclass import OneVsOneClassifier
ovo_clf = OneVsOneClassifier(SGDClassifier(random_state=42))
ovo_clf.fit(X_train, y_train)
ovo_clf.predict([some_digit])
len(ovo_clf.estimators_)
```

* `RandomForestClassifier` automatically runs multiclass
    * use `forest_clf.predict_proba` to get the probability on each lables

* We can check the accuracy like the binary classifications

```python
cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy")
```

* We can simplely improve the accuracy by scaling the input
    * See also section 2.5.4

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

## 3.5 Error Analysis

* Again, we need to look at the Confusion matrix, but this time is 10X10 instead of 2X2
* So it's easier to look at it graphically
    * Using `plt.matshow(conf_mx, cmap=plt.cm.gray)`
* The steps to do the error analysis:
    1. Normalize the confusion matrix with row sum: `rowsum = conf_mx.sum(axis=1, keepdims=True)`
       and `norm_conf_mx = conf_mx / rowsum`
    2. To highlight the errors, make the diagnoal of the confusion matrix to be 0 
       `np.fill_diagonal(norm_conf_mx, 0)`
    3. `plt.matshow()`
    4. Then you can see which row/column is brighter than others, in the example of the book
       column 8 is brighter, which means other digits are classified as 8, then author gives
       3 suggestions:
        1. get more images looks like 8 but not, so let the classifier learn to distiguish them
           from real 8.
        2. engineer new features: write an algorithm to count the loops. And the number of loops
           becomes a new feature
        3. preprocessing the image, make some pattern to stand out more, like closed loops.
* Then the book plot the image for the following, which is pretty intresting
    * real 3, pred 3
    * real 3, pred 5
    * real 5, pred 3
    * real 5, pred 5
    * See the `plot_digits` function below

```python
def plot_digits(instances, images_per_row=10, **options):
    size = 28
    pad_num = len(instances) % images_per_row
    instances_pad = np.concatenate([instances, np.zeros((pad_num, size**2))])
    image = []
    for i in range(0, len(instances_pad), images_per_row):
        row_image = np.concatenate([j.reshape((size,size)) for j in instances_pad[i:i+images_per_row]], axis=1)
        image.append(row_image)
    image = np.concatenate(image)
    plt.imshow(image, cmap = matplotlib.cm.binary, interpolation="nearest")
    plt.axis('off')
```

* So why the linear model doesn't work well?
    * Because it assigns a weight to each pixel, 3 and 5's pixel are really similar.

## 3.6 Multilabel classification

* Sometimes we want more than one label
    * Face detection in photo app: recognize `['Alice', 'Bob', 'Charlie']`
      it should output `[1, 0, 1]`
* The example in the book created `y_train_large` and `y_train_odd`
  the code is straightforward

```python
from sklearn.neighbors import KNeighborsClassifier
y_multilabel = np.c_[y_train_larger, y_train_odd]
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_multilabel)
knn_clf.predict([some_digit])
```

*  The metrics for Multilabel classification
    * We use `f1_score`, the `average` options can be `macro` or `weighted`

```python
y_train_knn_pred = cross_val_predict(knn_clf, X_train, y_multilabel, cv=3)
f1_score(y_multilabel, y_train_knn_pred, average='macro')
```

## 3.7 Multioutput Classification

* So multioutput is the generalization version of Multilabel classification.
  In previous Multilabel classification, there are 2 labels, each lable can only be 0 or 1
* Now in multioutput classification, each lable can be more than 0 or 1
* Here is an example of multioutput classification, it filters noise of the original image
    * And the result image looks much cleaner

```python
noise = np.random.randint(0, 100, (len(X_train), 784))
X_train_mod = X_train + noise
noise = np.random.randint(0, 100, (len(X_test), 784))
X_test_mod = X_test + noise
y_train_mod = X_train
y_test_mod = X_test
knn_clf.fit(X_train_mod, y_train_mod)
```

## 3.8 Exercise

### ex 01

* First I learned from answer is `accuracy_score(knn_pred, y_test)`
* Second is for `GridSearchCV`, we can pass a `verbose=3` to print out more messages.

### ex02

* To initialize the model with optimal parameters found in previous `grid_search`
    * `knn_clf = KNeighborsClassifier(**grid_search.best_params_)`

### ex04

* One way to initialize a sparse matrix is like this, which is used in the solution
  to convert the word `Counter` to a matrix:

```python
rows = [0, 0, 0]
cols = [0, 0, 1]
data = [3, 2, 1]
m = csr_matrix((data, (rows, cols)), shape=(1, 2))
m.toarray()
```

* I cannot get the good results as the sample code

```python
# My results
Precision: 22.73%
Recall: 5.26%

# Sample results
Precision: 95.88%
Recall: 97.89%
```

# Chapter 4 Training Models

* Start with linear model
    * "closed-form" approach
    * iterative approach: gradient descent (GD) and its variants.
        * Batch GD
        * Mini-batch GD
        * Stochastic GD
* Polynomial Regression
    * More parameters so more prone to overfitting
    * Learning curve to detect overfitting
    * Regularization to reduce the risk of overfitting training data
* Logistic Regression and Softmax Regression

## 4.1 Linear Regression

### 4.1.1 Normal equation

* Memorize this equation, I call it manual approach:

```python
(X^T X)^{-1} X^T y

# code
np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

```

* Dimension
    * `X^T X` is `n x n` matrix
    * `(X^T X)^{-1} X^T` is `n x l` matrix
    * `(X^T X)^{-1} X^T y` is `n x 1` matrix

* Use `sklearn.linear_model.LinearRegression`, I call it automatical approach:

```python
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.intercept_, lin_reg.coef_)
```

* Internall, it calls `np.linalg.lstsq()`, we can call it directly.

```python
theta_best_svd, residules, rank, s = np.linalg.lstsq(X_b, y, rcond=None)
print(theta_best_svd)
```

* Or we can get the pseudoinverse like following 
    * It uses singular value decomposition (SVD)

```python
np.linalg.pinv(X_b).dot(y)
```

### 4.1.2 Computation Complexity

* Inverse the matrix: `O(n^{2.4}) ~ O(n^3)`
* SVD: `O(n^2)`

### 4.2 Gradient Descent

* If learning rate is too small: converge slow
* If learning rate is too big: make the algorithms diverge
* Not all cost functions are good, holes, ridges, plateaus
* MSE cost function is convex, gradient descent is guarantee to converge
    * learning rate is not too big
    * wait enough long time
* Using gradient descent needs to make sure features having similar scale
    * Use `StandardScalar`

### 4.2.1 Batch Gradient

* The gradient equation 4.5, see my notes in AML section 1.3
* The matrix version 4.6, see my notes in AML section 1.3

```python
# Equation: 2/m X^{T} (X \theta - y)
# Code:
gradient = 2. / m * X_b.T.dot(X_b.dot(theta) - y)
```

* Learning rate: use gird search
    * limit the number of iterations
* Number or iterations
    * set a large number at the beginning
    * stop the training early when the gradient is small
* `1/epsilon` iterations to reach `epsilon` range

### 4.2.2 Stochastic Gradient Descent

* Each step just pick one sample to do the gradient descent

```python
# Graident
gradient = 2 * (xi.dot(theta) - yi) * xi

# Complete code
for epoch in range(n_epochs):
    for i in range(m):
        random_index = np.random.randint(100)
        xi = X_b[random_index]
        yi = y[random_index]
        gradients = 2 * (xi.dot(theta) - yi) * xi
        eta = learning_schedule(epoch * m + i)
        theta = theta - eta * gradients.reshape(2,1)
```

* The cost function will bounce up and down. Finally, it will be close to optimal, but not optimal.
* Slow down the learning rate over the time.
* Iterate by `m` iterations, is call an epoch.
* If we want to make sure every sample is picked in one epoch, we need to shuffle the
  trainning set at the beginning of each epoch.
* Use `sklearn.linear_model.SGDRegressor`
    * `max_iter`: is the number of epoch
    * `tol`: the threshold hold of cost function to stop
    * `penalty`: Regularization
    * `eta0`: the initial learning rate, see the `doc` for more info

```python
from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, penalty=None, eta0=0.1)
sgd_reg.fit(X, y.ravel())
sgd_reg.coef_, sgd_reg.intercept_
```

### 4.2.3 Mini-Batch Gradient Descent

* Computes the gradients based on a small random subset of instances
    * Compare to SGD, have a performance boost with GPUs

## 4.3 Polynomial Regression

* It's essentially same as linear model and the code is here
    * Note the important thing here is `PolynomialFeatures`, it transforms `[x]` to `[x^2, x]`
    * If there are 2 features, it's able to get the interaction.

```python
from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)
```

## 4.4 Learning curve

* How can you tell your model is overfitting or underfitting?
    * One way is to use training
    * Another way is the learning curve
* Training error goes up as the training data grows
    * the model cannot fit a lot of data perfectly
* Validation error goes down
    * the model generalize better with more training data
* underfitting model:
    * Both curves reached plateau
    * They are close and fairly high
    * No use to add more training data
* overfitting model:
    * The error on training data is much lower than underfitting model.
    * There is a gap between train curve and validation curve. This is the hallmark of overfitting.
    * Increase training data can bring these 2 curves together.

### 4.4.1 Bias/Variance Tradeoff

* Generalization error = bias + variance + irreducible
* Bias error:
    * Wrong assumption, assume linear model but actually is quadratic model
    * high bias will underfit training data
* Variance error:
    * Excessive sensitive to variance in training data
    * Model with too much freedom is likely to have high variance, overfitting the
      training data
* Irreducible error:
    * Due to the noise of the data
    * Can only be reduced by cleaning the data: fix data source

## 4.5 Regulized Linear Model

### 4.5.1 Ridge Regression

* The cost function for Ridge Regression:

![alt text](./ch04/Equation_4_8.png "Logo Title Text 1")

* Very important: needs to scale the input data
  e.g. use `StandardScalar`. Most Regulized Model is sensitive to the scale
  of input data.
* Also very important, note the Regulized term doesn't include bias term.
* Three ways to perform ridge regression in `sklearn`
    * `Ridge` with `cholesky` solver
    * `Ridge` with `sag` solver
    * `SGDRegressor` with `penalty='l2'`

```python
from sklearn.linear_model import Ridge

ridge_reg = Ridge(alpha=1, solver='cholesky', random_state=42)
ridge_reg.fit(X, y)
print(ridge_reg.predict([[1.5]]))
print(ridge_reg.coef_, ridge_reg.intercept_)

ridge_reg = Ridge(alpha=1, solver='sag', random_state=42)
ridge_reg.fit(X, y)
print(ridge_reg.predict([[1.5]]))
print(ridge_reg.coef_, ridge_reg.intercept_)
from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(alpha=0.001, max_iter=5000, tol=-np.infty, penalty='l2', random_state=42)
sgd_reg.fit(X, y.ravel())
print(sgd_reg.coef_, sgd_reg.intercept_)
print(sgd_reg.predict([[1.5]]))
```

### 4.5.2 Lasso Regression

* The cost function for Ridge Regression:

![alt text](./ch04/Equation_4_10.png "Logo Title Text 1")

* The implementation is easy.
    * We can also use `SGDRegressor(penalty='l1')`

```python
from sklearn.linear_model import Lasso
lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X, y)
lasso_reg.predict([[1.5]])
```

* It tends to completely eliminate the weights of least important features.
* See my note on how to plot coutour plot

### 4.5.3 Elastic net

* The cost function for Elastic Net:

![alt text](./ch04/Equation_4_12.png "Logo Title Text 1")

* Always prefer to have some regularization
    * Ridge is a good default
    * If suspect only a few features useful, then Lasso or Elastic net
    * Elastic Net is always preferred over Lasso

* `sklearn` example

```python
from sklearn.linear_model import ElasticNet

elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic_net.fit(X, y)
elastic_net.predict([[1.5]])

```

### 4.5.4 Early Stopping

* Works for iterative learning algorithms such as Gradient Descent
* Stops training when validation error reaches minimum.
* For Stochastic and Mini-batch, the curves might be bumpy. So might
  need to wait the validation error for sometime.
* Note in the code below
    * when `warm_start` is `True`, and when calling `fit`, it continues
      from where it left.

```python
sgd_reg = SGDRegressor(
    max_iter=1,
    tol=-np.infty,
    penalty=None,
    eta0=0.0005,
    warm_start=True,
    learning_rate='constant',
    random_state=42)
```

## 4.6 Logistic Regression

### 4.6.1 Estimating Probabilities

![alt text](./ch04/Equation_4_13.png "Logo Title Text 1")

![alt text](./ch04/Equation_4_14.png "Logo Title Text 1")

### 4.6.2 Training and Cost Function

![alt text](./ch04/Equation_4_17.png "Logo Title Text 1")

![alt text](./ch04/Equation_4_18.png "Logo Title Text 1")

### 4.6.3 Decision boundaries

* Use `astype` to convert the data labels
* Use `log_reg.predict_proba` to get the probability

```python
y = (iris['target'] == 2).astype(int)
y_proba = log_reg.predict_proba(X_new)
```

* Logistic Regression can also be used with regularization
  instead of `alpha`, it uses `C` like the following.

```python
log_reg = LogisticRegression(solver='liblinear', C=10**10, random_state=42)
```

* Check out the 2 plots to see the plot related commands

### 4.6.4 Softmax Regression

* Computes score for each class

![alt text](./ch04/Equation_4_19.png "Logo Title Text 1")

* Computes probability use softmax function, a.k.a. normalized exponential

![alt text](./ch04/Equation_4_20.png "softmax")

* When in classification, use `argmax` to return the class that has the highest probability

![alt text](./ch04/Equation_4_21.png "argmax")

* Cross entropy is the cost function

![alt text](./ch04/Equation_4_22.png "Cross entropy")

* Gradient of cross entropy

![alt text](./ch04/Equation_4_23.png "Gradient of Cross entropy")

* Default Logistic uses one-versus-all, to use softmax, have to use:
    * `multi_class='multinomial'`
    * `solver='lbfgs'`

```python
softmax_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', C=10)
```

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
* So can be combined with `name_scope` to make graph much clearer.

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

## 11.2 Reusing Pretrained Layers

* Not a good idea to train from scratch, reuse the lower levels, called transfer learning.
    * Speed up training
    * require less training data
* Example: Have DNN to classify 100 objects, need to classify specific types of vehicles.
* Transfer learning will only work well if the inputs have simliar low-levle features.

### Reusing a TensorFlow Model

* build new model with same definition
* create initialier
* get a list of trainable variables and matches the regex
* a dictionary to map original name to new name, we want to keep the name the same
* A saver will restore and another saver to store the entire
* Start a session and init all variables and then restore the layer 1 to 3 in this example
* More similar jobs, more hidden layers to use. Very similar layer, just keep the output layer

### Reusing Models from Other Frameworks (skip for now)

* Tedious

### Freezing the Lower Layers

* The simplest solution is to give the optimizer the list of variables to train, excluding
  variables from lower level.

```
train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope="hidden[34]|outputs")
training_op = optimizer.minimize(loss, var_list=train_vars)
```

### Caching the frozen layers

* Since the lower levels are frozen, we can pre-compute the output of the hidden layers.

### Tweaking, Dropping, or Replacing the Upper Layers

* You want to find the right number of layers to use
* First try to use all layers
* Unfreeze one or two, the more data you have, more layers you can unfreeze.

### Model Zoos

* [tensorflow]( https://github.com/tensorflow/models)
* Caffe's model zoo
    * converter to tensorflow: https://github.com/ethereon/caffe-tensorflow

### Unsupervised Pretraining

* Don't have much labeled training data and cannot find a similar task
* First try to gather more labeled training data. 
* Complex task, no similar model, little labeled training data but plenty
  of unlabeled training data

## 11.3 Faster Optimizer

### Momentum optimization

* at each iteration, it adds the local gradient to momentum vector m
* The optimizer may overshoot a bit, then come back and overshoot again.
* `optimizer = tf.train.MomentumOptimizer(learning_rate=learning_rate, momentum=0.9)`

### RMSProp

* `optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate, momentum=0.9, decay=0.9, epsilon=1e-10)`

### Adam

* `optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)`, `learning_rate` is usually just
  0.001

All the algorithm discussed is based on first order, second order is too slow and might not fit in memory.

## Learning rate scheduing

* Different strategies to reduce the learning rate during training.
* predetermined piecewise constant learning rate
* performance/exponential/power scheduling
* AdaGrad, RMSProp, and Adam optimization automatically reduce the learning rate, no need for this step

## 11.4 Avoiding Overfitting Through Regularization

### Early stopping

* Interrupt training when its performance on validation set starts dropping
* Evaluate the model on a validation set at regular interval, e.g. 50 steps

### L1 and L2 Regularization

* use l1 and l2 Regularization to constrain weights, but not biases.
* sample code, only work for less layers.

```python
base_loss = tf.reduce_mean(xentropy, name="avg_xentropy")
reg_losses = tf.reduce_mean(tf.abs(weights1), tf.reduce_sum())
loss = tf.add(base_loss, scale * reg_losses, name="loss")
```

* General approach: TF automatically adds these nodes to a special collection
  containing all the regularization losses. You just need to not forget to add
  them to your losses, otherwise, they will be ignored.

```python
with arg_scope(
	[fully_connected],
	weights_regularizer=tf.contrib.layers.l1_regularizer(scale=0.01)):
    hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
    hidden2 = fully_connected(hidden1, n_hidden2, scope="hidden2")
    logits = fully_connected(hidden2, n_outputs, activation_fn=None, scope="out")

reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
loss = tf.add_n([base_loss] + reg_losses, name="loss")
```

### Drop-out

* `dropout.ipynb`
* Arguably most popular
* Every training step/every neuron has a probability p of being dropped-out.
* One way to understand the better performance:
    * Neurons trained with drop-out cannot co-adapt with their neighboring neurons,
      they have to be as useful as their own.
    * They cannot just rely excessively on a few input neurons, and have to pay attention
      to each of their input neurons.
    * less sensitive to slight changes and more robust which generalizes better.
* Another way to understand:
    * Each training step generates a unique NN, each NN is impossible to be sampled
      twice. They can be seen as an averaging ensemble of all smaller NN.
* One small but important technical details.
    * If `p = 50`, then during testing, a neuron will be connected to twice as many input
      neurons as it was.
    * To compensate, we need to multiply each neuron's input connection weights by `0.5 (1-p)`
      (which is called keep probability) after training.
    * Alternatively, we can divide each neuron's output by the keep probability during
      training.
* Sample code:

```python
from tensorflow.contrib.layers import dropout
[...]
is_training = tf.placeholder(tf.bool, shape=(), name='is_training')

keep_prob = 0.5
X_drop = dropout(X, keep_prob, is_training=is_training)

hidden1 = fully_connected(X_drop, n_hidden1, scope="hidden1")
hidden1_drop = dropout(hidden1, keep_prob, is_training=is_training)

hidden2 = fully_connected(hidden1_drop, n_hidden2, scope="hidden2")
hidden2_drop = dropout(hidden2, keep_prob, is_training=is_training)

logits = fully_connected(hidden2_drop, n_outputs, activation_fn=None,
                         scope="outputs")
```

* The difference between these 2 `dropout` functions:
    * `tensorflow.contrib.layers`: turns off 'no-op' when not training, we want to use this one.
    * `tensorflow.nn`: does not do that.
* `is_training` needs to be `True` in training and `False` in testing.
* Overfitting, increase the drop out rate, i.e. reduce `keep_prob`.
* slow down convergence, but generates much better model, it's worth to try.
    * Indeed, e.g. compare with `plain.ipynb`, the test accuracy:
      iter 0, 0.848 v.s. 0.901
      iter 50, 0.9686 v.s. 0.9764
      iter 100, 0.9745 v.s. 0.9775
    * Eventually, it beats no drop-out model: 0.9801 v.s. 0.9788

### Max-norm

* Another quite popular technique.
* It constrains the weights w of incoming connections such that ||w||\_2 <= r, which is 
  max-norm Hyperparameters.

### Data augmentation

* This is a test for source tree
