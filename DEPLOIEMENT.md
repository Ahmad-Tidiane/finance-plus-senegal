# Déploiement de Finance Plus Sénégal

Le site statique est dans `dist/index.html`. Aucun build ni installation n’est nécessaire.

## Première activation

1. Avec GitHub Free, le dépôt doit être public. Le passage en public rend le code et son historique accessibles à tous. Sinon, vérifier une offre GitHub compatible avec Pages sur dépôt privé.
2. Dans Settings → Pages → Build and deployment, choisir Source : GitHub Actions.
3. Dans Actions → Deploy Finance Plus Senegal to GitHub Pages → Run workflow, lancer la branche main. Un workflow échoué peut également être relancé.
4. Consulter l’URL retournée par le job deploy après son succès.

Toute modification de dist/ sur main déclenche ensuite le déploiement automatiquement. Seul le dossier dist est publié.

## Modifier le site

Les styles CSS, le contenu des pages et les interactions JavaScript sont dans dist/index.html. Les illustrations externes proviennent d’Unsplash ; la page agences intègre Google Maps.

## Limites de la démonstration

Les formulaires ne transmettent ni ne stockent aucune donnée. Les fichiers sélectionnés restent dans le navigateur. Aucun e-mail n’est envoyé. Les agences et les actualités sont illustratives. Les fonctionnalités de gestion, l’espace client et les intégrations de traitement des demandes nécessitent une implémentation serveur adaptée.
