# Aperçu du stockage

Plusieurs options de stockage sont disponibles pour les utilisateurs d'AAW pour accéder et importer leurs données. Vous trouverez ci-dessous une description de chaque type. Il existe des pages de documentation distinctes pour la connexion à chaque type de stockage.

## Volumes Kubeflow (Disques)

Kubeflow utilise des disques virtuels appelés Volumes. Vous les rencontrerez sur l’écran de création de bloc-note server. Ces disques sont disponibles en deux variétés, appelées Workspace Volumes et Data Volumes. Les volumes de données et d'espace de travail peuvent être réutilisés et montés sur différents serveurs de bloc-note, mais pas en même temps.

### Volumes de l'espace de travail

Les volumes d'espace de travail sont similaires dans leur concept et leur fonction au disque dur de votre ordinateur portable, c'est là que tous les logiciels sont stockés et c'est le périphérique de stockage par défaut pour toutes vos affaires.

###Volumes de données

Si vous avez besoin de plus de stockage, un volume de données peut être nécessaire. Ceci est conceptuellement similaire à la connexion d'un disque dur USB haute capacité à votre PC.

## Stockage Blob Azure (Conteneurs)

Si vous avez besoin de collaborer avec d’autres, Azure Blob Storage (tel que fourni par FDI) peut être la meilleure option pour vous et vos données. Voir [Choisir votre stockage](#choosing-your-storage) pour plus d'informations.

## Choisir votre stockage

En fonction de vos besoins et exigences uniques et de ceux de votre projet, Kubeflow Volumes ou Azure Blob Storage (ou les deux) peuvent être les plus adaptés :

| Tapez | Simultanéité | Vitesse | Capacité | Partageabilité |
| :------------------------------------------------- -------- | :------------------------------------------------- ------------- | :------------------------------------------------- ----- | -------------------- | ------------- |
| **[Stockage Blob Azure (Conteneurs)](AzureBlobStorage.md)** | Accès simultané depuis plusieurs serveurs d'ordinateurs portables en même temps | Fast-ish (téléchargement rapide, téléchargement modeste, latence modeste) | Infini (dans la limite du raisonnable) | Partageable |
| **[Volumes Kubeflow (Disques)](KubeflowVolumes.md)** | Un serveur de bloc-note à la fois | Le plus rapide (débit et latence) | <=512 Go au total par disque | Non partageable |

<!-- plus joli-ignorer -->
!!! Info "Si vous ne savez pas lequel choisir, ne vous inquiétez pas !"
     Ce sont des lignes directrices, pas une science exacte : choisissez ce qui sonne le mieux maintenant et appliquez-le. Le meilleur choix pour une utilisation compliquée n’est pas évident et nécessite souvent une expérience pratique, il suffit donc d’essayer quelque chose. Dans la plupart des situations, les deux options fonctionnent bien même si elles ne sont pas parfaites, et rappelez-vous que les données peuvent toujours être copiées plus tard si vous changez d'avis.
