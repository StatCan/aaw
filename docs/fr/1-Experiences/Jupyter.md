# Jupyter

## Exp&eacute;rience conviviale de R et Python

Jupyter vous donne des **bloc-notes** pour &eacute;crire votre code et faire des visualisations. 
Vous pouvez rapidement it&eacute;rer, visualiser et partager vos analyses. Puisque Jupyter est ex&eacute;cut&eacute;
sur un serveur (que vous avez mis en place dans la derni&egrave;re section), il vous permet d'effectuer 
de tr&egrave;s grandes analyses sur un mat&eacute;riel centralis&eacute;! Ajoutez autant de puissance qu&#146;il vous faut! 
Et puisque c&#146;est dans le nuage, vous pouvez aussi le partager avec vos coll&egrave;gues.

### Explorez vos donn&eacute;es

Jupyter offre un certain nombre de fonctionnalit&eacute;s (et nous pouvons en ajouter d&#146;autres)

- &Eacute;l&eacute;ments visuels int&eacute;gr&eacute;s dans votre bloc-notes
- Volume de donn&eacute;es pour le stockage de vos donn&eacute;es
- Possibilit&eacute; de partager votre espace de travail avec vos coll&egrave;gues

![gadgets logiciels interactifs](../images/jupyter_visual.png)


### Environnement de d&eacute;veloppement dans le navigateur

Cr&eacute;ez pour explorer, et aussi pour &eacute;crire du code

- Linting et d&eacute;bogage
- Int&eacute;gration Git
- Terminal int&eacute;gr&eacute;
- Th&egrave;me clair/fonc&eacute; (changer les param&egrave;tres en haut)

![Fonctionnalit&eacute;s de l&#146;environnement de d&eacute;veloppement](../images/jupyter_ide.png)

**Plus de renseignements sur Jupyter [ici](https://jupyter.org)**



## Commencez par les exemples

Lorsque vous avez d&eacute;marr&eacute; votre serveur, il a &eacute;t&eacute; charg&eacute; de mod&egrave;les de bloc-notes.
Parmi les bons blocs-notes pour commencer, il y a `R/01-R-Notebook-Demo.ipynb` et ceux dans
dans `scikitlearn`. Les bloc-notes `pytorch` et `tensorflow` sont excellents si vous connaissez
l&#146;apprentissage automatique. `mapreduce-pipeline` et `ai-pipeline` sont plus avanc&eacute;s.

??? danger "Certains bloc-notes ne fonctionnent que dans certaines versions de serveur"
    Par exemple, `gdal` ne fonctionne que dans l&#146;image g&eacute;omatique. Donc, si vous utilisez une autre
    image, un bloc-notes utilisant `gdal` pourrait ne pas fonctionner.
    
## Ajout de logiciels

Vous n&#146;avez pas `sudo` dans Jupyter, mais vous pouvez utiliser 

```sh
conda install --use-local your_package_name
```

ou

```sh
pip install --user your_package_name
```


**N&#146;oubliez pas de red&eacute;marrer votre noyau Jupyter par la suite, pour acc&eacute;der &agrave; de nouvelles trousses.**

??? warning "Assurez-vous de red&eacute;marrer le noyau Jupyter apr&egrave;s l&#146;installation d&#146;un nouveau logiciel"
    Si vous installez un logiciel dans un terminal, mais que votre noyau Jupyter &eacute;tait d&eacute;j&agrave;
    en cours d&#146;ex&eacute;cution, il ne sera pas mis &agrave; jour.
    
??? warning "Y a-t-il quelque chose que vous ne pouvez pas installer?"
    Si vous avez besoin d&#146;installer quelque chose, communiquez avec nous 
    ou [ouvrir une question GitHub](https://github.com/StatCan/kubeflow-containers).
    Nous pouvons l&#146;ajouter au logiciel par d&eacute;faut.
 
 
# Entrer et sortir des donn&eacute;es de Jupyter
 
Vous pouvez t&eacute;l&eacute;charger et charger des donn&eacute;es vers ou depuis Jupyterhub directement dans le menu. 
Il y a un bouton de chargement en haut, et vous pouvez cliquer avec le bouton droit de la souris 
sur la plupart des fichiers ou dossiers pour les t&eacute;l&eacute;charger.



## Stockage partag&eacute; en compartiment

**L&#146;autre option** est le stockage de gros volumes avec 
[Stockage d&#146;objets](https://en.wikipedia.org/wiki/Object_storage).
&Eacute;tant donn&eacute; que le stockage est important pour les exp&eacute;rimentations, la diffusion 
et l&#146;exploration des ensembles de donn&eacute;es, une section lui est consacr&eacute;


**Consultez la [section sur le stockage](/Stockage)**
