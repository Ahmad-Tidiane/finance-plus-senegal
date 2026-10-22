# Déploiement GitHub Pages

Le site est publié depuis `dist/`, après génération à partir de `content/` et `src/template.html`.

Les changements dans `content/`, `src/`, `dist/`, `build.py` et `tests/` déclenchent le workflow GitHub Actions sur `main`. Pages doit rester configuré avec Source : GitHub Actions.

Pour gérer les contenus sans code, voir [le guide éditeur](GUIDE-EDITEUR.md) et la page `/admin/` du site. Une activation de Pages CMS par le propriétaire est nécessaire.

Pour vérifier localement :

```sh
python3 build.py
node tests/render.cjs
```

Ne pas modifier directement `dist/index.html`, qui est régénéré au déploiement. Les images téléversées par le CMS restent dans `dist/media/`.
