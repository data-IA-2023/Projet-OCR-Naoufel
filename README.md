# Projet-OCR-Naoufel
Projet Naoufel DÃ©veloppement d'interface OCR avec Azure

# Présentation
Lien de la présentation: https://docs.google.com/presentation/d/1ZsF5qhoQj_tdZViMEkEwMSoSarV553_z_gki8Twr5lU/edit?usp=sharing

# Rapport
Lien du rapport: https://docs.google.com/document/d/1QJ73phDJKWQcW6TOUsGE1DYJwAEuBOLcryZVqfAK0L8/edit?usp=sharing
# Context
Vous travaillez en tant que développeur⸱se en IA pour le compte d’une ESN.
Un client exprime un besoin d’évolution pour sa procédure de pré-traitement des factures fournisseurs. Le client souhaite étendre les fonctionnalités de pré-traitement au-delà avec des fonctionnalités d’OCR (ou “reconnaissance optique de caractères”) afin d’obtenir un reporting automatisé de sa comptabilité fournisseurs.

Le client en question vous donne accès aux sources de sa procédure de traitement : API d'accès aux factures numérisées

# Ressources
Lien API Facture:https://invoiceocrp3.azurewebsites.net/invoices
Lien API QrCodes:https://api.qrserver.com/v1/read-qr-code/

# Attendus
En tant que développeur⸱se en IA pour le compte d’une ESN, vous devez :

Intégrer la connexion à l’API Azure Cognitives Services
Intégrer les appels aux fonctions d’OCR
Extraire les informations pertinentes
Calculer les métriques attendues à partir des résultats de l’API
Identifier un seuil de qualité minimum pour l'OCR
Stocker les résultats en base de données
Automatiser le processus complet, depuis la facture jusqu'au stockage en base de données
Intégrer les résultats dans une interface web simple
Documenter, versionner, livrer

# Livrables
- Une base de données alimentées
- Dépôt Github : avec .gitignore, requirements.txt, readme, et tous les autres scripts
- Un rapport écrit de 5 pages mini : présentation du projet, présentation de l'OCR (principe, méthode et fonctionnement, limites, etc.)
- Trello du projet

- Une appli web fonctionnelle avec :
-- Une page pour l'OCR d'une facture (démo)
-- Une page pour le reporting automatisé de la comptabilité fournisseurs
-- Une page pour le monitoring du service Azure OCR

- Slides de présentation du projet avec au moins les éléments suivants :
-- Schéma fonctionnel de l’application avec les services nécessaires les technologies utilisées
-- Identification des services d'IA existants et utilisés. Savoir expliquer leur fonctionnement
-- Liste des spécifications fonctionnelles de l’application


# Critères de performances
L'application finale doit :
- Correspondre aux objectifs énoncés
- Intégrer tous les services nécessaires à son bon fonctionnement

Bonus :
- La procédure en cas de résultat en deçà d’un seuil de qualité minimum est appliquée
- L'application peut intégrer les modalités du "ML Feedback loop".
- L'application peut intégrer un template "user friendly"
- L'application est sécurisée selon le top 10 OWASP
- L'application est Dockerisée
- L'application offre le choix d'utiliser soit le service OCR par Azure (payant) ou le service OCR Python (développement ad'hoc, gratuit)
