# CLAUDE.md — Veille Bellangé

Contexte permanent pour toute session Claude ouverte sur ce dépôt. Lis-le avant d'agir. Français, tutoiement, propriétaire : Jérôme Gays (jerome.gays@brasserie-du-venasque.com).

## Ce qu'est ce projet

Veille hebdomadaire sur **Hippolyte Bellangé** (1800-1866, peintre et lithographe napoléonien) : nouvelles ventes de ses œuvres en ligne (enchères, marchands, marketplaces, libraires) et nouvelles publications. Le cœur est une **mémoire** (registre) : on ne signale que ce qui n'y est pas encore.

## Les quatre briques (existent déjà — ne pas recréer)

| Brique | Où | Rôle |
|---|---|---|
| Registre, Sources, Journal | Google Drive, dossier « Veille Bellangé » (id `1PQH7v1oXn_05ZxfNAWF2BXo2JbuH9Cmm`), trois Google Sheets — retrouver par titre, l'id du Registre change à chaque réécriture | Source de vérité vivante |
| Skill `veille-bellange` | `skill/veille-bellange/` (copie dans le compte Claude de Jérôme) | Procédure du passage hebdo en 8 étapes |
| Page tableau de bord | Artifact `https://claude.ai/code/artifact/2d934825-e061-4bd9-b3e8-a49f6e33fbee` — republier avec `url` ; source dans `dashboard/` | Historique, filtres, cote |
| Tâche planifiée « Veille Bellangé hebdo » | id `trig_01XuAgS8iRG5SkSE8kNqmMev`, cron `0 5 * * 1` UTC (lundi 7h Paris en été) | Rejoue la skill chaque semaine, brief en **brouillon** Gmail |

Ce dépôt est l'**instantané versionné** : `data/*.csv` = export des Sheets, `dashboard/index.html` = page autonome (GitHub Pages possible), `scripts/` = générateurs, `docs/briefs/` = briefs successifs.

## Conventions du registre (ne pas changer)

Colonnes : `ID, Date vue, Catégorie, Titre, Détails, Source, Type source, Pays, Date vente / publication, Estimation, Prix, Statut, URL, Intérêt (à remplir), Mes notes`.
Catégories : Peinture · Aquarelle-gouache · Dessin · Lithographie-estampe · Livre illustré · Publication · Objet-divers.
Statuts : À venir · En vente · Vendu · Invendu · Invendu probable · Clôturé · Inconnu · Publié · À vérifier.
ID : `B` + 4 chiffres, séquentiel (dernier : B0072). Dédup par URL normalisée + clé `titre|source|date`.

## Règles absolues

- **Rien d'inventé.** Chaque ligne vient d'une page ouverte, URL en colonne M, prix tels qu'affichés, devise d'origine.
- Peintures / aquarelles / dessins d'abord ; lithographies et livres regroupés. Les invendus comptent.
- Homonymes à exclure : Jacques Bellange (graveur 1575-1616), ébénistes Bellangé, Eugène Bellangé (fils), Aurélien Bellanger.
- Sources bloquées aux robots (Interencheres, Drouot, eBay, Leboncoin, Catawiki, Delcampe, Cairn, HAL, Gazette Drouot, Tribune de l'Art) : ne pas insister, elles arrivent par les alertes Gmail.
- Le brief est **déposé en brouillon** Gmail, jamais envoyé sans que Jérôme le demande.
- Ne jamais acheter, enchérir, ni contacter un vendeur.

## Regénérer

```bash
python3 scripts/build_registre.py    # data/registre.xlsx
python3 scripts/build_dashboard.py   # dashboard/index.html + dashboard/artifact.html
```

## Commits

Messages en français, un commit par passage hebdo : `Passage hebdo AAAA-MM-JJ — N nouveautés`. Mettre à jour `data/*.csv`, `dashboard/`, `docs/briefs/`. Push sur `main` ; si `git push` renvoie 403 (app GitHub non liée à la session), passer par l'outil GitHub MCP `push_files` (un appel = un commit). `data/registre.xlsx` n'est pas versionné (binaire) : il se régénère avec `scripts/build_registre.py`.
