# Formation de modèles d'apprentissage automatique sur l'ETAA

<center>
![Robots au travail](../images/mlops.jpg)
</center>

<!-- prettier-ignore -->
!!! info
    La formation de modèles d'apprentissage automatique implique l'utilisation d'algorithmes pour apprendre des modèles et des relations dans les données. Ce processus implique d'identifier les caractéristiques ou les variables pertinentes pour le problème en question et d'utiliser ces caractéristiques pour effectuer des prédictions ou des classifications.

## Pourquoi s'entraîner avec nous ?

_La formation de modèles d'apprentissage automatique sur Advanced Analytics Workspace (AAW) présente plusieurs avantages._

1. **Code Logiciel Ouvert :** L'ETAA est une *plate-forme de données open source hébergée par Statistique Canada* qui offre un accès sécurisé (Protégé B) à une variété de sources de données, y compris les données de recensement, les enquêtes et les dossiers administratifs. Ces données peuvent être utilisées pour former des modèles d'apprentissage automatique et générer des informations susceptibles d'éclairer les décisions politiques et d'améliorer les processus métier.

2. **Polyvalent :** L'ETAA est *conçu pour gérer des ensembles de données volumineux et complexes*. Il donne accès à une gamme d'outils d'analyse avancés, dans le langage de votre choix, notamment *Python, R et SAS*, qui peuvent être utilisés pour prétraiter les données, former des modèles d'apprentissage automatique et générer des visualisations. *Étant donné que l'ETAA exploite les technologies cloud, *les utilisateurs peuvent augmenter leur puissance de calcul selon leurs besoins*.
*
3. **Sécurisé :** L'ETAA est une *plateforme sécurisée (Protégée B) qui adhère aux normes les plus élevées en matière de confidentialité et de sécurité des données*. Les données peuvent être stockées et traitées sur la plateforme sans risque d'accès non autorisé ou de violation de données.

## MLOps et pipelines de données

<!-- plus joli-ignorer -->
!!! info "Optimiser les flux de données"
     Les MLOps et les pipelines de données sont des outils importants utilisés dans le domaine de la science des données pour gérer et optimiser les flux de travail de données.

### MLOps

MLOps fait référence à l'ensemble de pratiques et d'outils utilisés pour gérer l'ensemble du cycle de vie d'un modèle d'apprentissage automatique. Cela comprend tout, depuis le développement et la formation du modèle jusqu'à son déploiement en production et sa maintenance au fil du temps. MLOps garantit que les modèles d'apprentissage automatique sont fiables, précis et évolutifs, et qu'ils peuvent être mis à jour et améliorés selon les besoins.

### Pipelines de données

Les pipelines de données sont une série d'étapes qui permettent de déplacer les données d'un système ou d'une application à un autre. Cela inclut la collecte, le nettoyage, la transformation et le stockage des données, ainsi que leur récupération en cas de besoin. Les pipelines de données sont importants pour garantir que les données sont exactes, fiables et accessibles à ceux qui en ont besoin.

<!-- prettier-ignore -->
!!! info "Automatisation et fiabilité"
     Les MLOps et les pipelines de données aident les organisations à gérer le processus complexe consistant à travailler avec de grandes quantités de données et à développer des modèles d'apprentissage automatique. En automatisant ces processus et en garantissant que les données sont exactes et fiables, les organisations peuvent économiser du temps et des ressources tout en prenant de meilleures décisions basées sur des informations basées sur les données.

### Pourquoi des MLOps conteneurisés ?

Les avantages de l'utilisation d'une approche conteneurisée pour la formation de modèles d'apprentissage automatique avec flux de travail Argo incluent :

1. **Reproductibilité :** La conteneurisation du modèle d'apprentissage automatique et de ses dépendances garantit que l'environnement reste cohérent d'une exécution à l'autre, ce qui facilite la reproduction des résultats.

2. **Évolutivité :** Les flux de travail Argo peut orchestrer des tâches parallèles et des flux de travail complexes, ce qui facilite l'évolution du processus de formation selon les besoins.

3. **Portabilité :** Les conteneurs peuvent être exécutés sur n'importe quelle plate-forme prenant en charge la conteneurisation, ce qui facilite le déplacement du processus de formation vers différents environnements ou fournisseurs de cloud.

