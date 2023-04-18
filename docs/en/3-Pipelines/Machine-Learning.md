# Machine Learning Models

Machine learning models are computational algorithms that are designed to automatically learn patterns and relationships from data. These models are trained on a dataset, which is typically a collection of examples or instances, each of which consists of a set of features or variables, as well as a target variable or output.

The goal of a machine learning model is to identify patterns and relationships within the data that can be used to make predictions or decisions about new, unseen data. This involves developing a mathematical representation of the relationship between the input features and the output variable, based on the patterns observed in the training data. Once the model is trained, it can be used to make predictions or decisions about new, unseen data.

There are several different types of machine learning models, each of which is designed to address different types of problems or data. Some of the most common types of machine learning models include:

1. **Regression Models:** Regression models are used to predict continuous numerical values, such as stock prices or housing prices.

2. **Classification Models:** Classification models are used to predict discrete categorical values, such as whether a customer will buy a product or not.

3. **Clustering Models:** Clustering models are used to identify groups or clusters within a dataset based on similarities between instances.

4. **Recommendation Models:** Recommendation models are used to recommend products or services to users based on their past behavior or preferences.

5. **Neural Networks:** Neural networks are a type of machine learning model that is designed to mimic the structure and function of the human brain. They are commonly used in image recognition, speech recognition, and natural language processing applications.

<!-- prettier-ignore -->
!!! info "Machine Learning Models Can be Biased"
    Machine learning models are a powerful tool for analyzing and making predictions about data, and they have a wide range of applications in fields such as finance, healthcare, marketing, and more. However, it is important to note that machine learning models are not perfect and can sometimes make errors or produce biased results. Therefore, it is important to carefully evaluate and test machine learning models before using them in real-world applications.

## Examples

### Linear Regression

![Linear Regression](../images/linear-regression.jpg)

<!-- prettier-ignore -->
!!! info "Linear Regression"
    $$
    \hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1 X_i + \hat{\epsilon}_i
    $$

    _Where $\hat{Y}_i$ denotes the $i$th estimator of the true value $Y$ based on the $i$th training epoch. Each $\hat{\beta}$ is a parameter to be learned. $\hat{\epsilon}_i$ is the amount of noise permitted in the model and may vary depending on the training epoch number denoted by $i$. Each $X_i$ represents the $i$th batch of training data._

In classical statistical models like linear regression, the goal is to find a line that best fits the data, allowing us to make predictions about new data points.

As the complexity of the problem increases, more sophisticated algorithms are needed, such as decision trees, support vector machines, and random forests. However, these methods have limitations, and they may not be able to capture complex patterns in large datasets.

#### Example Code

=== "Python"
    ``` py title="linear_regression.py" linenums="1"
    #!/usr/bin/env python

    # Load the required libraries
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

    # Load the dataset
    data = pd.read_csv('path/to/dataset.csv')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

    # Train the linear regression model
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = linear_model.predict(X_test)

    # Evaluate the model performance
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    print('Root Mean Squared Error:', rmse)
    ```

=== "R"
    ``` r title="linear_regression.r" linenums="1"
    #!/usr/bin/env Rscript
    
    # Set random seed for reproducibility
    set.seed(123)

    # Load the dataset
    data <- read.csv('path/to/dataset.csv')

    # Split the data into training and testing sets
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    train_data <- data[train_index,]
    test_data <- data[-train_index,]

    # Train the linear regression model
    lm_model <- lm(target_variable ~ ., data=train_data)

    # Make predictions on the testing set
    y_pred <- predict(lm_model, newdata=test_data[,-which(names(test_data)=='target_variable')])

    # Evaluate the model performance
    mse <- mean((y_pred - test_data$target_variable)^2)
    rmse <- sqrt(mse)
    print(paste('Root Mean Squared Error:', rmse))
    ```

### Support Vector Machine (SVM)

![Support Vector Machine](../images/svm.jpg)

<!-- prettier-ignore -->
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

#### Example Code

=== "Python"
    ``` py title="svm.py" linenums="1"
    #!/usr/bin/env python

    # Load the required libraries
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score

    # Load the dataset
    data = pd.read_csv('path/to/dataset.csv')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

    # Train the SVM model
    svm_model = SVC(kernel='linear', C=1.0, random_state=42)
    svm_model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = svm_model.predict(X_test)

    # Evaluate the model performance
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)
    ```
=== "R"
    ``` r title="svm.r" linenums="1"
    #!/usr/bin/env Rscript

    # Load the required libraries
    library(e1071)

    # Load the dataset
    data <- read.csv('path/to/dataset.csv')

    # Split the data into training and testing sets
    set.seed(123)
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    train_data <- data[train_index,]
    test_data <- data[-train_index,]

    # Train the SVM model
    svm_model <- svm(target_variable ~ ., data=train_data, kernel='linear', cost=1)

    # Make predictions on the testing set
    y_pred <- predict(svm_model, newdata=test_data[,-which(names(test_data)=='target_variable')])

    # Evaluate the model performance
    accuracy <- mean(y_pred == test_data$target_variable)
    print(paste('Accuracy:', accuracy))
    ```

### Random Forest

![Random Forest](../images/random-forest.jpg)

