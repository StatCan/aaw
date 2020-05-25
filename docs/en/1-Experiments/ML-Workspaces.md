<h1 align="center">
    <a href="https://github.com/ml-tooling/ml-workspace" title="ML Workspace Home">
    <img width=50% alt="" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/ml-workspace-logo.png"> </a>
    <br>
</h1>

<p align="center">
    <strong>All-in-one web-based development environment for machine learning</strong>
</p>

<p align="center">
    <a href="https://hub.docker.com/r/mltooling/ml-workspace" title="Docker Image Version"><img src="https://images.microbadger.com/badges/version/mltooling/ml-workspace.svg"></a>
    <a href="https://hub.docker.com/r/mltooling/ml-workspace" title="Docker Pulls"><img src="https://img.shields.io/docker/pulls/mltooling/ml-workspace.svg"></a>
    <a href="https://hub.docker.com/r/mltooling/ml-workspace" title="Docker Image Metadata"><img src="https://images.microbadger.com/badges/image/mltooling/ml-workspace.svg"></a>
    <a href="https://github.com/ml-tooling/ml-workspace/blob/master/LICENSE" title="ML Workspace License"><img src="https://img.shields.io/badge/License-Apache%202.0-green.svg"></a>
    <a href="https://gitter.im/ml-tooling/ml-workspace" title="Chat on Gitter"><img src="https://badges.gitter.im/ml-tooling/ml-workspace.svg"></a>
    <a href="https://twitter.com/mltooling" title="ML Tooling on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?style=social"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#features">Features & Screenshots</a> •
  <a href="#support">Support</a> •
  <a href="https://github.com/ml-tooling/ml-workspace/issues/new?labels=bug&template=01_bug-report.md">Report a Bug</a> •
  <a href="#faq">FAQ</a> •
  <a href="#known-issues">Known Issues</a> •
  <a href="#contribution">Contribution</a>
</p>

The ML workspace is an all-in-one web-based IDE specialized for machine learning and data science. It is simple to deploy and gets you started within minutes to productively built ML solutions on your own machines. This workspace is the ultimate tool for developers preloaded with a variety of popular data science libraries (e.g., Tensorflow, PyTorch, Keras, Sklearn) and dev tools (e.g., Jupyter, VS Code, Tensorboard) perfectly configured, optimized, and integrated.

## Highlights

- 💫 Jusual Studio Code web-based IDEs.
- 🖥 Full Linux desktop GUI accessible via web browser.
- 🔀 Seamless Git integration optimized for notebooks.
- 📈 Integrated hardware & training monitoring via Tensorboard & Netdata.
- 🚪 Access from anywhere via Web, 


<p>

## Features

<p align="center">
  <a href="#desktop-gui">Desktop GUI</a> •
  <a href="#visual-studio-code">VS Code</a> •
  <a href="#git-integration">Git Integration</a> •
  <a href="#file-sharing">File Sharing</a> •
  <a href="#access-ports">Access Ports</a> •
  <a href="#hardware-monitoring">Hardware Monitoring</a> •
  <a href="#remote-development">Remote Development</a> •
</p>

The workspace is equipped with a selection of best-in-class open-source development tools to help with the machine learning workflow. Many of these tools can be started from the `Open Tool` menu from Jupyter (the main application of the workspace):

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/open-tools.png"/>

### Desktop GUI

