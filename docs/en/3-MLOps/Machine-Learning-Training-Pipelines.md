# Training Machine Learning Models on the AAW

<center>
![MLOps](../images/mlops.jpg)
</center>


!!! info
    Training machine learning models involves using algorithms to learn patterns and relationships in data. This process involves identifying features or variables that are relevant to the problem at hand and using these features to make predictions or classifications. 

## Why train with us?

_Training machine learning models on the Advanced Analytics Workspace (AAW) has several advantages._

1. The AAW is an open source data platform hosted by Statistics Canada that provides secure (Protected B) access to a variety of data sources, including census data, surveys, and administrative records. This data can be used to train machine learning models and generate insights that can inform policy decisions and improve business processes.

2. The AAW is designed to handle large and complex datasets. It provides access to a range of advanced analytics tools, including Python, R, and SAS, which can be used to preprocess data, train machine learning models, and generate visualizations. The AAW also provides access to cloud computing resources, allowing users to scale up their computing power as needed.

3. The AAW is a secure platform (Protected B) that adheres to the highest standards of data privacy and security. Data can be stored and processed on the platform without risk of unauthorized access or data breaches.

## How to Train Models

### Using JupyterLab

![JupyterLab](../images/jupyterlab.jpg)

_Training machine learning models with JupyterLab is a popular approach among data scientists and machine learning engineers._

Here are the steps to train a machine learning model with JupyterLab on the AAW:

#### 1. Create a Notebook Server on the AAW

