# Jupyter

## Friendly R and Python experience

Jupyter gives you **notebooks** to write your code and make visualizations. You
can quickly iterate, visualize, and sahre your analyses. Because it's running on
a server (that you set up in the last section) you can do really big analyses on
centralized hardware! Adding as much horsepower as you need! And because it's on
the cloud, you can share it with your colleagues too.

![Embed your visualizations](../images/jupyter_scikit.png)


## Get started with the examples

When you started your server, it got loaded with a bunch of example notebooks.
Great notebooks to start with are `R/01-R-Notebook-Demo.ipynb`, or the notebooks
in `scikitlearn`. `pytorch` and `tensorflow` are great if you are familiar with
machine learning. The `mapreduce-pipeline` and `ai-pipeline` are more advanced.

??? danger "Some notebooks only work in certain server versions"
    For instance, `gdal` is only in the geomatics image. So if you use another
    image then a notebook using gdal might not work.
    
## Adding software

You do not have `sudo` in Jupyter, but you can use 

```sh
conda install --use-local your_package_name
```

or

```sh
pip install --user your_package_name
```

**Don't forget to restart your jupyter kernel afterwards, to make new packages
available.****

??? tip "Make sure to restart the Jupyter kernel after installing new software"
    If you install software in a terminal, but your jupyter kernel was already
    running, then it will not be updated.
    
??? tip "Is there something that you can't install?"
    If you need something installed, reach us or [open a github issue](https://github.com/StatCan/kubeflow-containers).
    We can add it to the default software.
 
 
# Getting Data in and out of Jupyter
 
You can upload and download data to/from Jupyterhub directly in the menu. There
is an upload button at the top, and you can right-click most files or folders to
download them.

# TODO S3 browser?
 
 
 
 
 
 
 
!!! warning "Phasellus posuere in sem ut cursus"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
 
!!! note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
    
!!! success
    Lorem ipsum dolor sit amt, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
    
!!! tip
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
    
!!! failure
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
 
!!! danger
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! example
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.




