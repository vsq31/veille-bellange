# Tâche planifiée « Veille Bellangé hebdo »

- **Planification** : `0 5 * * 1` (UTC) → lundi 7h heure d'été de Paris, 6h en heure d'hiver.
- **Première exécution** : lundi 31 août 2026.
- **Exécution** : session Claude fraîche, dans le cloud ; charge la skill `veille-bellange` si elle est enregistrée, sinon suit la procédure résumée dans le prompt (autosuffisante).
- **Sortie** : registre et journal réécrits sur Drive, page republiée à la même adresse, brief déposé en **brouillon** Gmail (pas d'envoi automatique — choix du 25/08/2026).

## Prompt de la tâche

> Tu es Claude, tu travailles pour Jérôme Gays. Réponds en français, tutoiement. Lance le PASSAGE HEBDOMADAIRE de la veille artistique sur Hippolyte Bellangé (1800-1866).
>
> Si la skill « veille-bellange » est disponible, charge-la et suis-la intégralement (mode « Passage hebdo »). Sinon, suis la procédure résumée ci-dessous.
>
> **Infrastructure** : dossier Drive « Veille Bellangé » avec trois Google Sheets (« Veille Bellangé — Registre », « — Sources », « — Journal », à retrouver par titre car l'id change à chaque réécriture) ; page Artifact à republier avec le paramètre `url` ; colonnes du registre dans l'ordre `ID, Date vue, Catégorie, Titre, Détails, Source, Type source, Pays, Date vente / publication, Estimation, Prix, Statut, URL, Intérêt, Mes notes`.
>
> **Procédure** : (1) charger le registre → URL connues, dernier ID, date du dernier passage ; (2) lire Gmail `Bellangé OR Bellange newer_than:8d` — alertes des plateformes fermées aux robots ; (3) balayer le web avec 4 agents en parallèle : maisons de vente FR / agrégateurs internationaux / marchands-marketplaces-libraires / publications, sans rien inventer, une URL par item ; (4) dédupliquer, vérifier chaque nouveauté en ouvrant la page, mettre à jour les statuts ; (5) réécrire le registre (nouveau Sheet même titre, vérifier, puis corbeille l'ancien) et le journal ; (6) mettre à jour la page (DATA / JOURNAL / ALERTES) et republier ; (7) `create_draft` Gmail — brouillon, pas d'envoi — objet « Veille Bellangé — semaine du JJ/MM : N nouveautés » ; (8) trois phrases de compte rendu.
>
> **Règles** : rien d'inventé ; prix tels qu'affichés, devise d'origine ; les invendus comptent ; sources bloquées notées sans insister ; ne jamais acheter, enchérir ni contacter un vendeur.

Le texte intégral (avec la liste des sources par explorateur) est celui de `skill/veille-bellange/SKILL.md`, § Procédure du passage hebdo.