This workspace provides an HTTP-based VNC access to the workspace via [noVNC](https://github.com/novnc/noVNC). Thereby, you can access and work within the workspace with a fully-featured desktop GUI. To access this desktop GUI, go to `Open Tool`, select `VNC`, and click the `Connect` button. In the case you are asked for a password, use `vncpassword`.

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/desktop-vnc.png"/>

Once you are connected, you will see a desktop GUI that allows you to install and use full-fledged web-browsers or any other tool that is available for Ubuntu. Within the `Tools` folder on the desktop, you will find a collection of install scripts that makes it straightforward to install some of the most commonly used development tools, such as Atom, PyCharm, R-Runtime, R-Studio, or Postman (just double-click on the script).

**Clipboard:** If you want to share the clipboard between your machine and the workspace, you can use the copy-paste functionality as described below:

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/desktop-vnc-clipboard.png"/>


### Visual Studio Code

[Visual Studio Code](https://github.com/microsoft/vscode) (`Open Tool -> VS Code`) is an open-source lightweight but powerful code editor with built-in support for a variety of languages and a rich ecosystem of extensions. It combines the simplicity of a source code editor with powerful developer tooling, like IntelliSense code completion and debugging. The workspace integrates VS Code as a web-based application accessible through the browser-based on the awesome [code-server](https://github.com/cdr/code-server) project. It allows you to customize every feature to your liking and install any number of third-party extensions.

<p align="center"><img src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/vs-code.png"/></p>

The workspace also provides a VS Code integration into Jupyter allowing you to open a VS Code instance for any selected folder, as shown below:

<p align="center"><img src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/vs-code-open.png"/></p>


### File Sharing

The workspace has a feature to share any file or folder with anyone via a token-protected link. To share data via a link, select any file or folder from the Jupyter directory tree and click on the share button as shown in the following screenshot:

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/file-sharing-open.png"/>

This will generate a unique link protected via a token that gives anyone with the link access to view and download the selected data via the [Filebrowser](https://github.com/filebrowser/filebrowser) UI:

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/file-sharing-filebrowser.png"/>

To deactivate or manage (e.g., provide edit permissions) shared links, open the Filebrowser via `Open Tool -> Filebrowser` and select `Settings->User Management`.

### Access Ports

It is possible to securely access any workspace internal port by selecting `Open Tool -> Access Port`. With this feature, you are able to access a REST API or web application running inside the workspace directly with your browser. The feature enables developers  to build, run, test, and debug REST APIs or web applications directly from the workspace.

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/access-port.png"/>

If you want to use an HTTP client or share access to a given port, you can select the `Get shareable link` option. This generates a token-secured link that anyone with access to the link can use to access the specified port.

> _The HTTP app requires to be resolved from a relative URL path or configure a base path (`/tools/PORT/`)._

<details>

<summary>Example (click to expand...)</summary>

1. Start an HTTP server on port `1234` by running this command in a terminal within the workspace: `python -m http.server 1234`
2. Select `Open Tool -> Access Port`, input port `1234`, and select the `Get shareable link` option.
3. Click `Access`, and you will see the content provided by Python's `http.server`.
4. The opened link can also be shared to other people or called from external applications (e.g., try with Incognito Mode in Chrome).

</details>


<details>
<summary><b>VS Code - Remote Machine</b> (click to expand...)</summary>

The Visual Studio Code [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension allows you to open a remote folder on any remote machine with SSH access and work with it just as you would if the folder were on your own machine. Once connected to a remote machine, you can interact with files and folders anywhere on the remote filesystem and take full advantage of VS Code's feature set (IntelliSense, debugging, and extension support). The discovers and works out-of-the-box with passwordless SSH connections as configured by the workspace SSH setup script. To enable your local VS Code application to connect to a workspace:

1. Install [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension inside your local VS Code.
2. Run the SSH setup script of a selected workspace as explained in the [SSH Access](#ssh-access) section.
3. Open the Remote-SSH panel in your local VS Code. All configured SSH connections should be automatically discovered. Just select any configured workspace connection you like to connect to as shown below:

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/remote-dev-vscode.gif"/>

> 📖 _You can find additional features and information about the Remote SSH extension in [this guide](https://code.visualstudio.com/docs/remote/ssh)._

</details>


### Hardware Monitoring

The workspace provides two pre-installed web-based tools to help developers during model training and other experimentation tasks to get insights into everything happening on the system and figure out performance bottlenecks.

[Netdata](https://github.com/netdata/netdata) (`Open Tool -> Netdata`) is a real-time hardware and performance monitoring dashboard that visualize the processes and services on your Linux systems. It monitors metrics about CPU, GPU, memory, disks, networks, processes, and more.

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/hardware-monitoring-netdata.png" />

[Glances](https://github.com/nicolargo/glances) (`Open Tool -> Glances`) is a web-based hardware monitoring dashboard as well and can be used as an alternative to Netdata.

<img style="width: 100%" src="https://github.com/ml-tooling/ml-workspace/raw/master/docs/images/features/hardware-monitoring-glances.png"/>

> _Netdata and Glances will show you the hardware statistics for the entire machine on which the workspace container is running._

### Run as a job

> _A job is defined as any computational task that runs for a certain time to completion, such as a model training or a data pipeline._

The workspace image can also be used to execute arbitrary Python code without starting any of the pre-installed tools. This provides a seamless way to productize your ML projects since the code that has been developed interactively within the workspace will have the same environment and configuration when run as a job via the same workspace image.

<details>
<summary><b>Run Python code as a job via the workspace image</b> (click to expand...)</summary>

To run Python code as a job, you need to provide a path or URL to a code directory (or script) via `EXECUTE_CODE`. The code can be either already mounted into the workspace container or downloaded from a version control system (e.g., git or svn) as described in the following sections. The selected code path needs to be python executable. In case the selected code is a directory (e.g., whenever you download the code from a VCS) you need to put a `__main__.py` file at the root of this directory. The `__main__.py` needs to contain the code that starts your job.

#### Run code from version control system

You can execute code directly from Git, Mercurial, Subversion, or Bazaar by using the pip-vcs format as described in [this guide](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support). For example, to execute code from a [subdirectory](https://github.com/ml-tooling/ml-workspace/tree/master/resources/tests/ml-job) of a git repository, just run:

```bash
docker run --env EXECUTE_CODE="git+https://github.com/ml-tooling/ml-workspace.git#subdirectory=resources/tests/ml-job" mltooling/ml-workspace:latest
```

> 📖 _For additional information on how to specify branches, commits, or tags please refer to [this guide](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support)._

#### Run code mounted into the workspace

In the following example, we mount and execute the current working directory (expected to contain our code) into the `/workspace/ml-job/` directory of the workspace:

```bash
docker run -v "${PWD}:/workspace/ml-job/" --env EXECUTE_CODE="/workspace/ml-job/" mltooling/ml-workspace:latest
```


### Pre-installed Libraries and Interpreters

The workspace is pre-installed with many popular interpreters, data science libraries, and ubuntu packages:

- **Interpreter:** Python 3.7 (Miniconda 3), Java 11 (OpenJDK), NodeJS 13, Scala, Perl 5
- **Python libraries:** Tensorflow, Keras, Sklearn, XGBoost, MXNet, Theano, and [many more](https://github.com/ml-tooling/ml-workspace/tree/master/resources/libraries)
- **Package Manager:** `conda`, `pip`, `npm`, `apt-get`, `yarn`, `sdk`, `gdebi`, `mvn` ...  

The full list of installed tools can be found within the [Dockerfile](https://github.com/ml-tooling/ml-workspace/blob/master/Dockerfile).

> _For every minor version release, we run vulnerability, virus, and security checks within the workspace using [vuls](https://vuls.io/), [safety](https://pyup.io/safety/), and [clamav](https://www.clamav.net/) to make sure that the workspace environment is as secure as possible._

### Extensibility

The workspace provides a high degree of extensibility. Within the workspace, you have **full root & sudo privileges** to install any library or tool you need via terminal (e.g., `pip`, `apt-get`, `conda`, or `npm`). You can open a terminal by one of the following ways:

- **Desktop VNC:** `Applications -> Terminal Emulator`
- **VS Code:** `Terminal -> New Terminal`

Additionally, pre-installed tools such as Jupyter, JupyterLab, and Visual Studio Code each provide their own rich ecosystem of extensions. The workspace also contains a [collection of installer scripts](https://github.com/ml-tooling/ml-workspace/tree/master/resources/tools) for many commonly used development tools or libraries (e.g., `PyCharm`, `Zeppelin`, `RStudio`, `Starspace`). You can find and execute all tool installers via `Open Tool -> Install Tool`. Those scripts can be also executed from the Desktop VNC (double-click on the script within the `Tools` folder on the Desktop VNC).

</details>

