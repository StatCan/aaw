# Modèles d'apprentissage automatique

Les modèles d'apprentissage automatique sont des algorithmes de calcul conçus pour apprendre automatiquement des modèles et des relations à partir de données. Ces modèles sont entraînés sur un ensemble de données, qui est généralement une collection d'exemples ou d'instances, chacun d'entre eux se composant d'un ensemble de fonctionnalités ou de variables, ainsi que d'une variable cible ou d'une sortie.

L'objectif d'un modèle d'apprentissage automatique est d'identifier des modèles et des relations au sein des données qui peuvent être utilisés pour faire des prédictions ou des décisions concernant de nouvelles données invisibles. Cela implique de développer une représentation mathématique de la relation entre les caractéristiques d'entrée et la variable de sortie, sur la base des modèles observés dans les données d'apprentissage. Une fois le modèle entraîné, il peut être utilisé pour faire des prédictions ou prendre des décisions concernant de nouvelles données inédites.

Il existe plusieurs types de modèles d'apprentissage automatique, chacun étant conçu pour traiter différents types de problèmes ou de données. Certains des types les plus courants de modèles d'apprentissage automatique incluent :

1. **Modèles de régression :** Les modèles de régression sont utilisés pour prédire des valeurs numériques continues, telles que les cours des actions ou les prix des logements.

2. **Modèles de classification :** Les modèles de classification sont utilisés pour prédire des valeurs catégorielles discrètes, par exemple si un client achètera ou non un produit.

3. **Modèles de clustering :** Les modèles de clustering sont utilisés pour identifier des groupes ou des clusters au sein d'un ensemble de données en fonction des similitudes entre les instances.

4. **Modèles de recommandation :** Les modèles de recommandation sont utilisés pour recommander des produits ou des services aux utilisateurs en fonction de leur comportement ou de leurs préférences passés.

5. **Réseaux de neurones :** Les réseaux de neurones sont un type de modèle d'apprentissage automatique conçu pour imiter la structure et la fonction du cerveau humain. Ils sont couramment utilisés dans les applications de reconnaissance d'images, de reconnaissance vocale et de traitement du langage naturel.

<!-- prettier-ignore -->
!!! info "Les modèles d'apprentissage automatique peuvent être biaisés"
     Les modèles d'apprentissage automatique sont un outil puissant pour analyser et faire des prédictions sur les données, et ils ont un large éventail d'applications dans des domaines tels que la finance, la santé, le marketing, etc. Cependant, il est important de noter que les modèles d'apprentissage automatique ne sont pas parfaits et peuvent parfois faire des erreurs ou produire des résultats biaisés. Par conséquent, il est important d'évaluer et de tester soigneusement les modèles d'apprentissage automatique avant de les utiliser dans des applications réelles.

## Exemples

### Régression linéaire

![Régression linéaire](../images/linear-regression.jpg)

<!-- prettier-ignore -->
!!! info "Régression linéaire"
     $$
     \hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1 X_i + \hat{\epsilon}_i
     $$

     _Où $\hat{Y}_i$ désigne le $i$ième estimateur de la vraie valeur $Y$ en fonction de la $i$ième période d'apprentissage. Chaque $\hat{\beta}$ est un paramètre à apprendre. $\hat{\epsilon}_i$ est la quantité de bruit autorisée dans le modèle et peut varier en fonction du nombre d'époques d'entraînement indiqué par $i$. Chaque $X_i$ représente le $i$ième lot de données d'apprentissage._

Dans les modèles statistiques classiques comme la régression linéaire, l'objectif est de trouver une ligne qui correspond le mieux aux données, nous permettant de faire des prédictions sur de nouveaux points de données.

À mesure que la complexité du problème augmente, des algorithmes plus sophistiqués sont nécessaires, tels que des arbres de décision, des machines à vecteurs de support et des forêts aléatoires. Cependant, ces méthodes ont des limites et peuvent ne pas être en mesure de capturer des modèles complexes dans de grands ensembles de données.

