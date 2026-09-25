# Modèles de CV compatibles ATS

90% des CV envoyés en ligne sont filtrés par un logiciel de tri (ATS —
Applicant Tracking System) avant qu'un humain ne les lise. La plupart des
rejets viennent de la mise en page (colonnes, tableaux, icônes, texte en
image), pas du contenu.

Ce dépôt fournit des modèles de CV en Markdown — un format texte brut, une
seule colonne, sans aucun élément qu'un ATS pourrait mal interpréter — et un
script qui les exporte proprement en PDF.

## Utilisation

1. Copiez le modèle qui vous convient (`templates/cv-template-fr.md` ou
   `templates/cv-template-en.md`) et remplissez vos informations.
2. Reprenez dans votre CV les mots-clés exacts de l'offre visée — un ATS
   cherche des correspondances littérales, pas des synonymes.
3. Installez la dépendance et générez votre PDF :

```bash
pip install -r requirements.txt
python3 export_cv.py templates/cv-template-fr.md mon-cv.pdf
```

## Pourquoi Markdown plutôt qu'un logiciel de design

Un CV conçu dans un outil graphique (colonnes, encadrés, icônes) est souvent
mal — voire pas du tout — lu par un ATS : le texte peut être interprété dans
le désordre, ou carrément ignoré s'il est intégré comme image. Le format
Markdown élimine ce risque à la source : il n'existe tout simplement pas de
mise en page à mal interpréter.

## Règles ATS respectées par ces modèles

- Une seule colonne, aucun tableau
- Aucune icône ni élément graphique remplaçant du texte
- Intitulés de sections standards (Expérience professionnelle, Formation,
  Compétences, Langues)
- Police standard, export PDF en texte réel (jamais une image scannée)

## Aller plus loin : le CV augmenté

Une fois votre CV validé côté ATS, il se retrouve dans une pile de centaines
d'autres CV tout aussi conformes. Pour vous démarquer une fois ce filtre
passé, il est possible de compléter ce même CV par une version courte,
animée par IA, à joindre en lien dans vos candidatures ou sur LinkedIn.
Des formules de création (studio vidéo + voix IA premium) existent pour ceux
qui veulent une version entièrement produite — voir la vidéo associée à ce
dépôt pour plus de détails.
