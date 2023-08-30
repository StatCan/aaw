# Former des modèles d'apprentissage automatique sur l'ETAA

<center>
![MLOps](../images/mlops.jpg)
</center>

<!-- prettier-ignore -->
!!! info
    La formation de modèles d'apprentissage automatique implique l'utilisation d'algorithmes pour apprendre des modèles et des relations dans les données. Ce processus implique l'identification de caractéristiques ou de variables pertinentes pour le problème en question et l'utilisation de ces caractéristiques pour faire des prédictions ou des classifications.

## Pourquoi s'entraîner avec nous ?

_L'entraînement des modèles d'apprentissage automatique sur l'espace de travail d'analyse avancée (ETAA) présente plusieurs avantages._

1. **Open Source :** L'ETAA est une *plate-forme de données open source hébergée par Statistique Canada* qui fournit un accès sécurisé (protégé B) à une variété de sources de données, y compris des données de recensement, des enquêtes et des dossiers administratifs. Ces données peuvent être utilisées pour former des modèles d'apprentissage automatique et générer des informations qui peuvent éclairer les décisions politiques et améliorer les processus métier.

2. **Polyvalent :** L'ETAA est *conçu pour gérer des ensembles de données volumineux et complexes*. Il donne accès à une gamme d'outils d'analyse avancés, dans le langage de votre choix, y compris *Python, R et SAS*, qui peuvent être utilisés pour prétraiter les données, former des modèles d'apprentissage automatique et générer des visualisations. *Parce que l'ETAA exploite les technologies cloud, *les utilisateurs peuvent augmenter leur puissance de calcul selon leurs besoins*.
*
3. **Sécurisé :** L'ETAA est une *plate-forme sécurisée (protégé B) qui respecte les normes les plus élevées en matière de confidentialité et de sécurité des données*. Les données peuvent être stockées et traitées sur la plateforme sans risque d'accès non autorisé ou de violation de données.

## MLOps et pipelines de données

<!-- prettier-ignore -->
!!! info "Optimiser les workflows de données"
    Les MLOps et les pipelines de données sont des outils importants utilisés dans le domaine de la science des données pour gérer et optimiser les workflows de données.

### MLOps

MLOps fait référence à l'ensemble des pratiques et des outils utilisés pour gérer l'ensemble du cycle de vie d'un modèle d'apprentissage automatique. Cela comprend tout, du développement et de la formation du modèle à son déploiement en production et à sa maintenance dans le temps. MLOps garantit que les modèles d'apprentissage automatique sont fiables, précis et évolutifs, et qu'ils peuvent être mis à jour et améliorés selon les besoins.

### Pipelines de données

Les pipelines de données sont une série d'étapes qui permettent de déplacer des données d'un système ou d'une application à un autre. Cela comprend la collecte, le nettoyage, la transformation et le stockage des données, ainsi que leur récupération en cas de besoin. Les pipelines de données sont importants pour garantir que les données sont exactes, fiables et accessibles à ceux qui en ont besoin.

<!-- prettier-ignore -->
!!! info "Automatisation et fiabilité"
    Les MLOps et les pipelines de données aident les organisations à gérer le processus complexe consistant à travailler avec de grandes quantités de données et à développer des modèles d'apprentissage automatique. En automatisant ces processus et en s'assurant que les données sont exactes et fiables, les organisations peuvent économiser du temps et des ressources tout en prenant de meilleures décisions basées sur des informations basées sur les données.

### Pourquoi des MLOps conteneurisés ?

Les avantages de l'utilisation d'une approche conteneurisée pour la formation de modèles d'apprentissage automatique avec Argo Workflows incluent :

1. **Reproductibilité :** La conteneurisation du modèle de l'apprentissage automatique et de ses dépendances garantit que l'environnement reste cohérent d'une exécution à l'autre, ce qui facilite la reproduction des résultats.

2. **Évolutivité :** Argo Workflows peut orchestrer des tâches parallèles et des flux de travail complexes, ce qui facilite l'évolution du processus de formation selon les besoins.

3. **Portabilité :** Les conteneurs peuvent être exécutés sur n'importe quelle plate-forme prenant en charge la conteneurisation, ce qui facilite le déplacement du processus de formation vers différents environnements ou fournisseurs de cloud.

