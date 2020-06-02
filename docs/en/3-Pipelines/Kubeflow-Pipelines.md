# Overview

[Kubeflow Pipelines](https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/) is a platform for building machine learning workflows for deployment in a Kubernetes environment.  It enables authoring *pipelines* that encapsulate analytical workflows (transforming data, training models, building visuals, etc.).  These *pipelines* can be shared, reused, and scheduled, and are built to run on compute provided via Kubernetes. 

In the context of the Advanced Analytics Workspace, Kubeflow Pipelines are interacted with through:

* The Kubeflow [UI](../1-Experiments/Kubeflow.md), where from the Pipelines menu you can upload pipelines, view the pipelines you have and their results, etc.
* The Kubeflow Pipelines python [SDK](https://www.kubeflow.org/docs/pipelines/sdk/sdk-overview/), accessible through the [Jupyter Notebook Servers](../1-Experiments/Kubeflow.md#create-a-server), where you can define your components and pipelines, submit them to run now, or even save them for later.

This document provides a brief explanation of KubeFlow Pipelines and how to get started with them on the Advanced Analytics Workspace.  More comprehensive pipeline examples specifically made for this platform are available on [github](https://github.com/StatCan/jupyter-notebooks) (and mirrored automatically to every Notebook Server at `/jupyter-notebooks`), as well as from [public sources](https://github.com/kubeflow/pipelines/tree/master/samples).  See [here](https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/) for a more detailed general explanation of Kubeflow Pipelines.
 
# What are Pipelines and How do they Work?

A [*pipeline*](https://www.kubeflow.org/docs/pipelines/overview/concepts/pipeline/) in Kubeflow Pipelines consists of one or more [*pipeline components*](https://www.kubeflow.org/docs/pipelines/overview/concepts/component/) chained together to form a workflow as a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (effectively a flow chart that describes the order of operations within your pipeline).  As a rough analogy a *pipeline* is the script that you'd run to do your work while the *components* are the functions that script calls upon to make that happen.  So the *pipeline* describes the entire workflow of what you want to accomplish, while the *pipeline components* each describe individual steps in that process (such as pulling columns from a data store, transforming data, or training a model).  Each *component* is (ideally) a single purpose operation (eg: if during preprocessing you need to remove a column and merge two data sources, do those as two separate, single purpose, operations rather than a single component.  

At their core, each *component* has:
 
 *  a standalone application, packaged as a [docker images](https://docs.docker.com/get-started/), for doing the actual work.  The code in the docker image could be a shell script, python script, or anything else you can run from a Linux terminal
 *  A description of how Kubeflow Pipelines runs the code (where is the image, what command line arguments does it accept, what outputs does it generate), as a YAML file
 
A *pipeline* then, using the above *components*, defines the logic for how *components* are connected, such as:
 
 1. run ComponentA
 1. pass the output from ComponentA to ComponentB and ComponentC
 1. ...
 
*Pipelines* are also defined by YAML files (these YAML file pipelines are what you would pass to Kubeflow to run your pipeline).
 
# Define and run your first Pipeline

While *pipelines* and *components* are defined by YAML files, the python [SDK](https://www.kubeflow.org/docs/pipelines/sdk/sdk-overview/) let's you define them from python code.  The following is an example of how to define a [simple pipeline](https://github.com/StatCan/jupyter-notebooks/blob/master/kfp-basics/average_with_docker_components.ipynb) using the python SDK.  

The objective of our pipeline is, given five numbers, compute:

1. The average of the first three numbers
1. The average of the last two numbers
3. The average of the results of (1) and (2) 

To do this, we define a *pipeline* that uses our average *component* to do the computations.  

The *average* component is defined by a docker image with a simple python script that:
 * accepts one or more numbers as command line arguments 
 * returns the average of these numbers, written to the file `out.txt` within its container

To tell Kubeflow Pipelines how to use this image, we define our average *component* through a ContainerOp which tells Kubeflow our image's API.  The ContainerOp instance sets the docker image location, how to pass arguments to it, and what outputs to pull from the container.  To actually use these ContainerOp's in our pipeline, we build factory functions like `average_op` (as we'll probably want more than just one average *component*).  

```
from kfp import dsl

def average_op(*numbers):
    """
    Factory for average ContainerOps
    
    Accepts an arbitrary number of input numbers, returning a ContainerOp that passes those
    numbers to the underlying docker image for averaging
    
    Returns output collected from ./out.txt from inside the container

    """
    # Input validation
    if len(numbers) < 1:
        raise ValueError("Must specify at least one number to take the average of")
        
    return dsl.ContainerOp(
        name="averge",  # What will show up on the pipeline viewer
        image="k8scc01covidacr.azurecr.io/kfp-components/average:v1",  # The image that KFP runs to do the work
        arguments=numbers,  # Passes each number as a separate (string) command line argument
        # Script inside container writes the result (as a string) to out.txt, which 
        # KFP reads for us and brings back here as a string
        file_outputs={'data': './out.txt'},  
    )
```

We define our pipeline as a python function that uses our above ComponentOp factories, decorated by the @dsl.pipeline decorator.  Our pipeline uses our *average* component by passing it numbers, and we use the *average* results by passing them to later functions through accessing `avg_*.output`.

```
@dsl.pipeline(
    name="my pipeline's name"
)
def my_pipeline(a, b, c, d, e):
    """
    Averaging pipeline which accepts five numbers and does some averaging operations on them
    """
    # Compute averages for two groups
    avg_1 = average_op(a, b, c)
    avg_2 = average_op(d, e)
    
    # Use the results from _1 and _2 to compute an overall average
    average_result_overall = average_op(avg_1.output, avg_2.output)
```

And finally, we save a YAML definition of our pipeline for later passing to Kubeflow Pipelines.  This YAML describes to Kubeflow Pipelines exactly how to run our pipeline - unzip it and take a look yourself!

```
from kfp import compiler
pipeline_yaml = 'pipeline.yaml.zip'
compiler.Compiler().compile(
    my_pipeline,
    pipeline_yaml
)
print(f"Exported pipeline definition to {pipeline_yaml}")
```

??? warning "Kubeflow Pipelines is a lazy beast"
    It is useful to keep in mind what computation is happening when you run this python code versus what happens when you submit the pipeline to Kubeflow Pipelines.  Although it seems like everything is happening in the moment, try adding `print(avg_1.output)` to the above pipeline and see what happens when you compile your pipeline.  The python SDK we're using is for **authoring** pipelines, not for running them, so results from components will never be available when you run this python code.  The is discussed more below in **# Understanding what computation occurs when**.

To actually run our pipeline, we define an experiment:

```
experiment_name = "averaging-pipeline"

import kfp
client = kfp.Client()
exp = client.create_experiment(name=experiment_name)

pl_params = {
    'a': 5,
    'b': 5,
    'c': 8,
    'd': 10,
    'e': 18,
}

```

Which is observable in the Kubeflow Pipelines [UI](../1-Experiments/Kubeflow.md):

![Kubeflow Pipeline Experiment](../images/kfp_experiment.png)

And then run an instance of our pipeline with the arguments we want:

```
import time

run = client.run_pipeline(
    exp.id,  # Run inside the above experiment
    experiment_name + '-' + time.strftime("%Y%m%d-%H%M%S"),  # Give our job a name with a timestamp so its unique
    pipeline_yaml,  # Pass the .yaml.zip we created above.  This defines the pipeline
    params=pl_params  # Pass our parameters we want to run the pipeline with
)
```

which can also be seen in the UI:

![Kubeflow Pipeline Experiment](../images/kfp_experiment.png)

Later when we want to reuse the pipeline, we can pass different arguments and do it all again (or even reuse it from within the Kubeflow UI).

To understand this example further, open it up in Kubeflow and try it for yourself.

# Lightweight components

Under construction, sorry!

# Understanding what computation occurs when

Under construction, sorry!
