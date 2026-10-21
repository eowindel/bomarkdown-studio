# BoMarkdown Studio

Version web autonome de l'extension VS Code [BoMarkdown](https://github.com/Roeperni/bomarkdown) de
[Roeperni](https://github.com/Roeperni) : on décrit une
nomenclature (BOM) en texte et on obtient un graphe SVG en arborescence, avec types, révisions, statuts,
bulles, effectivités et liens transverses.

**Un seul fichier : `index.html`.** Pas d'installation, pas de serveur, pas de dépendance, fonctionne hors ligne.
Double-cliquez dessus pour l'ouvrir dans un navigateur récent (Chrome, Edge, Firefox ou Safari).

## Ce qui change par rapport à l'extension

| Extension VS Code | BoMarkdown Studio |
|---|---|
| `BOM Preview` : webview statique à relancer | Aperçu **en direct** pendant la frappe, zoom, déplacement, **édition directe sur le graphe** (voir plus bas) |
| `BOM Export` : SVG à côté du fichier | Export du bloc courant en **SVG**, **PNG ×2** ou copie dans le presse-papiers |
| `Insert as SVG` | *Exporter → Insérer les liens image* (ajoute `![…](….svg)` sous chaque bloc) + *Tous les blocs → dossier* (écrit chaque SVG à son chemin) ou *→ ZIP* |
| `BOM Commands` | Tiroir **Référence** : types, statuts, bulles et liens, avec insertion en un clic |
| `AddIcons` / `Edit UserIcons.json` | Bibliothèque d'icônes : **glisser-déposer** d'images, libellés modifiables, import/export JSON compatible avec l'extension |
| Snippets + `Update snippets` | **Autocomplétion contextuelle** toujours à jour (`(i:`, `(s:`, `(b:`, `(l:`, alias, `(e:`, `+newcolumn`) |
| Grammaire TextMate | Coloration syntaxique intégrée, thème clair/sombre |
| Réglages `bomarkdown.*` | Dialogue **Réglages** (formulaire + JSON avancé) ; importe un `settings.json` de VS Code |
| Table `Fontsize.json` pour mesurer le texte | Mesure réelle par le navigateur (marche avec toutes les polices et tous les caractères) |
| — | Panneau **Problèmes** : type/statut/bulle/type de lien inconnu, alias introuvable ou en double, JSON `${{ }}$` invalide… |
| — | Étiquettes sur les liens : `(l:i:cible!texte)`, `!<texte` (début), `!>texte` (fin) |

La syntaxe est la même : un fichier `.bmd` ou un document Markdown écrit pour l'extension s'ouvre tel quel.
Les blocs ` ```bomarkdown chemin ` et `<!--bomarkdown chemin` sont détectés, et le curseur choisit le bloc affiché.

## Utilisation rapide

```text
+ (i:assembly,Vélo,B)(s:IW)(a:velo)
 + (i:component,Cadre,A)(s:R)(b:matrice)
 + (e:[A -> #oo[)(i:component,Roue,C)(s:F)(a:roue)
+newcolumn 40
+ (i:spec,Spécification roues)(l:i:roue!implémente)
```

- `Ctrl+Espace` : autocomplétion · `Tab` / `Maj+Tab` : changer de niveau · `Entrée` : nouvel élément au même niveau
- `Ctrl+S` / `Ctrl+O` : enregistrer / ouvrir · `Ctrl+Maj+E` : exporter le SVG · `F1` : aide complète
- Le document, les réglages et les icônes personnelles sont **sauvegardés automatiquement** dans le navigateur
  (`localStorage`).

### Édition directe sur le graphe

Le texte reste la source unique : chaque action graphique réécrit les lignes concernées, en une seule
opération annulable avec `Ctrl+Z`.

| Je veux… | Sur le graphe |
|---|---|
| Ajouter un niveau (un enfant) | Cliquer l'élément puis `Tab` ou le bouton *enfant* ; le nom se saisit sur place (`Tab` enchaîne avec un autre enfant) |
| Ajouter un élément au même niveau | `Entrée` ou le bouton *frère* |
| Changer de niveau | `Alt+→` / `Alt+←` (ou `Maj+Tab`) : la branche suit |
| Réordonner | `Alt+↑` / `Alt+↓`, ou glisser l'élément sur un autre avec `Maj` (placé juste après lui) |
| Rattacher à un autre parent | Glisser l'élément sur son nouveau parent |
| Créer un lien | Glisser la **poignée bleue** de l'élément vers la cible, ou `L` puis clic sur la cible. Le type vient du sélecteur en haut de l'aperçu, et l'alias de la cible est créé automatiquement s'il manque |
| Modifier / supprimer un lien | Cliquer sur le lien : changer son type ou `Suppr` |
| Ajouter une colonne | Bouton **+ Colonne** (insérée après la colonne de l'élément sélectionné) |
| Ajouter une racine | Bouton **+ Racine** ou double-clic sur le fond |
| Renommer, typer, statut, supprimer | Double-clic ou `F2`, `T`, `S`, `Suppr` |

Les flèches déplacent la sélection (← parent, → premier enfant), et `Ctrl+clic` amène à la ligne source.

### Fichiers

- Chrome et Edge (File System Access API) : *Enregistrer* réécrit le fichier ouvert, et *Tous les blocs → dossier*
  écrit les SVG dans le dossier choisi, en recréant les sous-dossiers (`images/produit.svg`…).
- Firefox et Safari : ouverture par sélecteur de fichier ou glisser-déposer ; l'enregistrement passe par un
  téléchargement et l'export multiple par un ZIP.

## Différences de comportement assumées

Le rendu reprend la mise en page de l'extension (`Computelayout.ts`, `HTMLgeneration.ts`). Quelques défauts ont été
corrigés au passage :

- les libellés sont échappés (`Fil>e`, `Masse < 2 kg` ne cassent plus le SVG) ;
- les remplacements d'effectivité (`->`, `#oo`…) s'appliquent à toutes les occurrences, pas seulement à la première ;
- la largeur du SVG tient compte de la légende et des effectivités des colonnes suivantes (plus de texte coupé) ;
- les identifiants SVG sont préfixés (`t-`, `s-`, `b-`) : un type peut désormais porter le même nom qu'un statut ou
  qu'une bulle ;
- le réglage « afficher la légende » est réellement pris en compte (il était toujours actif) ;
- les lignes dont le préfixe contient autre chose que des espaces, `-` ou `+` sont considérées comme des commentaires ;
- le SVG injecté par les réglages ou un bloc `${{ }}$` est nettoyé (scripts, `on*`) avant affichage et export,
  puisqu'un document partagé peut en contenir.

## Licence et crédits

BoMarkdown Studio est © 2026 **Arnaud Rousseau**, distribué sous [licence Apache 2.0](LICENSE).
Vous pouvez l'utiliser, le modifier et le redistribuer, y compris à des fins commerciales, à condition :

- de conserver le fichier [`NOTICE`](NOTICE) et la mention de l'auteur dans toute redistribution ;
- d'indiquer les fichiers que vous avez modifiés.

Ce projet est dérivé de l'extension [BoMarkdown](https://github.com/Roeperni/bomarkdown) créée par
**[Roeperni](https://github.com/Roeperni)** et ses contributeurs (licence MIT), à qui l'on doit la syntaxe, la logique de
rendu, les réglages et icônes par défaut, ainsi que les exemples du menu *Exemples*. Merci à eux ! Sa notice MIT est reproduite dans
[`THIRD_PARTY_LICENSES`](THIRD_PARTY_LICENSES).
