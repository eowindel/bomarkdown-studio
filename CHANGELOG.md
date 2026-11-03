# Journal des versions

Toutes les évolutions notables de BoMarkdown Studio sont listées ici.
Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et la numérotation
[Semantic Versioning](https://semver.org/lang/fr/).

## [0.6.0] - 2026-11-03

Troisième lot de la migration vers l'architecture de rendu de l'extension BoMarkdown 1.x
([#6](https://github.com/eowindel/bomarkdown-studio/issues/6)).

### Ajouté
- Génération de nomenclature : une ligne `+genbom:type,nombre,préfixe[,révision[,lien]];…` décrit un niveau par bloc
  séparé par `;`. Le bouton *Générer* de l'éditeur (ou `Ctrl+Maj+G`) insère sous cette ligne la nomenclature
  correspondante, annulable avec `Ctrl+Z`. Le nombre peut être une plage (`2-5` : tirage aléatoire), le préfixe est
  complété par un identifiant `x.y.z`, et le lien (une lettre) donne le style du lien vers le parent, comme `a+`.
  Exemple : `+genbom:assembly,2-5,Product ,1;component,1-3,Part ,A.1;component,2,Alternatives ,A.1,a`.
  La ligne peut aussi s'écrire `genbom:`. Une syntaxe invalide ou plus de 5 000 éléments sont refusés avec un
  message. Coloration et autocomplétion de `+genbom:`.

## [0.5.0] - 2026-11-03

Deuxième lot de la migration vers l'architecture de rendu de l'extension BoMarkdown 1.x
([#6](https://github.com/eowindel/bomarkdown-studio/issues/6)).

### Ajouté
- Étiquettes : le bloc `(t:texte,style)` ajoute un ou plusieurs cadres colorés à la fin d'un élément. Le style est un
  nom du réglage `tagstyles` ou, à défaut, une couleur de fond (`(t:banana,orange)`) ; sans style, le style `regular`
  (rouge) s'applique. Chaque style définit le cadre (`rect` : `fill`, `stroke`, `stroke_width`, `fill_opacity`…) et la
  police (`fontdef` : `wtag` texte blanc, `btag` texte noir, ou toute clé de `fontdefs`). Le réglage `tagstyles` se
  définit dans Réglages → *Avancé (JSON)* ou dans le bloc `${{ }}$` d'un diagramme.
- Édition depuis le graphe : bouton *Étiquette* de la barre d'actions (touche `E`) avec saisie du texte et choix du
  style, et bouton pour retirer l'étiquette. Autocomplétion de `(t:` et des styles après la virgule, coloration, et
  avertissement pour une étiquette sans texte.

## [0.4.0] - 2026-11-03

Premier lot de la migration vers l'architecture de rendu de l'extension BoMarkdown 1.x
([#6](https://github.com/eowindel/bomarkdown-studio/issues/6)).

### Ajouté
- Préfixe de hiérarchie `a+` : une lettre juste avant le `+` donne le style du lien vers le parent, comme dans
  l'extension (`a+ (i:component,Alternative)`). C'est un raccourci de `(h:a)` : les deux écritures sont équivalentes.
  Le code peut être un style de hiérarchie ou un type de lien transverse (`a`, `i`, `c`…). Un code inconnu est signalé
  dans le panneau *Problèmes*, et le sélecteur graphique du style de lien remplace le préfixe par `(h:…)`.
- Réglage `vpanfactor` (global, dans le bloc `${{ }}$` ou le JSON avancé) : espacement vertical en fraction de la hauteur
  d'une ligne (`panv = h / vpanfactor`). La valeur 4 reproduit l'espacement par défaut.
- Réglage `fontdefs` : surcharge facultative des polices (`label`, `eff`, `rev`, `linklabel`, `legend`) avec les clés
  `font_family`, `font_size`, `font_weight`, `font_style`, `fill`, `stroke`, `stroke_width`, `paint_order`. Sans surcharge,
  le rendu est inchangé.
- Réglage `revisionstyle` : attributs SVG du cadre de la révision (`fill`, `stroke`, `stroke_width`, `fill_opacity`…).

## [0.3.0] - 2026-11-03

### Ajouté
- Recherche dans les sélecteurs de type et de statut du diagramme ([#7](https://github.com/eowindel/bomarkdown-studio/issues/7)) :
  un champ de saisie filtre la liste au fil de la frappe (nom et libellé), `↑` / `↓` parcourent les résultats,
  `Entrée` valide et `Échap` ferme le sélecteur.

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

[0.6.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.6.0
[0.5.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.5.0
[0.4.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.4.0
[0.3.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.3.0
[0.2.1]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.2.1
[0.2.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.2.0
[0.1.1]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.1.1
[0.1.0]: https://github.com/eowindel/bomarkdown-studio/releases/tag/v0.1.0
