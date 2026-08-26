# Veille Bellangé

Veille artistique hebdomadaire sur **Hippolyte Bellangé** (Joseph-Louis-Hippolyte Bellangé, Paris 1800 – 1866), élève de Gros, peintre de batailles et lithographe majeur de la légende napoléonienne, conservateur du musée de Rouen de 1837 à 1853.

Deux objectifs :

1. **Marché** — détecter toute œuvre de Bellangé qui apparaît en ligne : enchères à venir et résultats (maisons de vente françaises et internationales, agrégateurs), stock des marchands, galeries et libraires, petites annonces et marketplaces.
2. **Publications** — articles universitaires, livres, catalogues, expositions, acquisitions et notices de musées, presse spécialisée, thèses.

Le principe : une **mémoire** (le registre) qui liste tout ce qui a déjà été vu, un **passage hebdomadaire** qui balaie les sources et les alertes e-mail, et ne signale que l'inédit, un **brief** déposé dans Gmail, et une **page** qui garde l'historique et construit la cote au fil des mois.

**Page publique : https://vsq31.github.io/veille-bellange/** — GitHub Pages, redéployée depuis `dashboard/` à chaque push sur `main`.

## Architecture

```
veille-bellange/
├── README.md
├── skill/veille-bellange/        # la procédure, rejouée chaque semaine par Claude (Cowork)
│   ├── SKILL.md                  # modes, infrastructure, procédure en 8 étapes, règles
│   └── references/
│       ├── sources.md            # sources par famille, URL de surveillance, accès robot, alertes
│       ├── brief_template.md     # gabarit du mail hebdo
│       └── dashboard_template.html
├── data/
│   ├── registre.csv              # le registre (une ligne par lot / annonce / publication)
│   ├── sources.csv               # les sources et leur état d'accès
│   ├── journal.csv               # un enregistrement par passage
│   └── registre.xlsx             # même contenu, 4 onglets, mis en forme (généré, non versionné)
├── dashboard/
│   ├── index.html                # page autonome (GitHub Pages), générée depuis les données
│   ├── template.html             # gabarit avec placeholders __DATA__ / __JOURNAL__ / __ALERTES__
│   └── artifact.html             # variante sans enveloppe <html>, pour la publication Artifact claude.ai
├── scripts/
│   ├── build_registre.py         # données de l'état des lieux → data/registre.xlsx
│   └── build_dashboard.py        # données → dashboard/index.html + artifact.html
└── docs/
    ├── tache-planifiee.md        # prompt de la tâche hebdo (lundi 7h, Europe/Paris)
    └── briefs/                   # les briefs successifs
```

La version « vivante » du registre est un Google Sheet (dossier Drive « Veille Bellangé ») : c'est lui que le passage hebdo lit et réécrit. Ce dépôt en conserve un instantané versionné à chaque passage.

## Comment ça tourne

Chaque lundi à 7h, une tâche planifiée Claude exécute la skill `veille-bellange` :

1. lit le registre sur Drive et construit l'ensemble des URL connues ;
2. lit Gmail — les alertes des plateformes qui refusent les robots (Interencheres, Drouot, eBay, Leboncoin, Catawiki, Delcampe…) ;
3. balaie le web avec quatre explorateurs en parallèle (maisons de vente FR ; agrégateurs internationaux ; marchands, marketplaces, libraires ; publications) ;
4. déduplique et vérifie chaque nouveauté en ouvrant la page ;
5. réécrit le registre et le journal ;
6. met à jour la page ;
7. dépose le brief en brouillon Gmail ;
8. exporte l'instantané vers ce dépôt (CSV, page, brief du jour — commit `Passage hebdo AAAA-MM-JJ — N nouveautés` sur `main`) ;
9. rend compte en trois phrases.

Règle de fond : **rien d'inventé** — chaque ligne du registre vient d'une page ouverte, avec son URL.

## Ce que la veille ne voit pas seule

La moitié des sources bloquent l'accès automatisé : Interencheres, Drouot, eBay, Leboncoin, Catawiki, Delcampe, la Gazette Drouot, Cairn, HAL, la Tribune de l'Art. Elles proposent toutes une alerte par e-mail sur mot-clé ; créées une fois avec « Bellangé », elles arrivent dans Gmail et le passage hebdo les lit. Liste complète et niveau d'importance dans `skill/veille-bellange/references/sources.md` et sur la page.

## Repères de cote (registre au 25/08/2026)

| Type | Fourchette observée |
|---|---|
| Grande huile de Salon (> 1 m) | 12 500 € – 57 000 $ |
| Huile moyenne (50–100 cm) | 2 300 – 6 500 € |
| Petit panneau / HST < 45 cm | 330 – 2 300 € |
| Dessin annoté / aquarelle importante | 700 – 4 000 € |
| Aquarelle courante | 250 – 700 € |
| Lithographie rare, album complet | 300 – 2 000 € |
| Lithographie courante, planche d'uniformes | 20 – 260 € |

## Regénérer la page

```bash
python3 scripts/build_registre.py    # → data/registre.xlsx
python3 scripts/build_dashboard.py   # → dashboard/index.html et dashboard/artifact.html
```

Les données de l'état des lieux sont dans `scripts/build_registre.py` (liste `ITEMS`). Pour les passages suivants, la source de vérité est le Google Sheet ; ce dépôt reçoit un export CSV.

## Bibliographie de référence

- Francis Wey, *Exposition des œuvres d'Hippolyte Bellangé à l'École impériale des beaux-arts : étude biographique*, 1867 — [Gallica](https://gallica.bnf.fr/ark:/12148/bpt6k6555744x)
- Jules Adeline, *Hippolyte Bellangé et son œuvre*, Quantin, 1880
- Henri Béraldi, « Bellangé », *Les Graveurs du XIXe siècle*, t. 2, 1885
- Solène Sazio, *Hippolyte Bellangé (1800-1866), reconnaissance et oubli d'un artiste aux origines de la légende napoléonienne*, thèse, Université de Rouen Normandie, 2018 — [theses.fr](https://theses.fr/2018NORMR021)
- Solène Sazio, « Hippolyte Bellangé (1800-1866), imagier de la légende napoléonienne », *Napoleonica. La Revue*, 2024/3 — [Cairn](https://shs.cairn.info/revue-napoleonica-la-revue-2024-3-page-159?lang=fr), [HAL](https://hal.science/hal-04995757v1)

## Homonymes à exclure

Jacques Bellange (graveur lorrain, 1575-1616) · Pierre-Antoine et Louis-Alexandre Bellangé (ébénistes) · Eugène Bellangé (fils, 1837-1895) · Aurélien Bellanger (romancier).
