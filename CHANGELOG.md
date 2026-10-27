# Journal des versions

Toutes les évolutions notables de BoMarkdown Studio sont listées ici.
Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et la numérotation
[Semantic Versioning](https://semver.org/lang/fr/).

## [0.2.1] - 2026-10-27

### Ajouté
- Métadonnées (auteur, version, catégorie, tags, couleur) dans le `<head>` de `index.html`, pour que l'application
  s'affiche correctement dans le lanceur Porta[b]l Apps.

## [0.2.0] - 2026-10-23

### Ajouté
- Styles des liens de hiérarchie ([#1](https://github.com/eowindel/bomarkdown-studio/issues/1)) : le bloc
  `(h:style)` sur un enfant dessine son lien vers le parent avec un style de hiérarchie (couleur, épaisseur, tirets ou
  pointillés, extrémités). Ces styles forment une liste distincte des liens transverses, éditable dans
  Réglages → *Types de liens* ; deux styles sont fournis : `o` (optionnel, tirets) et `v` (variante, pointillés).
  Dès qu'un diagramme utilise plusieurs styles de hiérarchie, ils figurent dans la légende.
- Le style du lien vers le parent se modifie aussi depuis le diagramme : bouton de la barre d'actions, touche `P` ou
  clic sur un trait de hiérarchie. Autocomplétion, coloration, détection des styles inconnus et nouvel exemple
  *Styles des liens de hiérarchie*.
- Nouveautés en un clic : le badge de version, à côté du logo, ouvre ce journal des versions directement dans
  l'application, même hors ligne. Après une mise à jour, une pastille sur le badge signale qu'il y a du nouveau
  jusqu'à la première consultation.

### Modifié
- Le type de lien `h` (lien parent → enfant) quitte la liste des liens transverses et devient le style de hiérarchie
  par défaut. Les réglages existants et les réglages importés de VS Code sont convertis automatiquement.

## [0.1.1] - 2026-10-21

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

[0.2.1]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.2.1
[0.2.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.2.0
[0.1.1]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.1.1
[0.1.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.1.0