First, you need to create and spin up a new notebook server. [Follow the instructions found here to get started.](https://docs.google.com/presentation/d/12yTDlbMCmbg0ccdea2h0vwhs5YTa_GHm_3DieG5A-k8/edit?usp=sharing)

#### 2. Import the required libraries

Once you a JupyterLab session running, you need to import the required libraries for your machine learning model. This could include libraries such as NumPy, Pandas, Scikit-learn, Tensorflow, or PyTorch.

=== "Python"
    ``` py title="cool_libraries.py" linenums="1" hl_lines="5"
    # tensorflow and keras for building and training deep learning models  
    import tensorflow as tf
    from tensorflow import keras

    # numpy for numerical computations  
    import numpy as np

    # pandas for data manipulation and analysis  
    import pandas as pd

    # matplotlib for data visualization  
    import matplotlib.pyplot as plt
    ```
=== "R"
    ``` r title="import_data.r" linenums="1" hl_lines="5"
    library(tidyverse)
    ```
=== "SASPy"
    ``` py title="saspy_import_data.py" linenums="1" hl_lines="8"
    import saspy
    ```
=== "SAS"
    ``` sas

    ```

!!! note
    This is just an example, and depending on the specific task or project, other libraries such as `PyTorch` may also be used.

#### 3. Load and preprocess the data

Next, you need to load and preprocess the data you'll be using to train your machine learning model. This could include data cleaning, feature extraction, and normalization. The exact preprocessing steps you'll need to perform will depend on the specific data you're working with and the requirements of your machine learning model.

=== "Python"
    ``` py title="import_data.py" linenums="1" hl_lines="5"
    # Import necessary packages
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    # Load data from a CSV file
    data = pd.read_csv('data.csv')

    # Data cleaning! A lot more can be done, this is basic
    data = data.dropna()  # Drop rows with missing values
    data = data.drop_duplicates()  # Drop duplicate rows

    # Feature extraction
    X = data[['feature1', 'feature2', 'feature3']]  # Select relevant features

    # Normalization
    scaler = StandardScaler()  # Create a scaler object
    X_norm = scaler.fit_transform(X)  # Normalize the feature values
    ```
=== "R"
    ``` r title="import_data.r" linenums="1" hl_lines="5"
    # Import necessary packages
    library(tidyverse)
    
    # Load data from a CSV file
    data <- read_csv("data.csv")
    ```
=== "SASPy"
    ``` py title="saspy_import_data.py" linenums="1" hl_lines="8"
    # Import necessary packages
    import saspy

    # Start a SAS session and check configuration information
    sas = saspy.SASsession(cfgname='default')

    # Load data from a CSV file
    data = sas.read_csv("./data.csv")
    ```
=== "SAS"
    ``` sas
    /* Reading a comma delimited file with a .csv extension                       */
    /*                                                                            */
    /* Since the DBMS= value is CSV, you do not have to use the DELIMITER=        */
    /* statement.  By default, it is assumed the variable names are on the first  */
    /* row, so the GETNAMES= statement is not required.                           */
    /*                                                                            */
    /* Create comma delimited test file to read using PROC IMPORT below.          */

    /* Load data from a CSV file */
    proc import
        datafile='data.csv'
        out=data
        dbms=csv
        replace; 
    run;

    /* Display data */
    proc print;
    run;
    ```

#### 4. Split the data into training and testing sets

 Once the data is preprocessed, you need to split it into training and testing sets. The training set will be used to train the machine learning model, while the testing set will be used to evaluate its performance.

=== "Python"
    ``` py title="cool_libraries.py" linenums="1" hl_lines="5"
    import pandas as pd
    from sklearn.model_selection import train_test_split

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_norm,
    data['target'], test_size=0.2, random_state=42)
    ```
=== "R"
    ``` r title="import_data.r" linenums="1" hl_lines="5"
    library(tidyverse)
    ```
=== "SASPy"
    ``` py title="saspy_import_data.py" linenums="1" hl_lines="8"
    import saspy
    ```
=== "SAS"
    ``` sas

    ```

!!! note
    We split the data into training and testing sets using the `train_test_split` function from scikit-learn, which randomly splits the data into two sets based on the specified test size and random seed.

#### 5. Define and train the machine learning model

With the data split, you can now define and train your machine learning model using the training set. This could involve selecting the appropriate algorithm, hyperparameter tuning, and cross-validation.

#### 6. Evaluate the model

After training the model, you need to evaluate its performance on the testing set. This will give you an idea of how well the model will perform on new, unseen data.

#### 7. Deploy the model

Finally, you can deploy the trained machine learning model in a production environment. This could involve packaging the model as a REST API, deploying it as a container, or integrating it with other applications or systems.

JupyterLab provides a powerful and flexible environment for training machine learning models. By following these steps, you can leverage JupyterLab's capabilities to build and train machine learning models that meet your specific needs and requirements.

### Using Argo Workflows

![Argo Workflows](../images/argo-workflows-assembly-line.jpg)

Argo Workflows is an open source container-native workflow engine designed for orchestrating parallel jobs and complex workflows on Kubernetes. It allows you to build, deploy, and manage machine learning workflows using containerized applications, making it an ideal tool for training machine learning models. Here are the steps to train a machine learning model using Argo Workflows:

#### 1. Define the workflow

First, you need to define the workflow for training the machine learning model. This involves specifying the sequence of steps, input data, and output data. You can use the Argo Workflows DSL to define your workflow.

#### 2. Build the container

Next, you need to build the container that contains the machine learning model and its dependencies. This can be done using a Dockerfile, which specifies the environment and dependencies needed to run the machine learning model.

#### 3. Push the container to a registry

Once the container is built, you need to push it to our Protected B container registry. This allows you and other users to download the container and use it in workflows.

#### 4. Define the workflow steps

With the container built and pushed to a registry, you can now define the workflow steps for training the machine learning model. This could include loading and preprocessing the data, training the model, and evaluating its performance.

#### 5. Run the workflow

After defining the workflow steps, you can now run the workflow using Argo Workflows. This will execute the steps in the containerized environment, ensuring reproducibility and consistency across different runs.

#### Examples

We have a couple of example scripts to get you started. Please take a look!

=== "Couler"
    ``` py title="couler.py" linenums="1" hl_lines="5"

    # Prepare your system
    !pip config --user set global.index-url https://jfrog.aaw.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
    !python3 -m pip install git+https://github.com/couler-proj/couler --ignore-installed

    # Define global variable for convenience
    NAMESPACE = "<your-namespace>"

    # Import necessary packages
    import json
    import random

    import couler.argo as couler
    from couler.argo_submitter import ArgoSubmitter


    # Define the steps (functions) used in the workflow
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
    ``` py title="hera.py" linenums="1" hl_lines="5"
    # Prepare your system
    !pip config --user set global.index-url https://jfrog.aaw.cloud.statcan.ca/artifactory/api/pypi/pypi-remote/simple
    !pip install hera-workflows
    
    # Import necessary packages
    import hera
    from hera import Task, Workflow

    # Configure Hera
    hera.global_config.GlobalConfig.token = "<your-token>"
    hera.global_config.GlobalConfig.host = "https://argo-workflows.aaw-dev.cloud.statcan.ca:443"
    hera.global_config.GlobalConfig.namespace = "<your-namespace>"
    hera.global_config.GlobalConfig.service_account_name = "<your-account-name>"


    # Define the steps (functions) used in the workflow
    def random_code():
        res = "heads" if random.randint(0, 1) == 0 else "tails"
        print(res)


    def heads():
        print("it was heads")


    def tails():
        print("it was tails")

    # Define the workflow
    with Workflow("coin-flip") as w:
        r = Task("r", random_code)
        h = Task("h", heads)
        t = Task("t", tails)

        h.on_other_result(r, "heads")
        t.on_other_result(r, "tails")

    # Run the workflow
    w.create()
    ```
=== "YAML"
    ``` py title="workflow.yaml" linenums="1" hl_lines="8"

    ```
=== "Seldon?"
    ``` py

    ```

## Why Containerized MLOps?

The advantages of using a containerized approach for training machine learning models with Argo Workflows include:

1. **Reproducibility:** Containerizing the machine learning model and its dependencies ensures that the environment remains consistent across different runs, making it easy to reproduce results.

2. **Scalability:** Argo Workflows can orchestrate parallel jobs and complex workflows, making it easy to scale up the training process as needed.

3. **Portability:** Containers can be run on any platform that supports containerization, making it easy to move the training process to different environments or cloud providers.

4. **Collaboration:** By pushing the container to a container registry, other users can easily download and use the container for their own purposes, making it easy to collaborate on machine learning projects.

Argo Workflows and containerization provide a powerful and flexible approach for training machine learning models. By leveraging these tools, data scientists and machine learning engineers can build, deploy, and manage machine learning workflows with ease and reproducibility.
