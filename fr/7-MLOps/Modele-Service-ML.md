# Introduction à la diffusion de modèles

Dans le contexte des gouvernements, servir des modèles d’apprentissage automatique signifie rendre les modèles formés disponibles pour être utilisés par d’autres applications et systèmes. Cela pourrait inclure la réalisation de prédictions ou de classifications basées sur les données d'entrée, ou la fourniture d'informations et de recommandations basées sur les résultats de l'analyse des données.

La mise en œuvre de modèles d'apprentissage automatique dans un contexte gouvernemental soulève des problèmes importants liés à la confidentialité des données. Les agences gouvernementales sont souvent chargées de collecter et de gérer des données personnelles sensibles, telles que les dossiers médicaux, les données financières et les casiers judiciaires. Lorsque vous servez des modèles d'apprentissage automatique, il est essentiel de garantir que ces données sont protégées et que leur accès est strictement contrôlé.

Pour répondre à ces préoccupations, les agences gouvernementales doivent mettre en œuvre des mesures robustes de confidentialité et de sécurité des données lorsqu'elles servent des modèles d'apprentissage automatique. Cela pourrait inclure le chiffrement des données au repos et en transit, la mise en œuvre de contrôles d'accès et d'authentification des utilisateurs, ainsi qu'une surveillance régulière des violations de données et des vulnérabilités.

Outre la confidentialité et la sécurité des données, il est également important de prendre en compte les implications éthiques de la mise en œuvre de modèles d'apprentissage automatique dans un contexte gouvernemental. Les modèles d’apprentissage automatique peuvent être biaisés ou discriminatoires, conduisant à un traitement injuste de certains groupes de personnes. Pour atténuer ces risques, les agences gouvernementales doivent évaluer et surveiller soigneusement leurs modèles d'apprentissage automatique et prendre des mesures pour remédier à tout préjugé ou discrimination qui pourrait survenir.

Dans l’ensemble, la mise en œuvre de modèles d’apprentissage automatique dans un contexte gouvernemental nécessite un examen attentif de la confidentialité des données, de la sécurité et des préoccupations éthiques. En mettant en œuvre des mesures robustes pour protéger les données personnelles et prévenir les préjugés, les agences gouvernementales peuvent tirer parti de la puissance de l'apprentissage automatique pour prendre de meilleures décisions et améliorer les résultats pour les citoyens tout en préservant la confiance et la transparence.

## Pourquoi servir avec nous ?

Servir des modèles d'apprentissage automatique avec l'Espace de travail d'analyse avancée (ETAA) présente plusieurs avantages. Premièrement, ETAA est une plate-forme d'analyse de données open source qui donne accès à une variété d'outils d'analyse avancés, notamment Python, R et SAS. Cela facilite le déploiement de modèles d'apprentissage automatique et leur intégration dans les flux de travail existants.

Deuxièmement, l'ETAA prend en charge plusieurs frameworks MLOps, notamment les workflows Couler, Seldon et Argo. Ces frameworks fournissent une gamme de fonctionnalités, notamment la gestion des versions de modèles, la diffusion de modèles et la surveillance de modèles, qui simplifient le processus de déploiement et de gestion des modèles d'apprentissage automatique en production.

Troisièmement, l'ETAA fournit une plate-forme sécurisée et évolutive pour servir des modèles d'apprentissage automatique avec le statut Protégé B. Les modèles peuvent être servis à l'aide d'environnements conteneurisés, tels que Docker, qui offrent un haut niveau d'isolation et de sécurité. L'ETAA donne également accès aux ressources de cloud computing, permettant aux utilisateurs d'augmenter leur puissance de calcul selon leurs besoins pour gérer des volumes élevés de requêtes.

Enfin, l'ETAA est une plateforme collaborative qui permet aux utilisateurs de partager du code et des données avec d'autres chercheurs et analystes. Cela favorise une communauté d'utilisateurs qui peuvent apprendre du travail de chacun et collaborer sur des projets nécessitant des capacités d'analyse avancées.

En résumé, servir des modèles d'apprentissage automatique avec Advanced Analytics Workspace donne accès à des outils d'analyse avancés, à plusieurs frameworks MLOps, à une plate-forme Proteced B sécurisée et évolutive et à une communauté collaborative d'utilisateurs, ce qui en fait une plate-forme idéale pour les scientifiques et les analystes de données qui souhaitent pour déployer et gérer des modèles d’apprentissage automatique en production.

## Noyau Seldon

Seldon Core est une plate-forme open source permettant de déployer, de mettre à l'échelle et de surveiller des modèles d'apprentissage automatique sur Kubernetes. Il fournit un moyen simple et efficace de déployer des modèles d'apprentissage automatique sous forme de microservices dans un environnement de production.

La diffusion de modèles d'apprentissage automatique à l'aide de Seldon Core implique les étapes suivantes :

1. Conditionnement du modèle : la première étape consiste à empaqueter le modèle d'apprentissage automatique formé dans une image de conteneur avec toutes les dépendances requises. Seldon Core prend en charge divers frameworks d'apprentissage automatique, notamment TensorFlow, PyTorch et Scikit-learn.

2. Déploiement du modèle : une fois l'image du conteneur créée, l'étape suivante consiste à déployer le modèle sur Kubernetes à l'aide de Seldon Core. Cela implique de définir le fichier de configuration de déploiement, qui spécifie les ressources requises pour le déploiement, telles que le nombre de réplicas et les ressources de calcul.

3. Service de modèle : une fois le modèle déployé, Seldon Core expose un point de terminaison d'API REST qui peut être utilisé pour effectuer des prédictions. Les clients peuvent envoyer des requêtes au point de terminaison avec des données d'entrée, et le modèle renverra la sortie correspondante. Seldon Core prend également en charge divers modèles de déploiement, tels que le déploiement Canary et les tests A/B, pour permettre une expérimentation et un test faciles de différents modèles.

4. Surveillance des modèles : Seldon Core fournit diverses capacités de surveillance pour suivre les performances des modèles déployés. Cela inclut la surveillance en temps réel des métriques du modèle, telles que la latence et le débit, ainsi que la journalisation des données de requête et de réponse à des fins de débogage.

Seldon Core facilite la mise en œuvre de modèles d'apprentissage automatique à grande échelle, avec la prise en charge de la haute disponibilité, de l'évolutivité et de la tolérance aux pannes. Il fournit également une intégration avec divers outils natifs de Kubernetes, tels que Istio et Prometheus, pour permettre une surveillance et une observabilité avancées.