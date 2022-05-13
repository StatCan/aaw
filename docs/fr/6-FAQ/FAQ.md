**IMPORTANT** Si votre question ne figure pas dans ce document, veuillez nous contacter sur Slack dans le canal #général.


# GÉNÉRALE

## Qu'est-ce que l'EEA?

L'espace de travail d'analyse avancée est une plateforme du programme d'analyse de données en tant que service (DAaaS) de Statistique Canada. Il est mis à la disposition des utilisateurs de Statistique Canada et des collaborateurs externes. Il comprend plusieurs outils de science des données à code source ouvert, est basé sur Kubeflow et utilise MinIO pour le stockage.

## Qu'est-ce que Kubeflow?

Kubeflow est une plateforme d'apprentissage automatique gratuite et open-source conçue pour permettre l'utilisation de pipelines d'apprentissage automatique afin d'orchestrer des flux de travail compliqués fonctionnant sur Kubernetes (par exemple, effectuer un traitement de données puis utiliser TensorFlow ou PyTorch pour entraîner un modèle, et le déployer sur TensorFlow Serving ou Seldon). Kubeflow était basé sur la méthode interne de Google pour déployer les modèles TensorFlow, appelée TensorFlow Extended.


## Qu'est-ce que MinIO?

MinIO est un type de stockage objet haute performance. Il est compatible avec l'API du service de stockage en nuage Amazon S3. Il peut gérer des données non structurées telles que des photos, des vidéos, des fichiers journaux, des sauvegardes et des images de conteneurs avec une taille d'objet maximale prise en charge de 5 TB.

## Quel sont les espaces de noms?

Les espaces de noms isolent les utilisateurs ou un groupe d'utilisateurs de Kubeflow. Un utilisateur de Kubeflow peut posséder plus qu'un espace de noms et il peut inviter des utilisateurs à rejoindre son espace de noms pour permettre la collaboration sur les mêmes données et code.

## À quoi servent les GPU?

Les GPU sont des multiplicateurs de matrice efficaces. Lors de la formation d'un modèle d'apprentissage automatique, en particulier d'un réseau neuronal, la plupart des calculs effectués sont des multiplications matricielles, et les GPU sont donc bien adaptés à la formation des réseaux neuronaux. Si vous n'avez pas besoin de former un modèle de réseau neuronal, vous n'avez probablement pas besoin d'un GPU. Comme les GPU consomment beaucoup d'énergie, ils sont coûteux à exécuter dans le nuage et doivent donc être utilisés avec parcimonie.

# PORTAIL

## Qui peut accéder l'EAA?

Toute personne ayant une adresse de courriel de Statistique Canada (@statcan.gc.ca) peut accéder l'EAA. Si un organisme ou un partenaire externe a besoin d'y avoir accès, il devra avoir un compte en nuage de Statistique Canada et devra faire une demande et conclure une entente avec Statistique Canada.

## Comment puis-je accéder au portail?

L'EAA et ses services sont accessibles par [le portail EAA](https://analytics-platform.statcan.gc.ca/covid19).

## Quels sont les services disponibles à partir du portail?

A partir du portail EAA, vous pouvez trouver Kubeflow et MinIO.

