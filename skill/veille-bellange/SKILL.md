---
name: veille-bellange
description: Veille artistique hebdomadaire sur Hippolyte Bellangé (1800-1866), peintre et lithographe napoléonien. Détecte les nouvelles publications (articles, livres, expositions, notices de musée) et les nouvelles ventes de ses œuvres en ligne (maisons de vente, agrégateurs, marketplaces, antiquaires, galeries, libraires), les compare au registre (CSV du dépôt GitHub) pour ne signaler que l'inédit, met à jour le registre et publie la page tableau de bord. Aucun e-mail, aucun Google Drive. Déclenche dès que Jérôme demande « la veille Bellangé », « quoi de neuf sur Bellangé », « lance le passage hebdo », « des nouvelles ventes de Bellangé », « mets à jour le registre Bellangé », ou quand la tâche planifiée « Veille Bellangé hebdo » se déclenche. Utilise aussi pour un point ponctuel (« est-ce que ce lot est déjà dans le registre ? », « ajoute cette pièce au registre », « où en est la cote de Bellangé »).
---

# Veille Bellangé

Veille hebdomadaire pour Jérôme Gays sur **Hippolyte Bellangé** (Joseph-Louis-Hippolyte Bellangé, Paris 1800 – Paris 1866), élève de Gros, peintre de batailles, lithographe majeur de la légende napoléonienne, conservateur du musée de Rouen (1837-1853). Toujours en français, tutoiement.

Deux objectifs, dans cet ordre de priorité :

