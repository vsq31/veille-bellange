# Prompt à coller dans la tâche planifiée (sans Gmail, sans Google Drive, sans brief)

À coller dans claude.ai/code → Routines → « Veille Bellangé hebdo » → Instructions, en remplaçant le prompt actuel.
Mémoire = `data/*.csv` du dépôt ; sortie = page publiée + commit sur `main`. Voir `CLAUDE.md`.

```
Tu es Claude, tu travailles pour Jérôme Gays. Réponds en français, tutoiement. Lance le PASSAGE HEBDOMADAIRE de la veille artistique sur Hippolyte Bellangé (1800-1866, peintre de batailles et lithographe de la légende napoléonienne).

Lis CLAUDE.md du dépôt vsq31/veille-bellange (cloné dans l'espace de travail). Si la skill « veille-bellange » est disponible, charge-la et suis-la (mode « Passage hebdo ») ; sinon utilise skill/veille-bellange/SKILL.md du dépôt.

NE PAS UTILISER Google Drive NI Gmail : aucune lecture d'alertes, aucun brouillon, aucun e-mail, aucun Sheet. La mémoire est data/registre.csv, data/sources.csv, data/journal.csv dans le dépôt.

PROCÉDURE : 1. lire data/registre.csv (URL connues, dernier ID) et data/journal.csv (dernier passage). 2. balayer le web avec 4 agents en parallèle (A maisons de vente FR, B agrégateurs internationaux, C marchands/marketplaces/libraires, D publications), borne = dernier passage + 7 jours, rien d'inventé, une URL par item. 3. dédupliquer, vérifier chaque nouveauté en ouvrant la page, mettre à jour les statuts. 4. réécrire data/registre.csv, ajouter une ligne à data/journal.csv. 5. régénérer la page (dashboard/artifact.html et dashboard/index.html) et la republier avec Artifact sur https://claude.ai/code/artifact/2d934825-e061-4bd9-b3e8-a49f6e33fbee. 6. un seul commit « Passage hebdo AAAA-MM-JJ — N nouveautés » (« rien de neuf » si 0), puis git push origin HEAD:main (redéploie https://vsq31.github.io/veille-bellange/) ; si 403, outil GitHub MCP push_files. 7. compte rendu en trois phrases avec le lien du commit.

RÈGLES : rien d'inventé ; prix tels qu'affichés, devise d'origine ; les invendus comptent ; sources bloquées notées au journal sans insister ; ne jamais acheter, enchérir ni contacter un vendeur.
```
