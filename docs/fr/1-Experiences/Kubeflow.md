# Aperçu

## Que fait Kubeflow?

Kubeflow exécute vos **espaces de travail**. Vous pouvez avoir des serveurs de
bloc-notes (appelés serveurs Jupyter), et vous pouvez y créer des analyses en R
et Python avec des visuels interactifs. Vous pouvez enregistrer et charger des
données, télécharger des données, et créer des espaces de travail partagés pour
votre équipe.

![Kubeflow prend en charge les serveurs Jupyter](../images/jupyter_visual.png)

**Commençons sans plus tarder!**

# Créer un serveur

## Se connecter à Kubeflow

# Didacticiel vidéo

<!-- prettier-ignore -->
!!! note "" 
    Cette vidéo n'est pas à jour, certaines choses pourraient avoir changé depuis.

[![Click here for the video](../images/KubeflowVideo.PNG)](https://www.youtube.com/watch?v=xaI6ExYdxc4&list=PL1zlA2D7AHugkDdiyeUHWOKGKUd3MB_nD&index=1 "Espace de travail d'analyse avancée - Kubeflow")

# Installation

## Connectez-vous à Kubeflow

<!-- prettier-ignore -->
!!! avertissement "Connectez-vous au portail Azure à l'aide de vos identifiants cloud"
    Vous devez vous connecter au portail Azure ** en utilisant vos informations d'identification StatCan **.`first.lastname@cloud.statcan.ca` ou ** en utilisant vos informations d'identification StatCan ** `first.lastname@statcan.gc.ca`. Vous pouvez le faire en utilisant
    [Portail Azure](https://portal.azure.com).
    ![Azure Portal: Choisir l'adresse `@cloud.statcan.ca` ](../images/azure-login.png)

- Se connecter à [Kubeflow](https://kubeflow.aaw.cloud.statcan.ca)

- Accédez à l'onglet Serveurs bloc-notes

![Kubeflow gère les serveurs Jupyter](../images//kubeflow-main-ui.PNG)

- Puis clique **+ Nouveau serveur**

## Configuration de votre serveur

- Vous obtiendrez un modèle pour créer votre serveur de bloc-notes. **Remarque
  :** le nom de votre serveur doit être en lettres minuscules avec des tirets.
  **Pas d'espaces, et non souligne.**

- Vous devrez choisir une image. Vérifiez le nom des images et choisissez-en une
  qui correspond à ce que tu veux faire. (Vous ne savez pas lequel choisir ?
  Vérifiez vos options [ici](./Selecting-an-Image.md).)

![Choisissez une image](../images/select-image-screenshot.PNG)

- Si vous souhaitez utiliser un GPU, vérifiez si l'image indique `cpu` ou `gpu`.

### Image personnalisée

Un utilisateur peut utiliser une image personnalisée, auquel cas il doit connaître la forme exacte de l'image et son nom.

Les images personnalisées de l'utilisateur sont fournies via le dépôt aaw-contrib-containers qui, une fois poussées vers la branche principale, poussera également l'image vers notre ACR. Une fois cette action terminée avec succès, vous pouvez utiliser l'image personnalisée.

Lors de la création d'un bloc-notes, cliquez sur « Options avancées », cochez la case pour l'image personnalisée et saisissez l'image en saisissant `k8scc01covidacr.azurecr.io/[your-image-name-here]:[sha]`.

![Choisir une image](../images/customNotebook.PNG)

Une fois le notebook créé, si le statut n'est pas prêt au bout de quelques minutes, cliquez sur son nom pour voir la page de détails. Ensuite l'onglet « Événements » vous permet de savoir exactement ce qui se passe. Si nécessaire, contactez le canal d’aide sur Slack si le problème persiste.

## CPU et mémoire

- Au moment de la rédaction (23 décembre, 2021), il existe deux types
  d'ordinateurs dans la grappe

  - **CPU:** `D16s v3` (16 CPU , 64 G mémoire; 15 CPU et 48 G mémoire sont
    disponible pour l'utilisateur, 1 CPU et 16 G mémoire sont réservés pour
    l'utilisation du système)
  - **GPU:** `NC6s_v3` (6 CPU , 112 G mémoire, 1 GPU; 96 G de mémoire disponible
    pour l'utilisateur, 16 G sont réservés pour l'utilisation du système)

Lors de la création d'un serveur de bloc-notes, le système vous limitera aux
spécifications maximales ci-dessus. Pour les serveurs de bloc-notes CPU, vous
pouvez spécifier la quantité exacte de CPU et de mémoire dont vous avez besoin.
Cela vous permet de répondre à vos besoins de calcul tout en minimisant les
coûts. Pour un serveur portable GPU, vous obtiendrez toujours le serveur complet
(6 cœurs CPU, 96 Gio de mémoire accessible et 1 GPU).

À l'avenir, il se peut que des machines plus grandes soient disponibles, vous
pourriez donc avoir des restrictions plus souples.

<!-- prettier-ignore -->
!!! note "Bogue de création de nœud lent."
    En raison d'un bug avec le pare-feu, la création d'un nouveau nœud peut être très
    lente dans certains cas (jusqu'à quelques heures). Un correctif pour ce problème est en cours.

<!-- prettier-ignore -->
!!! note "Utilisez les machines GPU de manière responsable"
    Il y a moins de machines GPU que de machines CPU, alors utilisez-les de manière responsable.

![Choisir CPU et RAM](../images/cpu-ram.PNG)

## Stockage de vos données

-Vous aurez envie de créer un volume de données ! Vous pourrez enregistrer votre
travail ici, et si vous éteignez votre serveur, vous pourrez simplement remonter
vos anciennes données en entrant le nom de votre ancien disque. **Il est
important que vous vous souveniez du nom du volume.**

![Créer un volume de données](../images/kubeflow_volumes.png)

<!-- prettier-ignore -->
!!! conseil "Vérifiez les anciens volumes en regardant l'option Existant"
    Lorsque vous créez votre serveur vous avez la possibilité de réutiliser un ancien volume
    ou en créer un nouveau. Vous souhaitez probablement réutiliser votre ancien volume.


## Paramètres divers

Les éléments suivants peuvent être personnalisés ici :

- **Activer la mémoire partagée** : ceci est requis si vous utilisez PyTorch avec plusieurs données
   chargeurs, qui autrement généreront une erreur. Si vous utilisez PyTorch, assurez-vous de ceci
   est activé, sinon cela n'a pas d'importance sauf si vous avez une autre application
   cela nécessite une mémoire partagée.
- **Langue du système** : Vous pouvez spécifier ici l'anglais ou le français.

## Et... Créer!!!

- Si vous êtes satisfait des paramètres, vous pouvez maintenant créer le serveur
  ! Cela pourrait prenez quelques minutes pour démarrer en fonction des
  ressources que vous avez demandées. (GPU prendre plus de temps.)

<!-- prettier-ignore -->
!!! Succès "Votre serveur est en cours d'exécution"
    Si tout se passe bien, votre serveur devrait fonctionner !!! Vous aurez maintenant le
    possibilité de se connecter, et [essayer Jupyter!](/daaas/en/1-Experiments/Jupyter)

# Une fois que vous avez les bases...

## Partagez votre espace de travail

Dans Kubeflow, chaque utilisateur dispose d'un **espace de noms** qui contient
son travail (son serveurs de blocs-note, pipelines, disques, etc.). Votre espace
de nom vous appartient, mais peut être partagé si vous souhaitez collaborer avec
d'autres. **Pour plus de détails sur collaboration sur la plateforme, voir
[Collaboration](../4-Collaboration/Overview.md).**