#### Exemple de code

=== "Python"
    ``` py title="linear_regression.py" linenums="1"
    #!/usr/bin/env python

    # Charger les bibliothèques requises
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

    # Charger le jeu de données
    data = pd.read_csv('path/to/dataset.csv')

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

    # Former le modèle de régression linéaire
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    # Faire des prédictions sur l'ensemble de test
    y_pred = linear_model.predict(X_test)

    # Évaluer les performances du modèle
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    print('Root Mean Squared Error:', rmse)
    ```

=== "R"
    ``` r title="linear_regression.r" linenums="1"
    #!/usr/bin/env Rscript
    
    # Définir une graine aléatoire pour la reproductibilité
    set.seed(123)

    # Charger le jeu de données
    data <- read.csv('path/to/dataset.csv')

    # Diviser les données en ensembles d'entraînement et de test
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    train_data <- data[train_index,]
    test_data <- data[-train_index,]

    # Former le modèle de régression linéaire
    lm_model <- lm(target_variable ~ ., data=train_data)

    # Faire des prédictions sur l'ensemble de test
    y_pred <- predict(lm_model, newdata=test_data[,-which(names(test_data)=='target_variable')])

    # Évaluer les performances du modèle
    mse <- mean((y_pred - test_data$target_variable)^2)
    rmse <- sqrt(mse)
    print(paste('Root Mean Squared Error:', rmse))
     ```

### Machine à vecteurs de support (SVM)

![Supporter la machine vectorielle](../images/svm.jpg)

<!-- prettier-ignore -->
!!! note "SVM"
     $$
     \underset{\mathbf{w},b,\boldsymbol{\xi}}{\operatorname{minimize}} \hspace{0.2cm} \frac{1}{2} ||\mathbf{w}||^2 + C \sum_{i=1}^{N} \xi_i
     $$

     $$
     \text{où} \hspace{0.2cm} y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1-\xi_i \quad \text{and} \quad \hspace{0.2cm} \xi_i \geq 0 \hspace{0.2cm} \forall i \in {1,2,...,N}
     $$

     _Dans cette formule, nous utilisons la formulation SVM standard où $\mathbf{w}$ est le vecteur de poids, $b$ est le terme de biais et $\boldsymbol{\xi}$ est le vecteur variable d'écart. L'objectif est de minimiser la norme L2 du vecteur de poids $\mathbf{w}$, sous la contrainte que tous les exemples d'apprentissage sont classés correctement avec une marge d'au moins 1, plus une tolérance pour certaines violations de marge contrôlées par le paramètre de régularisation $C$. La variable cible $y_i$ prend les valeurs 1 ou -1, représentant les deux classes du problème de classification binaire, et $\mathbf{x}_i$ est le vecteur de caractéristiques pour le $i$ième exemple d'entraînement._

Une machine à vecteurs de support (SVM) est un algorithme d'apprentissage automatique supervisé qui peut être utilisé pour la classification, la régression et la détection des valeurs aberrantes. C'est un algorithme populaire dans le domaine de l'apprentissage automatique, en particulier pour résoudre les problèmes de classification.

L'idée de base derrière SVM est de trouver un hyperplan qui sépare au mieux les données d'entrée en différentes classes. Dans un problème de classification à deux classes, l'hyperplan est une ligne qui sépare les points de données d'une classe des points de données de l'autre classe. SVM essaie de trouver l'hyperplan qui maximise la marge entre les deux classes, où la marge est la distance entre l'hyperplan et les points de données les plus proches de chaque classe.

#### Exemple de code

=== "Python"
    ``` py title="svm.py" linenums="1"
    #!/usr/bin/env python

    # Charger les bibliothèques requises
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score

    # Charger le jeu de données
    data = pd.read_csv('path/to/dataset.csv')

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

    # Former le modèle SVM
    svm_model = SVC(kernel='linear', C=1.0, random_state=42)
    svm_model.fit(X_train, y_train)

    # Faire des prédictions sur l'ensemble de test
    y_pred = svm_model.predict(X_test)

    # Évaluer les performances du modèle
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)
    ```

