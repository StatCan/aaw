# Données B protégées par Statcan

<!-- prettier-ignore -->
!!! info "Protégé B"
     L'ETAA est certifié pour l'hébergement de données protégé B !

Afin de télécharger des données protégées B sur l'ETAA, les utilisateurs devront demander l'accès via l'Unité de Succès à la Clientèle (USC). Les utilisateurs d'ETAA devront également fournir un espace de noms, obtenir un sponsor et obtenir l'approbation d'OPMIC. Une fois le processus approuvé, notre équipe infrastructure de données F.A.I.R créera alors un dossier sur Net A qui à son tour donnera accès aux utilisateurs via le répertoire actif. Les données pourront alors être transférées de Net A vers le cloud ETAA.

Le stockage des modèles d'apprentissage automatique dans un environnement de stockage cloud protégé est essentiel pour garantir la sécurité et la confidentialité des données sensibles. L'espace de travail d'analyse avancée (ETAA) fournit un environnement de stockage cloud sécuritaire et robuste qui peut être utilisé pour stocker des modèles d'apprentissage automatique et d'autres actifs de données.

La plate-forme ETAA fournit un environnement de stockage cloud protégé conçu pour répondre aux exigences les plus strictes en matière de sécurité et de confidentialité des données. L'environnement de stockage est protégé par un cryptage et des contrôles d'accès conformes aux normes de l'industrie, ce qui garantit que seul le personnel autorisé peut accéder aux données sensibles. Cela protège contre les accès non autorisés, les violations de données et autres menaces de sécurité.

En plus de ses fonctions de sécurité robustes, l'environnement de stockage en cloud ETAA est également hautement évolutif et flexible. Cela signifie que les data scientists et les ingénieurs en apprentissage automatique peuvent facilement faire évoluer leurs besoins de stockage à mesure que leurs ensembles de données et la taille de leurs modèles augmentent. Cela leur permet de stocker et de gérer de gros volumes de données et de modèles sans avoir à se soucier des limitations de stockage ou des goulots d'étranglement des performances.

Le stockage des modèles d'apprentissage automatique dans un environnement de stockage cloud protégé sur l'espace de travail d'analyse avancée fournit une solution sécurisée, évolutive et flexible pour la gestion et la protection des données sensibles. En tirant parti des capacités de stockage dans le cloud fournies par la plate-forme ETAA, les data scientists et les ingénieurs en apprentissage automatique peuvent se concentrer sur la création et le déploiement de leurs modèles en toute confiance, sachant que leurs données sont protégées et sécurisées.

## Stockage en ligne

<!-- prettier-ignore -->
!!! info "Avantages du stockage en cloud"
     Le stockage en cloud offre plusieurs avantages pour la science des données et l'apprentissage automatique, notamment en termes d'évolutivité, d'accessibilité et de rentabilité.

Premièrement, le stockage dans le cloud permet aux data scientists de stocker et de traiter de grandes quantités de données sans avoir à se soucier des limites du stockage local. Ceci est particulièrement important dans le contexte de l'apprentissage automatique, où de grands ensembles de données sont nécessaires pour la formation et le test des modèles. Le stockage dans le cloud permet aux data scientists d'augmenter leur capacité de stockage selon les besoins, sans avoir à investir dans du matériel coûteux.

Deuxièmement, le stockage en cloud permet aux data scientists d'accéder aux données de n'importe où, en utilisant n'importe quel appareil doté d'une connexion Internet. Cela permet la collaboration entre des équipes géographiquement dispersées et permet aux data scientists de travailler à distance. De plus, le stockage dans le cloud facilite le partage de données avec d'autres parties prenantes, telles que des partenaires commerciaux ou des clients. Enfin, le stockage dans le cloud est généralement plus rentable que le stockage sur site, en particulier pour les petites entreprises ou celles dont les ressources informatiques sont limitées.

Dans l'ensemble, le stockage en cloud est une solution fiable et pratique pour stocker et gérer vos données. Que vous ayez besoin de stocker de grandes quantités de données ou seulement quelques fichiers, le stockage en cloud facilite la gestion de vos besoins de stockage sans les tracas des solutions de stockage traditionnelles.

La plateforme ETAA propose plusieurs types de stockage :

- Disques (également appelés Volumes sur l'écran de création de Kubeflow Notebook Server)
- Buckets ("Blob" ou stockage S3, fournis via MinIO)
- Lacs de données (à venir)

Selon votre cas d'utilisation, le disque ou le bucket peut être le plus approprié. Notre [aperçu du stockage](../5-Storage/Overview.md) vous aidera à les comparer.

### Disques

[![Disques](../images/Disks.PNG)](Storage.md/)

**[Disks](../5-Storage/Disks.md)** sont ajoutés à votre serveur notebook en ajoutant des volumes de données.

### Seaux

MinIO est un système de stockage d'objets compatible S3-API qui fournit une alternative open source aux services de stockage cloud propriétaires. Bien que nous utilisions actuellement MinIO comme solution de stockage dans le cloud, nous prévoyons de le remplacer par s3-proxy dans un proche avenir. S3-proxy est un serveur proxy inverse léger et open source qui vous permet d'accéder à des services de stockage compatibles avec Amazon S3 avec vos applications existantes. En passant à s3-proxy, nous pourrons améliorer les performances, la sécurité et l'évolutivité de notre stockage dans le cloud, tout en maintenant la compatibilité avec l'API S3.

[![MinIO](../images/Buckets.PNG)](AzureBlobStorage.md/)

**[MinIO](../5-Storage/AzureBlobStorage.md)** est un magasin d'objets évolutif cloud natif. Nous l'utilisons pour les buckets (stockage blob ou S3).

### Lacs de données (à venir)

Un lac de données est un référentiel central qui vous permet de stocker toutes vos données structurées et non structurées à n'importe quelle échelle. C'est un moyen rentable de stocker et de gérer tous les types de données, des données brutes aux données traitées, et c'est un outil essentiel pour les data scientists.

L'un des principaux avantages d'un lac de données est sa flexibilité. Il permet de stocker tous types de données sans avoir besoin de définir un schéma au préalable, ce qui est particulièrement utile lorsqu'il s'agit de données non structurées. Cette flexibilité permet aux data scientists d'explorer, d'expérimenter et d'extraire facilement des informations à partir de leurs données sans être contraints par les limites d'une base de données relationnelle traditionnelle.

Les lacs de données permettent également aux data scientists de centraliser leurs données, ce qui facilite la gestion et l'analyse de gros volumes de données provenant de diverses sources. Avec un lac de données, les data scientists peuvent facilement ingérer et stocker des données provenant de diverses sources, telles que des bases de données, le stockage dans le cloud et des API tierces. De plus, les lacs de données fournissent souvent des fonctionnalités pour la gouvernance des données, la gestion des métadonnées et le contrôle d'accès, ce qui permet de garantir que les données sont de haute qualité et conformes aux réglementations en vigueur.

De plus, les lacs de données basés sur le cloud offrent des solutions de stockage évolutives et économiques qui peuvent être facilement étendues en un clic. À mesure que les besoins de stockage de données d'un scientifique des données augmentent, il peut ajouter une capacité de stockage supplémentaire à son lac de données avec un minimum d'effort, sans se soucier de l'infrastructure sous-jacente ou de la maintenance.

Dans l'ensemble, les lacs de données sont un outil essentiel pour les data scientists, car ils offrent la flexibilité, l'évolutivité et la facilité d'utilisation nécessaires pour stocker et gérer de gros volumes de données, permettant aux data scientists de se concentrer sur l'extraction d'informations et de valeur à partir des données.
