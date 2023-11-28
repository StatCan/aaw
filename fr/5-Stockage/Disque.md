# Aperçu

Les disques sont les systèmes de fichiers familiers de type disque dur auxquels vous êtes habitué, fournis à vous des disques SSD rapides !

# Installation

Lors de la création de votre serveur bloc-notes, vous demandez des disques en ajoutant des volumes de données à votre serveur de bloc-note (illustré ci-dessous, en allant dans `Options avancées`). Ils sont automatiquement montés dans le répertoire (`Point de montage`) que vous choisissez et constituent un moyen simple et fiable de conserver les données attachées à un serveur bloc-note.

![Ajout d'un volume existant à un nouveau serveur de bloc-notes](../images/kubeflow_existing_volume.png)

<!-- prettier-ignore -->
??? avertissement "Vous payez pour tous les disques que vous possédez, qu'ils soient connectés à un serveur bloc-note ou non"
    Dès que vous créez un disque, vous le [payez](#prix) jusqu'à ce qu'il soit [supprimé](#suppression-du-stockage-sur-disque), même si le Serveur de blocs-note  d'origine est supprimé. Voir [Suppression du stockage sur disque](#suppression-du-stockage-sur-disque) pour plus d'informations

# Une fois que vous avez les bases...

Lorsque vous supprimez votre serveur bloc-notes, vos disques **ne sont pas supprimés**. Cela vous permet de réutiliser ultérieurement ce même disque (avec tout son contenu) sur un nouveau serveur bloc-notes (comme indiqué ci-dessus avec `Type = Existant` et le `Nom` défini sur le volume que vous souhaitez réutiliser). Si vous en avez terminé avec le disque et son contenu, [supprimez-le](#suppression-du-stockage-sur-disque).

## Suppression du stockage sur disque

Pour voir vos disques, consultez la section Volumes de la page Serveur bloc-notes (illustré ci-dessous). Vous pouvez supprimer n'importe quel disque non connecté (icône à gauche) en cliquant sur l'icône de la corbeille.

![Supprimer un volume non connecté de l'écran Serveur blocs-note ](../images/kubeflow_delete_disk.png)

## Prix

<!-- prettier-ignore -->
??? info "Les modèles de tarification sont provisoires et peuvent changer"
    Au moment de la rédaction, la tarification est couverte par la plate-forme pour les utilisateurs initiaux. Ce guide explique comment les choses devraient être tarifées à l'avenir, mais cela peut changer.

Lors du montage d'un disque, vous obtenez un [Disque managé Azure](https://azure.microsoft.com/en-us/pricing/details/managed-disks/). La tarification des **Disques gérés SSD Premium** indique le coût par disque en fonction de la taille. Notez que vous payez pour la taille du disque demandée, et non pour la quantité d'espace que vous utilisez actuellement.

<!-- prettier-ignore -->
??? info "Conseils pour minimiser les coûts"
    Comme les disques peuvent être attachés à un Serveur blocs-note  et réutilisés, un modèle d'utilisation typique pourrait être :

    * À 9h, créez un Serveur blocs-note  (demandez 2CPU/8GB RAM et un 32GB attaché
      disque)
    * Travaillez tout au long de la journée, en enregistrant les résultats sur le disque attaché
    * À 17h, éteignez votre Serveur blocs-note  pour éviter de le payer du jour au lendemain
    * REMARQUE : Le disque attaché ** n'est pas détruit ** par cette action
    * À 9 heures du matin le lendemain, créez un nouveau serveur blocs-note et ** joignez votre disque**
    * Continuez votre travail...

    Cela protège tout votre travail sans payer pour l'ordinateur lorsque vous ne l'utilisez pas
