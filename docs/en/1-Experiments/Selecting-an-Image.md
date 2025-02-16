# Selecting an Image for your Notebook Server

Depending on your project or use case of the Notebook Server, some images may be more suitable than others. The following will go through the main features of each to help you pick the most appropriate image for you.

When selecting an image, you have 3 main options:

- Jupyter Notebook (CPU, TensorFlow, PyTorch)
- RStudio
- Remote Desktop

## Jupyter Notebooks

[Jupyter Notebooks](https://jupyter.org/) are used to create and share interactive documents that contain a mix of live code, visualizations, and text. These can be written in `Python`, `Julia`, or `R`.

<center>
![Jupyter Notebooks](../images/jupyter_in_action.png)
</center>

<!-- prettier-ignore -->
??? info "Common uses include:"
    data transformation, numerical simulation, statistical
    modelling, machine learning and more.

The jupyter notebooks are great launchpads for analytics including machine learning. The `jupyterlab-cpu` image gives a good core experience for python, including common packages such as `numpy`, `pandas` and `scikit-learn`. If you're interested specifically in using **_TensorFlow_**, we also have `jupyterlab-tensorflow` which come with those tools pre-installed.

For users interested in working with PyTorch, there is support for quickly installing the required packaged.
In the terminal on your created notebook, run the following command:
`mamba clean -a -y && mamba create -n torch && mamba install -n torch -c conda-forge -c pytorch -c nvidia -y --file /usr/local/bin/requirements.txt`
The PyTorch packages (torch, torchvision, and torchaudio) will be installed in the `torch` conda environment.
You must activate this environment using `mamba activate torch` to use PyTorch.
The environment can also be added to the to the JupyterLab Launcher with the following command:

```bash
python -m ipykernel install --user --name "torch" --display-name "PyTorch"
```

For the `jupyterlab-cpu`, and `jupyterlab-tensorflow` images, in the default shell the `conda activate` command may not work. This is due to the environment not being initialized properly. In this case run `bash`, you should see the AAW logo and a few instructions appear. After this `conda activate` should work properly. If you see the AAW logo on startup it means the environment is correctly initialized and `conda activate` should work properly. A fix for this bug is in the works, once this is fixed this paragraph will be removed.

Each image comes pre-loaded with VS Code in the browser if you prefer a full IDE experience.

## RStudio

**[RStudio](../RStudio/)** gives you an integrated development environment specifically for `R`. If you're coding in `R`, this is typically the Notebook Server to use. Use the `rstudio` image to get an RStudio environment.

![RStudio](../images/rstudio_visual.png)

## Remote-Desktop

For a full Ubuntu desktop experience, use the remote desktop image. It comes pre-loaded with Python, R and Geomatics tooling, but are delivered in a typical desktop experience that also comes with Firefox, VS Code, and open office tools. The operating system is **[Ubuntu](https://ubuntu.com/about)** 22.04 with the **[XFCE](https://www.xfce.org/about)** desktop environment.

![Screenshot of the Virtual Desktop](../images/rd_desktop.png)
