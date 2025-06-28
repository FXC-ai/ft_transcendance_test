# ft_transcendance

# Partie obligatoire

## Contraintes minimales du sujet

- [x]  Si vous choisissez d’inclure un backend, il doit être codé en pur Ruby.

<aside>
💡 PEUT ÊTRE OUTREPASSÉ PAR LE MODULE FRAMEWORK EN BACKEND

</aside>

[Une introduction à Ruby • Tutoriels • Zeste de Savoir](https://zestedesavoir.com/tutoriels/634/une-introduction-a-ruby/)

- [x]  Le frontend doit être développé en utilisant du Javascript natif (original sans framework ni extensions).

<aside>
💡 PEUT ÊTRE OUTREPASSÉ PAR LE MODULE FRONTEND

</aside>

[Créez des pages web dynamiques avec JavaScript](https://openclassrooms.com/fr/courses/1916641-dynamisez-vos-sites-web-avec-javascript)

[Créez des pages web dynamiques avec JavaScript](https://openclassrooms.com/fr/courses/7697016-creez-des-pages-web-dynamiques-avec-javascript)

- [x]  Votre site web doit être une application simple-page. L’utilisateur doit pouvoir utiliser les boutons Précédent et Suivant du navigateur.
- [x]  Votre site web doit être compatible avec la dernière version stable à jour de Google Chrome .
- [x]  L’utilisateur ne doit pas rencontrer d’erreurs non-gérées ou d’avertissements lorsqu’il navigue sur le site web.
- [x]  Tout le projet doit être compilé en lançant une seule ligne de commande qui démarrera un conteneur autonome fourni par Docker. Exemple : docker-compose up --build

## Jeu

- [x]  Les utilisateurs doivent pouvoir participer à une partie de Pong en temps réel contre un autre utilisateur directement sur le site web. Les 2 joueurs vont utiliser le même clavier.

<aside>
💡 PEUT ÊTRE AMÉLIORÉ PAR LE MODULE JOUEURS A DISTANCE.

</aside>

- [ ]  Un joueur doit pouvoir jouer contre un autre joueur, mais doit aussi pouvoir organiser un tournoi. Ce tournoi consiste en plusieurs joueurs qui peuvent jouer les uns contre les autres. Vous avez la flexibilité de déterminer comment vous allez implémenter le tournoi, mais il doit clairement indiquer qui joue contre qui et l’ordre des joueurs.
- [ ]  Un système d’inscription est requis : au début d’un tournoi, chaque joueur doit entrer son alias. Les alias seront réinitialisés lorsqu’un nouveau tournoi débute.

<aside>
💡 PEUT ÊTRE MODIFIÉ PAR LE MODULE DE GESTION DES UTILISATEURS.

</aside>

- [ ]  Il doit y avoir un système de "matchmaking" : le système de tournoi organise le "matchmaking" des participants, et annonce la prochaine partie.
- [ ]  Tous les joueurs respectent les mêmes règles, incluant une vitesse identique des barres (paddles). Ce pré-requis s’applique également lorsque vous utilisez une IA ; celle-ci doit se déplacer à la même vitesse que le joueur.
- [ ]  Le jeu en soi doit être développé en respectant les mêmes contraintes par défaut que le Frontend (javascript natif sans framework ni extension)

<aside>
💡 PEUT ÊTRE OUTREPASSÉ PAR LE MODULE FRONTEND.

</aside>

<aside>
💡 PEUT ÊTRE **OUTREPASSÉ** PAR LE MODULE GRAPHIQUE.

</aside>

## Questions de sécurité

- [ ]  Tout mot de passe stocké dans votre base de données doit être chiffré.
- [ ]  Votre site web doit être protégé contre les injections SQL/XSS.

[Injection SQL](https://fr.wikipedia.org/wiki/Injection_SQL)

- [ ]  Si vous avez un backend ou n’importe quelle autre fonctionnalité, il est obligatoire d’implémenter une connexion HTTPS pour tous les aspects (wss au lieu de ws...).
- [ ]  Vous devez implémenter une form de validation pour les formulaires ou toute entrée utilisateur, que ce soit sur la page de base s’il n’y a pas de backend, ou côté serveur si un backend est utilisé.

# Modules

## Web

### Module majeur : Utiliser un framework en backend

Dans ce module majeur, vous devez utiliser un framework web spécifique pour le développement de votre backend, et ce framework est Django.

[](http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf)

Tutoriel simple pour python

[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

Environnements virtuels en Python

[Django](https://docs.djangoproject.com/en/5.0/intro/)

[Integrating Django with SPA Frontend Frameworks & WebSockets](https://www.squash.io/django-integration-with-spa-frontend-frameworks-and-websockets/)

### Module mineur : Utiliser un framework ou toolkit en frontend

Votre développement frontend doit utiliser Bootstrap toolkit .

### Module mineur : Utiliser une base de données en backend

La base de données désignée pour toutes les instances de base de données dans votre projet est PostgreSQL . Ce choix garantit la cohérence des données et la compatibilité entre tous les composants du projet et peut être une condition préalable pour d’autres modules, tels que le Module Framework backend.

[How to install psql on Mac, Ubuntu, Debian, Windows](https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows/)

Interface en ligne de commande de postgres : psql

[How to use the PostgreSQL Command line to Manage Databases? | Simplified](https://hevodata.com/learn/postgresql-command-line/)

[Installer PostgreSQL et pgAdmin avec Docker sur Windows](https://thomasperrot.medium.com/installer-postgresql-et-pgadmin-avec-docker-sur-windows-ff5d49dadba9)

### Module majeur : Stocker les pointages d’un tournoi dans la Blockchain

Ce module majeur se concentre sur la mise en œuvre d’une fonctionnalité au sein du site Pong pour stocker de manière sécurisée les scores des tournois sur une blockchain. Il est essentiel de préciser que, à des fins de développement et de test, nous utiliserons un environnement de blockchain de test. La blockchain choisie pour cette implémentation est Ethereum , et le langage de programmation utilisé pour le développement de contrats intelligents sera Solidity.

- Intégration Blockchain : L’objectif principal de ce module est d’intégrer de manière transparente la technologie blockchain, spécifiquement Ethereum , dans le site Pong. Cette intégration garantit le stockage sécurisé et immuable des scores de tournois, offrant aux joueurs un enregistrement transparent et inviolable de leurs réalisations de jeu.
- Solidity Contrats intelligents : Pour interagir avec la blockchain, nous développerons des contrats intelligents en Solidity . Ces contrats seront chargés d’enregistrer, de gérer et de récupérer les scores des tournois.
- Tester la Blockchain : Comme mentionné précédemment, une blockchain de test sera utilisée pour fins de développement et de tests. Cela garantit que toutes les fonctionnalités liées à la blockchain sont rigoureusement validées sans aucun risque associé à une blockchain en direct.
- Interopérabilité : Ce module peut avoir des dépendances avec d’autres modules, en particulier le module Framework Backend. L’intégration de la fonctionnalité blockchain pourrait nécessiter des ajustements dans le backend pour permettre les interactions avec la blockchain.

En implémentant ce module, nous visons à améliorer le site de Pong en introduisant un système basé sur la blockchain pour stocker les scores. Les utilisateurs vont bénéficier de cet ajout d’une couche de sécurité et transparence, assurant ainsi l’intégrité de leurs scores. Le module met l’accent sur l’utilisation d’un environnement test de blockchain afin de minimiser les risques associés au développement blockchain.

[Ethereum](https://fr.wikipedia.org/wiki/Ethereum)

[Solidity](https://fr.wikipedia.org/wiki/Solidity)

## Gestion utilisateur

### Module majeur : Gestion utilisateur standard, authentification, utilisateurs en tournois

- Les utilisateurs peuvent s’inscrire au site web de manière sécuritaire.
- Les utilisateurs enregistrés peuvent s’authentifier de manière sécuritaire.
- Les utilisateurs peuvent choisir un nom d’affichage unique pour jouer en tournoi.
- Les utilisateurs peuvent mettre à jour leurs informations.
- Les utilisateurs peuvent téléverser un avatar, mais un avatar par défaut existe si aucun n’est fourni.
- Les utilisateurs peuvent ajouter d’autres utilisateurs comme amis et voir leur statut (en ligne / hors-ligne / en partie).
- Les profils d’utilisateurs affichent des statistiques, comme les victoires et défaites.
- Chaque utilisateur a un Historique des parties incluant les parties 1v1, les dates et autres détails pertinents, accessibles aux utilisateurs authentifiés.

### Module majeur : Implémenter une authentification à distance

Dans ce module majeur, le but est d’implémenter le système d’authentification suivant : OAuth 2.0 authentication with 42 . Les fonctionnalités à inclure sont :

- Intégrer un système d’authentification permettant aux utilisateurs d’accéder au site en toute sécurité.
- Obtenir les informations et permissions nécessaires de l’autorité afin d’activer une authentification sécuritaire.
- Mettez en place des flux de connexion et d’autorisation conviviaux pour les utilisateurs, conformes aux meilleures pratiques et normes de sécurité.
- Assurez-vous de l’échange sécurisé des jetons (tokens) d’authentification et des informations de l’utilisateur entre l’application web et le fournisseur d’authentification.

Ce module majeur vise à obtenir une authentification distante de l’utilisateur, procurant à celui-ci une façon simple et sécuritaire d’accéder à l’application web.

[OAuth](https://fr.wikipedia.org/wiki/OAuth)

### Gameplay et expérience utilisateur

### Module majeur : Joueurs à distance

Il est possible d’avoir 2 joueurs distants. Chaque joueur est sur un ordinateurs différent, accédant au même site web et jouant la même partie de Pong.

### Module majeur : Multijoueurs (plus de 2 dans la même partie)

Il est possible d’avoir plus de deux joueurs. Chaque joueur doit avoir ses propres contrôles (donc, le module précédent "Joueurs à distance" est hautement recommandé). Il vous appartient de définir comment on peut jouer à 3, 4, 5, 6 ... joueurs. En plus du jeu classique à 2 joueurs, vous pouvez choisir un nombre de joueurs unique, supérieur à 2, pour ce module multijoueur. Par exemple, 4 joueurs peuvent jouer sur un plateau carré, chaque joueur possédant un côté unique du carré.

### Module majeur : Ajout d’un second jeu avec historique utilisateur et "match-making"

Dans ce module majeur, l’objectif est d’introduire un nouveau jeu, distinct de Pong, et d’y incorporer des fonctionnalités telles que l’historique de l’utilisateur et le "matchmaking".

- Développez un nouveau jeu pour diversifier l’offre de la plateforme et divertir les utilisateurs.
- Implémentez une gestion de l’historique de l’utilisateur pour enregistrer et afficher les statistiques individuelles du joueur.
- Créez un système de "matchmaking" pour permettre aux utilisateurs de trouver des adversaire afin de disputer des parties équitables et équilibrées.
- Assurez vous que les données sur l’historique des parties et le "matchmaking" sont stockées de manière sécuritaire et demeurent à jour.
- Optimisez la performance et la réactivité du nouveau jeu afin de fournir une expérience utilisateur agréable. Mettez à jour et maintenez régulièrement le jeu afin de réparer les bogues, ajouter de nouvelles fonctionnalités et améliorer la jouabilité.

Ce module majeur vise à développer votre plateforme en introduisant un nouveau jeu, améliorant ainsi l’engagement de l’utilisateur avec l’historique des parties, et facilitant le "matchmaking" pour une expérience utilisateur agréable.

### Module mineur : Option de personnalisation du jeu

Dans ce module mineur, le but est de fournir des options de personnalisation pour tous les jeux disponibles sur votre plateforme. Les objectifs et fonctionnalités clés incluent :

- Offrir des fonctionnalités de personnalisation, comme des bonus (power-ups), attaques, différentes cartes, qui améliorent l’expérience de jeu.
- Permettre aux utilisasteurs de choisir une version du jeu par défaut avec fonctionnalités de base s’ils préfèrent une expérience plus simple.
- Assurez-vous que les options de personnalisation sont disponibles et s’appliquent à tous les jeux offerts sur la plateforme.
- Implémentez des menus de réglages conviviaux ou des interfaces pour ajuster les paramètres du jeu.
- Conservez une constance dans les fonctionnalités de personnalisation pour tous les jeux de la plateforme afin de permettre une expérience utilisateur unifiée.

Ce module vise à donner aux utilisateurs la flexibilité d’ajuster leur expérience de jeu pour tous les jeux disponibles, en fournissant une variété d’options de personnalisation, tout en offrant aussi une version par défaut, simple, pour les utilisateurs qui désirent ce type d’expérience.

### Module majeur : Clavardage en direct (live chat)

Vous devez créer un système de clavardage (chat) pour vos utilisateurs dans ce module :

- L’utilisateur doit pouvoir envoyer des messages directs à d’autres utilisateurs.
- L’utilisateur doit pouvoir en bloquer d’autres. Ainsi, l’utilisateur ne verra plus les messages provenant du compte qu’il a bloqué.
- L’utilisateur doit pouvoir inviter d’autres utilisateurs à jouer une partie de Pong à partir de l’interface de Chat.
- Le système de tournoi doit pouvoir avertir les utilisateurs qui sont attendus pour la prochaine partie.
- L’utilisateur doit pouvoir accéder aux profiles d’autres joueurs à partir de l’interface de Chat.

## IA-Algo

### Module majeur : Implémenter un adversaire contrôlé par IA

Dans ce module majeur, l’objectif est d’incorporer un joueur contrôlé par Intelligence Artificielle (IA) dans le jeu. Notamment, l’utilisation d’un A* algorithm n’est pas permise pour réaliser cette tâche. Les buts et fonctionnalités clés incluent :

- Développez un adversaire IA qui fournissent un défi et une expérience engageante aux utilisateurs.
- L’IA doit reproduire un comportement humain, signifiant que dans l’implémentation de votre IA, vous devez simuler les entrées au clavier. La contrainte ici est que l’IA peut seulement rafraîchir sa vue du jeu une fois par seconde, lui demandant donc d’anticiper les rebonds et autres actions.

<aside>
💡 L’IA doit pouvoir utiliser des bonus (power-ups) si vous avez choisi d’implémenter le Module Option de personnalisation de jeu.

</aside>

- Implémentez la logique de l’IA et le processus de décision qui permettent à votre IA de faire des mouvements et décisions intelligentes et stratégiques.
- Explorer des algorithmes alternatifs et techniques afin de créer une IA efficace sans utiliser A*.
- Assurer vous que l’IA s’adapte aux différents scénarios de gameplay et interactions utilisateurs.

Ce module majeur vise à améliorer le jeu en introduisant un adversaire contrôlé par Intelligence Artificielle qui ajoute des aspects excitants et compétitifs, tout en n’utilisant pas l’Algorithme A*.

### Module mineur : Panneaux d’affichage (dashboards) d’utilisateurs et statistiques des parties

Dans ce module mineur, le but est d’introduire des tableaux de bords qui affichent des statistiques individuelles pour les utilisateurs et sessions de jeu. Les fonctions-clés et objectifs incluent :

- Créer des tableaux de bords conviviaux qui fournissent aux utilisateurs des informations sur leurs propres statistiques.
- Développez un tableau de bord séparé pour les sessions de jeux, montrant des statistiques détaillées, des données sur les résultats et l’historique pour chaque match.
- Assurez-vous que les tableaux de bords offrent une interface informative et intuitive pour suivre et analyser les données.
- Implémentez différentes façons de visualiser les données, comme des chartes ou des graphiques, afin de présenter les statistiques de manière agréables.
- Permettez aux utilisateurs d’accéder et explorer leur propre historique de jeu et métriques de performance.
- Vous êtes libre d’ajouter n’importe quel métrique que vous jugez pertinent.

Ce module mineur vise à permettre aux utilisateurs de faire un suivi sur leurs statistiques et performances. À travers des tableaux de bords conviviaux et bien conçus, l’utilisateur peut suivre leur historique de jeu sur la plateforme et avoir une vue détaillée de leur expérience.

## Cybersécurité

### Module majeur : Mettez en place un pare-feu d’application Web (WAF) ou ModSecurity avec une configuration renforcée et utilisez HashiCorp Vault pour la gestion des secrets

Mise en place d’un pare-feu d’application Web (WAF) ou ModSecurity avec une configuration renforcée et utilisez HashiCorp Vault pour la gestion des secrets. Dans ce module majeur, l’objectif est d’améliorer l’infrastructure sécurité du projet en implémentant plusieurs composantes clés. Celles-ci incluent :

- Configurer et déployer un pare-feu d’application web (WAF) et ModSecurity avec une configuration stricte et sécuritaire afin de protéger contre les attaques potentielles.
- Intégrer HashiCorp Valut pour gérer et stocker sécuritairement toute information sensible, comme les clés API, les informations d’authentification et les variables d’environnement, s’assurant ainsi que les secrets sont correctement encryptés et isolés.

Ce module majeur vise a renforcer l’infrastructure de sécurité du projet en implémentant des mesures robustes, incluant WAF/ModSecurity pour la protection de l’application web et HashiCorp Vault pour la gestion des secrets afin d’assurer un environnement sécuritaire

[Web application firewall](https://fr.wikipedia.org/wiki/Web_application_firewall)

[Modsecurity](https://fr.wikipedia.org/wiki/Modsecurity)

[HashiCorp](https://en.wikipedia.org/wiki/HashiCorp)

### Module mineur : Options de conformité au RGPD avec anonymisation des utilisateurs, gestion des données locales et suppression de comptes

Dans ce module mineur, le but est d’introduire les options de conformité au RGPD pour permettre aux utilisateurs d’exercer leur droit en matière de protection des données. Les fonctionnalités et objectifs clés incluent :

- Implémenter des fonctionnalités qui se conforment au RGPD, permettant aux utilisateurs de demander l’anonymisation de leurs données personnelles, s’assurant ainsi que leur identité et informations personnelles et sensibles sont protégées.
- Fournir des outils aux utilisateurs pour gérer leurs données locales, incluant la possibilité de voir, modifier ou supprimer leurs informations personnelles stockées dans le système.
- Offrir un processus simplifié permettant aux utilisateurs de demander la suppression permanente de leur compte, y compris toutes les données associées, garantissant la conformité avec les réglementations de protection des données.
- Maintenir une communication claire et transparente avec les utilisateurs concernant leur droit à la protection des données avec des options facilement accessibles pour exercer ce droit.

Ce module mineur vise à améliorer la protection des données et la vie privée de l’utilisateur en offrant la conformité au RGPD qui permet aux utilisateurs de contrôler leurs informations personnelles et d’exercer leur droit à la vie privée et la protection des données à l’intérieur du système.

Si vous n’êtes pas familier avec le Règlement Général sur la Protection des Données (RGPD), il est essentiel de comprendre ses principes et implications, spécialement concernant la gestion des données de l’utilisateur et sa vie privée. Le RGPD est
une réglementation qui vise à protéger la vie privée et les données personnelles des individus sous l’Union Européenne (UE) et l’Espace Économique Européen (EEE). Il établit des règles strictes et des lignes directrices pour les organisations sur la manière dont elles doivent traiter et gérer les données personnelles.

Pour mieux comprendre le RGPD et ses exigences, il est fortement recommandé de visiter le site officiel de la Commission européenne sur la protection des données 1. Ce site fournit des informations complètes sur le RGPD, y compris ses principes, ses objectifs et les droits des utilisateurs. Il propose également des ressources supplémentaires pour approfondir le sujet et garantir la conformité à la réglementation.

Si vous n’êtes pas familier avec le RGPD, prenez le temps de visiter le lien fourni et de vous familiariser avec la réglementation avant de poursuivre ce projet.

[Data protection in the EU](https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_en)

### Module majeur : Implémenter l’authentification à 2 facteurs (2FA) et JWT (JSON Web Tokens)

Dans ce module majeur, le but est d’améliorer la sécurité et l’authentification de l’utilisateur en introduisant l’authentification à 2 facteurs (2FA) et d’utiliser JSON Web Tokens(JWT). Les fonctionnalités et objectifs incluent :

- Implémenter l’authentification à 2 facteurs (2FA) comme une couche de sécurité additionnelle pour les comptes utilisateurs, requérant à ceux-ci de fournir une seconde méthode de vérification, comme un code à usage unique, en plus de leur mot de passe.
- Utiliser JSON Web Tokens (JWT) comme méthode d’authentification et d’autorisation, assurant ainsi que les sessions utilisateur et l’accès aux ressources sont gérés de manière sécurisée.
- Fournir une interface de configuration conviviale pour l’activation du 2FA, avec des options comme un code SMS, application d’authentification, ou une vérification par courriel.
- S’assurer que les jetons JWT sont émis et validés de manière sécurisée afin de prévenir les accès non-autorisés à des comptes utilisateurs et aux données sensibles.

Ce module majeur vise à renforcer la sécurité du compte utilisateur en offrant l’authentification à 2 facteurs (2FA) et d’améliorer l’authentification et l’autorisation grâce à l’utilisation des jetons JSON Web Tokens (JWT

## Devops

### Module majeur : Configuration de l’infrastructure pour la gestion des journaux (logs)

Configuration de l’infrastructure avec ELK (Elasticsearch, Logstash, Kibana) pour la gestion des journaux (logs).
Dans ce module majeur, l’objectif est d’établir une infrastructure robuste pour la gestion et l’analyse des journaux en utilisant la pile ELK (Elasticsearch, Logstash, Kibana). Les principales caractéristiques et objectifs comprennent :

- Déployer Elasticsearch pour stocker et indexer efficacement les données de journal, les rendant facilement consultables et accessibles.
- Configurer Logstash pour collecter, traiter et transformer les données de journal provenant de différentes sources et les envoyer vers Elasticsearch.
- Mettre en place Kibana pour la visualisation des données de journal, la création de tableaux de bord et la génération d’informations à partir des événements de journal.
- Définir des politiques de rétention et d’archivage des données pour gérer efficacement le stockage des données de journal.
- Mettre en place des mesures de sécurité pour protéger les données de journal et l’accès aux composants de la pile ELK .

Ce module majeur vise à mettre en place un système de gestion et d’analyse des journaux puissant en utilisant la pile ELK, permettant un dépannage, une surveillance et des informations efficaces sur le fonctionnement et les performances
du système.

[Elasticsearch](https://fr.wikipedia.org/wiki/Elasticsearch)

[Kibana](https://fr.wikipedia.org/wiki/Kibana)

[Logstash](https://fr.wikipedia.org/wiki/Logstash)

### Module mineur : Système de monitoring

Dans ce module mineur, l’objectif est de mettre en place un système de monitoring utilisant Prometheus and Grafana . Les objectifs du module incluent :

- Déployer Prometheus en tant que trousse d’outils de surveillance et d’alerte pour collecter des métriques et surveiller la santé et les performances de divers composants du système.
- Configurer des exportateurs de données et des intégrations pour capturer des métriques à partir de différents services, bases de données et composants d’infrastructure.
- Créer des tableaux de bord personnalisés et des visualisations à l’aide de Grafana pour fournir des informations en temps réel sur les métriques et les performances du système.
- Configurer des règles d’alerte dans Prometheus pour détecter et réagir de manière proactive aux problèmes critiques et aux anomalies.
- Veiller à des stratégies appropriées de rétention et de stockage des données pour les données historiques des métriques.
- Mettre en place des mécanismes d’authentification sécurisés et de contrôle d’accès pour Grafana afin de protéger les données de surveillance sensibles.

Ce module mineur vise à établir une infrastructure de surveillance robuste en utilisant Prometheus et Grafana , permettant une visibilité en temps réel sur les métriques du système et la détection proactive des problèmes pour améliorer les performances et la fiabilité du système.

[](https://hub.docker.com/r/grafana/grafana)

Image Docker pour Grafana

### Module majeur : Design du backend comme Microservices

Dans ce module majeur, le but est de concevoir le backend du system en utilisant l’approche microservices. Cela inclue :

- Diviser le backend en de plus petits microservices peu couplés, chacun étant responsable de fonctions ou fonctionnalités spécifiques.
- Définir des limites claires et des interfaces entre les microservices pour permettre un développement, un déploiement et une mise à l’échelle indépendants.
- Mettre en place des mécanismes de communication entre les microservices, tels que des API RESTful ou des files de messages, pour faciliter l’échange de données et la coordination.
- Veiller à ce que chaque microservice soit responsable d’une tâche ou d’une capacité métier unique et bien définie, ce qui favorise la maintenabilité et la scalabilité.

Ce module majeur vise à améliorer l’architecture du système en adoptant une approche de conception basée sur les microservices, ce qui permet une plus grande flexibilité, évolutivité et maintenabilité des composants du backend.

[Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

[Deploying a Django Application with Docker, Nginx, and Certbot](https://medium.com/@akshatgadodia/deploying-a-django-application-with-docker-nginx-and-certbot-eaf576463f19)

[Qu'est-ce qu'une API RESTful ? – L'API RESTful expliquée – AWS](https://aws.amazon.com/fr/what-is/restful-api/)

## Graphiques

### Module majeur : Utilisation de techniques avancées 3D

Ce module majeur, appelé "Graphiques", se concentre sur l’amélioration de l’aspect visuel du jeu de Pong. Il introduit l’utilisation de techniques 3D avancées pour créer une expérience de jeu plus immersive. Spécifiquement, le jeu de Pong sera développé utilisant ThreeJS/WebGL pour atteindre le but désiré.

- Graphiques 3D avancés : Le but premier de ce module est d’implémenter des techniques 3D avancées afin d’élever la qualité visuelle du jeu de Pong. En utilisant ThreeJS/WebGL , nous visons à créer des effets visuels époustouflants qui plongent les joueurs dans l’environnement de jeu.
- Jouabilité immersive : L’ajout de techniques 3D avancées améliore l’expérience de jouabilité en procurant à l’utilisateur une expérience de jeu et un visuel captivants.
- Intégration technologique : La technologie choisie pour ce module est ThreeJS/WebGL. Ces outils seront utilisés pour créer les graphiques 3D, assurant la compatibilité et des performances optimales.

Ce module majeur vise à révolutionner les éléments visuels du jeu Pong en introduisant des techniques 3D avancées. Grâce à l’utilisation de ThreeJS/WebGL, nous aspirons à offrir aux joueurs une expérience de jeu immersive et visuellement époustouflante.

## Accessibilité

### Module mineur : Support sur tous types d’appareils

Dans ce module, le focus principal est de s’assurer que votre site web fonctionne sans problèmes sur tout types d’appareils. Cela inclue :

- Assurez-vous que le site web est réactif, s’adaptant à différentes tailles d’écran et orientations, garantissant une expérience utilisateur cohérente sur les ordinateurs de bureau, les ordinateurs portables, les tablettes et les smartphones.
- Assurez-vous que les utilisateurs peuvent naviguer et interagir facilement avec le site web en utilisant différents modes de saisie, tels que les écrans tactiles, les claviers et les souris, en fonction de l’appareil qu’ils utilisent.

Ce module vise a fournir une expérience constante et conviviale sur tout type d’appareils, en maximisant l’accessibilité et la satisfaction des utilisateurs.

### Module mineur : Étendre la compatibilité des navigateurs web

Dans ce module mineur, l’objectif est d’améliorer la compatibilité de l’application web en ajoutant la compatibilité pour un navigateur web supplémentaire. Cela inclue :

- Étendre le support navigateur afin d’inclure un navigateur supplémentaire, s’assurant ainsi que les utilisateurs peuvent accéder l’application web sans problèmes.
- Effectuer des tests approfondis et des optimisations pour s’assurer que l’application web fonctionne correctement et s’affiche correctement dans le nouveau navigateur pris en charge.
- Gérer et régler tout problème de compatibilité ou de rendu qui pourrait survenir dans le nouveau navigateur.
- S’assurer d’une expérience utilisateur constante sur tous les navigateurs supportés, conservant l’usage et les fonctionnalités.

Ce module mineur vise à élargir l’accessibilité de l’application web en supportant un navigateur additionnel, offrant ainsi plus de choix d’usage de l’application par l’utilisateur.

[Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/)

### Module mineur : Support de multiple langues

Dans ce module mineur, l’objectif est de s’assurer que votre site web supporte plusieurs langues afin de s’adresser à une clientèle plus large. Cela inclue :

- Implémenter le support pour un minimum de 3 langues sur le site web pour pouvoir rejoindre une audience plus large.
- Fournir une sélection de langues qui permettent de choisir et changer facilement leur langue d’affichage sur le site web.
- Traduire l’essentiel du contenu du site web, comme les menus, en-têtes et informations importantes.
- S’assurer que les utilisateurs peuvent naviguer le site web sans problèmes, peu importe la langue choisie.
- Envisagez d’utiliser des packs de langues ou des bibliothèques de localisation pour simplifier le processus de traduction et maintenir la cohérence entre les différentes langues.
- Permettre aux utilisateurs de choisir leur langue préférée par défaut pour les visites subséquentes sur le site web.

Ce module mineur vise à améliorer l’accessibilité et l’inclusivité au site web en offrant le contenu en plusieurs langues, le rendant ainsi plus convivial pour une clientèle internationale.

### Module mineur : Ajout de l’accessibilité pour les utilisateurs malvoyants

Dans ce module mineur, le but est de rendre votre site web plus accessible pour les utilisateurs malvoyants. Cela inclue :

- Prise en charge des lecteurs d’écran et des technologies d’assistance.
- Texte alternatif clair et descriptif pour les images.
- Schéma de couleurs à fort contraste pour une meilleure lisibilité.
- Navigation au clavier et gestion de la mise au point.
- Options pour ajuster la taille du texte.
- Mises à jour régulières pour respecter les normes d’accessibilité.

Ce module vise à améliorer l’utilisabilité du site web pour les individus avec problèmes de vision et des standards d’accessibilité.

### Module mineur : Intégration du rendu côté serveur (SSR)

Dans ce module mineur, le focus est sur l’intégration du rendu côté serveur (SSR) afin d’améliorer la performance et l’expérience utilisateur de votre site web. Cela inclue :

- Implémenter SSR pour améliorer les temps de chargement et la performance.
- S’assurer que le contenu est pré-rendu sur le serveur et livré au navigateur de l’utilisateur pour des chargements de pages plus rapides.
- Optimiser le référencement (SEO) en fournissant aux moteurs de recherche du contenu HTML pré-rendu.
- Maintenir une expérience utilisateur cohérente tout en bénéficiant des avantages du rendu côté serveur (SSR).

Ce module vise à améliorer les performances du site web et le référencement en intégrant le rendu côté serveur pour des chargements de page plus rapides et une meilleure expérience utilisateur.

## Orienté objet

### Module majeur : Remplacer le Pong de base par un Pong côté serveur et implémentation d’une API.

Dans ce module majeur, le but est de remplacer le jeu de Pong de base par un jeu de Pong côté serveur, avec la mise en place d’une API. Cela inclue :

- Développer la logique côté serveur pour le jeu Pong afin de gérer le gameplay, le mouvement de la balle, le comptage des points et les interactions des joueurs.
- Créer une API qui expose les ressources nécessaires et les points d’accès pour interagir avec le jeu Pong, permettant une utilisation partielle du jeu via l’interface en ligne de commande (CLI) et l’interface web.
- Concevoir et mettre en place les points d’accès de l’API pour prendre en charge l’initialisation du jeu, le contrôle des joueurs et les mises à jour de l’état du jeu.
- Assurez-vous que le jeu Pong côté serveur est réactif, offrant une expérience de jeu engageante et agréable.
- Intégrez le jeu Pong côté serveur avec l’application web, permettant aux utilisateurs de jouer au jeu directement sur le site web.

Ce module majeur vise à améliorer le jeu Pong en le migrant côté serveur, en permettant une interaction à la fois via une interface web et une interface en ligne de commande (CLI), tout en offrant une API pour un accès facile aux ressources et aux fonctionnalités du jeu.

### Module majeur : Activation du gameplay via ligne de commande (CLI) contre les utilisateurs Web avec intégration API.

Dans ce module majeur, le but est de développer une interface en ligne de commande (CLI) qui permettent aux utilisateurs de jouer à Pong contre des joueurs utilisant la version web du jeu. La CLI devrait se connecter de manière transparente à l’application web, permettant aux utilisateurs CLI de se joindre et d’interagir aux joueurs web. Les fonctionnalités incluent :

- Créez une application CLI robuste qui reproduit l’expérience de jeu Pong disponible sur le site web, offrant aux utilisateurs de la CLI la possibilité d’initier et de participer à des parties de Pong.
- Utilisez l’API pour établir une communication entre la CLI et l’application web, permettant aux utilisateurs de la CLI de se connecter au site et d’interagir avec les joueurs web.
- Développez un mécanisme d’authentification des utilisateurs au sein de la CLI, permettant aux utilisateurs de la CLI de se connecter de manière sécurisée à l’application web.
- Mettez en place une synchronisation en temps réel entre la CLI et les utilisateurs web, garantissant que les interactions de jeu sont fluides et cohérentes.
- Permettez aux utilisateurs de la CLI de rejoindre et de créer des parties de Pong avec les joueurs web, facilitant le jeu interplateforme.
- Fournissez une documentation complète et des conseils sur la manière d’utiliser efficacement la CLI pour des parties de Pong contre des utilisateurs web.

Ce module majeur vise à améliorer l’expérience du jeu de Pong en créant une CLI qui offre un environnement transparent, unifié et interactif de jouabilité.

# My ft_transcendance project

- [ ]  Si vous choisissez d’inclure un backend, il doit être codé en pur Ruby. (FX)
- [ ]  Le frontend doit être développé en utilisant du Javascript natif (original sans framework ni extensions). (Killian)
- [ ]  Votre site web doit être une application simple-page. L’utilisateur doit pouvoir utiliser les boutons Précédent et Suivant du navigateur.
- [ ]  Votre site web doit être compatible avec la dernière version stable à jour de Google Chrome .
- [x]  L’utilisateur ne doit pas rencontrer d’erreurs non-gérées ou d’avertissements lorsqu’il navigue sur le site web.
- [x]  Tout le projet doit être compilé en lançant une seule ligne de commande qui démarrera un conteneur autonome fourni par Docker. Exemple : docker-compose up --build (FX)

## Jeu

- [x]  Les utilisateurs doivent pouvoir participer à une partie de Pong en temps réel contre un autre utilisateur directement sur le site web. Les 2 joueurs vont utiliser le même clavier. (Benoit)
- [x]  Un joueur doit pouvoir jouer contre un autre joueur, mais doit aussi pouvoir organiser un tournoi. Ce tournoi consiste en plusieurs joueurs qui peuvent jouer les uns contre les autres. Vous avez la flexibilité de déterminer comment vous allez implémenter le tournoi, mais il doit clairement indiquer qui joue contre qui et l’ordre des joueurs. (Killian et PH)
- [x]  Un système d’inscription est requis : au début d’un tournoi, chaque joueur doit entrer son alias. Les alias seront réinitialisés lorsqu’un nouveau tournoi débute. (Killian et PH)
- [x]  Il doit y avoir un système de "matchmaking" : le système de tournoi organise le "matchmaking" des participants, et annonce la prochaine partie. (Killian et PH)
- [x]  Tous les joueurs respectent les mêmes règles, incluant une vitesse identique des barres (paddles). Ce pré-requis s’applique également lorsque vous utilisez une IA ; celle-ci doit se déplacer à la même vitesse que le joueur.
- [x]  Le jeu en soi doit être développé en respectant les mêmes contraintes par défaut que le Frontend (javascript natif sans framework ni extension)

Web

- [x]  Module majeur : Utiliser un framework en backend (FX)
- [x]  Module mineur : Utiliser un framework ou toolkit en frontend (Killian)
- [x]  Module mineur : Utiliser une base de données en backend (FX)
- [ ]  Module majeur : Stocker les pointages dʼun tournoi dans la Blockchain

Gestion utilisateur

- [x]  Module majeur : Gestion utilisateur standard, authentification, utilisateurs en tournois (Benoit PH)
- [ ]  Module majeur : Implémenter une authentification à distance
- [x]  Module majeur : Joueurs à distance (PH Killian)
- [x]  Module majeur : Multijoueurs (plus de 2 dans la même partie) (Killian et PH)
- [ ]  Module majeur : Ajout dʼun second jeu avec historique utilisateur et "match-making"
- [ ]  Module mineur : Option de personnalisation du jeu
- [ ]  Module majeur : Clavardage en direct (live chat)

IA Algo

- [x]  Module majeur : Implémenter un adversaire contrôlé par IA (Benoit et FX)
- [ ]  Module mineur : Panneaux dʼaffichage (dashboards) dʼutilisateurs et statistiques des parties

Cybersécurité

- [ ]  Module majeur : Mettez en place un pare-feu dʼapplication Web (WAF) ou ModSecurity avec une configuration renforcée et utilisez HashiCorp Vault pour la gestion des secrets
- [ ]  Module mineur : Options de conformité au RGPD avec anonymisation des utilisateurs, gestion des données locales et suppression de comptes
- [ ]  Module majeur : Implémenter lʼauthentification à 2 facteurs (2FA et JWT JSON Web Tokens)

Devops

- [ ]  Module majeur : Configuration de lʼinfrastructure pour la gestion des journaux (logs)
- [ ]  Module mineur : Système de monitoring
- [x]  Module majeur : Design du backend comme Microservices (FX)

Graphiques

- [ ]  Module majeur : Utilisation de techniques avancées 3D

Accessibilité

- [ ]  Module mineur : Support sur tous types dʼappareils
- [ ]  Module mineur : Étendre la compatibilité des navigateurs web
- [ ]  Module mineur : Support de multiple langues
- [ ]  Module mineur : Ajout de lʼaccessibilité pour les utilisateurs malvoyants
- [ ]  Module mineur : Intégration du rendu côté serveur (SSR)

Orienté objet

- [ ]  Module majeur : Remplacer le Pong de base par un Pong côté serveur et implémentation dʼune API.
- [ ]  Module majeur : Activation du gameplay via ligne de commande (CLI) contre les utilisateurs Web avec intégration API.

# Frontend

[Environment Variables in JavaScript: process.env](https://dmitripavlutin.com/environment-variables-javascript/)

[https://www.youtube.com/watch?v=6BozpmSjk-Y](https://www.youtube.com/watch?v=6BozpmSjk-Y)

## La logique du front :

Lorsque l’utilisateur se connecte à localhost:7890/, il charge la page index.html qui execute le script router.js

router.js :

```jsx
// Importe la View de chaque page
import renderFourPlayers from "../views/viewFourPlayers.js"
import renderFourOnline from "../views/viewFourOnline.js"
import renderFriends from "../views/viewFriends.js"
import renderLogin from "../views/viewLogin.js"
import renderProfile from "../views/viewProfile.js"
import renderTournament from "../views/viewTournament.js"
import renderTwoPlayers from "../views/viewTwoPlayers.js"
import renderTwoOnline from "../views/viewTwoOnline.js"
import renderGameHistory from "../views/ViewGameHistory.js"

// Importe le script de chaque page qui gere le load et listener
import handleFriends from "./friends.js"
import handleLogin from "./login.js"
import handleProfile from "./profile.js"
import handleTournament from "../games/tournament.js"
import handleTournamentOnline from "../games/tournamentOnline.js"
import handleTournamentRoom from "../games/tournamentRoom.js"
import handleTwoPlayers from "../games/pong2players.js"
import handleFourPlayers from "../games/pong4players.js"
import handleTwoPlayersOnline from "../games/pong2playersonline.js"
import handleFourPlayersOnline from "../games/pong4playersonline.js"
import handleGameHistory from "./gamehistory.js"

// Cas particulier pour index
import handleIndex from "./index.js"

/**
 * Routes object
 * Contains all the pages of the website
 * Each page has a title, a path, a view, a load function and a listener function
 * The title is the title of the page
 * The path is the path of the page
 * The view is the HTML content of the page
 * The load function is the function that checks if the user can access the page
 * The listener function is the function that attaches event listeners to the page
*/
const routes = {
	"index": {
		title: "Main",
		path: "/",
		view: handleIndex.renderIndex,
		load: handleIndex.loadIndex,
		listener: handleIndex.listenerIndex
	},
	"friends": {
		title: "Amis",
		path: "/friends/",
		view: renderFriends,
		load: handleFriends.loadFriends,
		listener: handleFriends.listenerFriends
	},
	"login": {
		title: "Login",
		path: "/login/",
		view: renderLogin,
		load: handleLogin.loadLogin,
		listener: handleLogin.listenerLogin
	},
	"profile": {
		title: "Profile",
		path: "/profile/",
		view: renderProfile,
		load: handleProfile.loadProfile,
		listener: handleProfile.listenerProfile
	},
	"tournament": {
		title: "Tournoi Local",
		path: "/tournament/",
		view: renderTournament.renderTournament,
		load: handleTournament.loadTournament,
		listener: handleTournament.listenerTournament
	},
	"tournament_online": {
		title: "Tournoi en Ligne",
		path: "/tournamentOnline/",
		view: renderTournament.renderTournamentOnline,
		load: handleTournamentOnline.loadTournamentOnline,
		listener: handleTournamentOnline.listenerTournamentOnline
	},
	"tournament_online_room": {
		title: "TournamentRoom",
		path: "/tournamentRoom/",
		view: renderTournament.renderTournamentRoom,
		load: handleTournamentRoom.loadTournamentRoom,
		listener: handleTournamentRoom.listenerTournamentRoom
	},
	"twoplayers": {
		title: "2 Joueurs Local",
		path: "/twoplayers/",
		view: renderTwoPlayers,
		load: handleTwoPlayers.loadTwoPlayers,
		listener: handleTwoPlayers.listenerTwoPlayers
	},
	"fourplayers": {
		title: "4 Joueurs Local",
		path: "/fourplayers/",
		view: renderFourPlayers,
		load: handleFourPlayers.loadFourPlayers,
		listener: handleFourPlayers.listenerFourPlayers
	},
	"twoplayersonline": {
		title: "2 Joueurs en Ligne",
		path: "/twoplayersonline/",
		view: renderTwoOnline,
		load: handleTwoPlayersOnline.loadTwoPlayersOnline,
		listener: handleTwoPlayersOnline.listenerTwoPlayersOnline
	},
	"gamehistory": {
		title: "Historique des parties",
		path: "/gamehistory/",
		view: renderGameHistory,
		load: handleGameHistory.loadGameHistory,
		listener: handleGameHistory.listenerGameHistory
	},
	"fourplayersonline": {
		title: "4 Joueurs en Ligne",
		path: "/fourplayersonline/",
		view: renderFourOnline,
		load: handleFourPlayersOnline.loadFourPlayersOnline,
		listener: handleFourPlayersOnline.listenerFourPlayersOnline
	},
};

/**
 * Logout handler function
 * Send a PATCH request to the server to logout the user
 * If the response status is 200, the user is successfully logged out and redirected to the login page
*/
async function handleLogout() {

	const csrftoken = document.cookie.split("; ").find((row) => row.startsWith("csrftoken"))?.split("=")[1];

	const init = {
		method: "PATCH",
		headers: { 'X-CSRFToken': csrftoken, },
	}

	try {

		let hostnameport = "http://" + window.location.host

		const response = await fetch(hostnameport + '/api/logout/', init);

		if (response.status === 200) {
			console.log("user successfull logged out");

			sessionStorage.clear();
			router("login");
		}
	} catch (e) {
		console.error(e);
	}
};

/**
 * Router function
 * @param {string} value - The value of the button that was clicked
 * Get the page from the routes object, if it exists
 * Call the load function of the page
 	* If the load function returns 1 (the user can access it), render the view of the page
*/
export default async function router(value) {

	var page = routes[value];

	if (!page)
		return;

	if (await page.load() === 1) {
		document.getElementById("main__content").innerHTML = page.view();

		document.getElementById("navbar__btn--text").textContent = sessionStorage.getItem("username") ? sessionStorage.getItem("username") : "user";
		document.getElementById("navbar__btn--avatar").src = sessionStorage.getItem("avatar") ? sessionStorage.getItem("avatar") : "/frontend/img/person-circle-Bootstrap.svg";
		document.getElementById("navbar__btn--avatar").alt = sessionStorage.getItem("avatar") ? sessionStorage.getItem("username") + " avatar" : "temp avatar";

		document.title = page.title;

		window.history.pushState({}, "", page.path);

		page.listener();
	}
	else
		router("login");
};

/**
 * Event listener for popstate event

*/
window.addEventListener("popstate", async (e) => {
	e.preventDefault();

	// Get the current url, remove all '/' and if the url is null assign it to 'index'
	let url = window.location.pathname.replaceAll("/", "");
	if (url === "")
		url = "index";

	var page = routes[url];

	if (!page)
		return;

	if (await page.load() === 1) {
		document.getElementById("main__content").innerHTML = page.view();

		document.getElementById("navbar__btn--text").textContent = sessionStorage.getItem("username") ? sessionStorage.getItem("username") : "user";
		document.getElementById("navbar__btn--avatar").src = sessionStorage.getItem("avatar") ? sessionStorage.getItem("avatar") : "/frontend/img/person-circle-Bootstrap.svg";
		document.getElementById("navbar__btn--avatar").alt = sessionStorage.getItem("avatar") ? sessionStorage.getItem("username") + " avatar" : "temp avatar";

		document.title = page.title;

		page.listener();
	}
	else
		loadIndex();
});

/**
 * Event listener for window.onload event
 * Load the page that the user is currently on
 * If the user is logged in, load the page that the user is currently on
 * If the user is not logged in, redirect to the login page
*/
window.onload = async function() {

	const currentPath = window.location.pathname;
	for (const route in routes) {
		if (routes[route].path === currentPath) {
			if (await routes[route].load() === 1) {
				document.getElementById('main__content').innerHTML = routes[route].view();  // Render the HTML content for the page

				document.getElementById("navbar__btn--text").textContent = sessionStorage.getItem("username") ? sessionStorage.getItem("username") : "user";
				document.getElementById("navbar__btn--avatar").src = sessionStorage.getItem("avatar") ? sessionStorage.getItem("avatar") : "/frontend/img/person-circle-Bootstrap.svg";
				document.getElementById("navbar__btn--avatar").alt = sessionStorage.getItem("avatar") ? sessionStorage.getItem("username") + " avatar" : "temp avatar";

				document.title = routes[route].title;

				routes[route].listener();  // Attach event listeners
			}
			else
				router("login");
			break;
		}
	}
};

/**
 * Load index function
 * Send a GET request to the server to check if the user is logged in
 * If the response status is 202, the user is logged in and redirected to the index page
 * If the response status is 203, the user is not logged in and redirected to the login page
*/
async function loadIndex() {

	try {

		let hostnameport = "http://" + window.location.host

		const response = await fetch(hostnameport + '/api/index/');

		if (response.status === 202) {

			router("index");
		}
		if (response.status === 203) {

			router("login");
		}
	} catch (e) {
		console.error(e);
	}
};

/*
function called when the user try to login with 42 app
*/
async function load42Profile(code)
{
	try {
		let hostnameport = "http://" + window.location.host

		const init = {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},

			body: JSON.stringify({code: code})
		};
		

		const response = await fetch(hostnameport + '/api/call_back/', init);

		if (response.status == 200)
		{
			const data = await response.json()
			
			console.log("username " + data["username"])
			console.log("avatar " + data["player"].avatar)
			console.log("nickname " + data["player"].nickname)

			sessionStorage.setItem("username", data["username"]);
			sessionStorage.setItem("avatar", data["player"].avatar);
			sessionStorage.setItem("nickname", data["player"].nickname);

			document.querySelector("div.modal-backdrop.fade.show").remove();

			document.querySelectorAll(".nav__link").forEach(btn => {
				btn.removeAttribute("disabled");
			});
			document.getElementById("navbar__btn--user").removeAttribute("disabled");
			document.getElementById("logout").removeAttribute("disabled");

			// router("index");
		}
		else
		{
			throw new Error(`HTTP error, status = ${response.status}`);
		}

	} catch (e) {
		console.error(e);
	}
}

/**
 * Event listener for DOMContentLoaded event
 * If the user is on the index page, index specific logic is executed
 * Attach event listener to the 'logout' button
 * Attach event listeners on all buttons with the class 'nav__link' i.e. all buttons that redirect to another "page"
*/
document.addEventListener("DOMContentLoaded", () => {

	if (window.location.search) {
		let code = window.location.search.split("=")[1]
		// console.log("code = ", code)
		load42Profile(code)
	}

	if (window.location.pathname === "/") {
		loadIndex();
	}

	document.getElementById("logout").addEventListener("click", (e) => {
		e.preventDefault();
		handleLogout();
	});

	document.querySelectorAll(".nav__link").forEach(element => {
		element.addEventListener("click", (e) => {
			e.preventDefault();
			if (element.value !== window.location.pathname.replaceAll("/", "")) {
				router(element.value);
			}
		})
	});

});

```

Tous d’abord, il faut attacher à la page les evenements auquelles ele doit pouvoir réagir :

- loadIndex est appelé dés le chargement de la page
- load42Profile est appelé dés le chargement de la page localhost:7890/code=”CODE_API_42”
- handleLogout est appelé en cas de clic sur le bouton logout
- router(”value”) est appelé en cas de clic sur l’un des boutons du menu de navigation

```jsx
/**
 * Event listener for DOMContentLoaded event
 * If the user is on the index page, index specific logic is executed
 * Attach event listener to the 'logout' button
 * Attach event listeners on all buttons with the class 'nav__link' i.e. all buttons that redirect to another "page"
*/
document.addEventListener("DOMContentLoaded", () => {

	if (window.location.search) {
		let code = window.location.search.split("=")[1]
		// console.log("code = ", code)
		load42Profile(code)
	}

	if (window.location.pathname === "/") {
		loadIndex();
	}

	document.getElementById("logout").addEventListener("click", (e) => {
		e.preventDefault();
		handleLogout();
	});

	document.querySelectorAll(".nav__link").forEach(element => {
		element.addEventListener("click", (e) => {
			e.preventDefault();
			if (element.value !== window.location.pathname.replaceAll("/", "")) {
				router(element.value);
			}
		})
	});

});

```

# Python

## Environnement virtuel

Pour créer un environnement virtuel : `python -m venv /path/to/new/virtual/environment`

Pour activer environnement virtuel dans bash : `source *<venv>*/bin/activate` 

# Django

Pour commencer un projet : `django-admin startproject mysite`

## manage.py

Pour créer une nouvelle application au sein du projet django : `python manage.py startapp polls` 

| `python manage.py makemigrations` | Cette commande est responsable de la création de nouvelles migrations basées sur les modifications que vous avez apportées à vos modèles Django. Il génère ensuite automatiquement des fichiers de migration contenant les opérations nécessaires pour appliquer ces changements au schéma de la base de données. Ces fichiers de migration sont stockés dans le dossier migrations de chaque répertoire d'application. |
| --- | --- |
| `python manage.py migrate` | Elle applique les migrations de base de données à la base de données spécifiée dans les paramètres de votre projet. Les migrations sont le moyen pour Django de propager les modifications que vous apportez à vos modèles (ajout d'un champ, suppression d'un modèle, etc.) dans le schéma de la base de données.
”migrate” prend les fichiers de migration générés par makemigrations (ou fournis par Django lui-même pour les applications intégrées) et les applique à la base de données. |

En pratique, on utilise la commande makemigration pour que django prenne en compte les modifications. Ensuite on utilise la commande migrate pour que ces migrations soient prise en compte parr l’application.

## Shell de django

Le Shell de django est un shell python classique. Il est nottament possible de créer des entrées en base de donnée grâce à lui.

```python
>>> from listings.models import Band
>>> mem = Members()
>>> mem.name = 'Lucky Luck'
>>> mem.save()
>>> Members.objects.count()
>>> Members.objects.all()
```

## Basiques du management des URLs :

Il existe 3 manière de gérer les URLs avec django. Dans le fichier urls.py :

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

### Nouvelle page avec la fonction view

Dans le fichier <project>/urls.py :

```python

from django.contrib import admin
from django.urls import path
from <app> import views

urlpatterns = [
    path('admin/', admin.site.urls),
		path('hello/', views.hello, name='hello'),
    path('hello/<int:id>/', views.hello_details, name='hello-details'),
		path('login/', views.login),
]

```

Le troisième argument d’un Path est une chaine de caractère qui peut être utilisées dans le code pour faire des hyperliens. Pour cela il faut utiliser un block url dans les gabarits :

```python
<a href="{% url 'hello' %}">Retour</a>
```

Dans le fichier <app>/view.py

```python
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello World !</h1>')
```

### Inclure un URLconf supplémetaire

Au sein d’u projet django, il y a 3 fichiers qui assurent le routage des URLs :

- <projects>/urls.py
- <app>/urls.py
- <app>/view.py

Le fichier <project>/urls.py contient : 

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

La fonction include permet au serveur d’aller chercher l’URL demandé par le client. Par exemple toutes les urls qui commencent par polls/ seront recherchées à partir de cette racine dans le fichier polls/urls.py

Le fichier <app>/urls.py contient :

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.subscribe, name="subscribe"),
]
```

Il repertorie tous les path commençant par polls

Le fichier <project>/views.py contient  la fonction subscribe 

```python
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def subscribe(request):
		return HttpResponse("subscribe")
```

## Le fichier setting.py

Pour ajouter une app au projet il faut :

- Ajouter un élément à la liste INSTALLED_APP :

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

polls.apps.PollsConfig est une classe du module PollsConfig. Elle contient le “name” de l’app ainsi que un attribut “default_auto_field”…

- Utiliser la commande : `python [manage.py](http://manage.py/) makemigrations polls`

Si aucun modèle n’a été spécifié, django répond : `No changes detected in app 'polls`. Cette commande permet de faire migrer les modifications apportés au modèle. Elle remplit le fichier OOO1_initial.py

En production, il est possible de modifier d’autres paramêtres 

| SECRET_KEY | Clé utilisé par django pour la sécurité de l’application |
| --- | --- |
| DEBUG | C’est booléen qui qctive ou désactive le mode debuggage. Cela permet d’avoir des pages d’erreurs détaillées. Certaines mesures de sécurité sont assouplis. Donc ne pas utiliser en production |
| ALLOWED_HOST | Liste des noms d’hôtes/domaines que le site django peut servir. Si l’en-tête Host de la requête n’est pas dans cette liste, Django renvoie une erreur> En développement, l’idéal d’utliser la valeur : ['localhost', '127.0.0.1', '[::1]'] |
- DATABASES

Pour configurer la DATABASES du projet avec une base de donnée différente de la base de donnée par défaut, on peut également utilisé les variables d’environnement :

```python
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
```

### Le fichier admin.py

Tout d’abord,, pour créer un superuser pour se connecter à <>/admin

```bash
python manage.py createssuperuer
```

Le fichier admin.py permet de modifier la page /admin/ fournit par Django.

Il faut importer les modèles que l’on veut administrer :

```python
from members_test_fx.models import Members
from members_test_fx.models import Games
```

Il est possible de modifier l’apparence de la page :

![Screenshot 2024-03-16 at 17.34.28.png](https://github.com/FXC-ai/ft_transcendance_test/blob/main/Screenshot_2024-03-16_at_17.34.28%201.png)

```python
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name','surname', 'age', 'active', 'connection_state')

class GamesAdmin(admin.ModelAdmin):
    list_display = ('title','members')

admin.site.register(Members, MembersAdmin)
admin.site.register(Games, GamesAdmin)
```

## Le fichier form.py

### Créer un formulaire :

Il est possible de définir un formulaire de la même manière que l’on définit une table dans un le fichier model.py. Les champs sont les mêmes que pour les modèles. Voici un exemple :

```python
from django import forms

class FormTest(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    surname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField(required=True)
```

Lorsque l’utilisateur clique sur le bouton pour l’envoie du formulaire, il est possible de traiter la requête grâce à l’objet `request`.

Pour ajouter notre form à notre page, il faut déjà l’importer dans la vue :

```python
from members_test_fx.forms import FormTest
```

Ensuite, il faut mettre une instance de cet objet form dans une variable :

```python
form = FormTest()
```

Dans la vue, il est possible de remplir le formulaire avec les données précédemment envoyées par l’utilisateur :

```python
form = FormTest(request.POST)
```

Enfin renvoyer à la vue grâce au dictionnaire :

```python
return render (request, "GABARIT.html", {"form" : form})
```

Cette objet contient plusieurs attributs. Pour plus de précisions :

[Django](https://docs.djangoproject.com/en/5.0/ref/request-response/)

Celui qui nous intéresse particulièrement est l’attribut `POST` qui contient un dictionnaire avec tous les champs remplis par l’utilisateur.
Si on l’afficher dans le terminal (), voici ce que nous obtenons :

```bash
<QueryDict: {'csrfmiddlewaretoken': ['PQ0cLghUV9qcmXpLVnUTnOOwaWAmro3rMCuA4P08Eg1Hks6JH3r5dF74AHoNESIO'], 'name': ['Coindreau'], 'surname': ['François-Xavier'], 'age': ['36'], 'email': ['fx.coindreau@gmail.com']}>
```

Ce dictionnaire peut être envoyé à la vue.
Pour éviter les problèmes lors du rafraîchissement de la page, on peut rediriger vers une autre page grâce à la fonction `redirect`.

```python
return redirect('email-sent')
```

### Créer un ModelForm

Il est possible de créer un formulaire à partir d’un modèle. Il se déclare de cette manière dans le fichier `form.py`

```python
from django import forms
from members_test_fx.models import Games

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'
				# exclude = ('NOM_DU_CHAMP')
```

Il est possible d’exclure des champs à l’aide de l’attribut exclude.

Ensuite ce formulaire est utilisable comme n’importe quel formulaire dans `view.py`

```python
form = GamesForm()
```

Pour modifier un objet en Base de données, il suffit de réutiliser le formulaire précédent en le remplissant à l’aide de l’objet choisis en DB. Voici comment :

```python
def game_change (request, id):
    game = Games.objects.get(id=id)
    if request.method == 'POST':
        form = GamesForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('hello')
        else :
            print("La forme est pas valide")
    else:
        form = GamesForm(instance=game)
    return render(request, "members_test_fx/game_change.html" ,{'form' : form})
```

La seule nouveauté par rapport au code précédent est la ligne : `form = GamesForm(request.POST, instance=game)`

Cette fois ci, GamesForm prend 2 arguments. Le deuxième informe Django que l’on veut modifier un objet existant. Si cet argument est absent la form ne pourra jamais être valide.

## Gestion de la base de donnée

### Le fichier model.py

Dans ce fichier chaque classe correspond à une Table et les attributs de ces classes sont les champs de la table.

```python
from django.db import models
# Create your models here.

class Members(models.Model):
    name = models.fields.CharField(max_length=100)

class Games(models.Model):
    title = models.fields.CharField(max_length=100)

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

A propos des différents champs :

Django est livré avec différents types de champs qui correspondent à différents types de données, comme `CharField` ou `IntegerField` . Il existe aussi des champs plus spécifiques qui vont contraindre l'entrée, comme `URLField` .

Nous pouvons définir des contraintes et des règles pour les champs en leur attribuant des options, comme `max_length` , `null` et `choices` .

```python
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Members(models.Model):
    class connection(models.TextChoices):
        HORS_LIGNE = "hors ligne"
        ONLINE = "online"
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(default="default")
    age = models.fields.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)])
    active = models.fields.BooleanField(default=True)
    connection_state = models.fields.CharField(max_length=10, choices=connection.choices, default=connection.HORS_LIGNE)

class Games(models.Model):
    title = models.fields.CharField(max_length=100)
```

Nous pouvons affiner davantage les contraintes sur les champs en spécifiant des validateurs sur les champs en utilisant l'option `validators` .

Si nous ajoutons des champs non nuls à un modèle, nous serons invités à leur fournir une valeur par défaut initiale lors de la migration.

[Django](https://docs.djangoproject.com/fr/5.0/ref/models/fields/#field-types)

- Le premier argument peut être une chaîne de caractère, il permet de donner un nom plus lisible au champ.

 Il est possible d’inspecter les requêtes effectués sur la base de donnée avec la commande : `python manage.py sqlmigrate polls 0001` 

- Nous pouvons créer des relations one-to-many en utilisant le champ`ForeignKey`.
- Nous contrôlons la stratégie de ce qui se passe lorsqu'un modèle lié est supprimé, en utilisant l'argument `on_delete`.
    - définir le champ comme nul en utilisant `models.SET_NULL`
    - définir le champ à sa valeur par défaut en utilisant `models.SET_DEFAULT`
    - supprimer l'objet en utilisant `models.CASCADE`

### Comment utiliser le contenu de la db dans le code

Dans le fichier <app>/view.py

```python
from django.shortcuts import render
from django.http import HttpResponse
from members_test_fx.models import Members
from members_test_fx.models import Games

# Create your views here.

def hello(request):
    tab_members = Members.objects.all()
    tab_games = Games.objects.all()
    return HttpResponse(f"<h1>{tab_members[0].name} joue une {tab_games[1].title}</h1>")

```

Il est possible également de récupérer les informations fournies dans l’URL :

```python
def hello_details(request, id):
    mem = Members.objects.get(id=id)
    return render(request, 'members_test_fx/hello_details.html', {'mem': mem})
```

Dans l’URL path il faudra préciser le type de données que l’on s’attend à recevoir :

```python
path('hello/<int:id>/', views.hello_details),
```

## Les gabarits ou templates

- Créer un fichier gabarit dans « <app>/templates/<app>/ » et lui donner l'extension « .html ».
- Changer la déclaration de retour de la vue pour appeler la méthode `render` et lui passer le chemin de votre fichier de gabarit.
- Passer également un dictionnaire de contexte à la méthode `render`.

```python
def hello(request):
    tab_members = Members.objects.all()
    tab_games = Games.objects.all()
    return render(request, "members_test_fx/hello.html", {"tab_members": tab_members, "tab_games": tab_games})
    #return HttpResponse(f"<h1>{tab_members[0].name} joue une {tab_games[1].title}</h1>")
```

- Utiliser des variables de gabarits pour injecter des données dans votre gabarit.
- Utiliser les balises de gabarits pour utiliser les boucles dans votre gabarit si besoin.

```html
<html>
    <head><title>django test</title></head>
    <body>
        <h1>Hello Django !</h1>
        <p>Liste des parties :</p>
        <ul>
			<li>{{tab_members.0.name}} joue une {{tab_games.1.title}}</li>
			<li>{{tab_members.1.name}} joue une {{tab_games.3.title}}</li>
		</ul>

        <p>Liste des membres :</p>
        {%for mem in tab_members %}
        {{ mem.name | upper}} /
        {%endfor%}

        <p>Liste des games :</p>
        {%for gam in tab_games %}
        {{ gam.title }} /
        {%endfor%}     
        
        <p>Liste des parties conditionnelles :</p>
        {% for gam in tab_games %}
            {% if 'pourrie' in gam.title %}
                Oulala...
            {% else %}
                Better...
            {% endif %}
            {{ gam.title }} /
        {% endfor %}
    
    </body>
</html>
```

Pour améliorer la gestion des gabarits, on peut utiliser des block.

On utilise une page html de base au sein de laquelle on a un block content :

```html
<html>
    <head><title>django test</title></head>
    <title>Merchex</title>
    <link rel="stylesheet" href="{% static 'members_test_fx/styles.css' %}" />
    <body>
				{% block content %}{% endblock %}
    </body>
</html>
```

Ce block content est dans une autre page html :

```html
{% extends 'members_test_fx/base.html' %}

{% block content %}

...

{% endblock %}
```

Pour que cela fonctionne, il faut utiliser les block extends et remplir le block content comme précédemment.

Pour ajouter une feuille de style :

- Il faut ajouter un dossier `static/<app>` dans le dossier de l’app pour y stocker le .css
- Pour faire référence à ce .css, on utilise le block `{% load static %}` en début de page. Ensuite, il est possible d’y faire référence avec `{% static 'members_test_fx/styles.css' %}`

# Django REST Framework

[Understanding Views In Django Rest Framework](https://medium.com/@sydney.idundun/understanding-views-in-django-rest-framework-d78ca8042f04)

## API view

Tout d’abord pour installer l’API dans l’environnement Python :

```bash
pip install djangorestframework
```

De la même manière que nous ajoutions une page à un projet Django classique :
Dans le fichier `<app>/urls.py` :

```python
from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIView.as_view()),
]
```

2 URLs ont été ajoutées :

- api-auth/ : pour se connecter à….
- api/category/ : pour lister sous forme d’un json le contenu de la database

Ensuite dans le fichier `<app>/serializers.py` :

```python
from rest_framework.serializers import ModelSerializer
from shop.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
```

Le principe est identique aux ModelForms, il faut créer une classe qui hérite de ModelSerializer. Ensuite, on utilise une classe imbriquée qui permet de sélectionner le modèle sur lequel se base notre serializer ainsi quel es champs à sérialiser.

Enfin dans le fichier `<app>/views.py` :

```python
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category
from shop.serializers import CategorySerializer
 
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
```

Concernant les importations, il y en 4. Deux concernent rest_framework. Les deux autres ne sont autres que le modèle sur lequel on veut travailler et le serializer. La fonction get est réécrite. Elle est appelée par le serveur lorsque la fonction GET apparait dans la requête. C’est le principe du ENDPOINT !!!!!

## ModelViewSet

### Le routeur

DjangoREST framework fournit un outils surpuissant pour faciliter la création d’une interface CRUD. Le routeur fonctionne ainsi :

```python
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from players_manager.views import PlayerViewSet

router = routers.SimpleRouter()
router.register('players', PlayerViewSet, basename='players')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
```

1. Creation du routeur
2. Registration du Router avec l’objet PlayerViewSet

Django REST crée automatiquement une collection de route pour l’interface CRUD. Ici, ces routes commenceront par `api/players`

1. On inclut toutes ces routes grâce à l’objet path

### Le ModelViewset de Player

```python
from rest_framework.viewsets import ModelViewSet

from players_manager.models import Player
from players_manager.serializers import PlayerSerializer

class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    #queryset = Player.objects.all()
    def get_queryset(self):
        return Player.objects.all()
```

L’objet PlayerViewSet hérite de ModelViewSet qui possède notamment parmi ses méthodes get_queryset qui doit être override pour que DjangoREST sache quoi faire lorsqu’on appelle l’url api/players. Il est possible d’interdire les modifications en remplaçant ModelViewSet pat ReadOnlyModelViewSet.

L’attribut serializer_class permets de specifier avec modele la classe travaille

Le serializer n’a pas été modifié.

### Ajouter des filtres

La fonction get_queryset peut être améliorée par les filtres pour des requêtes plus précises

On peut récupérer les variables get de l’URL grâce à l’objet request :

```python
param_name = self.request.GET.get('PARAM_NAME')
```

Exemple pour la table friends :

```python
class FriendViewSet(ModelViewSet):
	serializer_class = FriendSerializer
	#queryset = Friend.objects.all()
	def get_queryset(self):
		queryset = Friend.objects.all()

		player = self.request.GET.get('player')
		accept = self.request.GET.get('accept')

		if player is not None:
			queryset = queryset.filter(player_1=player) | queryset.filter(player_2=player)

		if accept is not None:
			queryset = queryset.filter(accept=accept)

		# queryset = queryset.filter(player_1=player)
		#player_1 = self.request.query_params.get('player_1', None)
		return queryset
```

[Django QuerySet - Filter](https://www.w3schools.com/django/django_queryset_filter.php)

## serializers.py

Le serializer est en charge de transformer les données de la db en fichier json. Il est possible de définir différents serializers utilisables ensuite dans la view.py

```python
from rest_framework.serializers import ModelSerializer

from players_manager.models import Player

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'login']

class PlayerDetailsSerializer(ModelSerializer):
    class Meta:
       model = Player
       fields = '__all__'
```

Ensuite, dans la view, il est possible de choisir le serializer en focntion de l’action demandé par le client.

Pour cela on override une fonction de l’objet ModelViewSet `get_serializer_class` :

```python
    def get_serializer_class(self):
        print("get_serializer_class", self.action)
        if self.action =='retrieve':
            return self.detail_serializer_class
        return self.serializer_class
```

Les actions disponibles sont :

- **list** : appel en `GET` sur l’URL de liste ;
- **retrieve** : appel en `GET` sur l’URL de détail (qui comporte alors un identifiant) ;
- **create** : appel en `POST` sur l’URL de liste ;
- **update** : appel en `PUT` sur l’URL de détail ;
- **partial_update** : appel en `PATCH` sur l’URL de détail ;
- **destroy** : appel en `DELETE` sur l’URL de détail.

Avant de se lancer dans la suite, il est indispensable de comprendre que les actions CRUD de base sont déjà codé lorsqu’on fait hérité notre Viewset de ModelViewSet. Selon la requête, la modification en base de donnée sera faite. Dans le cas d’une requête POST sur l’URL de liste

## rest_framework.decorators

Pour pouvoir utiliser ces décorateurs, il faut importer :

```python
from rest_framework.response import Response
from rest_framework.decorators import action
```

Pour ajouter des actions customisées, il est possible d’ajouter des décorateurs. Ces décorateurs prennent 3 paramètres :

- `methods` est la liste des méthodes HTTP qui appellent cette action, parmi GET, POST, PATCH, PUT, DELETE.
- `detail` est un booléen qui précise si l’action est disponible sur l’URL de liste ou de détail.
- `url_path` permet de déterminer l’URL qui sera ajoutée à la fin de l'endpoint de
liste ou de détail. S'il n’est pas précisé, alors le nom de la méthode
est utilisé.

Pour utiliser une action customisée on utilise le décorateur de la façon suivante :

```python
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from players_manager.models import Player
from players_manager.serializers import PlayerSerializer, PlayerDetailsSerializer

class PlayerViewSet(ModelViewSet):

    serializer_class = PlayerSerializer
    detail_serializer_class = PlayerDetailsSerializer

    def get_queryset(self):
        return Player.objects.all()

    #REDEFINITION DE LA METHODE GET_SERIALIZER_CLASS
    def get_serializer_class(self):
        print("get_serializer_class", self.action)
        if self.action =='retrieve':
            return self.detail_serializer_class
        return self.serializer_class

    @action(methods=['GET'], detail=True)
    def modify_nickname(self, request, pk):
        new_nickname = self.request.GET.get('new_nickname')
        if new_nickname is not None:
            current_player = self.get_object()
            current_player.nickname = new_nickname
            current_player.save()
            return Response(status=200)
        return Response(status=404)
 
```

La requête http qui permet d’utiliser cette action customisée est la suivante :
`http://localhost:7890/api/players/10/modify_nickname/?new_nickname=Pierre-Henri`

On utilise modify_nickname car nous n’avons pas précisé d URL au décorateur.

## Validations des champs

Tout d’abord, petite overv

## djangorestframework-simplejwt

Afin de rendre certains endpoint privés on utilise les tokens. Suite à la demande d’un utilisateur, l’API va fournir 2 tokens : un access_token et un refresh_token. L’acess token permet de s’assurer de l’identité du client. Le second est utilisé pour rafraichir le premier.

Dans le fichier settings.py, plusieurs modifications sont à effectuer pour ajouter simplejwt :

```python

INSTALLED_APPS = [
...
    'rest_framework_simplejwt',
...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}
```

Pour ajouter les token, il faut déjà ajouter les urls nécessaires dans urls.py :

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

Et c’est tout… Pour tester la création d’une paire de nouveaux tokens :

`POST http://localhost:7890/api/token/ username=USER_NAME password=PASSWORD`

`POST http://localhost:7890/api/token/refresh/ Refresh=ACCESS_TOKEN`

## Authentification simple

Tout d’abord models.py…

Il faut relier la table user avec de django avec le modele qui contient les informations supplémetaires. Pour cela il faut utiliser une ForeighKey

```python
from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    **owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)**
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
```

LA méthose save a été overide pour compléter les champs au moment de l’enregistrement en database. Le champ owner contient en premier parametre “auth.User” qui fqit reference au modele user de l’application “auth”. Cette notation permet d’eviter les importations circulaires…

Ensuite le serializer.py :

```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
			model = Snippet
			fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted']
			**owner = serializers.ReadOnlyField(source='owner.username')**

class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = User
		fields = ['id', 'username','snippets']
```

Comme le modele est modifié, il faut aussi modifier le serializer. Ici on utilise pas la correspondance directe dans laquelle un champ d’une table correspond au champ d’une autre table. On utilise l’argument source qui indiaue à DRF d’aller chercher dans l’instance de owner le champ username. Cocernant le type de champ “ReadOnly”, il s’agit d’un champ multi-type qui signifie que l’instance ne sera jamais modifié par le biais de ce serializer.

Maintenant les views :
C’est dans les views que nous allons autoriser l’accès ou non à certains endpoints. Pour cela on utilise l’attribut permission_classes. Il existe des permissions fournis par DRF mais il est aussi possible de creer nos propres classes de permission. 

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	**permission_classes = [permissions.IsAuthenticatedOrReadOnly]**

	def perform_create(self, serializer):
		print ("erer : ", self.request.user)
		serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	**permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]**
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
```

Le fichier permission.py

On ecrit des classes qui herite de la classe permissions.BasePermission et on peut overide les méthodes.

```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
		def has_object_permission(self, request, view, obj):
			if request.method in permissions.SAFE_METHODS:
				return True
			return obj.owner == request.user
```

[Django Rest Framework authentication: the easy way](https://www.guguweb.com/2022/01/23/django-rest-framework-authentication-the-easy-way/)

## Systeme d’inscription

[Login and Register User — Django Rest Framework](https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5)

[User Registration/Authentication with Django, Django Rest Framework, React, and Redux](https://iheanyi.com/journal/user-registration-authentication-with-django-django-rest-framework-react-and-redux/)

## Comment fonctionne l’inscription / log in avec l’API 42

Tout d’abord il faut créer une nouvelle application dans notre profil intra. 

![Getting started](https://github.com/FXC-ai/ft_transcendance_test/blob/main/Screenshot_2024-04-28_at_10.38.53.png)

![Screenshot 2024-04-28 at 10.38.53.png](ft_transcendance%2083c7088d594e4cfab43bcfa1f0d95b3d/Screenshot_2024-04-28_at_10.38.53.png)

SCOPES de l’application il serait peut-être plus judicieux de choisir un plus adapté à nos besoins. Par exemple, le scope profil ?

REDIRECT URI : il s’agit de l’URL vers laquelle l’utilisateur sera redirigé lorsqu’il se sera loggé avec ses identifiants 42.

Le clic sur le lien “se connecter avec 42” permet de configurer le premier appel à l’API avec les identifiants fournis lors de l’étape précédente.

```python
SOCIALACCOUNT_PROVIDERS = {
    '42': {
        'SCOPE': ['profile'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False,
        'KEY': 'u-s4t2ud-491a5d4d14d35ef25080f2f05937152abcd6c6f65ab162196a8c5ea26e7e5f65',
        'SECRET': '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',
    }
}
```

La classe suivante se charge d’envoyer au front le lien dûment configuré pour qu’il soit en mesure de rediriger l’utilisateur vers la page de login 42. Lorsque l’utilisateur s’est loggé sur la page login 42 il est redirigé vers l’url “REDIRECT URI”.
Cette requête est intercepté par le frontend du site dans le fichire router.js :

```jsx
	if (window.location.search) {
		let code = window.location.search.split("=")[1]
		// console.log("code = ", code)
		load42Profile(code)
	}
```

La fonction load42Profile est appelée, pour effectuer une requête POST vers une seconde classe du backend appelée Callback. La methode post de cette classe se charge de s’authentifier au prés de l’API 42 en utilisant le code renvoyé par celle-ci lorsque l’utilisateur s’est loggé. Cela est permis à l’aide d’une requête POST sur le endpoint 'https://api.intra.42.fr/oauth/token'  fournis par l’API 42. Cela est permis grâce à la bibliothéque requests de python.

```python
class Callback(APIView):

    def post(self, request):
        # Step 2: Receive authorization code and exchange for access token

        code = request.data["code"]

        # return Response(code, status=status.HTTP_200_OK)

        redirect_uri = 'http://localhost:7890/'  # Change to your callback URL
        token_url = 'https://api.intra.42.fr/oauth/token'
        data = {
            'client_id': settings.SOCIALACCOUNT_PROVIDERS['42']['KEY'],
            'client_secret': settings.SOCIALACCOUNT_PROVIDERS['42']['SECRET'],
            'code': code,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
            'scope': "public profile"

        }
        response = requests.post(token_url, data=data)
```

La response contient un “access_token”. Cet access_token permet d’effectuer une troisième requête sur le endpoint 'https://api.intra.42.fr/v2/me'. Ce endpoint fonctionne car nous sommes loggé à notre compte 42. Je présume qu’il utilise le cookie créé au moment ou nous avons été loggé à 42…

Tout d’abord, il faut effectuer la redirection vers l’API pour 

Il faut distinguer 2 cas pour notre projet :

- le cas ou l’utilisateur se log pour la première fois
- le cas où l’utilisateur s’est déjà loggé au paravent avec son login 42

D

# PostgresSQL

## Container et client postgres

 

1. Tout d’abord pull l’image du container : `docker pull postgres`
2. Run le container avec postgres : `docker run --name postgresql_test -p 5442:5432 -e POSTGRES_PASSWORD=test -d postgres`
    - Ici on choisit la variable d’environnement qui permettra de se connecter au serveur avec -e
3. Pour installer psql : `brew install libpq`
4. Pour lancer le client psql : `psql -p 5442 -h 127.0.0.1 -U postgres` 
    - -U permet de choisir l’utilisateur, par défaut il n’y a qu’un seul user : postgres qui est le owner des database de base

Depuis l’interieur du container : `psql --username=bck_django --dbname=db_bck_django`

\dt \c

# Design du backend en microservice

Comment fonctionne les containers en mode dev ?

On lance les containers en mode dev avec la commande `docker-compose up —build`

2 containers vont être built : web et db. IL N’Y A PAS DE CONTAINER POUR NGINX

- web contient tous les fichiers de l’app et est bind mount avec un volume
- db fait tourner postgresSQL. Ce sont les settings de django qui se chargent de se connecter à la base de données. La DB est montés  avec un volume postgres_data

![ft_transcendance_containers_dev.png](https://github.com/FXC-ai/)

Le serveur e

## Container nginx

Le container nginx peut être lancé séparément : `docker build -t test1_nginx . && docker run -p 80:8000 test1_nginx`

Le port 80 est utilisé mais le sujet requiert d’utiliser le protocole https, il faut donc utiliser le port 443.

Il permet d’avoir accès à toutes les page statiques du site.

## Container django

Le container django peut lui aussi être lancé indépendement à condition de supprimer la dépendance à la base de donnée : 

`docker build -t test1_django . && docker run -p 8000:8000 test1_django`

### Qu’est-ce qu’un WSGI comme gunicorn ?

WSGI (Web Server Gateway Interface) est un standard spécifiant comment un serveur Web peut interagir avec une application Python.

[Why Use WSGI/ASGI When We Have Nginx?](https://santoshk.dev/posts/2023/why-use-wsgi-asgi-when-we-have-nginx/)

[Le protocole HTTP et WSGI — documentation Programmation Web pour la bio-informatique 1.0](https://perso.liris.cnrs.fr/pierre-antoine.champin/2017/progweb-python/cours/cm1.html#:~:text=WSGI%20(Web%20Server%20Gateway%20Interface,interagir%20avec%20une%20application%20Python.)

### A quoi sert psycopg2 ?

Psycopg est un adaptateur de base de données PostgreSQL pour le langage de programmation Python.

## Container postgres

Il peut lui aussi être lancé de manière indépendante en utilisant la commande suivante : `docker build -t test1_postgres -f Dockerfile.postgres . && docker run -p 8000:8000 test1_postgres`

Cependant, Dockerfile.postgres ne sera pas utilisé par le docker-compose car il est inutile. Il n’existe qu’à des fins de test pour ce container à l’aide de la commande : `psql -h localhost -p 5432 -U bck_django -d db_bck_django`

## Dockerfile.prod

```yaml
###########
# BUILDER #
###########

# pull official base image
FROM python:3.11.4-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
# installation de gcc nécessaire car certains package python qui utilisent des extensions C
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
# flake8 est une librairie Python qui vérifie si le code suit la convention PEP 8
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/app/

# Ces flags dit à flake8 d'ignorer certains warnings/errors.
#    - E501 pour "line too long."
#    - F401 pour "module imported but unused."
RUN flake8 --ignore=E501,F401 .

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.11.4-slim-buster

# create directory for the app user
RUN mkdir -p /home/app 	

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
```

Un linter est comme un correcteur d’orthographe. Flake8 vérifie que le code Python suit la convention PEP 8.

[Utilisez des linters pour que votre code reste propre](https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable/7187871-utilisez-des-linters-pour-que-votre-code-reste-propre)

*Python wheel* est un format de paquetage binaire préconstruit pour les modules et les bibliothèques Python. Elles sont conçues pour faciliter l'installation et la gestion des paquets Python, en fournissant un format pratique à fichier unique qui peut être téléchargé et installé sans qu'il soit nécessaire de compiler le paquet à partir du code source.

[99% des principaux paquets Python sont maintenant des wheels, ce qui rendra plus rapide l'installation pour les paquets purement Python](https://python.developpez.com/actu/346978/99-pourcent-des-principaux-paquets-Python-sont-maintenant-des-wheels-ce-qui-rendra-plus-rapide-l-installation-pour-les-paquets-purement-Python/)

how to create an app SPA with javascript in frontend and django in backend ?

`pip freeze` permets de voir toutes les dépendances installées.

Pour arrêter runserver : 

`ps auxw | grep runserver`

`kill 7956`

docker

db

backend

api

frontend

certbot

procedure recuperation mdp

# Database

## Players

| Champs | Type |
| --- | --- |
| id |  |
| login |  |
| password |  |
| nickname |  |
| nb_games_2p_played |  |
| nb_games_2p_won |  |
| nb_games_2p_lost |  |
| nb_games_4p_played |  |
| nb_games_4p_won |  |
| nb_games_4p_lost |  |
| fict_score |  |
| Avatar |  |
| status |  |

## 2 players games

| Champs | Type |
| --- | --- |
| id |  |
| player1 |  |
| player2 |  |
| score_player1 |  |
| score_player2 |  |
| score_max |  |
| win_player |  |
| id_tournament |  |
| level |  |
| date |  |

## 4 players games

| Champs | Type |
| --- | --- |
| id |  |
| player1 |  |
| player2 |  |
| player3 |  |
| player4 |  |
| score_player1 |  |
| score_player2 |  |
| score_player3 |  |
| score_player4 |  |
| score_max |  |
| win_player |  |

## Friends

| Champs | Type |
| --- | --- |
| id |  |
| id_player1 | foreignKey |
| id_player2 |  |
| accept |  |

## Tournaments

| Champs | Type |
| --- | --- |
| id |  |
| player1 |  |
| player2 |  |
| player3 |  |
| player4 |  |
| player5 |  |
| player6 |  |
| player7 |  |
| player8 |  |
| nb_players |  |
| title |  |

# Partie obligatoire

## Contraintes minimales du sujet

- [x]  Si vous choisissez d’inclure un backend, il doit être codé en pur Ruby.

<aside>
💡 PEUT ÊTRE **OUTREPASSÉ** PAR LE MODULE FRAMEWORK EN BACKEND

</aside>

[Une introduction à Ruby • Tutoriels • Zeste de Savoir](https://zestedesavoir.com/tutoriels/634/une-introduction-a-ruby/)

- [x]  Le frontend doit être développé en utilisant du Javascript natif (original sans framework ni extensions).

<aside>
💡 PEUT ÊTRE **OUTREPASSÉ** PAR LE MODULE FRONTEND

</aside>

[Créez des pages web dynamiques avec JavaScript](https://openclassrooms.com/fr/courses/1916641-dynamisez-vos-sites-web-avec-javascript)

[Créez des pages web dynamiques avec JavaScript](https://openclassrooms.com/fr/courses/7697016-creez-des-pages-web-dynamiques-avec-javascript)

- [x]  Votre site web doit être une application simple-page. L’utilisateur doit pouvoir utiliser les boutons Précédent et Suivant du navigateur.
- [x]  Votre site web doit être compatible avec la dernière version stable à jour de Google Chrome .
- [x]  L’utilisateur ne doit pas rencontrer d’erreurs non-gérées ou d’avertissements lorsqu’il navigue sur le site web.
- [x]  Tout le projet doit être compilé en lançant une seule ligne de commande qui démarrera un conteneur autonome fourni par Docker. Exemple : docker-compose up --build

## Jeu

- [x]  Les utilisateurs doivent pouvoir participer à une partie de Pong en temps réel contre un autre utilisateur directement sur le site web. Les 2 joueurs vont utiliser le même clavier.

<aside>
💡 PEUT ÊTRE **AMÉLIORÉ** PAR LE MODULE JOUEURS A DISTANCE.

</aside>

- [ ]  Un joueur doit pouvoir jouer contre un autre joueur, mais doit aussi pouvoir organiser un tournoi. Ce tournoi consiste en plusieurs joueurs qui peuvent jouer les uns contre les autres. Vous avez la flexibilité de déterminer comment vous allez implémenter le tournoi, mais il doit clairement indiquer qui joue contre qui et l’ordre des joueurs.
- [ ]  Un système d’inscription est requis : au début d’un tournoi, chaque joueur doit entrer son alias. Les alias seront réinitialisés lorsqu’un nouveau tournoi débute.

<aside>
💡 PEUT ÊTRE **MODIFIÉ** PAR LE MODULE DE GESTION DES UTILISATEURS.

</aside>

- [ ]  Il doit y avoir un système de "matchmaking" : le système de tournoi organise le "matchmaking" des participants, et annonce la prochaine partie.
- [ ]  Tous les joueurs respectent les mêmes règles, incluant une vitesse identique des barres (paddles). Ce pré-requis s’applique également lorsque vous utilisez une IA ; celle-ci doit se déplacer à la même vitesse que le joueur.
- [ ]  Le jeu en soi doit être développé en respectant les mêmes contraintes par défaut que le Frontend (javascript natif sans framework ni extension)

<aside>
💡 PEUT ÊTRE **OUTREPASSÉ** PAR LE MODULE FRONTEND.

</aside>

<aside>
💡 PEUT ÊTRE **OUTREPASSÉ** PAR LE MODULE GRAPHIQUE.

</aside>

## Questions de sécurité

- [ ]  Tout mot de passe stocké dans votre base de données doit être chiffré.
- [ ]  Votre site web doit être protégé contre les injections SQL/XSS.

[Injection SQL](https://fr.wikipedia.org/wiki/Injection_SQL)

- [ ]  Si vous avez un backend ou n’importe quelle autre fonctionnalité, il est obligatoire d’implémenter une connexion HTTPS pour tous les aspects (wss au lieu de ws...).
- [ ]  Vous devez implémenter une form de validation pour les formulaires ou toute entrée utilisateur, que ce soit sur la page de base s’il n’y a pas de backend, ou côté serveur si un backend est utilisé.

# Modules

## Web

### Module majeur : Utiliser un framework en backend

Dans ce module majeur, vous devez utiliser un framework web spécifique pour le développement de votre backend, et ce framework est Django.

[](http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf)

Tutoriel simple pour python

[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

Environnements virtuels en Python

[Django](https://docs.djangoproject.com/en/5.0/intro/)

[Integrating Django with SPA Frontend Frameworks & WebSockets](https://www.squash.io/django-integration-with-spa-frontend-frameworks-and-websockets/)

### Module mineur : Utiliser un framework ou toolkit en frontend

Votre développement frontend doit utiliser Bootstrap toolkit .

### Module mineur : Utiliser une base de données en backend

La base de données désignée pour toutes les instances de base de données dans votre projet est PostgreSQL . Ce choix garantit la cohérence des données et la compatibilité entre tous les composants du projet et peut être une condition préalable pour d’autres modules, tels que le Module Framework backend.

[How to install psql on Mac, Ubuntu, Debian, Windows](https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows/)

Interface en ligne de commande de postgres : psql

[How to use the PostgreSQL Command line to Manage Databases? | Simplified](https://hevodata.com/learn/postgresql-command-line/)

[Installer PostgreSQL et pgAdmin avec Docker sur Windows](https://thomasperrot.medium.com/installer-postgresql-et-pgadmin-avec-docker-sur-windows-ff5d49dadba9)

### Module majeur : Stocker les pointages d’un tournoi dans la Blockchain

Ce module majeur se concentre sur la mise en œuvre d’une fonctionnalité au sein du site Pong pour stocker de manière sécurisée les scores des tournois sur une blockchain. Il est essentiel de préciser que, à des fins de développement et de test, nous utiliserons un environnement de blockchain de test. La blockchain choisie pour cette implémentation est Ethereum , et le langage de programmation utilisé pour le développement de contrats intelligents sera Solidity.

- Intégration Blockchain : L’objectif principal de ce module est d’intégrer de manière transparente la technologie blockchain, spécifiquement Ethereum , dans le site Pong. Cette intégration garantit le stockage sécurisé et immuable des scores de tournois, offrant aux joueurs un enregistrement transparent et inviolable de leurs réalisations de jeu.
- Solidity Contrats intelligents : Pour interagir avec la blockchain, nous développerons des contrats intelligents en Solidity . Ces contrats seront chargés d’enregistrer, de gérer et de récupérer les scores des tournois.
- Tester la Blockchain : Comme mentionné précédemment, une blockchain de test sera utilisée pour fins de développement et de tests. Cela garantit que toutes les fonctionnalités liées à la blockchain sont rigoureusement validées sans aucun risque associé à une blockchain en direct.
- Interopérabilité : Ce module peut avoir des dépendances avec d’autres modules, en particulier le module Framework Backend. L’intégration de la fonctionnalité blockchain pourrait nécessiter des ajustements dans le backend pour permettre les interactions avec la blockchain.

En implémentant ce module, nous visons à améliorer le site de Pong en introduisant un système basé sur la blockchain pour stocker les scores. Les utilisateurs vont bénéficier de cet ajout d’une couche de sécurité et transparence, assurant ainsi l’intégrité de leurs scores. Le module met l’accent sur l’utilisation d’un environnement test de blockchain afin de minimiser les risques associés au développement blockchain.

[Ethereum](https://fr.wikipedia.org/wiki/Ethereum)

[Solidity](https://fr.wikipedia.org/wiki/Solidity)

## Gestion utilisateur

### Module majeur : Gestion utilisateur standard, authentification, utilisateurs en tournois

- Les utilisateurs peuvent s’inscrire au site web de manière sécuritaire.
- Les utilisateurs enregistrés peuvent s’authentifier de manière sécuritaire.
- Les utilisateurs peuvent choisir un nom d’affichage unique pour jouer en tournoi.
- Les utilisateurs peuvent mettre à jour leurs informations.
- Les utilisateurs peuvent téléverser un avatar, mais un avatar par défaut existe si aucun n’est fourni.
- Les utilisateurs peuvent ajouter d’autres utilisateurs comme amis et voir leur statut (en ligne / hors-ligne / en partie).
- Les profils d’utilisateurs affichent des statistiques, comme les victoires et défaites.
- Chaque utilisateur a un Historique des parties incluant les parties 1v1, les dates et autres détails pertinents, accessibles aux utilisateurs authentifiés.

### Module majeur : Implémenter une authentification à distance

Dans ce module majeur, le but est d’implémenter le système d’authentification suivant : OAuth 2.0 authentication with 42 . Les fonctionnalités à inclure sont :

- Intégrer un système d’authentification permettant aux utilisateurs d’accéder au site en toute sécurité.
- Obtenir les informations et permissions nécessaires de l’autorité afin d’activer une authentification sécuritaire.
- Mettez en place des flux de connexion et d’autorisation conviviaux pour les utilisateurs, conformes aux meilleures pratiques et normes de sécurité.
- Assurez-vous de l’échange sécurisé des jetons (tokens) d’authentification et des informations de l’utilisateur entre l’application web et le fournisseur d’authentification.

Ce module majeur vise à obtenir une authentification distante de l’utilisateur, procurant à celui-ci une façon simple et sécuritaire d’accéder à l’application web.

[OAuth](https://fr.wikipedia.org/wiki/OAuth)

### Gameplay et expérience utilisateur

### Module majeur : Joueurs à distance

Il est possible d’avoir 2 joueurs distants. Chaque joueur est sur un ordinateurs différent, accédant au même site web et jouant la même partie de Pong.

### Module majeur : Multijoueurs (plus de 2 dans la même partie)

Il est possible d’avoir plus de deux joueurs. Chaque joueur doit avoir ses propres contrôles (donc, le module précédent "Joueurs à distance" est hautement recommandé). Il vous appartient de définir comment on peut jouer à 3, 4, 5, 6 ... joueurs. En plus du jeu classique à 2 joueurs, vous pouvez choisir un nombre de joueurs unique, supérieur à 2, pour ce module multijoueur. Par exemple, 4 joueurs peuvent jouer sur un plateau carré, chaque joueur possédant un côté unique du carré.

### Module majeur : Ajout d’un second jeu avec historique utilisateur et "match-making"

Dans ce module majeur, l’objectif est d’introduire un nouveau jeu, distinct de Pong, et d’y incorporer des fonctionnalités telles que l’historique de l’utilisateur et le "matchmaking".

- Développez un nouveau jeu pour diversifier l’offre de la plateforme et divertir les utilisateurs.
- Implémentez une gestion de l’historique de l’utilisateur pour enregistrer et afficher les statistiques individuelles du joueur.
- Créez un système de "matchmaking" pour permettre aux utilisateurs de trouver des adversaire afin de disputer des parties équitables et équilibrées.
- Assurez vous que les données sur l’historique des parties et le "matchmaking" sont stockées de manière sécuritaire et demeurent à jour.
- Optimisez la performance et la réactivité du nouveau jeu afin de fournir une expérience utilisateur agréable. Mettez à jour et maintenez régulièrement le jeu afin de réparer les bogues, ajouter de nouvelles fonctionnalités et améliorer la jouabilité.

Ce module majeur vise à développer votre plateforme en introduisant un nouveau jeu, améliorant ainsi l’engagement de l’utilisateur avec l’historique des parties, et facilitant le "matchmaking" pour une expérience utilisateur agréable.

### Module mineur : Option de personnalisation du jeu

Dans ce module mineur, le but est de fournir des options de personnalisation pour tous les jeux disponibles sur votre plateforme. Les objectifs et fonctionnalités clés incluent :

- Offrir des fonctionnalités de personnalisation, comme des bonus (power-ups), attaques, différentes cartes, qui améliorent l’expérience de jeu.
- Permettre aux utilisasteurs de choisir une version du jeu par défaut avec fonctionnalités de base s’ils préfèrent une expérience plus simple.
- Assurez-vous que les options de personnalisation sont disponibles et s’appliquent à tous les jeux offerts sur la plateforme.
- Implémentez des menus de réglages conviviaux ou des interfaces pour ajuster les paramètres du jeu.
- Conservez une constance dans les fonctionnalités de personnalisation pour tous les jeux de la plateforme afin de permettre une expérience utilisateur unifiée.

Ce module vise à donner aux utilisateurs la flexibilité d’ajuster leur expérience de jeu pour tous les jeux disponibles, en fournissant une variété d’options de personnalisation, tout en offrant aussi une version par défaut, simple, pour les utilisateurs qui désirent ce type d’expérience.

### Module majeur : Clavardage en direct (live chat)

Vous devez créer un système de clavardage (chat) pour vos utilisateurs dans ce module :

- L’utilisateur doit pouvoir envoyer des messages directs à d’autres utilisateurs.
- L’utilisateur doit pouvoir en bloquer d’autres. Ainsi, l’utilisateur ne verra plus les messages provenant du compte qu’il a bloqué.
- L’utilisateur doit pouvoir inviter d’autres utilisateurs à jouer une partie de Pong à partir de l’interface de Chat.
- Le système de tournoi doit pouvoir avertir les utilisateurs qui sont attendus pour la prochaine partie.
- L’utilisateur doit pouvoir accéder aux profiles d’autres joueurs à partir de l’interface de Chat.

## IA-Algo

### Module majeur : Implémenter un adversaire contrôlé par IA

Dans ce module majeur, l’objectif est d’incorporer un joueur contrôlé par Intelligence Artificielle (IA) dans le jeu. Notamment, l’utilisation d’un A* algorithm n’est pas permise pour réaliser cette tâche. Les buts et fonctionnalités clés incluent :

- Développez un adversaire IA qui fournissent un défi et une expérience engageante aux utilisateurs.
- L’IA doit reproduire un comportement humain, signifiant que dans l’implémentation de votre IA, vous devez simuler les entrées au clavier. La contrainte ici est que l’IA peut seulement rafraîchir sa vue du jeu une fois par seconde, lui demandant donc d’anticiper les rebonds et autres actions.

<aside>
💡 L’IA doit pouvoir utiliser des bonus (power-ups) si vous avez choisi d’implémenter le Module Option de personnalisation de jeu.

</aside>

- Implémentez la logique de l’IA et le processus de décision qui permettent à votre IA de faire des mouvements et décisions intelligentes et stratégiques.
- Explorer des algorithmes alternatifs et techniques afin de créer une IA efficace sans utiliser A*.
- Assurer vous que l’IA s’adapte aux différents scénarios de gameplay et interactions utilisateurs.

Ce module majeur vise à améliorer le jeu en introduisant un adversaire contrôlé par Intelligence Artificielle qui ajoute des aspects excitants et compétitifs, tout en n’utilisant pas l’Algorithme A*.

### Module mineur : Panneaux d’affichage (dashboards) d’utilisateurs et statistiques des parties

Dans ce module mineur, le but est d’introduire des tableaux de bords qui affichent des statistiques individuelles pour les utilisateurs et sessions de jeu. Les fonctions-clés et objectifs incluent :

- Créer des tableaux de bords conviviaux qui fournissent aux utilisateurs des informations sur leurs propres statistiques.
- Développez un tableau de bord séparé pour les sessions de jeux, montrant des statistiques détaillées, des données sur les résultats et l’historique pour chaque match.
- Assurez-vous que les tableaux de bords offrent une interface informative et intuitive pour suivre et analyser les données.
- Implémentez différentes façons de visualiser les données, comme des chartes ou des graphiques, afin de présenter les statistiques de manière agréables.
- Permettez aux utilisateurs d’accéder et explorer leur propre historique de jeu et métriques de performance.
- Vous êtes libre d’ajouter n’importe quel métrique que vous jugez pertinent.

Ce module mineur vise à permettre aux utilisateurs de faire un suivi sur leurs statistiques et performances. À travers des tableaux de bords conviviaux et bien conçus, l’utilisateur peut suivre leur historique de jeu sur la plateforme et avoir une vue détaillée de leur expérience.

## Cybersécurité

### Module majeur : Mettez en place un pare-feu d’application Web (WAF) ou ModSecurity avec une configuration renforcée et utilisez HashiCorp Vault pour la gestion des secrets

Mise en place d’un pare-feu d’application Web (WAF) ou ModSecurity avec une configuration renforcée et utilisez HashiCorp Vault pour la gestion des secrets. Dans ce module majeur, l’objectif est d’améliorer l’infrastructure sécurité du projet en implémentant plusieurs composantes clés. Celles-ci incluent :

- Configurer et déployer un pare-feu d’application web (WAF) et ModSecurity avec une configuration stricte et sécuritaire afin de protéger contre les attaques potentielles.
- Intégrer HashiCorp Valut pour gérer et stocker sécuritairement toute information sensible, comme les clés API, les informations d’authentification et les variables d’environnement, s’assurant ainsi que les secrets sont correctement encryptés et isolés.

Ce module majeur vise a renforcer l’infrastructure de sécurité du projet en implémentant des mesures robustes, incluant WAF/ModSecurity pour la protection de l’application web et HashiCorp Vault pour la gestion des secrets afin d’assurer un environnement sécuritaire

[Web application firewall](https://fr.wikipedia.org/wiki/Web_application_firewall)

[Modsecurity](https://fr.wikipedia.org/wiki/Modsecurity)

[HashiCorp](https://en.wikipedia.org/wiki/HashiCorp)

### Module mineur : Options de conformité au RGPD avec anonymisation des utilisateurs, gestion des données locales et suppression de comptes

Dans ce module mineur, le but est d’introduire les options de conformité au RGPD pour permettre aux utilisateurs d’exercer leur droit en matière de protection des données. Les fonctionnalités et objectifs clés incluent :

- Implémenter des fonctionnalités qui se conforment au RGPD, permettant aux utilisateurs de demander l’anonymisation de leurs données personnelles, s’assurant ainsi que leur identité et informations personnelles et sensibles sont protégées.
- Fournir des outils aux utilisateurs pour gérer leurs données locales, incluant la possibilité de voir, modifier ou supprimer leurs informations personnelles stockées dans le système.
- Offrir un processus simplifié permettant aux utilisateurs de demander la suppression permanente de leur compte, y compris toutes les données associées, garantissant la conformité avec les réglementations de protection des données.
- Maintenir une communication claire et transparente avec les utilisateurs concernant leur droit à la protection des données avec des options facilement accessibles pour exercer ce droit.

Ce module mineur vise à améliorer la protection des données et la vie privée de l’utilisateur en offrant la conformité au RGPD qui permet aux utilisateurs de contrôler leurs informations personnelles et d’exercer leur droit à la vie privée et la protection des données à l’intérieur du système.

Si vous n’êtes pas familier avec le Règlement Général sur la Protection des Données (RGPD), il est essentiel de comprendre ses principes et implications, spécialement concernant la gestion des données de l’utilisateur et sa vie privée. Le RGPD est
une réglementation qui vise à protéger la vie privée et les données personnelles des individus sous l’Union Européenne (UE) et l’Espace Économique Européen (EEE). Il établit des règles strictes et des lignes directrices pour les organisations sur la manière dont elles doivent traiter et gérer les données personnelles.

Pour mieux comprendre le RGPD et ses exigences, il est fortement recommandé de visiter le site officiel de la Commission européenne sur la protection des données 1. Ce site fournit des informations complètes sur le RGPD, y compris ses principes, ses objectifs et les droits des utilisateurs. Il propose également des ressources supplémentaires pour approfondir le sujet et garantir la conformité à la réglementation.

Si vous n’êtes pas familier avec le RGPD, prenez le temps de visiter le lien fourni et de vous familiariser avec la réglementation avant de poursuivre ce projet.

[Data protection in the EU](https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_en)

### Module majeur : Implémenter l’authentification à 2 facteurs (2FA) et JWT (JSON Web Tokens)

Dans ce module majeur, le but est d’améliorer la sécurité et l’authentification de l’utilisateur en introduisant l’authentification à 2 facteurs (2FA) et d’utiliser JSON Web Tokens(JWT). Les fonctionnalités et objectifs incluent :

- Implémenter l’authentification à 2 facteurs (2FA) comme une couche de sécurité additionnelle pour les comptes utilisateurs, requérant à ceux-ci de fournir une seconde méthode de vérification, comme un code à usage unique, en plus de leur mot de passe.
- Utiliser JSON Web Tokens (JWT) comme méthode d’authentification et d’autorisation, assurant ainsi que les sessions utilisateur et l’accès aux ressources sont gérés de manière sécurisée.
- Fournir une interface de configuration conviviale pour l’activation du 2FA, avec des options comme un code SMS, application d’authentification, ou une vérification par courriel.
- S’assurer que les jetons JWT sont émis et validés de manière sécurisée afin de prévenir les accès non-autorisés à des comptes utilisateurs et aux données sensibles.

Ce module majeur vise à renforcer la sécurité du compte utilisateur en offrant l’authentification à 2 facteurs (2FA) et d’améliorer l’authentification et l’autorisation grâce à l’utilisation des jetons JSON Web Tokens (JWT

## Devops

### Module majeur : Configuration de l’infrastructure pour la gestion des journaux (logs)

Configuration de l’infrastructure avec ELK (Elasticsearch, Logstash, Kibana) pour la gestion des journaux (logs).
Dans ce module majeur, l’objectif est d’établir une infrastructure robuste pour la gestion et l’analyse des journaux en utilisant la pile ELK (Elasticsearch, Logstash, Kibana). Les principales caractéristiques et objectifs comprennent :

- Déployer Elasticsearch pour stocker et indexer efficacement les données de journal, les rendant facilement consultables et accessibles.
- Configurer Logstash pour collecter, traiter et transformer les données de journal provenant de différentes sources et les envoyer vers Elasticsearch.
- Mettre en place Kibana pour la visualisation des données de journal, la création de tableaux de bord et la génération d’informations à partir des événements de journal.
- Définir des politiques de rétention et d’archivage des données pour gérer efficacement le stockage des données de journal.
- Mettre en place des mesures de sécurité pour protéger les données de journal et l’accès aux composants de la pile ELK .

Ce module majeur vise à mettre en place un système de gestion et d’analyse des journaux puissant en utilisant la pile ELK, permettant un dépannage, une surveillance et des informations efficaces sur le fonctionnement et les performances
du système.

[Elasticsearch](https://fr.wikipedia.org/wiki/Elasticsearch)

[Kibana](https://fr.wikipedia.org/wiki/Kibana)

[Logstash](https://fr.wikipedia.org/wiki/Logstash)

### Module mineur : Système de monitoring

Dans ce module mineur, l’objectif est de mettre en place un système de monitoring utilisant Prometheus and Grafana . Les objectifs du module incluent :

- Déployer Prometheus en tant que trousse d’outils de surveillance et d’alerte pour collecter des métriques et surveiller la santé et les performances de divers composants du système.
- Configurer des exportateurs de données et des intégrations pour capturer des métriques à partir de différents services, bases de données et composants d’infrastructure.
- Créer des tableaux de bord personnalisés et des visualisations à l’aide de Grafana pour fournir des informations en temps réel sur les métriques et les performances du système.
- Configurer des règles d’alerte dans Prometheus pour détecter et réagir de manière proactive aux problèmes critiques et aux anomalies.
- Veiller à des stratégies appropriées de rétention et de stockage des données pour les données historiques des métriques.
- Mettre en place des mécanismes d’authentification sécurisés et de contrôle d’accès pour Grafana afin de protéger les données de surveillance sensibles.

Ce module mineur vise à établir une infrastructure de surveillance robuste en utilisant Prometheus et Grafana , permettant une visibilité en temps réel sur les métriques du système et la détection proactive des problèmes pour améliorer les performances et la fiabilité du système.

[](https://hub.docker.com/r/grafana/grafana)

Image Docker pour Grafana

### Module majeur : Design du backend comme Microservices

Dans ce module majeur, le but est de concevoir le backend du system en utilisant l’approche microservices. Cela inclue :

- Diviser le backend en de plus petits microservices peu couplés, chacun étant responsable de fonctions ou fonctionnalités spécifiques.
- Définir des limites claires et des interfaces entre les microservices pour permettre un développement, un déploiement et une mise à l’échelle indépendants.
- Mettre en place des mécanismes de communication entre les microservices, tels que des API RESTful ou des files de messages, pour faciliter l’échange de données et la coordination.
- Veiller à ce que chaque microservice soit responsable d’une tâche ou d’une capacité métier unique et bien définie, ce qui favorise la maintenabilité et la scalabilité.

Ce module majeur vise à améliorer l’architecture du système en adoptant une approche de conception basée sur les microservices, ce qui permet une plus grande flexibilité, évolutivité et maintenabilité des composants du backend.

[Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

[Deploying a Django Application with Docker, Nginx, and Certbot](https://medium.com/@akshatgadodia/deploying-a-django-application-with-docker-nginx-and-certbot-eaf576463f19)

[Qu'est-ce qu'une API RESTful ? – L'API RESTful expliquée – AWS](https://aws.amazon.com/fr/what-is/restful-api/)

## Graphiques

### Module majeur : Utilisation de techniques avancées 3D

Ce module majeur, appelé "Graphiques", se concentre sur l’amélioration de l’aspect visuel du jeu de Pong. Il introduit l’utilisation de techniques 3D avancées pour créer une expérience de jeu plus immersive. Spécifiquement, le jeu de Pong sera développé utilisant ThreeJS/WebGL pour atteindre le but désiré.

- Graphiques 3D avancés : Le but premier de ce module est d’implémenter des techniques 3D avancées afin d’élever la qualité visuelle du jeu de Pong. En utilisant ThreeJS/WebGL , nous visons à créer des effets visuels époustouflants qui plongent les joueurs dans l’environnement de jeu.
- Jouabilité immersive : L’ajout de techniques 3D avancées améliore l’expérience de jouabilité en procurant à l’utilisateur une expérience de jeu et un visuel captivants.
- Intégration technologique : La technologie choisie pour ce module est ThreeJS/WebGL. Ces outils seront utilisés pour créer les graphiques 3D, assurant la compatibilité et des performances optimales.

Ce module majeur vise à révolutionner les éléments visuels du jeu Pong en introduisant des techniques 3D avancées. Grâce à l’utilisation de ThreeJS/WebGL, nous aspirons à offrir aux joueurs une expérience de jeu immersive et visuellement époustouflante.

## Accessibilité

### Module mineur : Support sur tous types d’appareils

Dans ce module, le focus principal est de s’assurer que votre site web fonctionne sans problèmes sur tout types d’appareils. Cela inclue :

- Assurez-vous que le site web est réactif, s’adaptant à différentes tailles d’écran et orientations, garantissant une expérience utilisateur cohérente sur les ordinateurs de bureau, les ordinateurs portables, les tablettes et les smartphones.
- Assurez-vous que les utilisateurs peuvent naviguer et interagir facilement avec le site web en utilisant différents modes de saisie, tels que les écrans tactiles, les claviers et les souris, en fonction de l’appareil qu’ils utilisent.

Ce module vise a fournir une expérience constante et conviviale sur tout type d’appareils, en maximisant l’accessibilité et la satisfaction des utilisateurs.

### Module mineur : Étendre la compatibilité des navigateurs web

Dans ce module mineur, l’objectif est d’améliorer la compatibilité de l’application web en ajoutant la compatibilité pour un navigateur web supplémentaire. Cela inclue :

- Étendre le support navigateur afin d’inclure un navigateur supplémentaire, s’assurant ainsi que les utilisateurs peuvent accéder l’application web sans problèmes.
- Effectuer des tests approfondis et des optimisations pour s’assurer que l’application web fonctionne correctement et s’affiche correctement dans le nouveau navigateur pris en charge.
- Gérer et régler tout problème de compatibilité ou de rendu qui pourrait survenir dans le nouveau navigateur.
- S’assurer d’une expérience utilisateur constante sur tous les navigateurs supportés, conservant l’usage et les fonctionnalités.

Ce module mineur vise à élargir l’accessibilité de l’application web en supportant un navigateur additionnel, offrant ainsi plus de choix d’usage de l’application par l’utilisateur.

[Can I use... Support tables for HTML5, CSS3, etc](https://caniuse.com/)

### Module mineur : Support de multiple langues

Dans ce module mineur, l’objectif est de s’assurer que votre site web supporte plusieurs langues afin de s’adresser à une clientèle plus large. Cela inclue :

- Implémenter le support pour un minimum de 3 langues sur le site web pour pouvoir rejoindre une audience plus large.
- Fournir une sélection de langues qui permettent de choisir et changer facilement leur langue d’affichage sur le site web.
- Traduire l’essentiel du contenu du site web, comme les menus, en-têtes et informations importantes.
- S’assurer que les utilisateurs peuvent naviguer le site web sans problèmes, peu importe la langue choisie.
- Envisagez d’utiliser des packs de langues ou des bibliothèques de localisation pour simplifier le processus de traduction et maintenir la cohérence entre les différentes langues.
- Permettre aux utilisateurs de choisir leur langue préférée par défaut pour les visites subséquentes sur le site web.

Ce module mineur vise à améliorer l’accessibilité et l’inclusivité au site web en offrant le contenu en plusieurs langues, le rendant ainsi plus convivial pour une clientèle internationale.

### Module mineur : Ajout de l’accessibilité pour les utilisateurs malvoyants

Dans ce module mineur, le but est de rendre votre site web plus accessible pour les utilisateurs malvoyants. Cela inclue :

- Prise en charge des lecteurs d’écran et des technologies d’assistance.
- Texte alternatif clair et descriptif pour les images.
- Schéma de couleurs à fort contraste pour une meilleure lisibilité.
- Navigation au clavier et gestion de la mise au point.
- Options pour ajuster la taille du texte.
- Mises à jour régulières pour respecter les normes d’accessibilité.

Ce module vise à améliorer l’utilisabilité du site web pour les individus avec problèmes de vision et des standards d’accessibilité.

### Module mineur : Intégration du rendu côté serveur (SSR)

Dans ce module mineur, le focus est sur l’intégration du rendu côté serveur (SSR) afin d’améliorer la performance et l’expérience utilisateur de votre site web. Cela inclue :

- Implémenter SSR pour améliorer les temps de chargement et la performance.
- S’assurer que le contenu est pré-rendu sur le serveur et livré au navigateur de l’utilisateur pour des chargements de pages plus rapides.
- Optimiser le référencement (SEO) en fournissant aux moteurs de recherche du contenu HTML pré-rendu.
- Maintenir une expérience utilisateur cohérente tout en bénéficiant des avantages du rendu côté serveur (SSR).

Ce module vise à améliorer les performances du site web et le référencement en intégrant le rendu côté serveur pour des chargements de page plus rapides et une meilleure expérience utilisateur.

## Orienté objet

### Module majeur : Remplacer le Pong de base par un Pong côté serveur et implémentation d’une API.

Dans ce module majeur, le but est de remplacer le jeu de Pong de base par un jeu de Pong côté serveur, avec la mise en place d’une API. Cela inclue :

- Développer la logique côté serveur pour le jeu Pong afin de gérer le gameplay, le mouvement de la balle, le comptage des points et les interactions des joueurs.
- Créer une API qui expose les ressources nécessaires et les points d’accès pour interagir avec le jeu Pong, permettant une utilisation partielle du jeu via l’interface en ligne de commande (CLI) et l’interface web.
- Concevoir et mettre en place les points d’accès de l’API pour prendre en charge l’initialisation du jeu, le contrôle des joueurs et les mises à jour de l’état du jeu.
- Assurez-vous que le jeu Pong côté serveur est réactif, offrant une expérience de jeu engageante et agréable.
- Intégrez le jeu Pong côté serveur avec l’application web, permettant aux utilisateurs de jouer au jeu directement sur le site web.

Ce module majeur vise à améliorer le jeu Pong en le migrant côté serveur, en permettant une interaction à la fois via une interface web et une interface en ligne de commande (CLI), tout en offrant une API pour un accès facile aux ressources et aux fonctionnalités du jeu.

### Module majeur : Activation du gameplay via ligne de commande (CLI) contre les utilisateurs Web avec intégration API.

Dans ce module majeur, le but est de développer une interface en ligne de commande (CLI) qui permettent aux utilisateurs de jouer à Pong contre des joueurs utilisant la version web du jeu. La CLI devrait se connecter de manière transparente à l’application web, permettant aux utilisateurs CLI de se joindre et d’interagir aux joueurs web. Les fonctionnalités incluent :

- Créez une application CLI robuste qui reproduit l’expérience de jeu Pong disponible sur le site web, offrant aux utilisateurs de la CLI la possibilité d’initier et de participer à des parties de Pong.
- Utilisez l’API pour établir une communication entre la CLI et l’application web, permettant aux utilisateurs de la CLI de se connecter au site et d’interagir avec les joueurs web.
- Développez un mécanisme d’authentification des utilisateurs au sein de la CLI, permettant aux utilisateurs de la CLI de se connecter de manière sécurisée à l’application web.
- Mettez en place une synchronisation en temps réel entre la CLI et les utilisateurs web, garantissant que les interactions de jeu sont fluides et cohérentes.
- Permettez aux utilisateurs de la CLI de rejoindre et de créer des parties de Pong avec les joueurs web, facilitant le jeu interplateforme.
- Fournissez une documentation complète et des conseils sur la manière d’utiliser efficacement la CLI pour des parties de Pong contre des utilisateurs web.

Ce module majeur vise à améliorer l’expérience du jeu de Pong en créant une CLI qui offre un environnement transparent, unifié et interactif de jouabilité.

# My ft_transcendance project

- [ ]  Si vous choisissez d’inclure un backend, il doit être codé en pur Ruby. (FX)
- [ ]  Le frontend doit être développé en utilisant du Javascript natif (original sans framework ni extensions). (Killian)
- [ ]  Votre site web doit être une application simple-page. L’utilisateur doit pouvoir utiliser les boutons Précédent et Suivant du navigateur.
- [ ]  Votre site web doit être compatible avec la dernière version stable à jour de Google Chrome .
- [x]  L’utilisateur ne doit pas rencontrer d’erreurs non-gérées ou d’avertissements lorsqu’il navigue sur le site web.
- [x]  Tout le projet doit être compilé en lançant une seule ligne de commande qui démarrera un conteneur autonome fourni par Docker. Exemple : docker-compose up --build (FX)

## Jeu

- [x]  Les utilisateurs doivent pouvoir participer à une partie de Pong en temps réel contre un autre utilisateur directement sur le site web. Les 2 joueurs vont utiliser le même clavier. (Benoit)
- [x]  Un joueur doit pouvoir jouer contre un autre joueur, mais doit aussi pouvoir organiser un tournoi. Ce tournoi consiste en plusieurs joueurs qui peuvent jouer les uns contre les autres. Vous avez la flexibilité de déterminer comment vous allez implémenter le tournoi, mais il doit clairement indiquer qui joue contre qui et l’ordre des joueurs. (Killian et PH)
- [x]  Un système d’inscription est requis : au début d’un tournoi, chaque joueur doit entrer son alias. Les alias seront réinitialisés lorsqu’un nouveau tournoi débute. (Killian et PH)
- [x]  Il doit y avoir un système de "matchmaking" : le système de tournoi organise le "matchmaking" des participants, et annonce la prochaine partie. (Killian et PH)
- [x]  Tous les joueurs respectent les mêmes règles, incluant une vitesse identique des barres (paddles). Ce pré-requis s’applique également lorsque vous utilisez une IA ; celle-ci doit se déplacer à la même vitesse que le joueur.
- [x]  Le jeu en soi doit être développé en respectant les mêmes contraintes par défaut que le Frontend (javascript natif sans framework ni extension)

Web

- [x]  Module majeur : Utiliser un framework en backend (FX)
- [x]  Module mineur : Utiliser un framework ou toolkit en frontend (Killian)
- [x]  Module mineur : Utiliser une base de données en backend (FX)
- [ ]  Module majeur : Stocker les pointages dʼun tournoi dans la Blockchain

Gestion utilisateur

- [x]  Module majeur : Gestion utilisateur standard, authentification, utilisateurs en tournois (Benoit PH)
- [ ]  Module majeur : Implémenter une authentification à distance
- [x]  Module majeur : Joueurs à distance (PH Killian)
- [x]  Module majeur : Multijoueurs (plus de 2 dans la même partie) (Killian et PH)
- [ ]  Module majeur : Ajout dʼun second jeu avec historique utilisateur et "match-making"
- [ ]  Module mineur : Option de personnalisation du jeu
- [ ]  Module majeur : Clavardage en direct (live chat)

IA Algo

- [x]  Module majeur : Implémenter un adversaire contrôlé par IA (Benoit et FX)
- [ ]  Module mineur : Panneaux dʼaffichage (dashboards) dʼutilisateurs et statistiques des parties

Cybersécurité

- [ ]  Module majeur : Mettez en place un pare-feu dʼapplication Web (WAF) ou ModSecurity avec une configuration renforcée et utilisez HashiCorp Vault pour la gestion des secrets
- [ ]  Module mineur : Options de conformité au RGPD avec anonymisation des utilisateurs, gestion des données locales et suppression de comptes
- [ ]  Module majeur : Implémenter lʼauthentification à 2 facteurs (2FA et JWT JSON Web Tokens)

Devops

- [ ]  Module majeur : Configuration de lʼinfrastructure pour la gestion des journaux (logs)
- [ ]  Module mineur : Système de monitoring
- [x]  Module majeur : Design du backend comme Microservices (FX)

Graphiques

- [ ]  Module majeur : Utilisation de techniques avancées 3D

Accessibilité

- [ ]  Module mineur : Support sur tous types dʼappareils
- [ ]  Module mineur : Étendre la compatibilité des navigateurs web
- [ ]  Module mineur : Support de multiple langues
- [ ]  Module mineur : Ajout de lʼaccessibilité pour les utilisateurs malvoyants
- [ ]  Module mineur : Intégration du rendu côté serveur (SSR)

Orienté objet

- [ ]  Module majeur : Remplacer le Pong de base par un Pong côté serveur et implémentation dʼune API.
- [ ]  Module majeur : Activation du gameplay via ligne de commande (CLI) contre les utilisateurs Web avec intégration API.

# Frontend

[Environment Variables in JavaScript: process.env](https://dmitripavlutin.com/environment-variables-javascript/)

[https://www.youtube.com/watch?v=6BozpmSjk-Y](https://www.youtube.com/watch?v=6BozpmSjk-Y)

## La logique du front :

Lorsque l’utilisateur se connecte à localhost:7890/, il charge la page index.html qui execute le script router.js

router.js :

```jsx
// Importe la View de chaque page
import renderFourPlayers from "../views/viewFourPlayers.js"
import renderFourOnline from "../views/viewFourOnline.js"
import renderFriends from "../views/viewFriends.js"
import renderLogin from "../views/viewLogin.js"
import renderProfile from "../views/viewProfile.js"
import renderTournament from "../views/viewTournament.js"
import renderTwoPlayers from "../views/viewTwoPlayers.js"
import renderTwoOnline from "../views/viewTwoOnline.js"
import renderGameHistory from "../views/ViewGameHistory.js"

// Importe le script de chaque page qui gere le load et listener
import handleFriends from "./friends.js"
import handleLogin from "./login.js"
import handleProfile from "./profile.js"
import handleTournament from "../games/tournament.js"
import handleTournamentOnline from "../games/tournamentOnline.js"
import handleTournamentRoom from "../games/tournamentRoom.js"
import handleTwoPlayers from "../games/pong2players.js"
import handleFourPlayers from "../games/pong4players.js"
import handleTwoPlayersOnline from "../games/pong2playersonline.js"
import handleFourPlayersOnline from "../games/pong4playersonline.js"
import handleGameHistory from "./gamehistory.js"

// Cas particulier pour index
import handleIndex from "./index.js"

/**
 * Routes object
 * Contains all the pages of the website
 * Each page has a title, a path, a view, a load function and a listener function
 * The title is the title of the page
 * The path is the path of the page
 * The view is the HTML content of the page
 * The load function is the function that checks if the user can access the page
 * The listener function is the function that attaches event listeners to the page
*/
const routes = {
	"index": {
		title: "Main",
		path: "/",
		view: handleIndex.renderIndex,
		load: handleIndex.loadIndex,
		listener: handleIndex.listenerIndex
	},
	"friends": {
		title: "Amis",
		path: "/friends/",
		view: renderFriends,
		load: handleFriends.loadFriends,
		listener: handleFriends.listenerFriends
	},
	"login": {
		title: "Login",
		path: "/login/",
		view: renderLogin,
		load: handleLogin.loadLogin,
		listener: handleLogin.listenerLogin
	},
	"profile": {
		title: "Profile",
		path: "/profile/",
		view: renderProfile,
		load: handleProfile.loadProfile,
		listener: handleProfile.listenerProfile
	},
	"tournament": {
		title: "Tournoi Local",
		path: "/tournament/",
		view: renderTournament.renderTournament,
		load: handleTournament.loadTournament,
		listener: handleTournament.listenerTournament
	},
	"tournament_online": {
		title: "Tournoi en Ligne",
		path: "/tournamentOnline/",
		view: renderTournament.renderTournamentOnline,
		load: handleTournamentOnline.loadTournamentOnline,
		listener: handleTournamentOnline.listenerTournamentOnline
	},
	"tournament_online_room": {
		title: "TournamentRoom",
		path: "/tournamentRoom/",
		view: renderTournament.renderTournamentRoom,
		load: handleTournamentRoom.loadTournamentRoom,
		listener: handleTournamentRoom.listenerTournamentRoom
	},
	"twoplayers": {
		title: "2 Joueurs Local",
		path: "/twoplayers/",
		view: renderTwoPlayers,
		load: handleTwoPlayers.loadTwoPlayers,
		listener: handleTwoPlayers.listenerTwoPlayers
	},
	"fourplayers": {
		title: "4 Joueurs Local",
		path: "/fourplayers/",
		view: renderFourPlayers,
		load: handleFourPlayers.loadFourPlayers,
		listener: handleFourPlayers.listenerFourPlayers
	},
	"twoplayersonline": {
		title: "2 Joueurs en Ligne",
		path: "/twoplayersonline/",
		view: renderTwoOnline,
		load: handleTwoPlayersOnline.loadTwoPlayersOnline,
		listener: handleTwoPlayersOnline.listenerTwoPlayersOnline
	},
	"gamehistory": {
		title: "Historique des parties",
		path: "/gamehistory/",
		view: renderGameHistory,
		load: handleGameHistory.loadGameHistory,
		listener: handleGameHistory.listenerGameHistory
	},
	"fourplayersonline": {
		title: "4 Joueurs en Ligne",
		path: "/fourplayersonline/",
		view: renderFourOnline,
		load: handleFourPlayersOnline.loadFourPlayersOnline,
		listener: handleFourPlayersOnline.listenerFourPlayersOnline
	},
};

/**
 * Logout handler function
 * Send a PATCH request to the server to logout the user
 * If the response status is 200, the user is successfully logged out and redirected to the login page
*/
async function handleLogout() {

	const csrftoken = document.cookie.split("; ").find((row) => row.startsWith("csrftoken"))?.split("=")[1];

	const init = {
		method: "PATCH",
		headers: { 'X-CSRFToken': csrftoken, },
	}

	try {

		let hostnameport = "http://" + window.location.host

		const response = await fetch(hostnameport + '/api/logout/', init);

		if (response.status === 200) {
			console.log("user successfull logged out");

			sessionStorage.clear();
			router("login");
		}
	} catch (e) {
		console.error(e);
	}
};

/**
 * Router function
 * @param {string} value - The value of the button that was clicked
 * Get the page from the routes object, if it exists
 * Call the load function of the page
 	* If the load function returns 1 (the user can access it), render the view of the page
*/
export default async function router(value) {

	var page = routes[value];

	if (!page)
		return;

	if (await page.load() === 1) {
		document.getElementById("main__content").innerHTML = page.view();

		document.getElementById("navbar__btn--text").textContent = sessionStorage.getItem("username") ? sessionStorage.getItem("username") : "user";
		document.getElementById("navbar__btn--avatar").src = sessionStorage.getItem("avatar") ? sessionStorage.getItem("avatar") : "/frontend/img/person-circle-Bootstrap.svg";
		document.getElementById("navbar__btn--avatar").alt = sessionStorage.getItem("avatar") ? sessionStorage.getItem("username") + " avatar" : "temp avatar";

		document.title = page.title;

		window.history.pushState({}, "", page.path);

		page.listener();
	}
	else
		router("login");
};

/**
 * Event listener for popstate event

*/
window.addEventListener("popstate", async (e) => {
	e.preventDefault();

	// Get the current url, remove all '/' and if the url is null assign it to 'index'
	let url = window.location.pathname.replaceAll("/", "");
	if (url === "")
		url = "index";

	var page = routes[url];

	if (!page)
		return;

	if (await page.load() === 1) {
		document.getElementById("main__content").innerHTML = page.view();

		document.getElementById("navbar__btn--text").textContent = sessionStorage.getItem("username") ? sessionStorage.getItem("username") : "user";
		document.getElementById("navbar__btn--avatar").src = sessionStorage.getItem("avatar") ? sessionStorage.getItem("avatar") : "/frontend/img/person-circle-Bootstrap.svg";
		document.getElementById("navbar__btn--avatar").alt = sessionStorage.getItem("avatar") ? sessionStorage.getItem("username") + " avatar" : "temp avatar";

		document.title = page.title;

		page.listener();
	}
	else
		loadIndex();
});

/**
 * Event listener for window.onload event
 * Load the page that the user is currently on
 * If the user is logged in, load the page that the user is currently on
 * If the user is not logged in, redirect to the login page
*/
window.onload = async function() {

	const currentPath = window.location.pathname;
	for (const route in routes) {
		if (routes[route].path === currentPath) {
			if (await routes[route].load() === 1) {
				document.getElementById('main__content').innerHTML = routes[route].view();  // Render the HTML content for the page

				document.getElementById("navbar__btn--text").textContent = sessionStorage.getItem("username") ? sessionStorage.getItem("username") : "user";
				document.getElementById("navbar__btn--avatar").src = sessionStorage.getItem("avatar") ? sessionStorage.getItem("avatar") : "/frontend/img/person-circle-Bootstrap.svg";
				document.getElementById("navbar__btn--avatar").alt = sessionStorage.getItem("avatar") ? sessionStorage.getItem("username") + " avatar" : "temp avatar";

				document.title = routes[route].title;

				routes[route].listener();  // Attach event listeners
			}
			else
				router("login");
			break;
		}
	}
};

/**
 * Load index function
 * Send a GET request to the server to check if the user is logged in
 * If the response status is 202, the user is logged in and redirected to the index page
 * If the response status is 203, the user is not logged in and redirected to the login page
*/
async function loadIndex() {

	try {

		let hostnameport = "http://" + window.location.host

		const response = await fetch(hostnameport + '/api/index/');

		if (response.status === 202) {

			router("index");
		}
		if (response.status === 203) {

			router("login");
		}
	} catch (e) {
		console.error(e);
	}
};

/*
function called when the user try to login with 42 app
*/
async function load42Profile(code)
{
	try {
		let hostnameport = "http://" + window.location.host

		const init = {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},

			body: JSON.stringify({code: code})
		};
		

		const response = await fetch(hostnameport + '/api/call_back/', init);

		if (response.status == 200)
		{
			const data = await response.json()
			
			console.log("username " + data["username"])
			console.log("avatar " + data["player"].avatar)
			console.log("nickname " + data["player"].nickname)

			sessionStorage.setItem("username", data["username"]);
			sessionStorage.setItem("avatar", data["player"].avatar);
			sessionStorage.setItem("nickname", data["player"].nickname);

			document.querySelector("div.modal-backdrop.fade.show").remove();

			document.querySelectorAll(".nav__link").forEach(btn => {
				btn.removeAttribute("disabled");
			});
			document.getElementById("navbar__btn--user").removeAttribute("disabled");
			document.getElementById("logout").removeAttribute("disabled");

			// router("index");
		}
		else
		{
			throw new Error(`HTTP error, status = ${response.status}`);
		}

	} catch (e) {
		console.error(e);
	}
}

/**
 * Event listener for DOMContentLoaded event
 * If the user is on the index page, index specific logic is executed
 * Attach event listener to the 'logout' button
 * Attach event listeners on all buttons with the class 'nav__link' i.e. all buttons that redirect to another "page"
*/
document.addEventListener("DOMContentLoaded", () => {

	if (window.location.search) {
		let code = window.location.search.split("=")[1]
		// console.log("code = ", code)
		load42Profile(code)
	}

	if (window.location.pathname === "/") {
		loadIndex();
	}

	document.getElementById("logout").addEventListener("click", (e) => {
		e.preventDefault();
		handleLogout();
	});

	document.querySelectorAll(".nav__link").forEach(element => {
		element.addEventListener("click", (e) => {
			e.preventDefault();
			if (element.value !== window.location.pathname.replaceAll("/", "")) {
				router(element.value);
			}
		})
	});

});

```

Tous d’abord, il faut attacher à la page les evenements auquelles ele doit pouvoir réagir :

- loadIndex est appelé dés le chargement de la page
- load42Profile est appelé dés le chargement de la page localhost:7890/code=”CODE_API_42”
- handleLogout est appelé en cas de clic sur le bouton logout
- router(”value”) est appelé en cas de clic sur l’un des boutons du menu de navigation

```jsx
/**
 * Event listener for DOMContentLoaded event
 * If the user is on the index page, index specific logic is executed
 * Attach event listener to the 'logout' button
 * Attach event listeners on all buttons with the class 'nav__link' i.e. all buttons that redirect to another "page"
*/
document.addEventListener("DOMContentLoaded", () => {

	if (window.location.search) {
		let code = window.location.search.split("=")[1]
		// console.log("code = ", code)
		load42Profile(code)
	}

	if (window.location.pathname === "/") {
		loadIndex();
	}

	document.getElementById("logout").addEventListener("click", (e) => {
		e.preventDefault();
		handleLogout();
	});

	document.querySelectorAll(".nav__link").forEach(element => {
		element.addEventListener("click", (e) => {
			e.preventDefault();
			if (element.value !== window.location.pathname.replaceAll("/", "")) {
				router(element.value);
			}
		})
	});

});

```

# Python

## Environnement virtuel

Pour créer un environnement virtuel : `python -m venv /path/to/new/virtual/environment`

Pour activer environnement virtuel dans bash : `source *<venv>*/bin/activate` 

# Django

Pour commencer un projet : `django-admin startproject mysite`

## manage.py

Pour créer une nouvelle application au sein du projet django : `python manage.py startapp polls` 

| `python manage.py makemigrations` | Cette commande est responsable de la création de nouvelles migrations basées sur les modifications que vous avez apportées à vos modèles Django. Il génère ensuite automatiquement des fichiers de migration contenant les opérations nécessaires pour appliquer ces changements au schéma de la base de données. Ces fichiers de migration sont stockés dans le dossier migrations de chaque répertoire d'application. |
| --- | --- |
| `python manage.py migrate` | Elle applique les migrations de base de données à la base de données spécifiée dans les paramètres de votre projet. Les migrations sont le moyen pour Django de propager les modifications que vous apportez à vos modèles (ajout d'un champ, suppression d'un modèle, etc.) dans le schéma de la base de données.
”migrate” prend les fichiers de migration générés par makemigrations (ou fournis par Django lui-même pour les applications intégrées) et les applique à la base de données. |

En pratique, on utilise la commande makemigration pour que django prenne en compte les modifications. Ensuite on utilise la commande migrate pour que ces migrations soient prise en compte parr l’application.

## Shell de django

Le Shell de django est un shell python classique. Il est nottament possible de créer des entrées en base de donnée grâce à lui.

```python
>>> from listings.models import Band
>>> mem = Members()
>>> mem.name = 'Lucky Luck'
>>> mem.save()
>>> Members.objects.count()
>>> Members.objects.all()
```

## Basiques du management des URLs :

Il existe 3 manière de gérer les URLs avec django. Dans le fichier urls.py :

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

### Nouvelle page avec la fonction view

Dans le fichier <project>/urls.py :

```python

from django.contrib import admin
from django.urls import path
from <app> import views

urlpatterns = [
    path('admin/', admin.site.urls),
		path('hello/', views.hello, name='hello'),
    path('hello/<int:id>/', views.hello_details, name='hello-details'),
		path('login/', views.login),
]

```

Le troisième argument d’un Path est une chaine de caractère qui peut être utilisées dans le code pour faire des hyperliens. Pour cela il faut utiliser un block url dans les gabarits :

```python
<a href="{% url 'hello' %}">Retour</a>
```

Dans le fichier <app>/view.py

```python
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello World !</h1>')
```

### Inclure un URLconf supplémetaire

Au sein d’u projet django, il y a 3 fichiers qui assurent le routage des URLs :

- <projects>/urls.py
- <app>/urls.py
- <app>/view.py

Le fichier <project>/urls.py contient : 

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

La fonction include permet au serveur d’aller chercher l’URL demandé par le client. Par exemple toutes les urls qui commencent par polls/ seront recherchées à partir de cette racine dans le fichier polls/urls.py

Le fichier <app>/urls.py contient :

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.subscribe, name="subscribe"),
]
```

Il repertorie tous les path commençant par polls

Le fichier <project>/views.py contient  la fonction subscribe 

```python
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def subscribe(request):
		return HttpResponse("subscribe")
```

## Le fichier setting.py

Pour ajouter une app au projet il faut :

- Ajouter un élément à la liste INSTALLED_APP :

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

polls.apps.PollsConfig est une classe du module PollsConfig. Elle contient le “name” de l’app ainsi que un attribut “default_auto_field”…

- Utiliser la commande : `python [manage.py](http://manage.py/) makemigrations polls`

Si aucun modèle n’a été spécifié, django répond : `No changes detected in app 'polls`. Cette commande permet de faire migrer les modifications apportés au modèle. Elle remplit le fichier OOO1_initial.py

En production, il est possible de modifier d’autres paramêtres 

| SECRET_KEY | Clé utilisé par django pour la sécurité de l’application |
| --- | --- |
| DEBUG | C’est booléen qui qctive ou désactive le mode debuggage. Cela permet d’avoir des pages d’erreurs détaillées. Certaines mesures de sécurité sont assouplis. Donc ne pas utiliser en production |
| ALLOWED_HOST | Liste des noms d’hôtes/domaines que le site django peut servir. Si l’en-tête Host de la requête n’est pas dans cette liste, Django renvoie une erreur> En développement, l’idéal d’utliser la valeur : ['localhost', '127.0.0.1', '[::1]'] |
- DATABASES

Pour configurer la DATABASES du projet avec une base de donnée différente de la base de donnée par défaut, on peut également utilisé les variables d’environnement :

```python
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
```

### Le fichier admin.py

Tout d’abord,, pour créer un superuser pour se connecter à <>/admin

```bash
python manage.py createssuperuer
```

Le fichier admin.py permet de modifier la page /admin/ fournit par Django.

Il faut importer les modèles que l’on veut administrer :

```python
from members_test_fx.models import Members
from members_test_fx.models import Games
```

Il est possible de modifier l’apparence de la page :

Avant :

![Screenshot 2024-03-16 at 17.34.28.png](ft_transcendance%2083c7088d594e4cfab43bcfa1f0d95b3d/Screenshot_2024-03-16_at_17.34.28.png)

```python
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name','surname', 'age', 'active', 'connection_state')

class GamesAdmin(admin.ModelAdmin):
    list_display = ('title','members')

admin.site.register(Members, MembersAdmin)
admin.site.register(Games, GamesAdmin)
```

Après :

![Screenshot 2024-03-16 at 17.34.28.png](ft_transcendance%2083c7088d594e4cfab43bcfa1f0d95b3d/Screenshot_2024-03-16_at_17.34.28%201.png)

## Le fichier form.py

### Créer un formulaire :

Il est possible de définir un formulaire de la même manière que l’on définit une table dans un le fichier model.py. Les champs sont les mêmes que pour les modèles. Voici un exemple :

```python
from django import forms

class FormTest(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    surname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField(required=True)
```

Lorsque l’utilisateur clique sur le bouton pour l’envoie du formulaire, il est possible de traiter la requête grâce à l’objet `request`.

Pour ajouter notre form à notre page, il faut déjà l’importer dans la vue :

```python
from members_test_fx.forms import FormTest
```

Ensuite, il faut mettre une instance de cet objet form dans une variable :

```python
form = FormTest()
```

Dans la vue, il est possible de remplir le formulaire avec les données précédemment envoyées par l’utilisateur :

```python
form = FormTest(request.POST)
```

Enfin renvoyer à la vue grâce au dictionnaire :

```python
return render (request, "GABARIT.html", {"form" : form})
```

Cette objet contient plusieurs attributs. Pour plus de précisions :

[Django](https://docs.djangoproject.com/en/5.0/ref/request-response/)

Celui qui nous intéresse particulièrement est l’attribut `POST` qui contient un dictionnaire avec tous les champs remplis par l’utilisateur.
Si on l’afficher dans le terminal (), voici ce que nous obtenons :

```bash
<QueryDict: {'csrfmiddlewaretoken': ['PQ0cLghUV9qcmXpLVnUTnOOwaWAmro3rMCuA4P08Eg1Hks6JH3r5dF74AHoNESIO'], 'name': ['Coindreau'], 'surname': ['François-Xavier'], 'age': ['36'], 'email': ['fx.coindreau@gmail.com']}>
```

Ce dictionnaire peut être envoyé à la vue.
Pour éviter les problèmes lors du rafraîchissement de la page, on peut rediriger vers une autre page grâce à la fonction `redirect`.

```python
return redirect('email-sent')
```

### Créer un ModelForm

Il est possible de créer un formulaire à partir d’un modèle. Il se déclare de cette manière dans le fichier `form.py`

```python
from django import forms
from members_test_fx.models import Games

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'
				# exclude = ('NOM_DU_CHAMP')
```

Il est possible d’exclure des champs à l’aide de l’attribut exclude.

Ensuite ce formulaire est utilisable comme n’importe quel formulaire dans `view.py`

```python
form = GamesForm()
```

Pour modifier un objet en Base de données, il suffit de réutiliser le formulaire précédent en le remplissant à l’aide de l’objet choisis en DB. Voici comment :

```python
def game_change (request, id):
    game = Games.objects.get(id=id)
    if request.method == 'POST':
        form = GamesForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('hello')
        else :
            print("La forme est pas valide")
    else:
        form = GamesForm(instance=game)
    return render(request, "members_test_fx/game_change.html" ,{'form' : form})
```

La seule nouveauté par rapport au code précédent est la ligne : `form = GamesForm(request.POST, instance=game)`

Cette fois ci, GamesForm prend 2 arguments. Le deuxième informe Django que l’on veut modifier un objet existant. Si cet argument est absent la form ne pourra jamais être valide.

## Gestion de la base de donnée

### Le fichier model.py

Dans ce fichier chaque classe correspond à une Table et les attributs de ces classes sont les champs de la table.

```python
from django.db import models
# Create your models here.

class Members(models.Model):
    name = models.fields.CharField(max_length=100)

class Games(models.Model):
    title = models.fields.CharField(max_length=100)

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

A propos des différents champs :

Django est livré avec différents types de champs qui correspondent à différents types de données, comme `CharField` ou `IntegerField` . Il existe aussi des champs plus spécifiques qui vont contraindre l'entrée, comme `URLField` .

Nous pouvons définir des contraintes et des règles pour les champs en leur attribuant des options, comme `max_length` , `null` et `choices` .

```python
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Members(models.Model):
    class connection(models.TextChoices):
        HORS_LIGNE = "hors ligne"
        ONLINE = "online"
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(default="default")
    age = models.fields.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)])
    active = models.fields.BooleanField(default=True)
    connection_state = models.fields.CharField(max_length=10, choices=connection.choices, default=connection.HORS_LIGNE)

class Games(models.Model):
    title = models.fields.CharField(max_length=100)
```

Nous pouvons affiner davantage les contraintes sur les champs en spécifiant des validateurs sur les champs en utilisant l'option `validators` .

Si nous ajoutons des champs non nuls à un modèle, nous serons invités à leur fournir une valeur par défaut initiale lors de la migration.

[Django](https://docs.djangoproject.com/fr/5.0/ref/models/fields/#field-types)

- Le premier argument peut être une chaîne de caractère, il permet de donner un nom plus lisible au champ.

 Il est possible d’inspecter les requêtes effectués sur la base de donnée avec la commande : `python manage.py sqlmigrate polls 0001` 

- Nous pouvons créer des relations one-to-many en utilisant le champ`ForeignKey`.
- Nous contrôlons la stratégie de ce qui se passe lorsqu'un modèle lié est supprimé, en utilisant l'argument `on_delete`.
    - définir le champ comme nul en utilisant `models.SET_NULL`
    - définir le champ à sa valeur par défaut en utilisant `models.SET_DEFAULT`
    - supprimer l'objet en utilisant `models.CASCADE`

### Comment utiliser le contenu de la db dans le code

Dans le fichier <app>/view.py

```python
from django.shortcuts import render
from django.http import HttpResponse
from members_test_fx.models import Members
from members_test_fx.models import Games

# Create your views here.

def hello(request):
    tab_members = Members.objects.all()
    tab_games = Games.objects.all()
    return HttpResponse(f"<h1>{tab_members[0].name} joue une {tab_games[1].title}</h1>")

```

Il est possible également de récupérer les informations fournies dans l’URL :

```python
def hello_details(request, id):
    mem = Members.objects.get(id=id)
    return render(request, 'members_test_fx/hello_details.html', {'mem': mem})
```

Dans l’URL path il faudra préciser le type de données que l’on s’attend à recevoir :

```python
path('hello/<int:id>/', views.hello_details),
```

## Les gabarits ou templates

- Créer un fichier gabarit dans « <app>/templates/<app>/ » et lui donner l'extension « .html ».
- Changer la déclaration de retour de la vue pour appeler la méthode `render` et lui passer le chemin de votre fichier de gabarit.
- Passer également un dictionnaire de contexte à la méthode `render`.

```python
def hello(request):
    tab_members = Members.objects.all()
    tab_games = Games.objects.all()
    return render(request, "members_test_fx/hello.html", {"tab_members": tab_members, "tab_games": tab_games})
    #return HttpResponse(f"<h1>{tab_members[0].name} joue une {tab_games[1].title}</h1>")
```

- Utiliser des variables de gabarits pour injecter des données dans votre gabarit.
- Utiliser les balises de gabarits pour utiliser les boucles dans votre gabarit si besoin.

```html
<html>
    <head><title>django test</title></head>
    <body>
        <h1>Hello Django !</h1>
        <p>Liste des parties :</p>
        <ul>
			<li>{{tab_members.0.name}} joue une {{tab_games.1.title}}</li>
			<li>{{tab_members.1.name}} joue une {{tab_games.3.title}}</li>
		</ul>

        <p>Liste des membres :</p>
        {%for mem in tab_members %}
        {{ mem.name | upper}} /
        {%endfor%}

        <p>Liste des games :</p>
        {%for gam in tab_games %}
        {{ gam.title }} /
        {%endfor%}     
        
        <p>Liste des parties conditionnelles :</p>
        {% for gam in tab_games %}
            {% if 'pourrie' in gam.title %}
                Oulala...
            {% else %}
                Better...
            {% endif %}
            {{ gam.title }} /
        {% endfor %}
    
    </body>
</html>
```

Pour améliorer la gestion des gabarits, on peut utiliser des block.

On utilise une page html de base au sein de laquelle on a un block content :

```html
<html>
    <head><title>django test</title></head>
    <title>Merchex</title>
    <link rel="stylesheet" href="{% static 'members_test_fx/styles.css' %}" />
    <body>
				{% block content %}{% endblock %}
    </body>
</html>
```

Ce block content est dans une autre page html :

```html
{% extends 'members_test_fx/base.html' %}

{% block content %}

...

{% endblock %}
```

Pour que cela fonctionne, il faut utiliser les block extends et remplir le block content comme précédemment.

Pour ajouter une feuille de style :

- Il faut ajouter un dossier `static/<app>` dans le dossier de l’app pour y stocker le .css
- Pour faire référence à ce .css, on utilise le block `{% load static %}` en début de page. Ensuite, il est possible d’y faire référence avec `{% static 'members_test_fx/styles.css' %}`

# Django REST Framework

[Understanding Views In Django Rest Framework](https://medium.com/@sydney.idundun/understanding-views-in-django-rest-framework-d78ca8042f04)

## API view

Tout d’abord pour installer l’API dans l’environnement Python :

```bash
pip install djangorestframework
```

De la même manière que nous ajoutions une page à un projet Django classique :
Dans le fichier `<app>/urls.py` :

```python
from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIView.as_view()),
]
```

2 URLs ont été ajoutées :

- api-auth/ : pour se connecter à….
- api/category/ : pour lister sous forme d’un json le contenu de la database

Ensuite dans le fichier `<app>/serializers.py` :

```python
from rest_framework.serializers import ModelSerializer
from shop.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
```

Le principe est identique aux ModelForms, il faut créer une classe qui hérite de ModelSerializer. Ensuite, on utilise une classe imbriquée qui permet de sélectionner le modèle sur lequel se base notre serializer ainsi quel es champs à sérialiser.

Enfin dans le fichier `<app>/views.py` :

```python
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category
from shop.serializers import CategorySerializer
 
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
```

Concernant les importations, il y en 4. Deux concernent rest_framework. Les deux autres ne sont autres que le modèle sur lequel on veut travailler et le serializer. La fonction get est réécrite. Elle est appelée par le serveur lorsque la fonction GET apparait dans la requête. C’est le principe du ENDPOINT !!!!!

## ModelViewSet

### Le routeur

DjangoREST framework fournit un outils surpuissant pour faciliter la création d’une interface CRUD. Le routeur fonctionne ainsi :

```python
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from players_manager.views import PlayerViewSet

router = routers.SimpleRouter()
router.register('players', PlayerViewSet, basename='players')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
```

1. Creation du routeur
2. Registration du Router avec l’objet PlayerViewSet

Django REST crée automatiquement une collection de route pour l’interface CRUD. Ici, ces routes commenceront par `api/players`

1. On inclut toutes ces routes grâce à l’objet path

### Le ModelViewset de Player

```python
from rest_framework.viewsets import ModelViewSet

from players_manager.models import Player
from players_manager.serializers import PlayerSerializer

class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    #queryset = Player.objects.all()
    def get_queryset(self):
        return Player.objects.all()
```

L’objet PlayerViewSet hérite de ModelViewSet qui possède notamment parmi ses méthodes get_queryset qui doit être override pour que DjangoREST sache quoi faire lorsqu’on appelle l’url api/players. Il est possible d’interdire les modifications en remplaçant ModelViewSet pat ReadOnlyModelViewSet.

L’attribut serializer_class permets de specifier avec modele la classe travaille

Le serializer n’a pas été modifié.

### Ajouter des filtres

La fonction get_queryset peut être améliorée par les filtres pour des requêtes plus précises

On peut récupérer les variables get de l’URL grâce à l’objet request :

```python
param_name = self.request.GET.get('PARAM_NAME')
```

Exemple pour la table friends :

```python
class FriendViewSet(ModelViewSet):
	serializer_class = FriendSerializer
	#queryset = Friend.objects.all()
	def get_queryset(self):
		queryset = Friend.objects.all()

		player = self.request.GET.get('player')
		accept = self.request.GET.get('accept')

		if player is not None:
			queryset = queryset.filter(player_1=player) | queryset.filter(player_2=player)

		if accept is not None:
			queryset = queryset.filter(accept=accept)

		# queryset = queryset.filter(player_1=player)
		#player_1 = self.request.query_params.get('player_1', None)
		return queryset
```

[Django QuerySet - Filter](https://www.w3schools.com/django/django_queryset_filter.php)

## serializers.py

Le serializer est en charge de transformer les données de la db en fichier json. Il est possible de définir différents serializers utilisables ensuite dans la view.py

```python
from rest_framework.serializers import ModelSerializer

from players_manager.models import Player

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'login']

class PlayerDetailsSerializer(ModelSerializer):
    class Meta:
       model = Player
       fields = '__all__'
```

Ensuite, dans la view, il est possible de choisir le serializer en focntion de l’action demandé par le client.

Pour cela on override une fonction de l’objet ModelViewSet `get_serializer_class` :

```python
    def get_serializer_class(self):
        print("get_serializer_class", self.action)
        if self.action =='retrieve':
            return self.detail_serializer_class
        return self.serializer_class
```

Les actions disponibles sont :

- **list** : appel en `GET` sur l’URL de liste ;
- **retrieve** : appel en `GET` sur l’URL de détail (qui comporte alors un identifiant) ;
- **create** : appel en `POST` sur l’URL de liste ;
- **update** : appel en `PUT` sur l’URL de détail ;
- **partial_update** : appel en `PATCH` sur l’URL de détail ;
- **destroy** : appel en `DELETE` sur l’URL de détail.

Avant de se lancer dans la suite, il est indispensable de comprendre que les actions CRUD de base sont déjà codé lorsqu’on fait hérité notre Viewset de ModelViewSet. Selon la requête, la modification en base de donnée sera faite. Dans le cas d’une requête POST sur l’URL de liste

## rest_framework.decorators

Pour pouvoir utiliser ces décorateurs, il faut importer :

```python
from rest_framework.response import Response
from rest_framework.decorators import action
```

Pour ajouter des actions customisées, il est possible d’ajouter des décorateurs. Ces décorateurs prennent 3 paramètres :

- `methods` est la liste des méthodes HTTP qui appellent cette action, parmi GET, POST, PATCH, PUT, DELETE.
- `detail` est un booléen qui précise si l’action est disponible sur l’URL de liste ou de détail.
- `url_path` permet de déterminer l’URL qui sera ajoutée à la fin de l'endpoint de
liste ou de détail. S'il n’est pas précisé, alors le nom de la méthode
est utilisé.

Pour utiliser une action customisée on utilise le décorateur de la façon suivante :

```python
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from players_manager.models import Player
from players_manager.serializers import PlayerSerializer, PlayerDetailsSerializer

class PlayerViewSet(ModelViewSet):

    serializer_class = PlayerSerializer
    detail_serializer_class = PlayerDetailsSerializer

    def get_queryset(self):
        return Player.objects.all()

    #REDEFINITION DE LA METHODE GET_SERIALIZER_CLASS
    def get_serializer_class(self):
        print("get_serializer_class", self.action)
        if self.action =='retrieve':
            return self.detail_serializer_class
        return self.serializer_class

    @action(methods=['GET'], detail=True)
    def modify_nickname(self, request, pk):
        new_nickname = self.request.GET.get('new_nickname')
        if new_nickname is not None:
            current_player = self.get_object()
            current_player.nickname = new_nickname
            current_player.save()
            return Response(status=200)
        return Response(status=404)
 
```

La requête http qui permet d’utiliser cette action customisée est la suivante :
`http://localhost:7890/api/players/10/modify_nickname/?new_nickname=Pierre-Henri`

On utilise modify_nickname car nous n’avons pas précisé d URL au décorateur.

## Validations des champs

Tout d’abord, petite overv

## djangorestframework-simplejwt

Afin de rendre certains endpoint privés on utilise les tokens. Suite à la demande d’un utilisateur, l’API va fournir 2 tokens : un access_token et un refresh_token. L’acess token permet de s’assurer de l’identité du client. Le second est utilisé pour rafraichir le premier.

Dans le fichier settings.py, plusieurs modifications sont à effectuer pour ajouter simplejwt :

```python

INSTALLED_APPS = [
...
    'rest_framework_simplejwt',
...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}
```

Pour ajouter les token, il faut déjà ajouter les urls nécessaires dans urls.py :

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

Et c’est tout… Pour tester la création d’une paire de nouveaux tokens :

`POST http://localhost:7890/api/token/ username=USER_NAME password=PASSWORD`

`POST http://localhost:7890/api/token/refresh/ Refresh=ACCESS_TOKEN`

## Authentification simple

Tout d’abord models.py…

Il faut relier la table user avec de django avec le modele qui contient les informations supplémetaires. Pour cela il faut utiliser une ForeighKey

```python
from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    **owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)**
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
```

LA méthose save a été overide pour compléter les champs au moment de l’enregistrement en database. Le champ owner contient en premier parametre “auth.User” qui fqit reference au modele user de l’application “auth”. Cette notation permet d’eviter les importations circulaires…

Ensuite le serializer.py :

```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
			model = Snippet
			fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted']
			**owner = serializers.ReadOnlyField(source='owner.username')**

class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = User
		fields = ['id', 'username','snippets']
```

Comme le modele est modifié, il faut aussi modifier le serializer. Ici on utilise pas la correspondance directe dans laquelle un champ d’une table correspond au champ d’une autre table. On utilise l’argument source qui indiaue à DRF d’aller chercher dans l’instance de owner le champ username. Cocernant le type de champ “ReadOnly”, il s’agit d’un champ multi-type qui signifie que l’instance ne sera jamais modifié par le biais de ce serializer.

Maintenant les views :
C’est dans les views que nous allons autoriser l’accès ou non à certains endpoints. Pour cela on utilise l’attribut permission_classes. Il existe des permissions fournis par DRF mais il est aussi possible de creer nos propres classes de permission. 

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	**permission_classes = [permissions.IsAuthenticatedOrReadOnly]**

	def perform_create(self, serializer):
		print ("erer : ", self.request.user)
		serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	**permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]**
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
```

Le fichier permission.py

On ecrit des classes qui herite de la classe permissions.BasePermission et on peut overide les méthodes.

```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
		def has_object_permission(self, request, view, obj):
			if request.method in permissions.SAFE_METHODS:
				return True
			return obj.owner == request.user
```

[Django Rest Framework authentication: the easy way](https://www.guguweb.com/2022/01/23/django-rest-framework-authentication-the-easy-way/)

## Systeme d’inscription

[Login and Register User — Django Rest Framework](https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5)

[User Registration/Authentication with Django, Django Rest Framework, React, and Redux](https://iheanyi.com/journal/user-registration-authentication-with-django-django-rest-framework-react-and-redux/)

## Comment fonctionne l’inscription / log in avec l’API 42

Tout d’abord il faut créer une nouvelle application dans notre profil intra. 

[Getting started](https://api.intra.42.fr/apidoc/guides/getting_started)

![Screenshot 2024-04-28 at 10.38.53.png](ft_transcendance%2083c7088d594e4cfab43bcfa1f0d95b3d/Screenshot_2024-04-28_at_10.38.53.png)

SCOPES de l’application il serait peut-être plus judicieux de choisir un plus adapté à nos besoins. Par exemple, le scope profil ?

REDIRECT URI : il s’agit de l’URL vers laquelle l’utilisateur sera redirigé lorsqu’il se sera loggé avec ses identifiants 42.

Le clic sur le lien “se connecter avec 42” permet de configurer le premier appel à l’API avec les identifiants fournis lors de l’étape précédente.

```python
SOCIALACCOUNT_PROVIDERS = {
    '42': {
        'SCOPE': ['profile'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False,
        'KEY': 'u-s4t2ud-491a5d4d14d35ef25080f2f05937152abcd6c6f65ab162196a8c5ea26e7e5f65',
        'SECRET': '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',
    }
}
```

La classe suivante se charge d’envoyer au front le lien dûment configuré pour qu’il soit en mesure de rediriger l’utilisateur vers la page de login 42. Lorsque l’utilisateur s’est loggé sur la page login 42 il est redirigé vers l’url “REDIRECT URI”.
Cette requête est intercepté par le frontend du site dans le fichire router.js :

```jsx
	if (window.location.search) {
		let code = window.location.search.split("=")[1]
		// console.log("code = ", code)
		load42Profile(code)
	}
```

La fonction load42Profile est appelée, pour effectuer une requête POST vers une seconde classe du backend appelée Callback. La methode post de cette classe se charge de s’authentifier au prés de l’API 42 en utilisant le code renvoyé par celle-ci lorsque l’utilisateur s’est loggé. Cela est permis à l’aide d’une requête POST sur le endpoint 'https://api.intra.42.fr/oauth/token'  fournis par l’API 42. Cela est permis grâce à la bibliothéque requests de python.

```python
class Callback(APIView):

    def post(self, request):
        # Step 2: Receive authorization code and exchange for access token

        code = request.data["code"]

        # return Response(code, status=status.HTTP_200_OK)

        redirect_uri = 'http://localhost:7890/'  # Change to your callback URL
        token_url = 'https://api.intra.42.fr/oauth/token'
        data = {
            'client_id': settings.SOCIALACCOUNT_PROVIDERS['42']['KEY'],
            'client_secret': settings.SOCIALACCOUNT_PROVIDERS['42']['SECRET'],
            'code': code,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
            'scope': "public profile"

        }
        response = requests.post(token_url, data=data)
```

La response contient un “access_token”. Cet access_token permet d’effectuer une troisième requête sur le endpoint 'https://api.intra.42.fr/v2/me'. Ce endpoint fonctionne car nous sommes loggé à notre compte 42. Je présume qu’il utilise le cookie créé au moment ou nous avons été loggé à 42…

Tout d’abord, il faut effectuer la redirection vers l’API pour 

Il faut distinguer 2 cas pour notre projet :

- le cas ou l’utilisateur se log pour la première fois
- le cas où l’utilisateur s’est déjà loggé au paravent avec son login 42

D

# PostgresSQL

## Container et client postgres

 

1. Tout d’abord pull l’image du container : `docker pull postgres`
2. Run le container avec postgres : `docker run --name postgresql_test -p 5442:5432 -e POSTGRES_PASSWORD=test -d postgres`
    - Ici on choisit la variable d’environnement qui permettra de se connecter au serveur avec -e
3. Pour installer psql : `brew install libpq`
4. Pour lancer le client psql : `psql -p 5442 -h 127.0.0.1 -U postgres` 
    - -U permet de choisir l’utilisateur, par défaut il n’y a qu’un seul user : postgres qui est le owner des database de base

Depuis l’interieur du container : `psql --username=bck_django --dbname=db_bck_django`

\dt \c

# Design du backend en microservice

Comment fonctionne les containers en mode dev ?

On lance les containers en mode dev avec la commande `docker-compose up —build`

2 containers vont être built : web et db. IL N’Y A PAS DE CONTAINER POUR NGINX

- web contient tous les fichiers de l’app et est bind mount avec un volume
- db fait tourner postgresSQL. Ce sont les settings de django qui se chargent de se connecter à la base de données. La DB est montés  avec un volume postgres_data

![ft_transcendance_containers_dev.png](ft_transcendance%2083c7088d594e4cfab43bcfa1f0d95b3d/ft_transcendance_containers_dev.png)

Le serveur e

## Container nginx

Le container nginx peut être lancé séparément : `docker build -t test1_nginx . && docker run -p 80:8000 test1_nginx`

Le port 80 est utilisé mais le sujet requiert d’utiliser le protocole https, il faut donc utiliser le port 443.

Il permet d’avoir accès à toutes les page statiques du site.

## Container django

Le container django peut lui aussi être lancé indépendement à condition de supprimer la dépendance à la base de donnée : 

`docker build -t test1_django . && docker run -p 8000:8000 test1_django`

### Qu’est-ce qu’un WSGI comme gunicorn ?

WSGI (Web Server Gateway Interface) est un standard spécifiant comment un serveur Web peut interagir avec une application Python.

[Why Use WSGI/ASGI When We Have Nginx?](https://santoshk.dev/posts/2023/why-use-wsgi-asgi-when-we-have-nginx/)

### A quoi sert psycopg2 ?

Psycopg est un adaptateur de base de données PostgreSQL pour le langage de programmation Python.

## Container postgres

Il peut lui aussi être lancé de manière indépendante en utilisant la commande suivante : `docker build -t test1_postgres -f Dockerfile.postgres . && docker run -p 8000:8000 test1_postgres`

Cependant, Dockerfile.postgres ne sera pas utilisé par le docker-compose car il est inutile. Il n’existe qu’à des fins de test pour ce container à l’aide de la commande : `psql -h localhost -p 5432 -U bck_django -d db_bck_django`

## Dockerfile.prod

```yaml
###########
# BUILDER #
###########

# pull official base image
FROM python:3.11.4-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
# installation de gcc nécessaire car certains package python qui utilisent des extensions C
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
# flake8 est une librairie Python qui vérifie si le code suit la convention PEP 8
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/app/

# Ces flags dit à flake8 d'ignorer certains warnings/errors.
#    - E501 pour "line too long."
#    - F401 pour "module imported but unused."
RUN flake8 --ignore=E501,F401 .

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.11.4-slim-buster

# create directory for the app user
RUN mkdir -p /home/app 	

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
```

Un linter est comme un correcteur d’orthographe. Flake8 vérifie que le code Python suit la convention PEP 8.

[Utilisez des linters pour que votre code reste propre](https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable/7187871-utilisez-des-linters-pour-que-votre-code-reste-propre)

*Python wheel* est un format de paquetage binaire préconstruit pour les modules et les bibliothèques Python. Elles sont conçues pour faciliter l'installation et la gestion des paquets Python, en fournissant un format pratique à fichier unique qui peut être téléchargé et installé sans qu'il soit nécessaire de compiler le paquet à partir du code source.

[99% des principaux paquets Python sont maintenant des wheels, ce qui rendra plus rapide l'installation pour les paquets purement Python](https://python.developpez.com/actu/346978/99-pourcent-des-principaux-paquets-Python-sont-maintenant-des-wheels-ce-qui-rendra-plus-rapide-l-installation-pour-les-paquets-purement-Python/)

how to create an app SPA with javascript in frontend and django in backend ?

`pip freeze` permets de voir toutes les dépendances installées.

Pour arrêter runserver : 

`ps auxw | grep runserver`

`kill 7956`

docker

db

backend

api

frontend

certbot

procedure recuperation mdp

# Database

## Players

| Champs | Type |
| --- | --- |
| id |  |
| login |  |
| password |  |
| nickname |  |
| nb_games_2p_played |  |
| nb_games_2p_won |  |
| nb_games_2p_lost |  |
| nb_games_4p_played |  |
| nb_games_4p_won |  |
| nb_games_4p_lost |  |
| fict_score |  |
| Avatar |  |
| status |  |

## 2 players games

| Champs | Type |
| --- | --- |
| id |  |
| player1 |  |
| player2 |  |
| score_player1 |  |
| score_player2 |  |
| score_max |  |
| win_player |  |
| id_tournament |  |
| level |  |
| date |  |

## 4 players games

| Champs | Type |
| --- | --- |
| id |  |
| player1 |  |
| player2 |  |
| player3 |  |
| player4 |  |
| score_player1 |  |
| score_player2 |  |
| score_player3 |  |
| score_player4 |  |
| score_max |  |
| win_player |  |

## Friends

| Champs | Type |
| --- | --- |
| id |  |
| id_player1 | foreignKey |
| id_player2 |  |
| accept |  |

## Tournaments

| Champs | Type |
| --- | --- |
| id |  |
| player1 |  |
| player2 |  |
| player3 |  |
| player4 |  |
| player5 |  |
| player6 |  |
| player7 |  |
| player8 |  |
| nb_players |  |
| title |  |