1. **Marché** — toute œuvre de Bellangé (ou attribuée / d'après) qui apparaît en ligne : enchères à venir, résultats, stock de marchands et de galeries, marketplaces, libraires pour les livres illustrés.
2. **Publications** — articles universitaires, livres, catalogues, expositions, acquisitions et notices de musées, presse spécialisée, thèses, conférences.

## Trois modes

| Demande | Mode |
|---|---|
| Tâche planifiée, « lance la veille », « passage hebdo » | **Passage hebdo** (procédure complète ci-dessous) |
| « ajoute X au registre », « ce lot est-il connu ? », « où en est la cote » | **Point ponctuel** : lire le registre, répondre, ajouter une ligne si demandé |
| « refais l'état des lieux », « balayage complet » | **Balayage complet** : même procédure que le passage hebdo, mais sans borne de date, 4 explorateurs à plein budget |

## Infrastructure (ne pas recréer, réutiliser)

| Élément | Où |
|---|---|
| Registre, Sources, Journal | `data/registre.csv`, `data/sources.csv`, `data/journal.csv` dans le dépôt `vsq31/veille-bellange` (branche `main`) — **source de vérité unique**. Plus de Google Drive (décision de Jérôme, 26/10/2026) : ne pas lire, créer ni écrire sur Drive. |
| Page tableau de bord (Artifact) | `https://claude.ai/code/artifact/2d934825-e061-4bd9-b3e8-a49f6e33fbee` — republier avec `url` pour garder l'adresse |
| Page publique (GitHub Pages) | `https://vsq31.github.io/veille-bellange/` — redéployée à chaque push sur `main` |
| Alertes e-mail et brief | **Abandonnés** (12/10/2026 pour les alertes, 26/10/2026 pour le brief) : balayage web uniquement, aucun brouillon ni envoi Gmail. Ne pas utiliser le connecteur Gmail. Le résultat du passage = la page publiée + le journal. |

Colonnes du registre (ne pas en changer l'ordre) : `ID, Date vue, Catégorie, Titre, Détails, Source, Type source, Pays, Date vente / publication, Estimation, Prix, Statut, URL, Intérêt (à remplir), Mes notes`.

Vocabulaire contrôlé :
- **Catégorie** : `Peinture` · `Aquarelle-gouache` · `Dessin` · `Lithographie-estampe` · `Livre illustré` · `Publication` · `Objet-divers`
- **Type source** : `Maison de vente` · `Agrégateur` · `Marchand` · `Marketplace` · `Publication`
- **Statut** : `À venir` · `En vente` · `Vendu` · `Invendu` · `Invendu probable` · `Clôturé` · `Inconnu` · `Publié` · `À vérifier`
- **ID** : `B` + 4 chiffres, séquentiel (continuer après le dernier du registre).
- Les entrées « référence de cote » (résultats anciens marquants) portent `(réf. cote)` dans Détails.

## Procédure du passage hebdo

### 1. Charger la mémoire
1. Lire `data/registre.csv` (et `data/journal.csv`) dans le clone local du dépôt.
2. Construire l'ensemble des **URL connues** (normalisées : sans `utm_*`, sans `?page=`, sans slash final, hostname en minuscules) et des **clés secondaires** `titre|source|date` pour attraper un même lot repris sur une autre URL (ex. lot Osenat relayé par Invaluable et Artnet : on garde une ligne par plateforme mais on signale « déjà connu via … »).
3. Noter le dernier ID et la date du dernier passage (Journal).

### 2. (supprimée) Lecture des alertes Gmail
Abandonnée par décision de Jérôme (12/10/2026) : ne pas lire Gmail, ne pas signaler de « panne de transfert ». Les sources bloquées aux robots (Interencheres, Drouot, eBay, Leboncoin, Catawiki, Delcampe) restent hors de portée : les noter dans le journal, sans insister ; WebSearch peut donner des pistes, à vérifier en ouvrant la page.

### 3. Balayer le web (4 explorateurs en parallèle, `Agent` general-purpose)
Donner à chacun : l'identité de l'artiste, les orthographes (`Bellangé`, `Bellange`, `Hyppolite Bellangé`, `H. Bellangé`, `hte Bellangé`), la borne de date (depuis le dernier passage, avec 7 jours de marge), la liste d'URL connues à ne pas re-signaler, et le format de retour (une ligne par item : titre ; catégorie ; source ; pays ; date ; estimation ; prix ; statut ; URL exacte). Consigne absolue : **n'inventer aucune donnée, ne retourner que ce qui a été vu sur une page ouverte, avec son URL**. Périmètres :

- **A. Maisons de vente françaises** — sites propres (Osenat en premier, puis Millon fiche artiste, Ader, Aguttes, Tajan, Thierry de Maigret, Coutau-Bégarie, Rossini, De Baecque, Libert, Émeraude, Giquello, Rouillac, Briscadieu, Pestel-Debord…), PDF de résultats `docs.prod-indb.io`. Interencheres et Drouot sont bloqués : ne pas insister, les noter dans le journal.
- **B. Agrégateurs et maisons internationales** — Invaluable (page artiste `sold-at-auction-prices` + `?page=2`), OneBid page artiste, Artnet `auction-results`, the-saleroom price guide, LiveAuctioneers price guide, MutualArt (compteur « upcoming »), Dorotheum, Lot-tissimo, Bonhams/Christie's/Sotheby's via recherche web.
- **C. Marchands, galeries, marketplaces, libraires** — Proantic (fiches indexées), Anticstore, Les Atamanes, Galerie Napoléon, Estampes MAS, Galerie Dantan, Le Serbon, La Nouvelle Athènes, Nahum, 1stDibs, Pamono, Selency, AbeBooks, Livre-rare-book, viaLibri, Galaxidion. Pour les lithographies bon marché : décompte par plateforme + les 5-10 pièces intéressantes, pas de liste exhaustive.
- **D. Publications** — Cairn/Napoleonica (bloqué : passer par la recherche web), HAL et CV de Solène Sazio, theses.fr, DUMAS, Persée, OpenEdition, Google Scholar, napoleon.org, POP/Joconde, Gallica, collections Louvre / Orsay / Carnavalet, programmation MBA Rouen, Musée de l'Armée, Malmaison, Versailles, Fondation Napoléon, Tribune de l'Art, Journal des Arts, Gazette Drouot, Wikipédia/Wikidata (historique des modifications).

URL de surveillance détaillées dans `references/sources.md`.

### 4. Dédupliquer et qualifier
- Nouveau = URL normalisée absente du registre **et** clé secondaire absente. Un lot **représenté** (même œuvre, nouvelle vente) est une nouvelle ligne, avec mention « déjà passé le … » dans Détails.
- Vérifier chaque nouveauté en ouvrant la page (`WebFetch`) avant de l'écrire : titre exact, technique, dimensions, estimation, date. Si la page ne s'ouvre pas, statut `À vérifier` et le noter dans le journal.
- Mettre à jour le statut des entrées existantes quand on l'apprend (ex. `À venir` → `Vendu 3 200 €`) : modifier la ligne existante plutôt qu'en créer une.
- Attribuer la catégorie ; « d'après Bellangé », « attribué à », « atelier de » restent dans la catégorie de la technique avec la mention dans le titre.

### 5. Écrire la mémoire
1. Réécrire `data/registre.csv` = anciennes lignes (avec statuts mis à jour) + nouvelles lignes (Date vue = aujourd'hui). UTF-8, mêmes colonnes.
2. Ajouter au `data/journal.csv` une ligne : `date, "Passage hebdo", nb ajoutées, nb signalées, "—", remarques (sources en panne, pistes non vérifiées)`.
3. `data/sources.csv` n'est modifié que si une source change d'état.

### 5 bis. Publier (commit et push, en fin de passage, après l'étape 6)
Le dépôt `vsq31/veille-bellange` est la mémoire ET la publication.
1. `dashboard/artifact.html` = le HTML produit à l'étape 6, et `dashboard/index.html` = le même contenu enveloppé dans `<!doctype html>\n<html lang="fr">\n<head>` (charset + viewport + `<style>`) `</head>\n<body>` … `</body>\n</html>` — même assemblage que `scripts/build_dashboard.py`.
2. Un seul commit : `Passage hebdo AAAA-MM-JJ — N nouveautés` (`rien de neuf` si N = 0) avec `data/*.csv` et `dashboard/`.
3. **Pousser sur `main` est autorisé d'avance par Jérôme (14/09/2026), même si la session tourne sur une branche `claude/…`** : `git push origin HEAD:main` (fast-forward, jamais de `--force`). Le push redéploie la page publique `https://vsq31.github.io/veille-bellange/` (workflow `.github/workflows/pages.yml`). Pas de pull request.
4. Si `git push` renvoie 403, passer par l'outil GitHub MCP `push_files` (owner `vsq31`, repo `veille-bellange`, branch `main`) : un appel = un commit. Sinon le noter dans le journal ; le passage suivant rattrape.
5. `data/registre.xlsx` n'est pas versionné ; il se régénère avec `scripts/build_registre.py`.

### 6. Mettre à jour la page
1. Charger `references/dashboard_template.html`.
2. Remplacer `__DATA__` par le JSON de toutes les lignes du registre (`id, vu, cat, titre, det, src, typ, pays, date, est, prix, statut, url, nouveau`) — `nouveau: true` pour les lignes ajoutées à ce passage ; `__JOURNAL__` par le journal complet (`date, type, ajout, brief, note`) ; `__ALERTES__` inchangé.
3. Écrire le fichier puis `Artifact` avec `url` = adresse ci-dessus, `favicon` 🎖️, `label` = `passage-AAAA-MM-JJ`.

### 7. (supprimée) Brief par e-mail
Abandonné par décision de Jérôme (26/10/2026) : ne pas créer de brouillon Gmail, ne pas envoyer d'e-mail. La page publiée remplace le brief ; les nouveautés y sont repérées par `nouveau: true`. Ne plus écrire dans `docs/briefs/`.

### 8. Rendre compte
Fin de session : trois phrases — nombre de nouveautés, la plus importante, ce qui n'a pas pu être vérifié. Lien de la page publique et du commit GitHub du passage (étape 5 bis).

## Règles de fond

- **Rien d'inventé.** Chaque ligne du registre vient d'une page ouverte. Estimation et prix tels qu'affichés, avec la mention « TTC » ou « frais compris » si elle figure sur la page. Devise d'origine.
- **Les lithographies ne noient pas la page.** Dans les résumés et le compte rendu, peintures / aquarelles / dessins d'abord, une ligne chacun ; lithographies et livres ensuite, regroupés (« 6 lithos entre 25 et 300 € chez X, Y, Z — la plus intéressante : … »). Une litho rare (album complet, grand format, modèle de coloris, 1re édition, épreuve avant la lettre) est traitée comme une pièce.
- **Les invendus comptent.** Un lot qui repasse ou reste en stock est une information de cote et une occasion de négocier.
- **Bruit à exclure** : Jacques Bellange (graveur lorrain, 1575-1616) ; Pierre-Antoine et Louis-Alexandre Bellangé (ébénistes, meubles) ; Eugène Bellangé (fils, 1837-1895 — à signaler à part seulement si c'est une pièce notable) ; Aurélien Bellanger (romancier) ; « Bellange » nom de lieu ou de rue.
- **Les sources bloquées ne sont pas des échecs** : les nommer dans le journal, ne pas relancer dix fois.
- **Ne jamais acheter, enchérir ou contacter un vendeur.** La veille signale ; Jérôme décide.

## Fichiers de référence

- `references/sources.md` — sources par famille, URL de surveillance, état d'accès robot, alerte e-mail correspondante.
- `references/dashboard_template.html` — gabarit de la page (placeholders `__DATA__`, `__JOURNAL__`, `__ALERTES__`).
