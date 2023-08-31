# Aperçu

[Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) est la solution de stockage d'objets de Microsoft pour le cloud. Blob Storage est optimisé pour stocker des quantités massives de données non structurées. Les données non structurées sont des données qui n'adhèrent pas à un modèle de données ou à une définition particulière, comme du texte ou des données binaires.

Les conteneurs de stockage Azure Blob sont efficaces dans trois domaines :

- De grandes quantités de données - Les conteneurs peuvent être énormes : bien plus gros que les disques durs. Et ils sont toujours rapides.
- Accessible par plusieurs consommateurs à la fois - Vous pouvez accéder à la même source de données à partir de plusieurs serveurs Notebook et pipelines en même temps sans avoir besoin de dupliquer les données.
- Partage - Les espaces de noms de projet peuvent partager un conteneur. C'est idéal pour partager des données avec des personnes extérieures à votre espace de travail.

# Installation

<!-- prettier-ignore -->
!!! avertissement "Les conteneurs de stockage Azure Blob et le support de buckets remplaceront les supports de stockage Minio Buckets et Minio"
     Les utilisateurs seront responsables de la migration des données des Minio Buckets vers les dossiers Azure Storage. Pour les fichiers plus volumineux, les utilisateurs peuvent contacter AAW pour obtenir de l'aide.

## Conteneur Blob monté sur un serveur de notebook

<!-- prettier-ignore -->

Les volumes Blob CSI sont conservés sous « /home/jovyan/buckets » lors de la création d'un serveur Notebook. Les fichiers sous « /buckets » sont sauvegardés par le stockage Blob. Tous les ordinateurs portables AAW auront le « /buckets » monté sur le système de fichiers, rendant les données accessibles de partout.

![Dossiers Blob montés en tant que répertoires Jupyter Notebook](../images/container-mount.png)

# Support de dossier AAW pour ordinateur portable non classé
![Dossiers de notebook non classifiés montés dans les répertoires Jupyter Notebook](../images/unclassified-mount.png)

# Support de dossier AAW pour ordinateur portable protégé-b
![Carnets protégés-b montés en tant que répertoires Jupyter Notebook](../images/protectedb-mount.png)

Ces dossiers peuvent être utilisés comme n'importe quel autre : vous pouvez copier des fichiers vers/depuis l'explorateur de fichiers, écrire à partir de Python/R, etc. La seule différence est que les données sont stockées dans le conteneur de stockage Blob plutôt que sur un disque local. (et est donc accessible partout où vous pouvez accéder à votre notebook Kubeflow).

## Comment migrer de MinIO vers Azure Blob Storage

Tout d’abord, importez les variables d’environnement stockées dans votre coffre-fort de secrets. Vous importerez soit depuis « minio-gateway » soit depuis « fdi-gateway » selon l'endroit où vos données ont été ingérées.

```
jovyan@rstudio-0 :~$ source /vault/secrets/fdi-gateway-protected-b
```

Ensuite, vous créez un alias pour accéder à vos données.

```
jovyan@rstudio-0 : ~$ mc alias défini minio $MINIO_URL $MINIO_ACCESS_KEY $MINIO_SECRET_KEY
```

Répertoriez le contenu de votre dossier de données avec `mc ls`.

```
jovyan@rstudio-0:~$ mc ls minio
```

Enfin, copiez vos données MinIO dans votre répertoire Azure Blob Storage avec `mc cp --recursive`.

```
jovyan@rstudio-0:~$ mc cp --recursive minio ~/buckets
```

<!-- prettier-ignore -->

## Types de conteneurs

Les conteneurs Blob suivants sont disponibles :

L’accès à tous les conteneurs Blob est le même. La différence entre les conteneurs réside dans le type de stockage qui les sous-tend :

- **aaw-unclassified :** Par défaut, utilisez celui-ci. Stocke les données non classifiées.

- **aaw-protected-b :** Stocke les données sensibles protégées-b.

- **aaw-unclassified-ro :** Cette classification est protégée-b mais en accès en lecture seule. Cela permet aux utilisateurs de visualiser les données non classifiées dans un bloc-notes protégé-b.

<!-- prettier-ignore -->

## Accès aux données internes

<!-- prettier-ignore -->
L'accès aux données internes utilise la connexion de stockage commune DAS qui est utilisée par les utilisateurs internes et externes qui ont besoin d'accéder à des données non classifiées ou protégées-b. Les conteneurs suivants peuvent être mis à disposition :

- **externe-non classé**
- **externe-protégé-b**
- **interne-non classé**
- **interne-protégé-b**

Ils suivent la même convention que les conteneurs AAW ci-dessus en termes de données, mais il existe une couche d'isolement entre les employés de StatCan et les non-employés de StatCan. Les employés non-Statcan ne sont autorisés que dans les conteneurs **externes**, tandis que les employés de StatCan peuvent avoir accès à n'importe quel conteneur.

AAW dispose d'une intégration avec l'équipe FAIR Data Infrastructure qui permet aux utilisateurs de transférer des données non classifiées et protégées vers des comptes de stockage Azure, permettant ainsi aux utilisateurs d'accéder à ces données à partir de serveurs Notebook.

Veuillez contacter l'équipe FAIR Data Infrastructure si vous avez un cas d'utilisation de ces données.

## Tarifs

<!-- prettier-ignore -->
!!! info "Les modèles de tarification sont basés sur l'utilisation du processeur et de la mémoire"
     Le prix est couvert par KubeCost pour les espaces de noms utilisateur (dans Kubeflow en bas de l'onglet Notebooks).

En général, le stockage Blob est beaucoup moins cher que [Azure Manage Disks](https://azure.microsoft.com/en-us/pricing/details/managed-disks/) et offre de meilleures E/S que les SSD gérés.