4. **Collaboration :** En transférant le conteneur vers un registre de conteneurs, d'autres utilisateurs peuvent facilement télécharger et utiliser le conteneur à leurs propres fins, ce qui facilite la collaboration sur des projets d'apprentissage automatique.

Lesflux de travail Argo et la conteneurisation offrent une approche puissante et flexible pour la formation de modèles d'apprentissage automatique. En tirant parti de ces outils, les scientifiques des données et les ingénieurs en apprentissage automatique peuvent créer, déployer et gérer des flux de travail d'apprentissage automatique avec facilité et reproductibilité.

## Comment former des modèles

Il existe de nombreuses façons de former des modèles d’apprentissage automatique et ce n’est pas à nous de dire à qui que ce soit comment procéder. Cela étant dit, nous avons fourni ci-dessous quelques guides sur la façon de former des modèles d'apprentissage automatique à l'aide des outils disponibles sur l'ETAA. Le premier tutoriel concerne la formation d'un modèle simple directement dans un bloc-note JupyterLab. Le deuxième didacticiel suppose que l'utilisateur est plus avancé et souhaite définir un pipeline MLOps pour la formation de modèles à l'aide des flux de travail Argo.

### Créer un serveur de bloc-note sur l'ETAA

<!-- prettier-ignore -->
!!! info "Serveurs bloc-notes"
    Que vous envisagiez de travailler dans JupyterLab, R Studio ou quelque chose de plus avancé avec les flux de travail Argo, vous aurez besoin du serveur bloc-notes approprié. [Suivez les instructions trouvées ici pour commencer.](https://docs.google.com/presentation/d/12yTDlbMCmbg0ccdea2h0vwhs5YTa_GHm_3DieG5A-k8/edit?usp=sharing) 

### Utiliser JupyterLab

![JupyterLab](../images/jupyterlab.jpg)

<!-- prettier-ignore -->
!!! info "JupyterLab est populaire"
    La formation de modèles d'apprentissage automatique avec JupyterLab est une approche populaire parmi les scientifiques des données et les ingénieurs en apprentissage automatique.

Vous trouverez ici les étapes nécessaires pour entraîner un modèle d'apprentissage automatique avec JupyterLab sur AAW. Parce que nous sommes un environnement multilingue, nous avons fait de notre mieux pour fournir des exemples de code dans nos langages les plus populaires, `Python`, `R` et `SAS`.

#### 1. Importez les bibliothèques requises

Une fois qu'une session JupyterLab est en cours d'exécution, vous devez importer les bibliothèques requises pour votre modèle d'apprentissage automatique. Cela pourrait inclure des bibliothèques telles que `NumPy`, `Pandas`, `Scikit-learn`, `Tensorflow` ou `PyTorch`. Si vous utilisez `R`, vous aurez besoin de `tidyverse`, `caret` et `janitor`.

=== "Python"
    ``` py title="libraries.py" linenums="1"
    #!/usr/bin/env python

    # tensorflow et keras pour la création et la formation de modèles d'apprentissage profond
    import tensorflow as tf
    from tensorflow import keras

    # numpy pour les calculs numériques
    import numpy as np

    # pandas pour la manipulation et l'analyse des données
    import pandas as pd

    # matplotlib pour la visualisation de données 
    import matplotlib.pyplot as plt
    ```
=== "R"
    ``` r title="libraries.R" linenums="1"
    #!/usr/bin/env Rscript

    # tidyverse pour des outils impressionnants d'analyse de données et de munging
    library(tidyverse)

    # janitor pour nettoyer vos données
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
     Les exemples de code que vous voyez dans ce document et dans toute la documentation sont fournis à des fins d'illustration pour vous aider à démarrer vos projets. En fonction de la tâche ou du projet spécifique, d'autres bibliothèques et étapes peuvent être nécessaires.

#### 2. Charger et prétraiter les données

Ensuite, vous devez charger et prétraiter les données que vous utiliserez pour entraîner votre modèle d'apprentissage automatique. Cela pourrait inclure le nettoyage des données, l’extraction de fonctionnalités et la normalisation. Les étapes exactes de prétraitement que vous devrez effectuer dépendront de l'ensemble de données spécifique avec lequel vous travaillez, des exigences de votre modèle d'apprentissage automatique et du travail à effectuer.

=== "Python"
    ``` py title="load_data.py" linenums="1"
    #!/usr/bin/env python

    # Importer les packages nécessaires
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    # Charger des données à partir d'un fichier CSV
    data = pd.read_csv('data.csv')

    # Nettoyage des données ! On peut faire beaucoup plus, c'est fondamental
    data = data.dropna()  # Drop rows with missing values
    data = data.drop_duplicates()  # Drop duplicate rows

    # Extraction de caractéristiques
    X = data[['feature1', 'feature2', 'feature3']]  # Select relevant features

    # Normalisation
    scaler = StandardScaler()  # Create a scaler object
    X_norm = scaler.fit_transform(X)  # Normalize the feature values
    ```
=== "R"
    ``` r title="load_data.R" linenums="1"
    #!/usr/bin/env Rscript

    # Importer les packages nécessaires
    library(tidyverse)
    library(janitor)
    
    # Charger des données à partir d'un fichier CSV
    data <- read_csv("data.csv")

    # Nettoyer les données en utilisant janitor
    data_cleaned <- data %>%

    # Supprimer les espaces de début/fin dans les noms de colonnes
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

    # Importer les packages nécessaires
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
     /* Puisque la valeur DBMS= est CSV, vous n'avez pas besoin d'utiliser DELIMITER= */
     /* déclaration. Par défaut, on suppose que les noms des variables sont en premier */
     /* ligne, donc l'instruction GETNAMES= n'est pas requise. */
     /* */
     /* Créez un fichier de test délimité par des virgules à lire en utilisant PROC IMPORT ci-dessous. */

     /* Charger les données depuis un fichier CSV */
    proc import
        datafile='data.csv'
        out=data
        dbms=csv
        replace; 
    run;

    /* Afficher les données */
    proc print;
    run;
    ```

#### 3. Divisez les données en ensembles de formation et de test

  Une fois les données prétraitées, vous devez les diviser en ensembles de formation et de test. L'ensemble de formation sera utilisé pour entraîner le modèle d'apprentissage automatique, tandis que l'ensemble de test sera utilisé pour évaluer ses performances.

=== "Python"
    ``` py title="train_test.py" linenums="1"
    #!/usr/bin/env python

    # Importer les packages nécessaires
    import pandas as pd
    from sklearn.model_selection import train_test_split

    # Divisez les données en ensembles de formation et de test
    X_train, X_test, y_train, y_test = train_test_split(X_norm,
    data['target'], test_size=0.2, random_state=42)
    ```
=== "R"
    ``` r title="train_test.R" linenums="1"
    #!/usr/bin/env Rscript

    # Importer les packages nécessaires
    library(caret)

    # Charger l'ensemble de données
    data <- read.csv("my-dataset.csv")

    # Définir la graine pour la reproductibilité
    set.seed(123)

    # Divisez l'ensemble de données en train et test à l'aide de la fonction createDataPartition de Caret
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
    Nous divisons les données en ensembles d'entraînement et de test à l'aide de la fonction `train_test_split` de `scikit-learn`, qui divise aléatoirement les données en deux ensembles en fonction de la taille de test spécifiée et de la graine aléatoire.

#### 4. Définir et entraîner le modèle d'apprentissage automatique

Avec la répartition des données, vous pouvez désormais définir et entraîner votre modèle d'apprentissage automatique à l'aide de l'ensemble de formation. Cela pourrait impliquer la sélection de l’algorithme approprié, le réglage des hyperparamètres et la validation croisée.

=== "Python"
    ``` py title="train.py" linenums="1"
    #!/usr/bin/env python

    # Importer les packages nécessaires
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    # Charger l'ensemble de données
    data = pd.read_csv("my-dataset.csv")

    # Divisez l'ensemble de données en entraînement et test
    X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data.iloc[:, -1], test_size=0.3, random_state=123)

    # Entraîner le modèle
    model = RandomForestClassifier(n_estimators=100, random_state=123)
    model.fit(X_train, y_train)

    # Imprimer le score de précision sur les données de test
    print("Accuracy on test set: {:.3f}".format(model.score(X_test, y_test)))
    ```
=== "R"
    ``` r title="train.R" linenums="1"
    #!/usr/bin/env Rscript

    # Importer les packages nécessaires
    library(caret)

    # Charger l'ensemble de données
    data <- read.csv("my-dataset.csv")

    # Définir la graine pour la reproductibilité
    set.seed(123)

    # Divisez l'ensemble de données en train et test à l'aide de la fonction curseur createDataPartition
    train_index <- createDataPartition(data$target_variable, p = 0.7, list = FALSE)
    train_data <- data[train_index, ]
    test_data <- data[-train_index, ]

    # Définir le contrôle de la formation
    train_control <- trainControl(method = "cv", number = 5)

    # Entraînez le modèle à l'aide de la fonction d'entraînement de Caret (la méthode = "rf" est pour la forêt aléatoire)
    model <- train(target_variable ~ ., data = train_data, method = "rf", trControl = train_control)

    # Imprimez l'objet modèle pour afficher les résultats
    print(model)
    ```
=== "SASPy"
    ``` py title="train.py" linenums="1"
    #!/usr/bin/env python

    # Importer les packages nécessaires
    import saspy
    import pandas as pd

    # Établir une connexion à une session SAS
    sas = saspy.SASsession()

    # Charger l'ensemble de données
    data = pd.read_csv("my-dataset.csv")

    # Téléchargez l'ensemble de données sur SAS
    sas_df = sas.df2sd(data, "mydata")

    # Divisez l'ensemble de données en train et test
    train, test = sas.surveyselect(data=sas_df,
                                method="SRS",
                                seed=123,
                                samprate=0.7,
                                outall=True,
                                strata="target_variable",
                                partind=True)

    # Entraîner le modèle à l'aide de la procédure HPFOREST
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
    /* Charger l'ensemble de données */
    proc import datafile="my-dataset.csv" out=mydata dbms=csv replace;
    run;

   /* Diviser l'ensemble de données en train et test */
    proc surveyselect data=mydata method=srs seed=123 out=selected outall
    samprate=0.7;
    strata target_variable;
    run;

    /* Entraîner le modèle */
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

    /* Imprimer le score de précision sur les données du test */
    proc freq data=testout;
    tables target_variable*p_target_variable / nocum nocol;
    run;
    ```

#### 5. Évaluer le modèle

Après avoir entraîné le modèle, vous devez évaluer ses performances sur l’ensemble de tests. Cela vous donnera une idée des performances du modèle sur de nouvelles données invisibles.

#### 6. Déployer le modèle

Enfin, vous pouvez déployer le modèle d'apprentissage automatique formé dans un environnement de production.

### Utiliser les flux de travail Argo

![Art de production de flux de travail](../images/argo-workflows-assembly-line.jpg)

<!-- prettier-ignore -->
!!! info "Meilleures pratiques MLOps"
     Les flux de travail Argo sont un excellent outil pour tous ceux qui cherchent à mettre en œuvre des pratiques MLOps et à rationaliser le processus de formation et de déploiement de modèles d'apprentissage automatique ou d'autres tâches de science des données telles que ETL.

**[Flux de travail Argo](https://argoproj.github.io/argo-workflows/)**  est un moteur de flux de travail open source natif pour conteneurs permettant d'orchestrer des tâches parallèles sur Kubernetes. Les flux de travail Argo sont implémentés en tant que Kubernetes CRD (Custom Resource Definition). Il est particulièrement adapté aux flux de travail d’apprentissage automatique et de science des données.

Les flux de travail Argo vous permettent de

- Définir des flux de travail où chaque étape du flux est un conteneur.
- Modélisez des flux de travail en plusieurs étapes sous la forme d'une séquence de tâches ou capturez les dépendances entre les tâches à l'aide d'un graphe acyclique dirigé (DAG).
- Exécutez facilement des tâches de calcul intensives pour l'apprentissage automatique ou le traitement des données en une fraction du temps à l'aide de flux de travail Argo sur Kubernetes.
- Exécutez des pipelines CI/CD de manière native sur Kubernetes sans configurer de produits de développement logiciel complexes.

ce qui facilite la gestion de l'ensemble du pipeline d'apprentissage automatique de bout en bout. Avec les flux de travail Argo, vous pouvez facilement créer des flux de travail qui intègrent des tâches telles que le prétraitement des données, la formation de modèles et le déploiement de modèles, le tout dans un environnement Kubernetes.

Voir la [section flux de travail argo](../3-Pipelines/Argo.md) pour plus de détails.
