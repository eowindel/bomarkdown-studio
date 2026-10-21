# Journal des versions

Toutes les évolutions notables de BoMarkdown Studio sont listées ici.
Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et la numérotation
[Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### Corrigé
- Réglages → *Avancé (JSON)* : une clé `links` (ou `bomarkdown.Linksdefinition`) collée dans le JSON avancé est
  désormais prise en compte au lieu d'être ignorée. Le JSON avancé accepte aussi les commentaires, les virgules
  finales et un extrait de `settings.json` VS Code collé sans ses accolades.

## [0.1.0] - 2026-10-21

Première version publique, base de départ pour recueillir vos retours.

### Conception en texte
- Éditeur avec coloration syntaxique, numéros de ligne et sauvegarde automatique dans le navigateur.
- Autocomplétion contextuelle des types, statuts, bulles, types de liens et alias (`Ctrl+Espace`).
- `Tab` / `Maj+Tab` pour changer de niveau, `Entrée` pour créer un élément au même niveau.
- Documents `.bmd` (une nomenclature) et `.md` (plusieurs blocs `bomarkdown` dans un document Markdown).
- Panneau *Problèmes* : types, statuts, bulles ou types de liens inconnus, alias introuvables ou en double,
  bloc de paramètres `${{ }}$` invalide.

### Conception en graphique
- Aperçu du diagramme en direct, avec zoom et déplacement.
- Barre d'actions sur l'élément sélectionné : ajouter un enfant ou un frère, changer de niveau, réordonner,
  renommer en place, choisir le type et le statut, supprimer.
- Glisser-déposer pour changer de parent, poignée pour tirer un lien vers un autre élément (alias créé
  automatiquement), clic sur un lien pour changer son type ou le supprimer.
- Ajout de racines et de colonnes ; navigation et actions au clavier ; annulation avec `Ctrl+Z`.

### Diagramme
- Icônes par type, révisions, statuts, bulles, effectivités, liens transverses avec étiquettes, légende
  automatique, mise en forme des libellés (gras, italique, règles personnalisées), plusieurs colonnes.

### Exports
- Diagramme courant en SVG ou PNG, copie du SVG.
- Tous les diagrammes d'un document vers un dossier ou une archive ZIP.
- Insertion automatique des liens image sous chaque bloc d'un document Markdown.

### Personnalisation
- Bibliothèque d'icônes (glisser-déposer, libellés, import/export JSON).
- Éditeur visuel des types de liens : couleur, épaisseur, trait, extrémités.
- Réglages de mise en page, statuts, bulles et règles de mise en forme ; import/export des réglages.
- Interface en français ou en anglais, thème clair ou sombre.

[0.1.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.1.0
