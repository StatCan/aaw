# Introduction au modèle de service

Dans le contexte des gouvernements, servir des modèles d'apprentissage automatique signifie rendre les modèles formés disponibles pour être utilisés par d'autres applications et systèmes. Cela peut inclure la réalisation de prédictions ou de classifications basées sur les données d'entrée, ou la fourniture d'informations et de recommandations basées sur les résultats de l'analyse des données.

Servir des modèles d'apprentissage automatique dans un contexte gouvernemental soulève des questions importantes liées à la confidentialité des données. Les agences gouvernementales sont souvent responsables de la collecte et de la gestion des données personnelles sensibles, telles que les dossiers médicaux, les données financières et les casiers judiciaires. Lors de la diffusion de modèles d'apprentissage automatique, il est essentiel de s'assurer que ces données sont protégées et que leur accès est strictement contrôlé.

Pour répondre à ces préoccupations, les agences gouvernementales doivent mettre en œuvre des mesures solides de confidentialité et de sécurité des données lorsqu'elles servent des modèles d'apprentissage automatique. Cela pourrait inclure le chiffrement des données au repos et en transit, la mise en œuvre de contrôles d'accès et d'authentification des utilisateurs, et la surveillance régulière des violations de données et des vulnérabilités.

En plus de la confidentialité et de la sécurité des données, il est également important de prendre en compte les implications éthiques de servir des modèles d'apprentissage automatique dans un contexte gouvernemental. Les modèles d'apprentissage automatique peuvent être biaisés ou discriminatoires, entraînant un traitement injuste de certains groupes de personnes. Pour atténuer ces risques, les agences gouvernementales doivent soigneusement évaluer et surveiller leurs modèles d'apprentissage automatique, et prendre des mesures pour lutter contre les préjugés ou la discrimination qui pourraient survenir.

Dans l'ensemble, servir des modèles d'apprentissage automatique dans un contexte gouvernemental nécessite un examen attentif de la confidentialité des données, de la sécurité et des préoccupations éthiques. En mettant en œuvre des mesures solides pour protéger les données personnelles et prévenir les préjugés, les agences gouvernementales peuvent tirer parti de la puissance de l'apprentissage automatique pour prendre de meilleures décisions et améliorer les résultats pour les citoyens tout en maintenant la confiance et la transparence.

## Pourquoi servir avec nous ?

Servir des modèles d'apprentissage automatique avec Advanced Analytics Workspace (AAW) présente plusieurs avantages. Premièrement, l'AAW est une plate-forme d'analyse de données open source qui donne accès à une variété d'outils d'analyse avancés, notamment Python, R et SAS. Cela facilite le déploiement de modèles d'apprentissage automatique et leur intégration dans les flux de travail existants.

Deuxièmement, l'AAW prend en charge plusieurs frameworks MLOps, notamment Couler, Seldon et Argo Workflows. Ces frameworks fournissent une gamme de fonctionnalités, notamment la gestion des versions de modèle, le service de modèle et la surveillance de modèle, qui simplifient le processus de déploiement et de gestion des modèles d'apprentissage automatique en production.

Troisièmement, l'AAW fournit une plate-forme sécurisée et évolutive pour servir les modèles d'apprentissage automatique avec le statut Protégé B. Les modèles peuvent être servis à l'aide d'environnements conteneurisés, tels que Docker, qui offrent un niveau élevé d'isolement et de sécurité. L'AAW fournit également un accès aux ressources de cloud computing, permettant aux utilisateurs d'augmenter leur puissance de calcul selon les besoins pour gérer des volumes élevés de demandes.

Enfin, l'AAW est une plateforme collaborative qui permet aux utilisateurs de partager du code et des données avec d'autres chercheurs et analystes. Cela favorise une communauté d'utilisateurs qui peuvent apprendre du travail des autres et collaborer sur des projets qui nécessitent des capacités d'analyse avancées.

En résumé, servir des modèles d'apprentissage automatique avec l'espace de travail d'analyse avancée donne accès à des outils d'analyse avancés, à plusieurs cadres MLOps, à une plate-forme Proteced B sécurisée et évolutive et à une communauté collaborative d'utilisateurs, ce qui en fait une plate-forme idéale pour les scientifiques et les analystes de données qui veulent pour déployer et gérer des modèles d'apprentissage automatique en production.

## Noyau de Seldon

Seldon Core est une plate-forme open source pour le déploiement, la mise à l'échelle et la surveillance des modèles d'apprentissage automatique sur Kubernetes. Il fournit un moyen simple et efficace de déployer des modèles d'apprentissage automatique en tant que microservices dans un environnement de production.

Servir des modèles d'apprentissage automatique à l'aide de Seldon Core implique les étapes suivantes :

1. Conditionnement du modèle : la première étape consiste à conditionner le modèle d'apprentissage automatique formé dans une image de conteneur avec toutes les dépendances requises. Seldon Core prend en charge divers frameworks d'apprentissage automatique, notamment TensorFlow, PyTorch et Scikit-learn.

2. Déploiement du modèle : une fois l'image du conteneur créée, l'étape suivante consiste à déployer le modèle sur Kubernetes à l'aide de Seldon Core. Cela implique de définir le fichier de configuration de déploiement, qui spécifie les ressources requises pour le déploiement, telles que le nombre de répliques et les ressources de calcul.

3. Service de modèle : une fois le modèle déployé, Seldon Core expose un point de terminaison d'API REST qui peut être utilisé pour effectuer des prédictions. Les clients peuvent envoyer des requêtes au point de terminaison avec des données d'entrée, et le modèle renverra la sortie correspondante. Seldon Core prend également en charge divers modèles de déploiement, tels que le déploiement Canary et les tests A/B, pour permettre une expérimentation et des tests faciles de différents modèles.

4. Surveillance des modèles : Seldon Core fournit diverses fonctionnalités de surveillance pour suivre les performances des modèles déployés. Cela inclut la surveillance en temps réel des métriques du modèle, telles que la latence et le débit, ainsi que la journalisation des données de demande et de réponse à des fins de débogage.

Seldon Core facilite la mise à disposition de modèles d'apprentissage automatique à grande échelle, avec une prise en charge de la haute disponibilité, de l'évolutivité et de la tolérance aux pannes. Il fournit également une intégration avec divers outils natifs de Kubernetes, tels qu'Istio et Prometheus, pour permettre une surveillance et une observabilité avancées.
