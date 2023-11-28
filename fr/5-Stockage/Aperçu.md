# Stockage

La plateforme propose plusieurs types de stockage :

- Disque (également appelé Volumes sur l'écran de création de serveur de   blocs-note)
- Compartiment (Stockage Azure Blob)
- Data Lakes (à venir)

Selon votre cas d'utilisation, le disque ou le compartiment peut être le plus approprié :

|                                     Type |                                                                  Utilisateurs simultanés |                                                                    Vitesse | Taille totale                          | Partageable avec d'autres utilisateurs |
| ---------------------------------------: | ---------------------------------------------------------------------------------------: | -------------------------------------------------------------------------: | -------------------------------------- | -------------------------------------- |
|                  **[Disque](Disque.md)** |                                              Une machine/serveur de bloc-notes à la fois |                                          Le plus rapide (débit et latence) | <=512GB total par stockage             | Non                                    |
| **[Compartiment (via Stockage Blob Azure)](StockageBlobAzure.md)** | Accès simultané depuis plusieurs machines/serveurs d'ordinateurs portables en même temps | Fast-ish (téléchargement rapide, téléchargement modeste, latence modeste) | Infini (dans la limite du raisonnable) | [Oui]                                  |

<!-- prettier-ignore -->
??? info "Si vous ne savez pas lequel choisir, ne vous en faites pas"
    Ce sont des lignes directrices, pas une science exacte - choisissez ce qui sonne le mieux maintenant et exécutez-le. Le meilleur choix pour une utilisation compliquée n'est pas évident et nécessite souvent une expérience pratique, donc essayer quelque chose vous aidera. Dans la plupart des situations, les deux options fonctionnent bien même si elles ne sont pas parfaites, et n'oubliez pas que les données peuvent toujours être copiées plus tard si vous changez d'avis.