<!-- prettier-ignore -->
!!! note "Random Forest"
    $$
    \hat{y} = \frac{1}{T} \sum_{t=1}^{T} f_t(\mathbf{x}),
    $$

    _where $\hat{y}$ is the predicted output, $f_t(\mathbf{x})$ is the prediction of the $t$th tree in the forest for the input $\mathbf{x}$, and $T$ is the number of trees in the forest._

Random Forests are an ensemble learning method that can be used for classification and regression problems. They are often used for their ability to handle high-dimContinuous Improvement:ensional datasets and nonlinear relationships between features and targets.

Each tree is trained on a bootstrapped subset of the original training data, and at each split, a random subset of features is considered for determining the split. The final prediction is obtained by averaging the predictions of all the trees in the forest.

#### Example Code

=== "Python"
    ``` py title="random_forest.py" linenums="1"
    #!/usr/bin/env python

    # Load the required libraries
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error

    # Load the dataset
    data = pd.read_csv('path/to/dataset.csv')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

    # Train the random forest model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = rf_model.predict(X_test)

    # Evaluate the model performance
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    print('Root Mean Squared Error:', rmse)
    ```

=== "R"
    ``` r title="random_forest.r" linenums="1"
    #!/usr/bin/env Rscript

    # Load the required libraries   
    library(randomForest)

    # Load the dataset
    data <- read.csv('path/to/dataset.csv')

    # Split the data into training and testing sets
    set.seed(123)
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    train_data <- data[train_index,]
    test_data <- data[-train_index,]

    # Train the random forest model
    rf_model <- randomForest(target_variable ~ ., data=train_data, ntree=100, importance=TRUE)

    # Make predictions on the testing set
    y_pred <- predict(rf_model, newdata=test_data[,-which(names(test_data)=='target_variable')])

    # Evaluate the model performance
    mse <- mean((y_pred - test_data$target_variable)^2)
    rmse <- sqrt(mse)
    print(paste('Root Mean Squared Error:', rmse))
    ```

### Deep Learning

![Deep Learning](../images/deep-learning.jpg)

<!-- prettier-ignore -->
!!! note "Deep Learning"
    $$
    \hat{y} = f(\mathbf{W}_L f(\mathbf{W}_{L-1} f(\dots f(\mathbf{W}_1\mathbf{x}+\mathbf{b}_1)\dots)+\mathbf{b}_{L-1})+\mathbf{b}_L)
    $$

    _where $\mathbf{x}$ is the input vector, $\mathbf{W}_i$ and $\mathbf{b}_i$ are the weight matrix and bias vector, respectively, for the $i$th layer, and $f$ is the activation function._

    _This formula represents a feedforward neural network with $L$ layers, where each layer applies a linear transformation to the output of the previous layer, followed by a non-linear activation function. The output of the final layer, $\hat{y}$, represents the predicted output of the neural network for the given input $\mathbf{x}$._

Deep learning is a subset of machine learning that involves training neural networks with many layers of interconnected nodes. This approach can handle large and complex datasets and is used in a wide range of applications, including image recognition, natural language processing, and speech recognition. The training process involves feeding the neural network a large dataset and adjusting the weights of the connections between the nodes to minimize the error between the predicted outputs and the actual outputs. Through repeated iterations, the neural network can learn to recognize patterns in the data and make accurate predictions on new data.

#### Example Code

=== "Python"
    ``` py title="deep_learning.py" linenums="1"
    #!/usr/bin/env python

    # Load the required libraries
    import pandas as pd
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score

    # Load the dataset
    data = pd.read_csv('path/to/dataset.csv')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

    # Standardize the input features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define the deep learning model
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=[X_train_scaled.shape[1]]),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.1)

    # Evaluate the model performance
    y_pred = model.predict_classes(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)
    ```

=== "R"
    ``` r title="deep_learning.r" linenums="1"
    #!/usr/bin/env Rscript
        
    # Load the required libraries
    library(keras)
    library(tensorflow)

    # Load the dataset
    data <- iris
    x <- as.matrix(data[, 1:4])
    y <- to_categorical(as.numeric(data[, 5])-1)

    # Split the data into training and testing sets
    set.seed(123)
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    x_train <- x[train_index,]
    y_train <- y[train_index,]
    x_test <- x[-train_index,]
    y_test <- y[-train_index,]

    # Define the neural network architecture
    model <- keras_model_sequential() %>%
    layer_dense(units = 8, input_shape = c(4)) %>%
    layer_activation('relu') %>%
    layer_dense(units = 3) %>%
    layer_activation('softmax')

    # Compile the model
    model %>% compile(
    loss = 'categorical_crossentropy',
    optimizer = 'adam',
    metrics = c('accuracy')
    )

    # Train the model
    history <- model %>% fit(
    x_train, y_train,
    epochs = 50,
    batch_size = 10,
    validation_split = 0.2,
    verbose = 0
    )

    # Evaluate the model performance
    metrics <- model %>% evaluate(x_test, y_test)
    print(paste('Test Loss:', metrics[1]))
    print(paste('Test Accuracy:', metrics[2]))

    # Plot the training and validation accuracy over time
    plot(history$metrics$accuracy, type='l', col='blue', ylim=c(0,1), ylab='Accuracy', xlab='Epoch')
    lines(history$metrics$val_accuracy, type='l', col='red')
    legend('bottomright', legend=c('Training', 'Validation'), col=c('blue', 'red'), lty=1)
    ```
