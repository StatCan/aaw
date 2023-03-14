# Machine Learning Models

## Linear Regression

![Linear Regression](../images/linear-regression.jpg)

!!! info "Linear Regression"
    $$
    \hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1 X_i + \hat{\epsilon}_i
    $$

    _Where $\hat{Y}_i$ denotes the $i$th estimator of the true value $Y$ based on the $i$th training epoch. Each $\hat{\beta}$ is a parameter to be learned. $\hat{\epsilon}_i$ is the amount of noise permitted in the model and may vary depending on the training epoch number denoted by $i$. Each $X_i$ represents the $i$th batch of training data._

In classical statistical models like linear regression, the goal is to find a line that best fits the data, allowing us to make predictions about new data points.

As the complexity of the problem increases, more sophisticated algorithms are needed, such as decision trees, support vector machines, and random forests. However, these methods have limitations, and they may not be able to capture complex patterns in large datasets.

## Support Vector Machine (SVM)

![Support Vector Machine](../images/svm.jpg)

!!! note "SVM"
    $$
    \underset{\mathbf{w},b,\boldsymbol{\xi}}{\operatorname{minimize}} \hspace{0.2cm} \frac{1}{2} ||\mathbf{w}||^2 + C \sum_{i=1}^{N} \xi_i
    $$

    $$
    \text{where} \hspace{0.2cm} y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1-\xi_i \quad \text{and} \quad \hspace{0.2cm} \xi_i \geq 0 \hspace{0.2cm} \forall i \in {1,2,...,N}
    $$

    _In this formula, we use the standard SVM formulation where $\mathbf{w}$ is the weight vector, $b$ is the bias term, and $\boldsymbol{\xi}$ is the slack variable vector. The objective is to minimize the L2-norm of the weight vector $\mathbf{w}$, subject to the constraint that all training examples are classified correctly with a margin of at least 1, plus an allowance for some margin violations controlled by the regularization parameter $C$. The target variable $y_i$ takes values of either 1 or -1, representing the two classes in the binary classification problem, and $\mathbf{x}_i$ is the feature vector for the $i$th training example._

A support vector machine (SVM) is a supervised machine learning algorithm that can be used for classification, regression, and outlier detection. It is a popular algorithm in the field of machine learning, especially for solving classification problems.

The basic idea behind SVM is to find a hyperplane that best separates the input data into different classes. In a two-class classification problem, the hyperplane is a line that divides the data points of one class from the data points of the other class. SVM tries to find the hyperplane that maximizes the margin between the two classes, where the margin is the distance between the hyperplane and the nearest data points from each class.

## Random Forest

![Random Forest](../images/random-forest.jpg)

!!! note "Random Forest"
    $$
    \hat{y} = \frac{1}{T} \sum_{t=1}^{T} f_t(\mathbf{x}),
    $$

    _where $\hat{y}$ is the predicted output, $f_t(\mathbf{x})$ is the prediction of the $t$th tree in the forest for the input $\mathbf{x}$, and $T$ is the number of trees in the forest._

Random Forests are an ensemble learning method that can be used for classification and regression problems. They are often used for their ability to handle high-dimensional datasets and nonlinear relationships between features and targets.

Each tree is trained on a bootstrapped subset of the original training data, and at each split, a random subset of features is considered for determining the split. The final prediction is obtained by averaging the predictions of all the trees in the forest.

## Deep Learning

![Deep Learning](../images/deep-learning.jpg)

!!! note "Deep Learning"
    $$
    \hat{y} = f(\mathbf{W}_L f(\mathbf{W}_{L-1} f(\dots f(\mathbf{W}_1\mathbf{x}+\mathbf{b}_1)\dots)+\mathbf{b}_{L-1})+\mathbf{b}_L)
    $$

    _where $\mathbf{x}$ is the input vector, $\mathbf{W}_i$ and $\mathbf{b}_i$ are the weight matrix and bias vector, respectively, for the $i$th layer, and $f$ is the activation function._

    _This formula represents a feedforward neural network with $L$ layers, where each layer applies a linear transformation to the output of the previous layer, followed by a non-linear activation function. The output of the final layer, $\hat{y}$, represents the predicted output of the neural network for the given input $\mathbf{x}$._

Deep learning is a subset of machine learning that involves training neural networks with many layers of interconnected nodes. This approach can handle large and complex datasets and is used in a wide range of applications, including image recognition, natural language processing, and speech recognition. The training process involves feeding the neural network a large dataset and adjusting the weights of the connections between the nodes to minimize the error between the predicted outputs and the actual outputs. Through repeated iterations, the neural network can learn to recognize patterns in the data and make accurate predictions on new data.