4. **Collaboration :** En transférant le conteneur vers un registre de conteneurs, les autres utilisateurs peuvent facilement télécharger et utiliser le conteneur à leurs propres fins, ce qui facilite la collaboration sur des projets de l'apprentissage automatique.

Les flux de travail Argo et la conteneurisation offrent une approche puissante et flexible pour la formation de modèles d'apprentissage automatique. En tirant parti de ces outils, les data scientists et les ingénieurs en apprentissage automatique peuvent créer, déployer et gérer des workflows d'apprentissage automatique avec facilité et reproductibilité.

## Comment former des modèles

Il existe plusieurs façons de former des modèles d'apprentissage automatique et ce n'est pas à nous de dire à qui que ce soit comment le faire. Cela étant dit, nous avons fourni ci-dessous quelques guides sur la façon de former des modèles d'apprentissage automatique à l'aide des outils disponibles sur l'ETAA. Le premier tutoriel concerne la formation d'un modèle simple directement dans un notebook JupyterLab. Le deuxième tutoriel suppose que l'utilisateur est plus avancé et souhaite définir un pipeline MLOps pour former des modèles à l'aide d'Argo Workflows.

### Créer un serveur de bloc-notes sur l'ETAA

<!-- prettier-ignore -->
!!! info "Serveurs portables"
    Que vous envisagiez de travailler dans JupyterLab, R Studio ou quelque chose de plus avancé avec Argo Workflows, vous aurez besoin du serveur de bloc-notes approprié. [Suivez les instructions trouvées ici pour commencer.](https://docs.google.com/presentation/d/12yTDlbMCmbg0ccdea2h0vwhs5YTa_GHm_3DieG5A-k8/edit?usp=sharing)

### Utilisation de JupyterLab

![JupyterLab](../images/jupyterlab.jpg)

<!-- prettier-ignore -->
!!! info "JupyterLab est populaire"
    La formation de modèles d'apprentissage automatique avec JupyterLab est une approche populaire parmi les data scientists et les ingénieurs en apprentissage automatique.

Vous trouverez ici les étapes nécessaires pour former un modèle d'apprentissage automatique avec JupyterLab sur l'ETAA. Parce que nous sommes un environnement multilingue, nous avons fait de notre mieux pour fournir des exemples de code dans nos langages les plus populaires, `Python`, `R` et `SAS`.

#### 1. Importez les bibliothèques requises

Une fois qu'une session JupyterLab est en cours d'exécution, vous devez importer les bibliothèques requises pour votre modèle d'apprentissage automatique. Cela peut inclure des bibliothèques telles que `NumPy`, `Pandas`, `Scikit-learn`, `Tensorflow` ou `PyTorch`. Si vous utilisez `R`, vous aurez besoin de `tidyverse`, `caret` et `janitor`.

=== "Python"
    ``` py title="libraries.py" linenums="1"
    #!/usr/bin/env python

    # tensorflow et keras pour la construction et la formation de modèles d'apprentissage en profondeur
    import tensorflow as tf
    from tensorflow import keras

    # numpy pour les calculs numériques
    import numpy as np

    # pandas pour la manipulation et l'analyse des données
    import pandas as pd

    # matplotlib pour la visualisation des données
    import matplotlib.pyplot as plt
     ```
=== "R"
    ``` r title="libraries.R" linenums="1"
    #!/usr/bin/env Rscript

    # tidyverse pour des outils impressionnants d'analyse de données et de munging
    library(tidyverse)

    # concierge pour nettoyer vos données
    library(janitor)

    # caret pour un apprentissage automatique facile
    library(caret)
    ```
=== "SASPy"
    ``` py  title="libraries.py" linenums="1"
    #!/usr/bin/env python

    # la seule bibliothèque dont vous aurez besoin pour accéder à SAS depuis Python
    import saspy
    ```
=== "SAS"
    ``` sas title="libraries.sas" linenums="1"

    ```

<!-- prettier-ignore -->
!!! note "À propos du code"
    Les exemples de code que vous voyez dans ce document et tout au long de la documentation sont à titre indicatif pour vous aider à démarrer vos projets. Selon la tâche ou le projet spécifique, d'autres bibliothèques et étapes peuvent être nécessaires.

#### 2. Charger et prétraiter les données

Ensuite, vous devez charger et prétraiter les données que vous utiliserez pour entraîner votre modèle d'apprentissage automatique. Cela peut inclure le nettoyage des données, l'extraction de caractéristiques et la normalisation. Les étapes de prétraitement exactes que vous devrez effectuer dépendront de l'ensemble de données spécifique avec lequel vous travaillez, des exigences de votre modèle d'apprentissage automatique et du travail à effectuer.

=== "Python"
    ``` py title="load_data.py" linenums="1"
    #!/usr/bin/env python

    # Importer les paquets nécessaires
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    # Charger des données à partir d'un fichier CSV
    data = pd.read_csv('data.csv')

    # Nettoyage des données ! Beaucoup plus peut être fait, c'est un principe de base
    data = data.dropna()  # Drop rows with missing values
    data = data.drop_duplicates()  # Drop duplicate rows

    # Extraction de caractéristiques
    X = data[['feature1', 'feature2', 'feature3']] # Sélectionnez les fonctionnalités pertinentes

    # Normalisation
    scaler = StandardScaler() # Crée un objet scaler
    X_norm = scaler.fit_transform(X) # Normaliser les valeurs des caractéristiques
    ```
=== "R"
    ``` r title="load_data.R" linenums="1"
    #!/usr/bin/env Rscript

    # Importer les paquets nécessaires
    library(tidyverse)
    library(janitor)
    
    # Charger des données à partir d'un fichier CSV
    data <- read_csv("data.csv")

    # Nettoyer les données à l'aide d'un concierge
    data_cleaned <- data %>%
    # Supprimer les espaces blancs de début/fin dans les noms de colonne
    clean_names() %>%
    # Supprimer les lignes avec des valeurs manquantes
    remove_empty() %>%
    # Convertir la colonne de date au format Date
    mutate(date = as.Date(date, format = "%m/%d/%Y")) %>%
    # Supprimer les lignes en double
    distinct() %>%
    # Réorganiser les colonnes
    select(date, column2, column1, column3)
     ```
=== "SASPy"
    ``` py title="load_data.py" linenums="1"
    #!/usr/bin/env python

    # Importer les paquets nécessaires
    import saspy

    # Démarrez une session SAS et vérifiez les informations de configuration
    sas = saspy.SASsession(cfgname='default')

    # Charger des données à partir d'un fichier CSV
    data = sas.read_csv("./data.csv")
    ```
=== "SAS"
    ``` sas title="load_data.sas" linenums="1"
    /* Lecture d'un fichier délimité par des virgules avec une extension .csv */
    /* */
    /* Puisque la valeur DBMS= est CSV, vous n'avez pas besoin d'utiliser le DELIMITER= */
    /* déclaration.Par défaut, il est supposé que les noms de variables sont sur la première */
    /* ligne, l'instruction GETNAMES= n'est donc pas requise. */
    /* */
    /* Créer un fichier de test délimité par des virgules à lire en utilisant PROC IMPORT ci-dessous. */

    /* Charger les données d'un fichier CSV */
    proc import
        datafile='data.csv'
        out=data
        dbms=csv
        replace; 
    run;

    /* Afficher les données */
    proc print ;
    courir;
    ```

#### 3. Divisez les données en ensembles d'entraînement et de test

  Une fois les données prétraitées, vous devez les diviser en ensembles d'apprentissage et de test. L'ensemble de formation sera utilisé pour former le modèle d'apprentissage automatique, tandis que l'ensemble de test sera utilisé pour évaluer ses performances.

=== "Python"
    ``` py title="train_test.py" linenums="1"
    #!/usr/bin/env python

    # Importer les paquets nécessaires
    import pandas as pd
    from sklearn.model_selection import train_test_split

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X_norm,
    data['target'], test_size=0.2, random_state=42)
    ```
=== "R"
    ``` r title="train_test.R" linenums="1"
    #!/usr/bin/env Rscript

    # Importer les paquets nécessaires
    library(caret)

    # Charger le jeu de données
    data <- read.csv("my-dataset.csv")

    # Définir la graine pour la reproductibilité
    set.seed(123)

    # Diviser l'ensemble de données en train et tester à l'aide de la fonction createDataPartition de caret
    train_index <- createDataPartition(data$target_variable, p = 0.7, list = FALSE)
    train_data <- data[train_index, ]
    test_data <- data[-train_index, ]
    ```
=== "SASPy"
    ``` py title="train_test.py" linenums="1"
    #!/usr/bin/env python

    ```
=== "SAS"
    ``` sas title="train_test.sas" linenums="1"

    ```

<!-- prettier-ignore -->
!!! note
    Nous divisons les données en ensembles d'apprentissage et de test à l'aide de la fonction "train_test_split" de "scikit-learn", qui divise de manière aléatoire les données en deux ensembles en fonction de la taille de test spécifiée et de la graine aléatoire.


#### 4. Définir et entraîner le modèle d'apprentissage automatique

Avec la division des données, vous pouvez désormais définir et entraîner votre modèle d'apprentissage automatique à l'aide de l'ensemble d'entraînement. Cela pourrait impliquer la sélection de l'algorithme approprié, le réglage des hyperparamètres et la validation croisée.

=== "Python"
    ``` py title="train.py" linenums="1"
    #!/usr/bin/env python

    # Importer les paquets nécessaires
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    # Charger les ensembles de données
    data = pd.read_csv("my-dataset.csv")

    # Diviser l'ensemble de données en train et tester
    X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data.iloc[:, -1], test_size=0.3, random_state=123)

    # Former le modèle
    model = RandomForestClassifier(n_estimators=100, random_state=123)
    model.fit(X_train, y_train)

    # Imprimer le score de précision sur les données de test
    print("Accuracy on test set: {:.3f}".format(model.score(X_test, y_test)))
    ```
=== "R"
    ``` r title="train.R" linenums="1"
    #!/usr/bin/env Rscript

    # Importer les paquets nécessaires
    library(caret)

    # Charger l'ensembles de données
    data <- read.csv("my-dataset.csv")

    # Définir la graine pour la reproductibilité
    set.seed(123)

    # Diviser l'ensemble de données en train et tester à l'aide de la fonction createDataPartition de caret
    train_index <- createDataPartition(data$target_variable, p = 0.7, list = FALSE)
    train_data <- data[train_index, ]
    test_data <- data[-train_index, ]

    # Définir le contrôle d'entraînement
    train_control <- trainControl(method = "cv", number = 5)

    # Entraînez le modèle à l'aide de la fonction d'entraînement de caret, (method = "rf" est pour la forêt aléatoire)
    model <- train(target_variable ~ ., data = train_data, method = "rf", trControl = train_control)

    # Imprimez l'objet modèle pour afficher les résultats
    print(model)
    ```
=== "SASPy"
    ``` py title="train.py" linenums="1"
    #!/usr/bin/env python

    # Importer les paquets nécessaires
    import saspy
    import pandas as pd

    # Établir une connexion à une session SAS
    sas = saspy.SASsession()

    # Charger l'ensembles de données
    data = pd.read_csv("my-dataset.csv")

    # Télécharger l'ensemble de données sur SAS
    sas_df = sas.df2sd(data, "mydata")

    # Diviser l'ensemble de données en train et tester
    train, test = sas.surveyselect(data=sas_df,
                                   method="SRS",
                                   seed=123,
                                   samprate=0.7,
                                   outall=True,
                                   strata="target_variable",
                                   partind=True)

    # Former le modèle en utilisant la procédure HPFOREST
    model = sas.hpforest(data=train,
                         target="target_variable",
                         input="input_variable_1-input_variable_n",
                         partition="rolevar",
                         rolevars={"test": "0", "train": "1"},
                         nominals=["input_variable_1-input_variable_n"],
                         forestopts={"ntree": 100, "seed": 123})

    # Noter le modèle sur les données de test
    predictions = model.predict(newdata=test, out=pred_out)

    # Calculer le score de précision sur les données de test
    accuracy = sas.freq(data=predictions, tables="target_variable*p_target_variable", nocum=True, nocol=True)

    # Imprimer le score de précision
    print("Accuracy on test set: {:.3f}".format(accuracy.Frequency.iloc[0, 1] / accuracy.Frequency.iloc[:, 1].sum()))

    # Se déconnecter de la session SAS
    sas.disconnect()
    ```
=== "SAS"
    ``` sas title="train.sas" linenums="1"
    /* Charger le jeu de données */
    proc import datafile="my-dataset.csv" out=mydata dbms=csv replace;
    run;

    /* Divise le jeu de données en train et test */
    proc surveyselect data=mydata method=srs seed=123 out=selected outall
    samprate=0.7;
    strata target_variable;
    run;

    /* Former le modèle */
    proc hpforest data=selected;
    class _all_;
    target target_variable / level=nominal;
    partition rolevar=target_variable(test="0" train="1");
    input _all_;
    forest ntree=100 seed=123;
    run;

    /* Noter le modèle sur les données de test */
    proc hpforest predict testdata=selected out=testout;
    run;

    /* Affiche le score de précision sur les données de test */
    proc freq data=testout;
    tables target_variable*p_target_variable / nocum nocol;
    run;
    ```

#### 5. Évaluer le modèle

Après avoir entraîné le modèle, vous devez évaluer ses performances sur l'ensemble de test. Cela vous donnera une idée de la performance du modèle sur de nouvelles données inédites.

=== "Python"
    ``` py title="evaluate.py" linenums="1"

    ```
=== "R"
    ``` r title="evaluate.R" linenums="1"

    ```
=== "SASPy"
    ``` py title="evaluate.py" linenums="1"

    ```
=== "SAS"
    ``` sas title="evaluate.sas" linenums="1"

    ```

#### 6. Déployer le modèle

Enfin, vous pouvez déployer le modèle d'apprentissage automatique formé dans un environnement de production.

=== "Python"
    ``` py title="deploy.py" linenums="1"

    ```
=== "R"
    ``` r title="deploy.R" linenums="1"

    ```
=== "SASPy"
    ``` py title="deploy.py" linenums="1"

    ```
=== "SAS"
    ``` sas title="deploy.sas" linenums="1"

    ```

### Utilisation des workflows Argo

![Argo Workflows](../images/argo-workflows-assembly-line.jpg)

<!-- prettier-ignore -->
!!! info "Bonnes pratiques MLOps"
    Argo Workflows est un excellent outil pour tous ceux qui cherchent à mettre en œuvre des pratiques MLOps et à rationaliser le processus de formation et de déploiement de modèles d'apprentissage automatique ou d'autres tâches de science des données telles que ETL.

**[Argo Workflows](https://argoproj.github.io/argo-workflows/)** est un engin de workflow open source natif de conteneur pour orchestrer des tâches parallèles sur Kubernetes. Argo Workflows est implémenté en tant que Kubernetes CRD (Custom Resource Definition). Il est particulièrement bien adapté pour une utilisation dans les flux de travail d'apprentissage automatique et de science des données.

Argo Workflows vous permet de

- Définissez des flux de travail où chaque étape du flux de travail est un conteneur.
- Modélisez les flux de travail en plusieurs étapes sous la forme d'une séquence de tâches ou capturez les dépendances entre les tâches à l'aide d'un graphe acyclique dirigé (DAG).
- Exécutez facilement des tâches de calcul intensives pour l'apprentissage automatique ou le traitement de données en une fraction du temps à l'aide des flux de travail Argo sur Kubernetes.
- Exécutez des pipelines CI/CD en mode natif sur Kubernetes sans configurer de produits de développement logiciel complexes.

ce qui facilite la gestion de l'ensemble du pipeline d'apprentissage automatique de bout en bout. Avec Argo Workflows, vous pouvez facilement créer des workflows qui intègrent des tâches telles que le prétraitement des données, la formation de modèles et le déploiement de modèles, le tout dans un environnement Kubernetes.

<!-- prettier-ignore -->
!!! info ""
     <center>
     [![Flux de travail Argo](../images/argo-workflows.jpg)](https://argoproj.github.io/argo-workflows/)
     <h3>Flux de travail Argo</h3>
     </center>

Vous trouverez ci-dessous les étapes pour former un modèle d'apprentissage automatique à l'aide d'Argo Workflows sur l'ETAA.

#### 1. Écrivez un script pour entraîner votre modèle

Voici un exemple de script qui entraîne un modèle de régression logistique sur l'ensemble de données iris. N'oubliez pas de consulter le code de chaque langue ci-dessous.

=== "Python"

    ``` python title="train.py" linenums="1"
    #!/usr/bin/env python

    # Importer les bibliothèques nécessaires
    import argparse
    import pandas as pd
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import joblib

    # Analyser les arguments d'entrée
    parser = argparse.ArgumentParser(description="Train logistic regression model on iris dataset.")
    parser.add_argument("--input", default="iris.csv", help="Path to input dataset file.")
    parser.add_argument("--output", default="model.pkl", help="Path to output model file.")
    args = parser.parse_args()

    # Charger le jeu de données de l'iris
    data = load_iris()
    X, y = data.data, data.target

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Former le modèle de régression logistique
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)

    # Évaluer le modèle sur l'ensemble de test
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Enregistrer le modèle dans un fichier
    joblib.dump(clf, args.output)
    ```

=== "R"

    ``` r title="train.R" linenums="1"
    #!/usr/bin/env Rscript

    # Importer les bibliothèques nécessaires
    library(caret)

    # Analyser les arguments d'entrée
    args <- commandArgs(trailingOnly = TRUE)
    input_file <- ifelse(length(args) > 0, args[1], "iris.csv")
    output_file <- ifelse(length(args) > 1, args[2], "model.rds")

    # Charger le jeu de données de l'iris
    data(iris)
    X <- iris[, 1:4]
    y <- iris[, 5]

    # Diviser les données en ensembles d'entraînement et de test
    set.seed(42)
    train_index <- createDataPartition(y, p = 0.8, list = FALSE)
    X_train <- X[train_index, ]
    y_train <- y[train_index]
    X_test <- X[-train_index, ]
    y_test <- y[-train_index]

    # Former le modèle de régression logistique
    clf <- train(x = X_train, y = y_train, method = "glm")

    # Évaluer le modèle sur l'ensemble de test
    y_pred <- predict(clf, newdata = X_test)
    accuracy <- confusionMatrix(y_pred, y_test)$overall["Accuracy"]
    print(paste0("Accuracy: ", accuracy))

    # Enregistrer le modèle dans un fichier
    saveRDS(clf, output_file)
    ```

#### 2. Écrivez un Dockerfile pour exécuter votre code

Vous aurez besoin d'un Dockerfile qui inclut toutes les dépendances nécessaires pour former votre modèle d'apprentissage automatique. Cela pourrait inclure

- des forfaits comme
   - `scikit-learn`, `pandas` ou `numpy` si vous utilisez `Python`
   - `caret`, `janitor` et `tidyverse` si vous utilisez `R`
- vos propres bibliothèques ou scripts personnalisés
- le code de votre modèle de l'apprentissage automatique sous la forme d'un script [comme dans l'exemple ci-dessus](#1-write-a-script-to-train-your-model).

Utilisez le `Dockerfile` suivant comme point de départ pour vos projets `R` et `Python`.

=== "Python"

    ``` docker title="Dockerfile" linenums="1"
    FROM python:3.8-slim-buster

    # Installez toutes les dépendances nécessaires
    RUN pip install --no-cache-dir scikit-learn pandas numpy

     # Définir le répertoire de travail
    WORKDIR /app

    # Copier le code dans le conteneur
    COPY train.py .

    # Définir le point d'entrée
    ENTRYPOINT ["python", "train.py"]
    ```

=== "R"
    ``` docker title="Dockerfile" linenums="1"
    FROM rocker/r-base:latest

    RUN apt-get update && apt-get install -y --no-install-recommends \
        libssl-dev \
        libcurl4-openssl-dev \
        libxml2-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

    RUN R -e 'install.packages(c("caret", "janitor", "tidyverse"))'

    COPY train.R /app/train.R

    WORKDIR /app

    ENTRYPOINT ["Rscript", "train.R"]
    ```

#### 3. Écrivez votre workflow en YAML

YAML est encore un autre langage de balisage et vous devrez écrire les étapes de votre pipeline de formation dans un fichier YAML Argo Workflows. Ce fichier doit inclure une référence au Dockerfile que vous avez créé à l'[Étape 1](#2-write-a-dockerfile-to-run-your-code), ainsi que toutes les données d'entrée et de sortie avec lesquelles vous travaillerez.

Voici un exemple de fichier YAML pour un pipeline d'apprentissage automatique simple qui forme un modèle de régression logistique sur l'ensemble de données iris. La seule vraie différence entre les versions `Python` et `R` est la commande `command : ["python", "train.py"]` vs `command : ["Rscript", "train.R"]` et la les modèles sont stockés dans différents formats, `pkl` pour `python` et `rds` pour `R`.

Le fichier YAML définit une seule étape appelée "train" qui exécute un script appelé "train.py" ou "train.R" dans l'image Docker "machine-learning:v1". Le script prend un fichier d'ensemble de données d'entrée, spécifié par un paramètre appelé `dataset`, et génère un fichier de modèle entraîné vers un artefact de sortie appelé `model.pkl` ou `model.rds` selon le langage utilisé.

=== "Python"
    ``` yaml title="workflow.yaml" linenums="1"
    apiVersion: argoproj.io/v1alpha1
    kind: Workflow
    metadata:
    generateName: ml-pipeline-
    spec:
    entrypoint: train
    templates:
    - name: train
        container:
        image: machine-learning:v1
        command: ["python", "train.py"]
        args: ["--input", "{{inputs.parameters.dataset}}", "--output", "{{outputs.artifacts.model}}"]
        inputs:
        parameters:
        - name: dataset
            default: "iris.csv"
        outputs:
        artifacts:
        - name: model
            path: /output/model.pkl
    ```
=== "R"
    ``` yaml title="workflow.yaml" linenums="1"
    apiVersion: argoproj.io/v1alpha1
    kind: Workflow
    metadata:
    generateName: ml-pipeline-
    spec:
    entrypoint: train
    templates:
    - name: train
        container:
        image: machine-learning:v1
        command: ["Rscript", "train.R"]
        args: ["--input", "{{inputs.parameters.dataset}}", "--output", "{{outputs.artifacts.model}}"]
        inputs:
        parameters:
        - name: dataset
            default: "iris.csv"
        outputs:
        artifacts:
        - name: model
            path: /output/model.rds
    ```


#### 4. Soumettez le workflow à l'aide de la CLI Argo Workflows

Pour exécuter le flux de travail ci-dessus, vous devez d'abord envoyer le fichier Dockerfile à notre registre de conteneurs, puis envoyer le fichier YAML à l'aide de la commande "argo submit". Une fois le pipeline terminé, vous pouvez récupérer le fichier de modèle formé en téléchargeant l'artefact de sortie à partir de la commande `argo logs`.

``` bash title="Terminal"
$ argo submit workflow.yaml       # soumettre une spécification de workflow à Kubernetes
```

#### 5. Surveiller le pipeline à l'aide de la CLI Argo Workflows

Au fur et à mesure que le pipeline s'exécute, vous pouvez surveiller sa progression à l'aide de la CLI Argo Workflows. Cela vous montrera quelles étapes ont réussi et lesquelles sont toujours en cours. Vous trouverez ci-dessous quelques commandes utiles. Pour plus d'informations sur la CLI Argo Workflows, veuillez consulter [la documentation officielle de la CLI Argo Workflows](https://argoproj.github.io/argo-workflows/walk-through/argo-cli/) .

``` bash title="Terminal"
$ argo list                       # liste les workflows actuels
$ argo get workflow-xxx           # obtenir des informations sur un workflow spécifique
$ argo logs workflow-xxx          # imprimer les logs d'un workflow
$ argo delete workflow-xxx        # supprimer le workflow

```

#### 6. Récupérer le modèle formé

Une fois le pipeline terminé, vous pouvez récupérer les données de sortie à l'aide de la commande argo logs ou en affichant les artefacts de sortie à l'aide de la CLI, c'est-à-dire accéder au répertoire que vous avez spécifié dans votre script et localiser le fichier `model.pkl` ou `model. rds`. L'extrait de code suivant, tiré du [script de formation ci-dessus](#1-define-the-machine-learning-model-and-its-dependencies), indique au langage de programmation respectif où enregistrer le modèle formé.

=== "Python"

    ``` python title="Enregistrement des données de sortie" linenums="1"
    #!/usr/bin/env python
     
    parser.add_argument("--output", default="model.pkl", help="Path to output model file.")
     
    # Enregistrer le modèle dans un fichier
    joblib.dump(clf, args.sortie)
    ```

=== "R"

    ``` r title="Enregistrement des données de sortie" linenums="1"
    #!/usr/bin/env Rscript
     
    output_file <- ifelse(length(args) > 1, args[2], "model.rds")
     
    # Enregistrer le modèle dans un fichier
    saveRDS(clf, output_file)
    ```

### Exemples d'utilisation de SDK basés sur Argo Workflows

Si vous préférez utiliser un cadre de niveau supérieur, nous avons `Couler` et `Hera`. Ces cadres rendent la création et la gestion de flux de travail complexes plus accessibles à un public plus large.

#### Hera

Hera vise à simplifier le processus de création et de soumission des flux de travail en éliminant de nombreux détails techniques via une interface de programmation d'application simple. Il utilise également un ensemble cohérent de terminologie et de concepts qui s'alignent sur Argo Workflows, ce qui permet aux utilisateurs d'apprendre et d'utiliser plus facilement les deux outils ensemble.

#### Couler

Couler fournit une interface de programmation d'application simple et unifiée pour définir les flux de travail à l'aide d'un style de programmation impératif. Il construit également automatiquement des graphes acycliques dirigés (DAG) pour les flux de travail, ce qui peut aider à simplifier le processus de création et de gestion de ceux-ci.

=== "Couler"
    ``` py title="couler.py" linenums="1"
    #!/usr/bin/env python

    # Préparez votre système
    !pip config --user set global.index-url https://jfrog.ETAA.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
    !python3 -m pip install git+https://github.com/couler-proj/couler --ignore-installed

    # Définir la variable globale pour plus de commodité

    NAMESPACE = "<your-namespace>"

    # Importer les paquets nécessaires
    import json
    import random

    import couler.argo as couler
    from couler.argo_submitter import ArgoSubmitter


    # Définir les étapes (fonctions) utilisées dans le workflow
    def random_code():
        import random
        res = "heads" if random.randint(0, 1) == 0 else "tails"
        print(res)


    def flip_coin():
        return couler.run_script(
            image="k8scc01covidacr.azurecr.io/ubuntu",
            source=random_code
        )


    def heads():
        return couler.run_container(
            image="k8scc01covidacr.azurecr.io/ubuntu",
            command=["sh", "-c", 'echo "it was heads"']
        )


    def tails():
        return couler.run_container(
            image="k8scc01covidacr.azurecr.io/ubuntu",
            command=["sh", "-c", 'echo "it was tails"']
        )


    result = flip_coin()

    couler.when(couler.equal(result, "heads"), lambda: heads())
    couler.when(couler.equal(result, "tails"), lambda: tails())

    submitter = ArgoSubmitter(namespace="NAMESPACE")
    result = couler.run(submitter=submitter)

    print(json.dumps(result, indent=2))
    ```
=== "Hera"
    ``` py title="hera.py" linenums="1"
    #!/usr/bin/env python

    # Préparez votre système
    !pip config --user set global.index-url https://jfrog.ETAA.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
    !pip install hera-workflows
    
    # Importer les paquets nécessaires
    import hera
    from hera import Task, Workflow

     # Configurer Hera
    hera.global_config.GlobalConfig.token = "<your-token>"
    hera.global_config.GlobalConfig.host = "https://argo-workflows.ETAA-dev.cloud.statcan.ca:443"
    hera.global_config.GlobalConfig.namespace = "<your-namespace>"
    hera.global_config.GlobalConfig.service_account_name = "<your-account-name>"


    # Définir les étapes (fonctions) utilisées dans le workflow
    def random_code():
        res = "heads" if random.randint(0, 1) == 0 else "tails"
        print(res)


    def heads():
        print("it was heads")


    def tails():
        print("it was tails")


    # Définir le flux de travail
    with Workflow("coin-flip") as w:
        r = Task("r", random_code)
        h = Task("h", heads)
        t = Task("t", tails)

        h.on_other_result(r, "heads")
        t.on_other_result(r, "tails")

    # Exécuter le flux de travail
    w.create()
    ```
=== "YAML"
    ``` py title="workflow.yaml" linenums="1"

    ```
=== "Seldon ?"
    ``` py

    ```

### Ressources supplémentaires pour les workflows Argo

Des exemples de workflows Argo Workflows peuvent être trouvés dans les répos Github suivants :

- [Documentation Argo Workflows](https://argoproj.github.io/argo-workflows/)
- [Référence Argo CLI] (https://argoproj.github.io/argo-workflows/walk-through/argo-cli/)
