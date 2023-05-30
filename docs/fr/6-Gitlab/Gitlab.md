## __NOTES IMPORTANTES__
1) Veuillez NE PAS stocker votre jeton _n'importe où_ dans le système de fichiers de votre serveur d'espace de travail. Les contributeurs d'un espace de noms y auront accès.
2) S'il y a un contributeur externe à Statistique Canada dans votre espace de noms, vous perdrez l'accès au nuage principal de GitLab !

-------------------


Heureusement, l'utilisation du cloud main GitLab sur l'ETAA se fait de la même manière que l'utilisation régulière de git. 

### Etape 1 : Localisez le dépôt Git que vous voulez cloner et copiez l'option cloner avec HTTPS.
Si votre dépôt est privé, vous devrez également faire l'étape 4 (Création d'un jeton d'accès personnel) pour que cela fonctionne. 
Pour moi, il s'agissait d'un dépôt de test 
![image](https://user-images.githubusercontent.com/23174198/217060353-ba229ced-b5c1-4eae-8878-9608835cc65f.png)

### Etape 2 : Coller le lien copié dans l'un des serveurs de votre espace de travail
![image](https://user-images.githubusercontent.com/23174198/217060697-535df6c1-d9bb-4bc3-a42b-9f085a5386d5.png)

### Étape 3 : Succès ! 
Comme le montre la capture d'écran ci-dessus, j'ai cloné le repo !

### Étape 4 : Créer un jeton d'accès personnel pour pousser (également utilisé pour extraire d'un dépôt privé)
Si vous essayez de `git push ....` vous rencontrerez une erreur qui vous mènera à la [documentation d'aide de GitLab](https://gitlab.k8s.cloud.statcan.ca/help/user/profile/account/two_factor_authentication.md#error-http-basic-access-denied-the-provided-password-or-token-)

Vous devrez créer un jeton d'accès personnel pour cela. Pour cela, allez dans GitLab, cliquez sur l'icône de votre profil, puis sur `Préférences` et ensuite sur `Tokens d'accès`
![image](https://user-images.githubusercontent.com/23174198/217061060-122dded8-dc80-46ce-a907-a85913cf5dd7.png)
Suivez les instructions en entrant le nom, la date d'expiration du token et en accordant les permissions au token (j'ai accordé `write_repository`).

### Etape 5 : Personnaliser `Git` pour qu'il soit à votre image
Exécutez `git config user.email ....` et `git config user.name ...` pour correspondre à votre identité GitLab.

### Étape 6 : Fournir le jeton généré lorsqu'on vous demande votre mot de passe
Le jeton sera copiable en haut une fois que vous aurez cliqué sur `Create personal access token` en bas.
![image](https://user-images.githubusercontent.com/23174198/217062846-03a715f1-ded5-4d80-ad4b-c647ae5e30fd.png)

Une fois que vous avez tout préparé, c'est le moment
![image](https://user-images.githubusercontent.com/23174198/217063198-c1bd6c3a-ebc5-444d-98ba-24ef32faa20e.png)


### Etape 7 : Voir les résultats de votre travail dans GitLab
![image](https://user-images.githubusercontent.com/23174198/217063990-efaa8e81-a0eb-4b6d-842e-2ca3112bb4f7.png)