=== "R"

    ``` r title="svm.r" linenums="1"
    #!/usr/bin/env Rscript

    # Charger les bibliothèques requises
    library(e1071)

    # Charger le jeu de données
    data <- read.csv('path/to/dataset.csv')

    # Diviser les données en ensembles d'entraînement et de test
    set.seed(123)
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    train_data <- data[train_index,]
    test_data <- data[-train_index,]

    # Former le modèle SVM
    svm_model <- svm(target_variable ~ ., data=train_data, kernel='linear', cost=1)

    # Faire des prédictions sur l'ensemble de test
    y_pred <- predict(svm_model, newdata=test_data[,-which(names(test_data)=='target_variable')])

    # Évaluer les performances du modèle
    accuracy <- mean(y_pred == test_data$target_variable)
    print(paste('Accuracy:', accuracy))
    ```

### Forêt aléatoire

![Forêt aléatoire](../images/random-forest.jpg)

<!-- prettier-ignore -->
!!! note "Forêt aléatoire"
     $$
     \hat{y} = \frac{1}{T} \sum_{t=1}^{T} f_t(\mathbf{x}),
     $$

     _où $\hat{y}$ est la sortie prédite, $f_t(\mathbf{x})$ est la prédiction du $t$ième arbre de la forêt pour l'entrée $\mathbf{x}$, et $T $ est le nombre d'arbres dans la forêt._

Les forêts aléatoires sont une méthode d'apprentissage d'ensemble qui peut être utilisée pour les problèmes de classification et de régression. Ils sont souvent utilisés pour leur capacité à gérer des ensembles de données dimensionnelles à haute variation et des relations non linéaires entre les entités et les cibles.

Chaque arbre est entraîné sur un sous-ensemble amorcé des données d'entraînement d'origine, et à chaque division, un sous-ensemble aléatoire de caractéristiques est pris en compte pour déterminer la division. La prédiction finale est obtenue en faisant la moyenne des prédictions de tous les arbres de la forêt.

#### Exemple de code

=== "Python"
     
    ``` py title="random_forest.py" linenums="1"
    #!/usr/bin/env python

    # Charger les bibliothèques requises
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error

    # Charger le jeu de données
    data = pd.read_csv('path/to/dataset.csv')

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

     # Former le modèle de forêt aléatoire
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Faire des prédictions sur l'ensemble de test
    y_pred = rf_model.predict(X_test)

    # Évaluer les performances du modèle
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    print('Root Mean Squared Error:', rmse)
    ```

=== "R"

    ``` r title="random_forest.r" linenums="1"
    #!/usr/bin/env Rscript

    # Charger les bibliothèques requises
    library(randomForest)

    # Charger le jeu de données
    data <- read.csv('path/to/dataset.csv')

    # Diviser les données en ensembles d'entraînement et de test
    set.seed(123)
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    train_data <- data[train_index,]
    test_data <- data[-train_index,]

    # Former le modèle de forêt aléatoire
    rf_model <- randomForest(target_variable ~ ., data=train_data, ntree=100, importance=TRUE)

    # Faire des prédictions sur l'ensemble de test
    y_pred <- predict(rf_model, newdata=test_data[,-which(names(test_data)=='target_variable')])

    # Évaluer les performances du modèle
    mse <- mean((y_pred - test_data$target_variable)^2)
    rmse <- sqrt(mse)
    print(paste('Root Mean Squared Error:', rmse))
    ```

### L'apprentissage en profondeur

![Apprentissage en profondeur](../images/deep-learning.jpg)

