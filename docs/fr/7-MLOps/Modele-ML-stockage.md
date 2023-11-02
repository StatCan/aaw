# Données B protégées par Statcan

<!-- plus joli-ignorer -->
!!! info "Protégé B"
     L'ETAA est certifié pour l'hébergement de données Protégé B !

Afin de télécharger des données Protégé B vers l'ETAA, les utilisateurs devront demander l'accès via la Customer Success Unit (CSU). Les utilisateurs d'ETAA devront également fournir un espace de noms, trouver un sponsor et obtenir l'approbation d'OPMIC. Une fois le processus approuvé, notre équipe Fair Data Infrastructure (FDI) créera ensuite un dossier sur Net A qui à son tour donnera accès aux utilisateurs via l'annuaire actif. Les données pourront ensuite être transférées de Net A vers le nuage ETAA

Le stockage des modèles d'apprentissage automatique dans un environnement de stockage cloud protégé est essentiel pour garantir la sécurité et la confidentialité des données sensibles. L'espace de travail d'analyse avancée (ETAA) fournit un environnement de nuage stockage sécurisé et robuste qui peut être utilisé pour stocker des modèles d'apprentissage automatique et d'autres actifs de données.

La plate-forme ETAA fournit un environnement de nuage stockage protégé conçu pour répondre aux exigences les plus strictes en matière de sécurité et de confidentialité des données. L'environnement de stockage est protégé par un cryptage et des contrôles d'accès conformes aux normes de l'industrie, ce qui garantit que seul le personnel autorisé peut accéder aux données sensibles. Cela protège contre les accès non autorisés, les violations de données et autres menaces de sécurité.

En plus de ses fonctionnalités de sécurité robustes, l'environnement de nuage stockage ETAA est également hautement évolutif et flexible. Cela signifie que les scientifiques des données et les ingénieurs en apprentissage automatique peuvent facilement faire évoluer leurs besoins de stockage à mesure que leurs ensembles de données et la taille de leurs modèles augmentent. Cela leur permet de stocker et de gérer de gros volumes de données et de modèles sans avoir à se soucier des limitations de stockage ou des goulots d'étranglement des performances.

Le stockage des modèles d'apprentissage automatique dans un environnement de stockage en nuage protégé sur l'espace de travail d'analyse avancée fournit une solution sécurisée, évolutive et flexible pour gérer et protéger les données sensibles. En tirant parti des capacités de nuage stockage fournies par la plateforme ETAA, les scientifiques des données et les ingénieurs en apprentissage automatique peuvent se concentrer sur la création et le déploiement de leurs modèles en toute confiance, sachant que leurs données sont protégées et sécurisées.

## Stockage en ligne

<!-- plus joli-ignorer -->
!!! info "Avantages du nuage de stockage"
     Le stockage en nuage offre plusieurs avantages pour la science des données et l'apprentissage automatique, notamment en termes d'évolutivité, d'accessibilité et de rentabilité.

Premièrement, le stockage dans le nuage permet aux scientifiques des données de stocker et de traiter de grandes quantités de données sans avoir à se soucier des limites du stockage local. Ceci est particulièrement important dans le contexte de l’apprentissage automatique, où de grands ensembles de données sont nécessaires pour la formation et le test des modèles. Le stockage dans le nuage permet aux scientifiques des données d'augmenter leur capacité de stockage selon leurs besoins, sans avoir à investir dans du matériel coûteux.

Deuxièmement, le stockage dans le nuage permet aux scientifiques des données d'accéder aux données de n'importe où, en utilisant n'importe quel appareil doté d'une connexion Internet. Cela permet la collaboration entre des équipes géographiquement réparties et permet aux scientifiques des données de travailler à distance. De plus, le stockage dans le nuage facilite le partage de données avec d'autres parties prenantes, telles que des partenaires commerciaux ou des clients. Enfin, le stockage dans le nuage est généralement plus rentable que le stockage sur site, en particulier pour les petites organisations ou celles disposant de ressources informatiques limitées.

Dans l’ensemble, le stockage dans le nuage est une solution fiable et pratique pour stocker et gérer vos données. Que vous ayez besoin de stocker de grandes quantités de données ou seulement quelques fichiers, le stockage dans le cloud facilite la gestion de vos besoins de stockage sans les tracas des solutions de stockage traditionnelles.

La plateforme ETAA propose plusieurs types de stockage :

- Disques (également appelés Volumes sur l'écran de création de Kubeflow Serveur Bloc-notes)
- Lacs de donnees (à venir)

Selon votre cas d'utilisation, le disque ou le compartiment peuvent être les plus adaptés. Notre [aperçu du stockage](../5-Stockage/Aperçu.md) vous aidera à les comparer.

### Disques
<center>
      [![Disques](../images/Disque.PNG)](../5-Stockage/Disque.md)
</center>
**[Disques](../5-Stockage/Disque.md)** sont ajoutés à votre serveur bloc-notes en augmentant les volumes de données.

### Lacs de données (à venir)

Un lac de données est un référentiel central qui vous permet de stocker toutes vos données structurées et non structurées à n'importe quelle échelle. C'est un moyen rentable de stocker et de gérer tous les types de données, des données brutes aux données traitées, et c'est un outil essentiel pour les scientifiques des données.

L’un des principaux avantages d’un lac de données est sa flexibilité. Il permet de stocker tous types de données sans avoir besoin de définir un schéma au préalable, ce qui est particulièrement utile lorsqu'il s'agit de données non structurées. Cette flexibilité permet aux scientifiques des données d'explorer, d'expérimenter et d'extraire facilement des informations à partir de leurs données sans être contraints par les limites d'une base de données relationnelle traditionnelle.

Les lacs de données permettent également aux scientifiques des données de centraliser leurs données, facilitant ainsi la gestion et l'analyse de gros volumes de données provenant de diverses sources. Avec un lac de données, les scientifiques des données peuvent facilement ingérer et stocker des données provenant de diverses sources, telles que des bases de données, le stockage cloud et des API tierces. De plus, les lacs de données fournissent souvent des fonctionnalités de gouvernance des données, de gestion des métadonnées et de contrôle d'accès, ce qui permet de garantir que les données sont de haute qualité et conformes aux réglementations en vigueur.

De plus, les lacs de données basés sur le cloud offrent des solutions de stockage évolutives et rentables qui peuvent être facilement étendues d'un simple clic. À mesure que les besoins de stockage des données des scientifiques des données augmentent, ils peuvent ajouter une capacité de stockage supplémentaire à leur lac de données avec un minimum d'effort, sans se soucier de l'infrastructure ou de la maintenance sous-jacente.

Dans l'ensemble, les lacs de données sont un outil essentiel pour les scientifiques des données, car ils offrent la flexibilité, l'évolutivité et la facilité d'utilisation nécessaires pour stocker et gérer de grands volumes de données, permettant aux data scientists de se concentrer sur l'extraction d'informations et de valeur à partir des données.