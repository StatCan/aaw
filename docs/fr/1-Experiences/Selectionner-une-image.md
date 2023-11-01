# Sélection d'une image pour votre serveur bloc-notes

En fonction de votre projet ou du cas d'utilisation du serveur bloc-notes, certaines images peuvent être plus adapté que d'autres. Ce qui suit passera en revue les caractéristiques principales de chacun pour vous aider à choisir l’image la plus appropriée pour vous.

Lors de la sélection d'une image, vous disposez de 3 options principales :

- Carnet Jupyter (CPU, TensorFlow, PyTorch)
- RStudio
- Bureau à distance

## Bloc-notes Jupyter

Les [bloc-notes Jupyter](https://jupyter.org/) sont utilisés pour créer et partager documents interactifs contenant un mélange de code en direct, de visualisations et de texte. Ceux-ci peuvent être écrits en `Python`, `Julia` ou `R`.

<center>
![Bloc-notes Jupyter](../images/jupyter_in_action.png)
</center>

<!-- plus joli-ignorer -->
??? info "Les utilisations courantes incluent :"
     transformation de données, simulation numérique, statistique
     modélisation, apprentissage automatique et bien plus encore.

Les bloc-notes Jupyter sont d'excellents tremplins pour l'analyse, y compris les apprentissage automatique. L'image `jupyterlab-cpu` donne une bonne expérience de base pour python, y compris des paquets courants tels que `numpy`, `pandas` et `scikit-learn`. Si vous souhaitez spécifiquement utiliser **_TensorFlow_** ou **_PyTorch_**, nous ont également `jupyterlab-tensorflow` et `jupyterlab-pytorch` qui viennent avec ceux outils préinstallés.

Pour l'image `jupyterlab-pytorch`, les paquets PyTorch (torch, torchvision, et torchaudio) sont installés dans l'environnement conda `torch`. Vous devez activez cet environnement pour utiliser PyTorch.

Pour `jupyterlab-cpu`, `jupyterlab-tensorflow` et `jupyterlab-pytorch` images, dans le shell par défaut, la commande `conda activate` peut ne pas fonctionner. C'est en raison de l'environnement qui n'est pas initialisé correctement. Dans ce cas, lancez `bash`, vous devriez voir le logo AAW et quelques instructions apparaître. Après ça `conda activate` devrait fonctionner correctement. Si vous voyez le logo AAW au démarrage signifie que l'environnement est correctement initialisé et que `conda activate` devrait fonctionner correctement. Un correctif pour ce bug est en préparation, une fois celui-ci corrigé, ce paragraphe sera supprimé.

Chaque image est préchargée avec VS Code dans le navigateur si vous préférez une expérience IDE complète.

## RStudio

**[RStudio](../RStudio/)** vous offre un environnement de développement intégré spécifiquement pour `R`. Si vous codez en `R`, il s'agit généralement du Serveur Bloc-notes à utiliser. Utilisez l'image `rstudio` pour obtenir un environnement RStudio.

![RStudio](../images/rstudio_visual.png)

## Bureau à distance

Pour une expérience de bureau Ubuntu complète, utilisez l'image du bureau à distance. Elle est préchargée avec les outils Python, R et Geomatics, mais dans une expérience de bureau typique qui comprend également Firefox, VS Code et les outils Open Office. Le système d'exploitation est **[Ubuntu](https://ubuntu.com/about)** 22.04 avec l'environnement de bureau **[XFCE](https://www.xfce.org/about)**.

![Capture d'écran du bureau virtuel](../images/rd_desktop.png)