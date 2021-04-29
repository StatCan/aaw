# Remote Desktop

![Remote Desktop](../images/rd_desktop.png)

# What is Remote Desktop?

Remote Desktop provides an in-browser GUI Ubuntu desktop experience as well as
quick access to supporting tools. The operating system is
[**Ubuntu**](https://ubuntu.com/about) **18.04** with the
[**XFCE**](https://www.xfce.org/about) desktop environment.

## Versions

Two versions of Remote Desktop are available. _R_ includes R and RStudio.
_Geomatics_ extends _R_ with QGIS and various supporting libraries. You may
further customize your Remote Desktop workspace to suit your specific needs and
preferences.

## Customization

_pip_, _conda_, _npm_ and _yarn_ are available to install various packages.

# Accessing the Remote Desktop

To launch the Remote Desktop or any of its supporting tools, create a Notebook
Server in [Kubeflow](./Kubeflow.md) and select one of the available versions in
the image dropdown. Then, click `Connect` to be redirected to the Remote
Desktop.

_Remote Desktop_ brings you to the Desktop GUI through a noVNC session. Click on
the > on the left side of the screen to expand a panel with options such as
fullscreen and clipboard access.

![NoVNC Panel](../images/rd_novnc_panel.png)

# In-browser Tools

## VS Code

Visual Studio Code is a lightweight but powerful source code editor. It comes
with built-in support for JavaScript, TypeScript and Node.js and has a rich
ecosystem of extensions for several languages (such as C++, C#, Java, Python,
PHP, Go).

![VS Code](../images/rd_vs_code.png)

# Footnotes

Remote Desktop is based on
[ml-tooling/ml-workspace](https://github.com/ml-tooling/ml-workspace).