- [Kubeflow](https://kubeflow.aaw.cloud.statcan.ca/)
- [MinIO](https://minio.aaw.cloud.statcan.ca/)

## Où puis-je trouver de la documentation supplémentaire?

Le portail contient des liens vers notre guide de l'utilisateur, des vidéos et notre canal Slack. Si le guide de l'utilisateur et les vidéos ne contiennent pas les réponses que vous recherchez, contactez-nous sur Slack.

## Puis-je laisser des commentaires?

Bien entendu, nous sommes ouverts à toutes sortes de commentaires. Il vous suffit de suivre le lien "Leave Feedback" sur notre portail et de laisser votre commentaire.

- [Advanced Analytics Workspace Portal](https://analytics-platform.statcan.gc.ca/covid19)

## Y a-t-il une préférence pour l'utilisation de @statcan.gc.ca ou de @cloud.statcan.ca ou cela a-t-il une importance?

Bien que vous soyez libre d'utiliser l'un ou l'autre, vos espaces de travail ne seront disponibles que pour le compte associé. Pour simplifier l'utilisation de l'EAA, il est recommandé de choisir une adresse électronique et de s'y tenir.

# SLACK

## Pourquoi ne puis-je pas accéder à Slack?

Il existe de nombreuses possibilités pour qu'un utilisateur ne puisse pas accéder à notre espace de travail Slack.  Votre département a peut-être refusé l'accès à Slack, pour le savoir, vérifiez :Est-ce bloqué dans mon département.ca. Un autre problème courant est que l'équipe EAA peut avoir besoin d'ajouter le domaine de messagerie de votre département pour permettre l'accès à Slack.

## Quel canal dans l'espace de travail Slack de l'EAA dois-je laisser ma demande / question / préoccupation?

Veuillez utiliser le canal #général.

# KUBEFLOW

## Espace(s) de noms

### Où puis-je trouver l'espace de nommage que j'utilise actuellement?

Vous pouvez trouver votre espace de nom dans KUBEFLOW dans le coin supérieur gauche à côté de l'icône KUBEFLOW.

### Puis-je partager les données de mon (mes) espace(s) de noms avec d'autres utilisateurs?

Vous pouvez certainement partager votre espace de noms avec d'autres utilisateurs. En tant que propriétaire d'un espace de nommage, vous avez la possibilité d'ajouter des contributeurs.

### Puis-je avoir plusieurs espaces de noms et être le propriétaire de chacun d'entre eux?

La réponse rapide est oui. Pour être propriétaire de plusieurs espaces de noms, vous devez demander à l’équipe EAA de créer les espaces de noms pour vous. Vous devrez fournir votre adresse email et le nom de l'espace de nom de votre choix. Nous demandons généralement que le nom de votre espace de nom soit unique et par projet.

### Comment ajouter d'autres personnes à mon espace de nom (pour la collaboration)?

Dans la barre latérale de gauche, vous trouverez GÉRER LES CONTRIBUTEURS.  En tant que propriétaire, vous pourrez ajouter des contributeurs en saisissant leur adresse électronique. L'adresse e-mail est celle que le contributeur utilise pour se connecter à KUBEFLOW. Attention : lorsque vous ajoutez des utilisateurs à votre espace de nom, le champ de l'adresse email est sensible à la casse et certains utilisateurs ont des majuscules, donc assurez-vous d'ajouter leur adresse email exactement comme elle apparaît dans l'interface Kubeflow.

# La section Gérer les contributeurs contient les informations relatives à votre compte.

*Les adresses électroniques sont sensibles à la casse!*

## Un espace de nom peut-il changer de propriétaire?

Oui, il est possible de transférer la propriété des espaces de noms des contributeurs. Veuillez nous le demander et nous le ferons pour vous.

## Quelle est la différence entre les espaces de travail non protégés B (non classifiés) et protégés B?

- ESPACE DE TRAVAIL NON CLASSIFIÉ / NON PROTÉGÉ B
  - Cet espace de travail n'a AUCUN ACCÈS aux données statistiques confidentielles et classifiées.
  - Cet espace de travail a accès à l'internet.
- PROTÉGÉ B
  - Un espace de travail Protégé B n'a pas d'accès à l'internet.
  - La création d'un espace de travail Protégé B ne signifie pas que vous aurez automatiquement des droits d'accès aux données confidentielles Protégé B. Un utilisateur devra soumettre une demande par l'intermédiaire de notre unité "Customer Success" qui devra analyser les besoins, trouver un sponsor et obtenir l'approbation de l'OPMIC.

# CRÉER DES ESPACES DE TRAVAIL / CARNETS DE NOTES

## Quelles sont les différences entre les types de volumes?

- Les volumes d'espace de travail sont équivalents à votre répertoire personnel sur un système d'exploitation de type Unix tel que Linux. Sur l'EAA, c'est là que seront installés vos paquets Python et R. Vous pouvez stocker tout ce que vous voulez dans votre volume d'espace de travail, mais l'EAA offre des options de stockage supplémentaires pour les grands ensembles de données.
- Les volumes de données sont plus appropriés pour les ensembles de données et peuvent être montés à n'importe quel endroit de votre serveur. Un volume de données ne peut être attaché qu'à un seul serveur à la fois.
- MinIO est notre offre de stockage sur cloud. Vos sceaux MinIO peuvent stocker les données que vous souhaitez partager entre projets et serveurs.

## EAA offre-t-il une collaboration en temps réel avec les espaces de travail?

Les espaces de travail ne peuvent pas avoir plusieurs instances. Un espace de travail est constitué d'un seul locataire à la fois.

## Combien de temps faut-il pour créer un serveur d'ordinateurs portables?

Cela devrait prendre environ 2 à 10 minutes. Si cela prend plus de temps, veuillez vous adresser à notre canal Slack pour obtenir une assistance supplémentaire.

## Existe-t-il une limite supérieure au temps nécessaire pour créer un nouveau serveur d'ordinateurs portables?

Si nous atteignons nos limites en termes de nombre de nœuds de calcul, cela peut prendre plus de 10 minutes pour que le cluster s'adapte et fasse de la place pour des nœuds supplémentaires. En outre, il peut arriver qu'un nouveau nœud doive rejoindre le cluster, ce qui peut prendre de quelques minutes à une demi-heure en fonction du type de nœud et de l'état d'esprit d'Azure (notre plateforme de cloud computing sous-jacente) ce jour-là.

## Puis-je modifier la configuration de mon serveur après qu'il ait été créé?

Vous ne pouvez pas faire cela à partir de l'interface Kubeflow. Si vous souhaitez faire évoluer votre serveur vers le haut ou vers le bas, la manière la plus simple de le faire est de détruire votre serveur tout en conservant vos volumes de stockage. Vous pouvez ensuite créer un nouveau serveur et attacher les volumes existants. Vous pouvez également nous contacter sur Slack pour que nous puissions vous aider.

# ESPACES DE TRAVAIL / CARNETS (Travailler avec)

## Quels sont les différents formats de fichiers que je peux utiliser dans R ou Python?

R et Python peuvent ouvrir la plupart des formats de fichiers. En voici quelques-uns :

- CSV
- XLS, XLSX
- ZIP
- JSON
- XML
- SQLITE
- SAS7BDAT
- HDF
- DOC, DOCX
- Beaucoup d'autres...

## Puisque EEA ne propose pas PowerBI, quelles sont les alternatives?

EAA propose une version de R-shiny et de DASH. Vous pouvez toujours exporter des données PowerBI et les utiliser dans notre plateforme. Pour l'instant, non. Nous étudions actuellement des solutions pour le partage de données entre l'EAA et EAC (qui supporte Power BI).

## Où pouvons-nous accéder aux données publiques de StatCan?

Vous pouvez trouver des données de StatCan accessibles au public aux endroits suivants:

- [English StatCan Data](https://www150.statcan.gc.ca/n1/en/type/data?MM=1)
- [Données du StatCan](https://www150.statcan.gc.ca/n1/fr/type/donnees?MM=1)

## Comment puis-je avoir accès aux données protégées B de Statcan?

Un utilisateur devra demander l'accès par l'intermédiaire de l'unité de réussite des clients (CSU). Il devra également fournir un espace de noms, obtenir un sponsor et obtenir l'approbation de l'OPMIC. Une fois le processus approuvé, notre équipe de l'infrastructure des données équitables (FDI) créera alors un dossier sur Net A qui, à son tour, donnera accès à un ou plusieurs utilisateurs via le répertoire actif. Les données pourront alors être transférées de Net A vers EAA Cloud.

## Puis-je partager des données avec des utilisateurs internes et externes?

La réponse courte est oui, à condition qu'ils fassent partie du même espace de noms.

## Devons-nous fermer les serveurs des ordinateurs portables afin de faire des économies?

Il n'existe pas de lignes directrices sur la manière d'arrêter les espaces de travail en cours par mesure d'économie.

## Comment suspendre votre serveur (pour économiser des coûts)?

Présentement, vous devez détruire votre serveur. Assurez-vous de sauvegarder les volumes de données, ils peuvent être réutilisés avec un nouveau serveur. La version de KUBEFLOW dans la branche dev a une option pour suspendre la session. Une fois que cela aura été mis en production, les utilisateurs auront la possibilité de suspendre les espaces de travail pour économiser sur les coûts.

## Combien coûte l'EAA?

StatCan couvre actuellement le coût de l'utilisation de l'espace de travail pour tous les utilisateurs (internes et externes). Dans un avenir proche (année fiscale 2022-23), EAA commencera à recouvrer les coûts en facturant l'utilisation des utilisateurs externes. Pour vous donner une estimation approximative des coûts, veuillez consulter le tableau suivant.

#### Seulement CPU

| **Cas d'utilisation**               | **Ressources informatiques** |            |       | **Temps (Heures/Semaine)** | **Coût (CAD)** |           |            |
|----------------------------|-----------------------|------------|-------|-----------------------|----------|-----------|------------|
|                            | _CPU_                 | _RAM (GB)_ | _GPU_ |                       | _Weekly_ | _Monthly_ | _Annually_ |
| CPU: Occasional Use        | 2                     | 8.0        | 0     | 8                     | $1.14   | $4.89   | $59.11    |
| CPU: During Business Hours | 2                     | 8.0        | 0     | 40                    | $5.68   | $24.44  | $295.54    |
| CPU: 24/7                  | 2                     | 8.0        | 0     | 168                   | $23.87  | $102.64 | $1,241.28   |

#### Coût GPU

| **Cas d'utilisation**               | **Ressources informatiques** |            |       | **Temps (Heures/Semaine)** | **Coût (CAD)** |           |            |
|----------------------------|-----------------------|------------|-------|-----------------------|----------|-----------|------------|
|                            | _CPU_                 | _RAM (GB)_ | _GPU_ |                       | _Weekly_ | _Monthly_ | _Annually_ |
| GPU: Occasional Use        | 0                     | 0          | 1     | 8                     | $34.47   | $148.21  | $1,792.34   |
| GPU: During Business Hours | 0                     | 0          | 1     | 40                    | $172.34   | $741.06   | $8,961.68    |
| GPU: 24/7                  | 0                     | 0          | 1     | 168                   | $723.83  | $3,112.46 | $37,639.06  |

## Quels sont les paquets disponibles?

Nous offrons tous les paquets R et Python trouvés sur le Python Package Index (PyPI), Conda Forge et CRAN. Les paquets stockés dans ces dépôts officiels sont mis en miroir et analysés chez nous. Si vous voulez savoir ce qui est disponible, veuillez consulter les sources suivantes.

- Paquet Index Python
- Conda Forge (Python et R)
- Awesome Open Source (R, Python, et autres)
- CRAN (paquets R)

**Si vous trouvez quelque chose sur Awesome Open Source qui n'est pas disponible sur l'EAA, faites-le nous savoir!**

## Existe-t-il un moyen de voir la configuration du serveur de l'espace de travail?

La configuration définit la quantité de ressources de calcul dont dispose chaque serveur. Si vous souhaitez connaître la puissance de calcul de chaque serveur, consultez la liste des serveurs dans l'interface Kubeflow. Vous y trouverez la quantité de CPU et de mémoire ainsi que des informations sur les volumes attachés.

## Si vous avez de nombreux serveurs et que vous souhaitez obtenir une vue agrégée des informations ci-dessus, ouvrez le serveur de votre ordinateur portable, démarrez une session de terminal et entrez la commande suivante :

`kubectl describe quota -n your-name-space`

Cela vous donnera un aperçu de la puissance de calcul que vous consommez sur le cluster.

# Stockage, bases de données et MinIO

Comment puis-je accéder à MinIO ?

Vous pouvez accéder à votre compte MinIO à partir du portail MinIO. Vous aurez besoin de votre nom d'utilisateur et de votre mot de passe Windows de Statistique Canada.

- [MinIO Portal](https://minio.aaw.cloud.statcan.ca/)

## Quelles sont les étapes pour obtenir des données Protégé B dans MinIO?

Il faut consulter la FDI (F.A.I.R. Data Infrastructure) avant de pouvoir charger des données protégées B dans MinIO. L'équipe de FDI possède un pipeline Azure Data Factory pour déplacer des données, typiquement depuis le site, vers un compte de stockage Azure et MinIO est notre passerelle S3 vers ce compte de stockage.

## Comment puis-je accéder de manière programmatique à MinIO depuis JupyterLab?

Ce dépôt d’archive Github contient des exemples d'accès programmatique à MinIO. De plus, ce dépôt d’archive est cloné automatiquement dans les images JupyterLab et R Studio.

## Pourquoi mes fichiers vides n'apparaissent-ils pas dans mon seau MinIO?

Les fichiers texte vides sont filtrés hors du service de données Protégé B.

## Comment puis-je avoir accès aux données Statcan Protected B?

Un utilisateur devra demander l'accès par l'intermédiaire de l'unité de réussite des clients (CSU). Il devra également fournir un espace de noms, obtenir un sponsor et obtenir l'approbation de l'OPMIC. Une fois le processus approuvé, notre équipe de l'infrastructure des données équitables (FDI) créera alors un dossier sur Net A qui, à son tour, donnera accès à un ou plusieurs utilisateurs via le répertoire actif. Les données pourront alors être transférées de Net A vers le Cloud EEA.

## Puis-je héberger une base de données sur EAA?

Non. Mais vous pouvez utiliser SQLite, qui est une base de données dans un fichier. Vous pouvez également utiliser des fichiers Parquet qui offrent une alternative performante aux bases de données.

## Quelle est la bonne taille pour les différents volumes?

16 GB, c'est assez sûr. Ce sont surtout vos paquets Python/R qui seront stockés dans le volume de stockage principal.

## Existe-t-il des jeux de données préchargés dans EAA auxquels nous pouvons accéder et que nous pouvons utiliser pour les notebooks R et Python?

Nos images JupyterLab sont accompagnées de quelques exemples de notebooks et de données, ils se trouvent dans `/aaw-contrib-jupyter-notebooks/`. L'image R Studio contient également des exemples de notebooks et de données, ils se trouvent dans `/aaw-contrib-r-notebooks/`.

# SAS

[SAS Kernel for Jupyter](https://github.com/sassoftware/sas_kernel)

## Peut-on utiliser le SAS dans l'EAA?

Si vous êtes un employé de StatCan, la réponse est oui ! Vous pouvez utiliser Saspy (un paquetage Python pour exécuter du code SAS). SAS est également supporté par les [Cell Magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cell-magics) de JupyterLab! Vous pouvez utiliser SAS Studio à partir de JupyterLab. Vous pouvez importer des fichiers sas7bdat dans R et Python en utilisant des bibliothèques facilement disponibles.

## L'utilisation de SAS entraîne-t-elle des coûts différents des autres?

We are using the Statistics Canada SAS licenses so the cost has already been taken care of by Statistics Canada.

## Y a-t-il un nombre limité de licences ou d'instances qui peuvent être utilisées?

Le soutien de SAS est actuellement expérimental et utilisera les licences de logiciel SAS existantes de Statistique Canada.

## Where can I get more information about SAS on EAA?

L'internet regorge de documents sur la manière d'utiliser SAS avec Python. Voici quelques bons points de départ pour vos recherches.

- [An Introduction to SASPy and Jupyter Notebooks](https://www.sas.com/content/dam/SAS/support/en/sas-global-forum-proceedings/2018/2822-2018.pdf)
- [SASPy | SAS Support](https://support.sas.com/en/software/saspy.html)

# Avancé

## Puis-je créer mon propre service d'API Web optimisé par Kubernetes?

Vous pouvez créer une API à partir de votre espace de noms. Pour l'instant, cela se fait en créant des déploiements [Seldon](https://www.kubeflow.org/docs/external-add-ons/serving/seldon/) ou en créant des déploiements Kubernetes/StatefulSets.

Seldon est destiné au déploiement de modèles ML, nécessitant des artefacts de modèle. Ces artefacts pourraient en principe être du code python arbitraire dans une certaine mesure. Les serveurs web de l'API sont configurés via python gunicorn. Si vous avez un cas d'utilisation particulier en tête, nous pouvons en discuter.

# Ressources supplémentaires

Consultez le lien suivant pour obtenir des ressources supplémentaires qui vous aideront à tirer le meilleur parti de l'Espace d’analyse avancée!

- [Kubeflow Pipelines](https://statcan.github.io/daaas/en/3-Pipelines/Kubeflow-Pipelines/)
- [Slack](http://statcan-aaw.slack.com/)
- [YouTube](https://www.youtube.com/playlist?list=PL1zlA2D7AHugkDdiyeUHWOKGKUd3MB_nD)

# Contribuez!

Si vous trouvez l'EAA utile et que vous souhaitez contribuer à son succès, consultez nos dépôts Github, examinez le code et soumettez une demande de modification !

[https://github.com/StatCan/daaas](https://github.com/StatCan/daaas)