<!-- prettier-ignore -->
!!! note "Apprentissage en profondeur"
     $$
     \hat{y} = f(\mathbf{W}_L f(\mathbf{W}_{L-1} f(\dots f(\mathbf{W}_1\mathbf{x}+\mathbf{b} _1)\dots)+\mathbf{b}_{L-1})+\mathbf{b}_L)
     $$

     _où $\mathbf{x}$ est le vecteur d'entrée, $\mathbf{W}_i$ et $\mathbf{b}_i$ sont respectivement la matrice de pondération et le vecteur de biais pour la $i$ième couche, et $ f$ est la fonction d'activation._

     _Cette formule représente un réseau de neurones à anticipation avec des couches $L$, où chaque couche applique une transformation linéaire à la sortie de la couche précédente, suivie d'une fonction d'activation non linéaire. La sortie de la couche finale, $\hat{y}$, représente la sortie prédite du réseau de neurones pour l'entrée donnée $\mathbf{x}$._

L'apprentissage en profondeur est un sous-ensemble de l'apprentissage automatique qui implique la formation de réseaux de neurones avec de nombreuses couches de nœuds interconnectés. Cette approche peut gérer des ensembles de données volumineux et complexes et est utilisée dans un large éventail d'applications, notamment la reconnaissance d'images, le traitement du langage naturel et la reconnaissance vocale. Le processus de formation consiste à alimenter le réseau de neurones avec un grand ensemble de données et à ajuster les poids des connexions entre les nœuds pour minimiser l'erreur entre les sorties prédites et les sorties réelles. Grâce à des itérations répétées, le réseau de neurones peut apprendre à reconnaître des modèles dans les données et à faire des prédictions précises sur de nouvelles données.

#### Exemple de code

=== "Python"
    ``` py title="deep_learning.py" linenums="1"
    #!/usr/bin/env python

    # Charger les bibliothèques requises
    import pandas as pd
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score

    # Charger le jeu de données
    data = pd.read_csv('path/to/dataset.csv')

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target_variable', axis=1), data['target_variable'], test_size=0.2)

    # Standardiser les caractéristiques d'entrée
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Définir le modèle de deep learning
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=[X_train_scaled.shape[1]]),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compiler le modèle
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Former le modèle
    history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.1)

    # Évaluer les performances du modèle
    y_pred = model.predict_classes(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)
    ```

=== "R"

    ``` r title="deep_learning.r" linenums="1"
    #!/usr/bin/env Rscript
        
    # Charger les bibliothèques requises
    library(keras)
    library(tensorflow)

    # Charger le jeu de données
    data <- iris
    x <- as.matrix(data[, 1:4])
    y <- to_categorical(as.numeric(data[, 5]) - 1)

    # Diviser les données en ensembles d'entraînement et de test
    set.seed(123)
    train_index <- sample(1:nrow(data), size=0.8*nrow(data))
    x_train <- x[train_index,]
    y_train <- y[train_index,]
    x_test <- x[-train_index,]
    y_test <- y[-train_index,]

    # Définir l'architecture du réseau neuronal
    model <- keras_model_sequential() %>%
    layer_dense(units = 8, input_shape = c(4)) %>%
    layer_activation('relu') %>%
    layer_dense(units = 3) %>%
    layer_activation('softmax')

    # Compiler le modèle
    model %>% compile(
    loss = 'categorical_crossentropy',
    optimizer = 'adam',
    metrics = c('accuracy')
    )

    # Former le modèle
    history <- model %>% fit(
    x_train, y_train,
    epochs = 50,
    batch_size = 10,
    validation_split = 0.2,
    verbose = 0
    )

    # Évaluer les performances du modèle
    metrics <- model %>% evaluate(x_test, y_test)
    print(paste('Test Loss:', metrics[1]))
    print(paste('Test Accuracy:', metrics[2]))

    # Tracez la précision de la formation et de la validation dans le temps
    plot(history$metrics$accuracy, type='l', col='blue', ylim=c(0,1), ylab='Accuracy', xlab='Epoch')
    lines(history$metrics$val_accuracy, type='l', col='red')
    legend('bottomright', legend=c('Training', 'Validation'), col=c('blue', 'red'), lty=1)
    ```