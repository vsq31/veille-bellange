# Brief de reprise — Veille Bellangé

À coller comme premier message d'une nouvelle session Claude Code (cloud, dépôt `vsq31/veille-bellange` sélectionné) ou d'une session Cowork. Tout ce qui suit est l'état exact au 26/08/2026.

---

## Message à coller

> Tu reprends le projet **Veille Bellangé** — veille hebdomadaire sur Hippolyte Bellangé (1800-1866), peintre et lithographe napoléonien : nouvelles ventes de ses œuvres en ligne et nouvelles publications. Tu travailles pour Jérôme Gays, en français, tutoiement. Lis `CLAUDE.md` à la racine du dépôt, puis `skill/veille-bellange/SKILL.md`.
>
> **État des lieux.** Tout est construit et vérifié, sauf la publication sur GitHub :
> - Registre de 72 entrées sur Google Drive (dossier « Veille Bellangé », trois Google Sheets : Registre, Sources, Journal). Le connecteur Drive ne modifie pas un Sheet : on le réécrit (create_file même titre → vérifier → trash_file l'ancien).
> - Page tableau de bord publiée : https://claude.ai/code/artifact/2d934825-e061-4bd9-b3e8-a49f6e33fbee (republier avec `url` pour garder l'adresse ; source `dashboard/template.html` + `scripts/build_dashboard.py`).
> - Skill `veille-bellange` livrée (dossier `skill/`), procédure en 8 étapes.
> - Tâche planifiée « Veille Bellangé hebdo » (id `trig_01XuAgS8iRG5SkSE8kNqmMev`), cron `0 5 * * 1` UTC = lundi 7h Paris, première exécution le 31/08/2026. Elle dépose le brief en **brouillon** Gmail, pas d'envoi.
> - Brief n°0 en brouillon Gmail depuis le 25/08 (copie : `docs/briefs/2026-08-25-brief-0.md`).
>
> **Ce qui reste à faire, dans l'ordre :**
> 1. Si le dépôt est vide : pousser le contenu du dépôt (déjà structuré) sur `main`. Si le contenu est déjà là : vérifier que `dashboard/index.html` se génère (`python3 scripts/build_dashboard.py`) et n'a pas d'erreur JS.
> 2. Ajouter à la skill (`SKILL.md`, étape 5 bis) et au prompt de la tâche planifiée une étape **« exporter vers GitHub »** : après réécriture des Sheets, écrire `data/registre.csv`, `data/sources.csv`, `data/journal.csv`, regénérer `dashboard/`, ajouter le brief du jour dans `docs/briefs/AAAA-MM-JJ-brief-N.md`, commit `Passage hebdo AAAA-MM-JJ — N nouveautés`, push sur `main`. Mettre à jour la tâche avec `update_trigger` (ne pas en créer une seconde). Me renvoyer le `.skill` repackagé.
> 3. Facultatif, si je le demande : activer GitHub Pages sur `dashboard/` et ajouter l'URL github.io dans le README et le pied de page.
>
> **Ce que je dois faire moi-même** (rappelle-le-moi si ce n'est pas fait) : créer les alertes e-mail « Bellangé » sur Interencheres, Drouot.com et eBay.fr (indispensables), puis Leboncoin, Catawiki, Delcampe, Invaluable, Proantic, Google Alerts, Google Scholar ; et un filtre Gmail posant le label « Veille Bellangé ».
>
> **Règles :** rien d'inventé (chaque ligne du registre vient d'une page ouverte, URL incluse) ; ne pas recréer ce qui existe (Sheets, page, tâche) ; brief en brouillon, jamais envoyé ; ne jamais acheter, enchérir ni contacter un vendeur. Exclure les homonymes (Jacques Bellange, ébénistes Bellangé, Eugène Bellangé, Aurélien Bellanger).
>
> Commence par me dire en trois lignes ce que tu vois dans le dépôt et ce que tu proposes de faire en premier.

---

## Fiche de référence (pour toi, Jérôme)

### Identifiants et adresses

| Élément | Valeur |
|---|---|
| Dossier Drive | `1PQH7v1oXn_05ZxfNAWF2BXo2JbuH9Cmm` — https://drive.google.com/drive/folders/1PQH7v1oXn_05ZxfNAWF2BXo2JbuH9Cmm |
| Registre (id initial, change à chaque réécriture) | `1zFazV5Abx4_2MNcwpQicJjqAy_W92bUj_NKW0hqVVeA` |
| Sources | `17OLnkqreEcBjhwzABM73w_ONjU_SY-0XzLFtm8EIxDI` |
| Journal | `1p88JUoEhECIyrXB5kXlw8bAf0n9WCwFWeQOU2eJRrf4` |
| Page | https://claude.ai/code/artifact/2d934825-e061-4bd9-b3e8-a49f6e33fbee |
| Tâche planifiée | `trig_01XuAgS8iRG5SkSE8kNqmMev` — « Veille Bellangé hebdo », `0 5 * * 1` UTC |
| Brouillon brief n°0 | Gmail, draft `r3836242278777710818` |
| Dépôt | https://github.com/vsq31/veille-bellange |

### Ce que contient le registre (25/08/2026)

25 pièces en vente (dont Grenadier 1829 à 2 200 € chez Dantan, Scène de rue 1822 à 2 350 € chez Mazarini, Sébastopol 1855 à 1 450 €, album Souvenirs militaires 1834 à 2 000 €, Adeline 1880 sur Hollande à 2 138 €) ; 26 passages en vente depuis janvier 2025 (Zouaves Osenat 12/2025 est. 3-4 000 € probablement invendu ; Barbier du pays de Caux passé deux fois ; convoi Carlo Bonte est. 2-3 000 €) ; 10 références de cote (Wagram 12 500 €, Aboukir 57 763 $, Moskowa 6 500 €, Retraite de Constantine 4 000 €) ; 10 publications (Sazio, Napoleonica 2024/3 + thèse 2018 ; notice Orsay 04/2026 ; aucune expo 2025-26).

### Sources : ce qui passe et ce qui bloque

Passent : Osenat, Millon, Ader, Aguttes, Tajan, Thierry de Maigret et la plupart des maisons sur leur site ; Invaluable, OneBid, Artnet (index), the-saleroom, LiveAuctioneers ; Proantic (fiches), 1stDibs, Pamono, AbeBooks, Livre-rare-book ; theses.fr, Persée, OpenEdition, Gallica, POP, Louvre, Orsay.
Bloquent : Interencheres, Drouot, Gazette Drouot, eBay (recherche), Leboncoin, Catawiki, Delcampe, Galerie Napoléon, Cairn, HAL, Tribune de l'Art, Bonhams, Christie's, Artprice → alertes e-mail.

### Décisions prises

- Périmètre : tout, trié par catégorie, lithographies regroupées.
- Livraison : brouillon Gmail + page. Fréquence : hebdo, lundi 7h. Zone : France + international.
- Le brief n'est pas envoyé automatiquement (choix du 25/08/2026).

### Historique de la session du 25-26/08/2026

1. Balayage initial : 4 explorateurs, ~500 requêtes, 72 entrées.
2. Registre créé sur Drive (3 Sheets) + copie xlsx.
3. Page publiée (Bodoni Moda / IBM Plex Sans, thèmes clair et sombre, filtres, cote, alertes).
4. Skill `veille-bellange` rédigée et livrée (.skill), puis corrigée : brouillon au lieu d'envoi.
5. Brief n°0 déposé en brouillon Gmail.
6. Tâche planifiée créée (lundi 7h).
7. Dépôt GitHub structuré et commité localement ; push refusé (dépôt non autorisé dans la session) → zip livré.
