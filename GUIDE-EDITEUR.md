# Gérer Finance Plus Sénégal avec Pages CMS

Le site garde son design et son hébergement GitHub Pages. Pages CMS fournit l’interface de gestion. La configuration est déjà dans `.pages.yml`.

## Activation unique par le propriétaire

1. Ouvrir https://app.pagescms.org/ et se connecter avec GitHub.
2. Installer l’application GitHub Pages CMS. Choisir « Only select repositories », puis uniquement **Ahmad-Tidiane/finance-plus-senegal**. Examiner les autorisations demandées avant de confirmer.
3. Ouvrir ce dépôt, branche **main**. Les rubriques apparaissent automatiquement ; ne pas créer une autre configuration.
4. Modifier une phrase de l’accueil, enregistrer, attendre le succès du workflow dans GitHub Actions, puis actualiser le site. Cette première sauvegarde confirme la connexion de bout en bout.

L’accès est également disponible sur https://ahmad-tidiane.github.io/finance-plus-senegal/admin/.

## Confier le site à un éditeur

Depuis Pages CMS, le propriétaire peut inviter un collaborateur par e-mail pour ce dépôt. Ce collaborateur peut gérer le contenu et les médias sans avoir de compte GitHub ; il ne peut pas modifier la configuration du CMS ni gérer les collaborateurs. Utiliser son compte personnel, sans partager le mot de passe du propriétaire. L’invitation reste à envoyer par le propriétaire après choix de la personne.

Documentation : https://pagescms.org/docs/configuration/collaborators/

## Rubriques disponibles

- **Accueil** : titres, introduction, légende, engagement et appel au contact.
- **À propos** : historique, dates clés, mission, vision, valeurs, gouvernance.
- **Contact** : adresse, téléphone, e-mail et horaires.
- **Informations générales** : bandeau, description SEO et mentions de bas de page.
- **Photos du site** : images principales. Les actualités possèdent leur propre image.
- **Produits et services** : liste des offres, catégories, descriptions et produits phares.
- **Agences** : ajout ou modification des agences, coordonnées, horaires et recherche Google Maps. Retirer la mention fictive uniquement pour une agence confirmée.
- **Actualités** : créer, modifier ou supprimer un article ; ajouter une photo ; cocher **Publier sur le site** pour le rendre visible. Un ordre plus faible apparaît avant les autres. L’accueil affiche les trois premiers articles publiés.

Les textes sont du texte simple : aucun code HTML à saisir. Les images peuvent être téléversées depuis le CMS ou renseignées avec une URL HTTPS. Les images téléversées sont conservées dans `dist/media`.

## Publication

Enregistrer dans Pages CMS crée un commit GitHub. Le workflow reconstruit le site à partir des contenus, vérifie les pages, puis déploie sur Pages. Attendre la coche verte dans Actions et actualiser le navigateur. Si la génération échoue, le site précédent reste en ligne : vérifier les champs obligatoires et les URL d’images.

Les brouillons ne figurent pas sur le site, mais le dépôt et son historique sont publics : ils ne sont pas confidentiels. N’ajouter ni pièces d’identité, ni dossiers de crédit, ni données clients dans le CMS.

Les formulaires contact/crédit restent des démonstrations sans envoi, sans stockage ni confirmation par e-mail. Le CMS sert à gérer les contenus publics, pas les dossiers clients.

## Maintenance technique

- `content/` : textes et collections gérés dans le CMS.
- `src/template.html` : design et interactions.
- `build.py` : générateur, Python standard sans installation.
- `dist/index.html` : résultat généré ; ne pas y modifier les textes directement.
- `dist/admin/` : page d’accès au CMS.
- `.github/workflows/deploy.yml` : construction et publication automatiques.

Commande locale : `python3 build.py`, puis `node tests/render.cjs`.

Les versions précédentes restent dans l’historique GitHub. Le CMS ne donne pas accès à la gestion des demandes de financement.
