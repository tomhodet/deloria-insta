"""Contenu éditorial DelorIA, du mercredi 30 septembre 2026 au dimanche 4 avril 2027.

Un post par jour. CALENDRIER couvre le lundi, le mercredi, le vendredi, le samedi et le
dimanche ; MARDIS (développement d'entreprise) et JEUDIS (l'automatisation du jeudi)
complètent la semaine. construire.py attribue les dates, le ton (clair, sombre, marron)
selon la position dans le fil, la numérotation des séries et les crédits photo.

Quatre piliers, en alternance : la messagerie voyageur des conciergeries, les réseaux
sociaux qui publient seuls, le site internet et l'identité visuelle, l'automatisation
des tâches répétitives en entreprise.

Règles d'écriture : une accroche concrète, une tension, une chute qui retourne la situation,
une légende courte. Faits réels uniquement, aucun chiffre inventé, aucun nom de client,
aucun outil nommé, vouvoiement, aucun tiret long ou moyen, jamais « assistant IA ».
"""

H_CONC = "#conciergerie #conciergerieairbnb #locationcourteduree #airbnb #hotes"
H_ACC = "#astuceaccueil #hote #locationcourteduree #conciergerie #airbnb"
H_PME = "#pme #automatisation #entrepreneur #france"
H_PME2 = "#pme #automatisation #industrie #entrepreneur #france"
H_DESIGN = "#identitevisuelle #chartegraphique #logo #design"
H_SITE = "#siteinternet #webdesign #pme #entrepreneur"
H_RESEAUX = "#reseauxsociaux #instagram #automatisation #communication"

CONTACT = "Une question ? Écrivez-moi en message privé."

TERRAIN = "Note de terrain"
INGE = "Note d'ingénieur"
DESIGN = "Note de design"
ASTUCE = "Astuce du samedi"

# Fonds des pages intérieures de carrousel : textures discrètes, réutilisables.
PAPIER = ["texture-papier#1", "texture-papier#6", "texture-lin#1", "texture-papier#3", "texture-lin#5"]
FIN = "texture-lin#3"


def pages(*contenus):
    """Pages intérieures d'un carrousel : (titre, texte), fond texture en alternance."""
    return [dict(titre=t, texte=x, fond=PAPIER[i % len(PAPIER)]) for i, (t, x) in enumerate(contenus)]


CALENDRIER = [
    # ─────────────── Semaine d'ouverture ───────────────
    # 1 · mer 30/09
    dict(template="constat", photo_fichier="secteur-artisan#6", label="Identité visuelle",
         texte="Tout a changé\ndepuis vos débuts.", chute="Sauf votre logo.",
         legende=f"""Vos clients, vos outils, votre niveau : tout a progressé. Le logo, lui, date souvent de la première semaine.

Personne ne vous en parlera. Un client qui ne vous connaît pas encore compare quelques secondes, puis choisit.

Une charte graphique, c'est la même image partout. La bonne.

{CONTACT}

{H_DESIGN}"""),

    # 2 · ven 02/10
    dict(template="plein", photo_fichier="region-lyon#3", lieu="Lyon", decalage=-250,
         phrase="Deux conciergeries, une ville.\n*On se souvient d'une seule.*",
         legende=f"""Même quartier, mêmes prestations, souvent le même prix. La différence se joue ailleurs.

Une réponse qui arrive tout de suite. Un ton qui ressemble à une personne. Le détail prévu avant qu'on le demande.

C'est là que naît le souvenir. Et l'avis qui va avec.

{CONTACT}

{H_CONC} #lyon"""),

    # 3 · sam 03/10
    dict(template="plein", photo_fichier="details-linge#6",
         phrase="Samedi, les draps changent.\n*Les questions, jamais.*",
         legende=f"""Jour de rotation. Pendant que les équipes font les lits, les messages continuent d'arriver : l'heure d'arrivée, le parking, le code du wifi.

Toujours les mêmes. C'est exactement ce qui se délègue.

Courage à toutes les équipes sur le terrain aujourd'hui.

{H_CONC}"""),

    # 4 · dim 04/10
    dict(template="service", photo_fichier="details-carnet#6", label="DelorIA en bref",
         titre="Automatiser\nce qui se répète.\n*Jamais ce qui vous distingue.*",
         points=["Les réponses à vos voyageurs, dans leur langue",
                 "Vos publications, prêtes des mois à l'avance",
                 "Votre site et votre identité, sur mesure"],
         legende=f"""Pour ceux qui découvrent ce compte.

Aux conciergeries, un assistant qui répond aux voyageurs avec les informations de chaque logement. Aux entreprises et aux indépendants, des publications prêtes des mois à l'avance. À tous, des sites et des identités visuelles sur mesure.

Une règle pour tout : ce qui fait votre style ne s'automatise pas.

{CONTACT}

#automatisation #conciergerie #siteinternet #reseauxsociaux #pme #entrepreneur"""),

    # ─────────────── Octobre ───────────────
    # 5 · lun 05/10
    dict(template="constat", photo_fichier="design-croquis#5", label="Qui est derrière",
         texte="Je suis ingénieur.", chute="Pas une agence.",
         legende=f"""Je m'appelle Tom. Ingénieur de formation, je conçois des systèmes qui prennent en charge le travail répétitif des entreprises et des conciergeries.

Pas de sous-traitance, pas d'intermédiaire : je configure avec vous, je surveille ce que j'installe, et vous savez à qui écrire quand vous avez une question.

{CONTACT}

#automatisation #entrepreneur #pme #conciergerie"""),

    # 6 · mer 07/10
    dict(template="constat", photo_fichier="astuce-rue#2", label="Le quotidien d'une conciergerie",
         texte="22h43.\n« Je me gare où ? »", chute="Quelqu'un répond toujours.\nAujourd'hui, c'est vous.",
         legende=f"""Le voyageur n'attend pas le lendemain. Il écrit maintenant, et il attend une réponse maintenant.

Dans beaucoup de conciergeries, cette réponse part du téléphone personnel du gérant, en plein dîner.

Ce n'est pas un problème d'organisation. C'est un problème de disponibilité. Et la disponibilité, ça se délègue.

{H_CONC}"""),

    # 7 · ven 09/10
    dict(template="terrain_photo", serie="terrain", photo_fichier="details-telephone#1", cadrage="center 85%", label=TERRAIN,
         titre="Un lien dans un message,\n*et Airbnb bloque tout.*",
         texte="Un site, une adresse e-mail, un numéro : le message entier ne part pas. Un outil automatique n'en sait rien.",
         chute="Le voyageur attend une réponse qui n'arrivera jamais.",
         legende=f"""Je l'ai appris en conditions réelles. Une bonne réponse sur les pharmacies de garde, avec le nom d'un site. Airbnb a refusé le message entier. Le voyageur n'a rien reçu.

Quand vous écrivez vous-même, l'application vous prévient. Un outil automatique, non.

Depuis, l'assistant que je configure n'écrit aucune coordonnée. Pour une adresse précise, il vous passe la main.

{H_CONC}"""),

    # 8 · sam 10/10
    dict(template="carte", serie="astuce", photo_fichier="astuce-lampe#1", label=ASTUCE,
         titre="Arrivée à 23h.\n*Où est l'interrupteur ?*",
         texte="Laissez une lampe allumée pour les arrivées tardives. Ça ne coûte rien. Ça change la première minute.",
         legende=f"""Nouvelle série du samedi : une astuce par semaine, applicable dès ce week-end. Côté accueil pour commencer.

Arriver de nuit dans un logement inconnu, c'est chercher l'interrupteur à tâtons, les valises à la main. Arriver dans une pièce éclairée, c'est se sentir attendu.

{H_ACC}"""),

    # 9 · dim 11/10
    dict(template="plein", photo_fichier="interieur-chambre#2",
         phrase="Dimanche.\n*Qui répond à vos voyageurs ?*",
         legende=f"""Si la réponse est vous, ce n'est pas vraiment un dimanche.

Bon dimanche à toutes les conciergeries.

{H_CONC}"""),

    # 10 · lun 12/10
    dict(template="constat", photo_fichier="pme-courrier#6", label="En entreprise",
         texte="Le même mail,\nécrit pour la centième fois.", chute="Il pourrait partir seul.",
         legende=f"""Une confirmation de rendez-vous, une demande de pièces, une relance : dans beaucoup d'entreprises, les mêmes messages s'écrivent à la main, chaque semaine.

Ce qui se répète à l'identique peut partir seul, au bon moment, avec les bonnes informations. Vous gardez votre temps pour les messages qui en valent la peine.

{CONTACT}

{H_PME}"""),

    # 11 · mer 14/10
    dict(template="constat", photo_fichier="site-bureau-clair#6", label="Site internet",
         texte="Votre site est beau.", chute="Mais où est le bouton\npour vous appeler ?",
         legende=f"""Un visiteur sur téléphone vous accorde quelques secondes. S'il doit chercher votre numéro, il ne le cherchera pas longtemps.

Un bon site n'est pas seulement beau. Il dit en une phrase ce que vous faites, pour qui, et comment vous joindre, en un geste.

{CONTACT}

{H_SITE}"""),

    # 12 · ven 16/10
    dict(template="terrain_photo", serie="terrain", photo_fichier="details-cles#6", label=TERRAIN,
         titre="Le code d'accès,\n*je refuse de l'automatiser.*",
         texte="Il part déjà tout seul la veille de l'arrivée, depuis le logiciel de gestion locative. L'assistant ne le connaît pas.",
         chute="Moins il circule, moins il fuit.",
         legende=f"""On pourrait laisser l'assistant donner le code d'accès. C'est l'information la plus sensible d'un logement, et un code périmé envoyé à un voyageur, c'est une porte fermée à 23h.

Le logiciel de gestion locative l'envoie déjà, la veille de l'arrivée. L'assistant, lui, explique simplement quand il arrive.

Automatiser, c'est aussi savoir ce qu'on n'automatise pas.

{H_CONC}"""),

    # 13 · sam 17/10
    dict(template="carte", serie="astuce", photo_fichier="reseaux-telephone#1", label=ASTUCE,
         titre="Publiez moins.\n*Mais publiez toujours.*",
         texte="Deux posts par semaine tenus toute l'année valent mieux que dix posts en une semaine, puis le silence.",
         legende=f"""L'astuce du samedi, côté réseaux.

Un compte qui publie par à-coups donne une impression d'abandon entre deux rafales. Un rythme modeste mais tenu inspire confiance.

Choisissez un rythme que vous pouvez tenir toute l'année. Ou confiez-le à un système qui le tiendra.

{H_RESEAUX}"""),

    # 14 · dim 18/10
    dict(template="plein", photo_fichier="interieur-cheminee#2",
         phrase="Dimanche, 19h.\n*La semaine commence déjà.*",
         legende=f"""Les départs du week-end sont faits. Les questions de la semaine arrivent déjà : les arrivées de lundi, les demandes de dernière minute, les avis à lire.

Si votre dimanche soir ressemble à un lundi matin, c'est qu'une partie de votre travail n'attend pas que vous soyez disponible.

{H_CONC}"""),

    # 15 · lun 19/10
    dict(template="constat", photo_fichier="reseaux-telephone#6", label="Réseaux sociaux",
         texte="Votre dernier post\ndate de quand ?", chute="Vos clients, eux, ont regardé.",
         legende=f"""Un compte Instagram qui ne bouge plus, c'est souvent la première chose qu'un client potentiel remarque. Il ne se demande pas si vous êtes occupé. Il se demande si vous êtes encore là.

La régularité ne demande pas de talent. Elle demande un système.

{CONTACT}

{H_RESEAUX}"""),

    # 16 · mer 21/10 · carrousel
    dict(template="carrousel", label="Coulisses",
         couverture=dict(template="constat", photo_fichier="site-bureau-sombre#4", label="Coulisses",
                         texte="Ce compte publie\nchaque jour.", chute="Je n'y touche pas."),
         pages=pages(
             ("Six mois\n*écrits d'avance.*", "Chaque post a sa date, son visuel et sa légende avant même d'être publié."),
             ("Des visuels\n*à mes couleurs.*", "Mes typographies, ma palette, des photos libres de droits. Chaque image est générée à partir de mes gabarits."),
             ("Publié\n*à 17h30.*", "Le jour venu, un programme récupère le post et le publie. Il vérifie d'abord qu'il ne l'a pas déjà fait."),
             ("Surveillé,\n*pas oublié.*", "Si une publication échoue, le programme s'arrête et me prévient. Le reste du temps, je n'y pense pas."),
         ),
         fin=dict(titre="Le même système\n*peut tourner\npour votre compte.*", fond=FIN),
         legende=f"""Petit aveu : ce compte tourne tout seul.

Le calendrier est écrit des mois à l'avance. Les visuels sont générés à mes couleurs. Et chaque jour à 17h30, un programme publie le post du jour.

Je n'ai pas moins de choses à dire. J'ai juste arrêté de les publier à la main.

{CONTACT}

{H_RESEAUX}"""),

    # 17 · ven 23/10
    dict(template="edito", photo_fichier="site-bureau-clair#2", label="Réseaux sociaux",
         titre="Un compte qui publie *sans vous.*",
         texte="Je prépare vos posts des mois à l'avance, à vos couleurs, avec votre ton. Ils partent seuls, au jour prévu.",
         pictos=[dict(icone="calendrier", texte="Planifié\nd'avance"), dict(icone="pinceau", texte="À vos\ncouleurs"),
                 dict(icone="horloge", texte="Publié\nà l'heure")],
         cta="Écrivez-moi en privé",
         legende=f"""Ce que je propose aux entreprises et aux indépendants : un compte Instagram qui vit toute l'année, sans que vous ayez à y penser chaque semaine.

On valide ensemble une ligne éditoriale et un calendrier. Ensuite, les publications partent seules, au jour et à l'heure prévus. Ce compte en est la démonstration.

{CONTACT}

{H_RESEAUX}"""),

    # 18 · sam 24/10
    dict(template="carte", serie="astuce", photo_fichier="reseaux-telephone#3", label=ASTUCE,
         titre="Votre numéro de téléphone\n*doit se toucher.*",
         texte="Sur mobile, un numéro qu'il faut recopier, c'est un appel en moins. Un lien d'appel se règle en une ligne.",
         legende=f"""L'astuce du samedi, côté site.

Sur téléphone, un numéro affiché en simple texte oblige le visiteur à le retenir ou à le recopier. Beaucoup ne le font pas.

Un numéro qui lance l'appel, un e-mail qui ouvre la messagerie, une adresse qui ouvre la carte. Trois détails, et votre site travaille pour vous.

{H_SITE}"""),

    # 19 · dim 25/10
    dict(template="plein", photo_fichier="region-bordeaux#4",
         phrase="Personne n'a créé sa boîte\n*pour répondre à des mails.*",
         legende=f"""Vous avez créé votre activité pour un métier. Pas pour recopier des informations, relancer des clients ou répondre dix fois à la même question.

Ce temps-là se récupère. Bon dimanche.

{H_PME}"""),

    # 20 · lun 26/10
    dict(template="terrain_photo", serie="ingenieur", photo_fichier="design-croquis#6", label=INGE,
         titre="Automatiser un processus flou,\n*c'est automatiser le désordre.*",
         texte="Avant d'écrire une ligne, on décrit le processus tel qu'il est vraiment, avec ses exceptions.",
         chute="La moitié du travail se fait sur papier.",
         legende=f"""Nouvelle série : des notes d'ingénieur sur l'automatisation en entreprise.

Un outil ne rend pas un processus plus clair. Il le rend plus rapide. Si le processus est confus, il devient confus plus vite.

On commence donc toujours par le décrire, cas particuliers compris.

{H_PME2}"""),

    # 21 · mer 28/10
    dict(template="terrain_photo", serie="design", photo_fichier="design-typographie#2", label=DESIGN,
         titre="Deux typographies,\n*pas plus.*",
         texte="Une pour les titres, une pour le texte. Au-delà, un support perd sa cohérence.",
         chute="La sobriété se voit avant de se lire.",
         legende=f"""Nouvelle série : des notes de design, pour les entreprises qui veulent une image plus nette sans tout refaire.

Première règle, et la plus simple : deux typographies suffisent. Celle de vos titres, celle de vos textes. Toujours les mêmes, partout.

{H_DESIGN}"""),

    # 22 · ven 30/10
    dict(template="terrain_photo", serie="terrain", photo_fichier="pme-courrier#3", label=TERRAIN,
         titre="Le prix affiché par l'outil\n*n'est pas celui que paie le voyageur.*",
         texte="Frais de ménage, frais de service, suppléments : le total final n'a rien à voir avec le prix de base.",
         chute="L'assistant ne donne jamais un prix.",
         legende=f"""Une leçon apprise en conditions réelles.

Le prix par nuit qu'un logiciel de location transmet est un prix de base. Le voyageur, lui, paie un total avec les frais de ménage, les frais de service et les suppléments. Annoncer le premier, c'est préparer une mauvaise surprise au moment de payer.

Depuis, l'assistant ne donne jamais de montant. Il renvoie vers l'annonce, où le total s'affiche tout compris.

{H_CONC}"""),

    # 23 · sam 31/10
    dict(template="carte", serie="astuce", photo_fichier="design-croquis#1", label=ASTUCE,
         titre="Notez ce que vous faites\n*plus de trois fois.*",
         texte="Pendant une semaine, listez chaque tâche qui revient. C'est la liste de ce qui s'automatise en premier.",
         legende=f"""L'astuce du samedi, côté organisation.

On pense connaître ses tâches répétitives. On les sous-estime presque toujours. Une semaine de notes suffit pour voir apparaître les mêmes lignes : les mêmes mails, les mêmes relances, les mêmes recopies.

Cette liste vaut de l'or. C'est par elle qu'on commence.

{H_PME}"""),

    # 24 · dim 01/11
    dict(template="plein", photo_fichier="region-bretagne#4",
         phrase="Les vacances finissent.\n*Les avis commencent.*",
         legende=f"""Fin des vacances de la Toussaint. Les derniers voyageurs repartent, et les avis arrivent.

Un avis se joue rarement sur un seul détail. Il se joue sur l'ensemble : l'arrivée, la propreté, et la sensation d'avoir été pris en charge du premier message au dernier.

{H_CONC}"""),

    # ─────────────── Novembre ───────────────
    # 25 · lun 02/11
    dict(template="edito", photo_fichier="interieur-chambre#3", cadrage="30% center", label="Pour les conciergeries",
         titre="Un assistant qui répond *comme vous le feriez.*",
         texte="Il connaît le logement, le calendrier et votre façon de parler aux voyageurs. S'il ne sait pas, il vous passe la main.",
         pictos=[dict(icone="globe", texte="Langue du\nvoyageur"), dict(icone="lune", texte="Jour\net nuit"),
                 dict(icone="cloche", texte="Alerte si\nproblème")],
         cta="Écrivez-moi en privé",
         legende=f"""Ce que je construis pour les conciergeries : un assistant branché sur votre messagerie de location, qui répond aux voyageurs avec les vraies informations de chaque logement.

Il répond dans la langue du voyageur, à toute heure. Et quand il ne sait pas, il ne devine pas : il vous prévient.

{CONTACT}

{H_CONC}"""),

    # 26 · mer 04/11 · carrousel
    dict(template="carrousel", label="Site internet",
         couverture=dict(template="constat", photo_fichier="site-bureau-sombre#3", label="Site internet",
                         texte="Cinq signes\nque votre site date.", chute="Vos visiteurs les voient\navant vous."),
         pages=pages(
             ("Illisible\n*sur téléphone.*", "Texte minuscule, boutons trop petits, pages qui débordent. C'est pourtant sur téléphone que vos visiteurs arrivent."),
             ("Impossible\n*de vous joindre.*", "Si le numéro ou le bouton de contact demande plus de deux secondes de recherche, le visiteur repart."),
             ("Des photos\n*qui ne sont pas vous.*", "Des images vues partout ne montrent ni vos locaux ni votre travail. Vos vraies photos rassurent davantage."),
             ("Trois polices,\n*quatre couleurs.*", "Chaque page a sa propre allure. L'ensemble ne ressemble à rien de précis, et donc pas à vous."),
             ("Une actualité\n*vieille de deux ans.*", "Un contenu daté fait croire que l'activité l'est aussi. Mieux vaut aucune actualité qu'une actualité ancienne."),
         ),
         fin=dict(titre="Un site qui vous ressemble,\n*et qui travaille pour vous.*", fond=FIN),
         legende=f"""Cinq signes qu'un site a fait son temps, à vérifier sur le vôtre en deux minutes, depuis votre téléphone.

Si vous en cochez deux ou plus, votre site vous coûte probablement des contacts sans que vous le sachiez.

{CONTACT}

{H_SITE}"""),

    # 27 · ven 06/11
    dict(template="constat", photo_fichier="reseaux-appareil#1", label="Réseaux sociaux",
         texte="Personne ne s'abonne\nà un catalogue.", chute="On s'abonne à une voix.",
         legende=f"""Un compte qui ne publie que ses produits ou ses prestations ressemble à une vitrine. On la regarde une fois.

Ce qui fait revenir, c'est un point de vue : ce que vous avez appris, ce que vous refusez, ce que vous voyez que les autres ne voient pas.

{H_RESEAUX}"""),

    # 28 · sam 07/11
    dict(template="carte", serie="astuce", photo_fichier="interieur-cuisine#4", label=ASTUCE,
         titre="Expliquez le tri\n*avant qu'on vous le demande.*",
         texte="Jours de collecte, bacs, conteneur à verre : trois lignes dans le livret évitent un message et une poubelle oubliée.",
         legende=f"""L'astuce du samedi, côté accueil.

Chaque commune a ses règles, et aucun voyageur ne les connaît. Trois lignes claires dans le livret d'accueil, et la question ne se pose plus.

{H_ACC}"""),

    # 29 · dim 08/11
    dict(template="plein", photo_fichier="region-biarritz#2",
         phrase="En novembre,\n*on prépare l'été.*",
         legende=f"""Les logements se vident, les agendas respirent. C'est le bon moment pour préparer ce qui vous a manqué cet été : un site à jour, des réponses prêtes, un compte qui publie sans vous.

Au printemps, il sera trop tard pour s'en occuper sereinement.

{H_CONC}"""),

    # 30 · lun 09/11
    dict(template="terrain_photo", serie="ingenieur", photo_fichier="pme-dossiers#4", label=INGE,
         titre="Commencez par l'étape\n*la plus ennuyeuse.*",
         texte="Pas la plus impressionnante. Celle que tout le monde repousse et qui revient chaque semaine.",
         chute="C'est elle qui rapporte le plus vite.",
         legende=f"""On a souvent envie d'automatiser ce qui impressionne. Ce qui rapporte, c'est l'inverse : la tâche ennuyeuse, répétitive, que personne ne veut faire et qui revient toutes les semaines.

C'est là que quelques heures de mise en place libèrent du temps chaque semaine, durablement.

{H_PME2}"""),

    # 31 · mer 11/11
    dict(template="constat", photo_fichier="interieur-salon#6", label="Pour les conciergeries",
         texte="Le canapé, il l'oubliera.", chute="La réponse à 23h, non.",
         legende=f"""On soigne la décoration, les photos, le linge. C'est important. Mais ce qu'un voyageur raconte en rentrant, c'est souvent autre chose : la personne qui a répondu quand il était perdu devant la porte.

L'accueil ne commence pas à l'arrivée. Il commence au premier message.

{H_CONC}"""),

    # 32 · ven 13/11
    dict(template="constat", photo_fichier="commerce-vitrine#6", label="Site internet",
         texte="Votre site date\nde votre création.", chute="Votre entreprise,\nelle, a grandi.",
         legende=f"""Beaucoup de sites ont été faits au lancement, avec les moyens du moment. L'entreprise a grandi depuis : nouveaux services, nouveaux clients, nouvelles réalisations. Le site, lui, raconte encore les débuts.

Votre vitrine en ligne devrait montrer ce que vous êtes aujourd'hui.

{CONTACT}

{H_SITE}"""),

    # 33 · sam 14/11
    dict(template="carte", serie="astuce", photo_fichier="design-papeterie#1", label=ASTUCE,
         titre="Votre bio doit dire\n*ce que vous faites.*",
         texte="Pas votre histoire, pas vos valeurs. Ce que vous faites, pour qui, et comment vous joindre. En une ligne.",
         legende=f"""L'astuce du samedi, côté réseaux.

La bio d'un profil est lue en deux secondes par quelqu'un qui ne vous connaît pas. Elle doit répondre à une seule question : est-ce que c'est pour moi ?

Le reste peut attendre vos publications.

{H_RESEAUX}"""),

    # 34 · dim 15/11
    dict(template="plein", photo_fichier="temps-sablier#2",
         phrase="Ce qui se répète\n*peut se déléguer.*",
         legende=f"""Une règle simple pour la semaine qui vient : notez ce que vous faites plus de trois fois. C'est la première liste de ce qui peut partir sans vous.

Bon dimanche.

{H_PME}"""),

    # 35 · lun 16/11
    dict(template="service", photo_fichier="pme-courrier#1", label="Pour les PME",
         titre="Trois tâches\n*à confier à une machine.*",
         points=["Les relances de devis sans réponse",
                 "La recopie d'un mail vers un tableau",
                 "Les réponses aux questions fréquentes"],
         legende=f"""Si vous ne deviez automatiser que trois choses, commencez par celles-là. Elles reviennent chaque semaine, elles ne demandent aucune créativité, et elles se perdent facilement.

Une relance oubliée, c'est un devis qui dort. Une recopie, c'est une erreur qui attend son heure.

{CONTACT}

{H_PME}"""),

    # 36 · mer 18/11 · carrousel
    dict(template="carrousel", label="Ce que je refuse",
         couverture=dict(template="constat", photo_fichier="strategie-echecs#2", label="Ce que je refuse",
                         texte="Il y a des choses\nque je n'automatise pas.", chute="Même quand c'est possible."),
         pages=pages(
             ("Le code d'accès\n*d'un logement.*", "L'information la plus sensible. Elle part déjà seule, la veille de l'arrivée, depuis le logiciel de gestion locative."),
             ("Un prix\n*annoncé à la volée.*", "Le total payé n'est jamais le prix de base. Un montant faux crée un litige. L'assistant renvoie vers l'annonce."),
             ("Un vrai problème,\n*réglé sans vous.*", "Une fuite, une porte bloquée, un voyageur inquiet : l'assistant rassure et vous alerte. La décision reste la vôtre."),
             ("Ce qui fait\n*votre style.*", "Votre ton, vos choix, votre façon de dire non. On s'en inspire pour les messages simples. On ne le remplace pas."),
         ),
         fin=dict(titre="Automatiser\nce qui se répète.\n*Garder ce qui compte.*", fond=FIN),
         legende=f"""Une question revient souvent : jusqu'où peut-on automatiser ?

Ma réponse tient en une règle. Tout ce qui se répète à l'identique peut partir seul. Tout ce qui engage votre responsabilité, votre sécurité ou votre relation avec un client reste entre vos mains.

Voici quatre choses que je n'automatise jamais.

{CONTACT}

{H_CONC} #automatisation"""),

    # 37 · ven 20/11
    dict(template="edito", photo_fichier="site-bureau-clair#1", label="Sites internet",
         titre="Un site qui inspire confiance *dès la première seconde.*",
         texte="Des pages claires, vos vraies photos, un contact en un geste. Et vos textes, vous les modifiez vous-même.",
         pictos=[dict(icone="mobile", texte="Pensé\nmobile"), dict(icone="pinceau", texte="À votre\nimage"),
                 dict(icone="document", texte="Modifiable\npar vous")],
         cta="Écrivez-moi en privé",
         legende=f"""Un site n'a qu'une mission : donner envie de vous contacter.

Je construis des sites sur mesure, rapides sur téléphone, fidèles à votre identité, et que vous pouvez mettre à jour sans toucher au code.

{CONTACT}

{H_SITE}"""),

    # 38 · sam 21/11
    dict(template="carte", serie="astuce", photo_fichier="astuce-mot#1", label=ASTUCE,
         titre="Un mot écrit à la main\n*vaut toutes les attentions.*",
         texte="Quelques lignes, le prénom du voyageur, un conseil pour le soir même. Deux minutes, et un souvenir.",
         legende=f"""L'astuce du samedi, côté accueil.

Dans un monde de messages automatiques, un mot manuscrit se remarque. C'est même tout l'intérêt d'automatiser le reste : garder du temps pour ce qui ne s'automatise pas.

{H_ACC}"""),

    # 39 · dim 22/11
    dict(template="plein", photo_fichier="interieur-salon#4",
         phrase="Le luxe, c'est de n'avoir\n*rien à demander.*",
         legende=f"""Un logement réussi répond aux questions avant qu'on les pose : le wifi est affiché, la lumière est allumée, le livret dit où se garer.

Chaque question évitée, c'est un message en moins pour vous et un voyageur plus serein.

{H_CONC}"""),

    # 40 · lun 23/11
    dict(template="constat", photo_fichier="bureau-nuit#3", label="Le quotidien d'une conciergerie",
         texte="Vous répondez vite.", chute="Mais à quelle heure\ndormez-vous ?",
         legende=f"""Répondre vite est devenu la norme. Les voyageurs s'y attendent, et les plateformes affichent votre délai de réponse.

Le problème, ce n'est pas la vitesse. C'est qu'elle repose souvent sur une seule personne, son téléphone et ses soirées.

Une réactivité qui dépend de votre sommeil n'est pas un système. C'est un sacrifice.

{H_CONC}"""),

    # 41 · mer 25/11
    dict(template="constat", photo_fichier="pme-dossiers#2", label="En entreprise",
         texte="Le devis part le lendemain.", chute="Le client, lui, a déjà\ndemandé ailleurs.",
         legende=f"""Un devis envoyé le lendemain n'est pas un mauvais devis. C'est un devis en retard sur celui du concurrent qui a répondu dans l'heure.

Quand les informations sont déjà là, dans un mail ou un formulaire, le devis peut se préparer tout seul. Il ne reste qu'à le relire et l'envoyer.

{CONTACT}

{H_PME}"""),

    # 42 · ven 27/11
    dict(template="constat", photo_fichier="design-papeterie#2", label="Identité visuelle",
         texte="Quatre versions\nde votre logo circulent.", chute="Vos clients les ont\ntoutes vues.",
         legende=f"""Une version sur le site, une autre sur la vitrine, une troisième étirée sur les devis, une quatrième floue sur les réseaux. Personne ne l'a décidé, et pourtant c'est courant.

Une charte graphique règle ça une fois pour toutes : un logo, ses déclinaisons, et des fichiers propres pour chaque usage.

{CONTACT}

{H_DESIGN}"""),

    # 43 · sam 28/11
    dict(template="carte", serie="astuce", photo_fichier="design-croquis#3", label=ASTUCE,
         titre="Un logo se teste\n*en tout petit.*",
         texte="Réduisez-le à la taille d'une photo de profil. S'il reste lisible là, il le sera partout.",
         legende=f"""L'astuce du samedi, côté identité.

Un logo passe l'essentiel de sa vie en petit : photo de profil, onglet de navigateur, signature de mail. Beaucoup de logos sont dessinés en grand et ne survivent pas à la réduction.

Le test prend dix secondes.

{H_DESIGN}"""),

    # 44 · dim 29/11
    dict(template="plein", photo_fichier="region-alpes#2",
         phrase="Décembre arrive.\n*Vos réponses sont prêtes ?*",
         legende=f"""La saison d'hiver commence dans les stations. Les mêmes questions vont revenir chaque semaine : l'accès en voiture, les équipements, le local à skis, l'heure d'arrivée.

Une réponse préparée une fois peut servir tout l'hiver.

{H_CONC} #montagne"""),

    # 45 · lun 30/11
    dict(template="constat", photo_fichier="reseaux-planning#1", label="Réseaux sociaux",
         texte="Vous publiez quand\nvous avez le temps ?", chute="Donc presque jamais.",
         legende=f"""Publier quand on a le temps revient à publier pendant les semaines creuses, puis plus du tout quand l'activité reprend. Exactement quand votre compte aurait le plus d'impact.

Un calendrier préparé d'avance supprime la question du temps.

{H_RESEAUX}"""),

    # ─────────────── Décembre ───────────────
    # 46 · mer 02/12 · carrousel
    dict(template="carrousel", label="Identité visuelle",
         couverture=dict(template="constat", photo_fichier="design-nuancier#1", label="Identité visuelle",
                         texte="Une charte graphique,\nc'est quatre décisions.", chute="Pas cinquante pages."),
         pages=pages(
             ("Un logo,\n*et ses versions.*", "Une version principale, une pour les fonds foncés, une en tout petit. Chacune a sa place."),
             ("Deux typographies,\n*pas plus.*", "Une pour les titres, une pour le texte. Toujours les mêmes, partout."),
             ("Une palette\n*courte.*", "Trois à cinq couleurs, avec leurs codes exacts. Pas une de plus au gré des envies."),
             ("Des règles\n*écrites.*", "Où va le logo, quelles marges, quelles photos. Écrites une fois, pour que tout le monde les applique."),
         ),
         fin=dict(titre="Une image cohérente,\n*partout où l'on vous voit.*", fond=FIN),
         legende=f"""Une charte graphique fait souvent peur : on imagine un document épais, cher, que personne ne lit.

En réalité, l'essentiel tient en quatre décisions. Prises une fois, elles rendent cohérents votre site, vos réseaux, vos devis et vos cartes de visite.

{CONTACT}

{H_DESIGN}"""),

    # 47 · ven 04/12
    dict(template="constat", photo_fichier="accueil-panier#1", label="Pour les conciergeries",
         texte="« Vous faites\nle petit-déjeuner ? »", chute="Cette question\nvaut de l'argent.",
         legende=f"""Vélos, petit-déjeuner, ménage supplémentaire, transfert : beaucoup de conciergeries proposent des services en plus du logement. Et beaucoup de demandes se perdent dans une conversation, faute d'avoir été repérées.

L'assistant que je configure les repère. Dès qu'un voyageur montre un intérêt réel, il vous prévient avec le détail de la demande.

Ce n'est plus un coût. C'est une vente.

{H_CONC}"""),

    # 48 · sam 05/12
    dict(template="carte", serie="astuce", photo_fichier="pme-courrier#4", label=ASTUCE,
         titre="Une adresse e-mail\n*par type de demande.*",
         texte="Devis, facturation, support : séparer les entrées, c'est déjà trier. Et c'est la base de toute automatisation.",
         legende=f"""L'astuce du samedi, côté organisation.

Quand tout arrive dans la même boîte, tout se mélange : un devis urgent entre deux publicités, une réclamation sous une facture. Des adresses séparées, ou au moins des règles de tri, rendent chaque demande visible.

Et une demande bien triée est une demande qu'on peut traiter automatiquement.

{H_PME}"""),

    # 49 · dim 06/12
    dict(template="plein", photo_fichier="astuce-lampe#2",
         phrase="Les soirées d'hiver\n*méritent mieux qu'un code wifi.*",
         legende=f"""Le wifi, l'heure d'arrivée, le parking : ces réponses-là peuvent partir sans vous, à toute heure, dans la langue du voyageur.

Gardez vos soirées pour ce qui mérite vraiment votre attention.

{H_CONC}"""),

    # 50 · lun 07/12
    dict(template="terrain_photo", serie="ingenieur", photo_fichier="auto-engrenages#4", label=INGE,
         titre="Un texte généré\n*se vérifie toujours.*",
         texte="La même question peut produire deux réponses différentes. Chaque sortie est contrôlée et complétée avant de partir.",
         chute="Ce n'est pas de la méfiance. C'est de l'ingénierie.",
         legende=f"""Une note d'ingénieur, tirée de la production.

Un modèle de langage ne répond pas toujours de la même façon à la même question. La plupart du temps, c'est sans conséquence. Parfois, un champ manque, et l'envoi casse.

Chaque réponse est donc vérifiée, et complétée si besoin, avant de partir. Un système fiable ne suppose jamais que tout ira bien.

{H_PME2}"""),

    # 51 · mer 09/12
    dict(template="constat", photo_fichier="bureau-nuit#4", label="Site internet",
         texte="Un client vous cherche à 22h.", chute="Votre site est\nle seul à répondre.",
         legende=f"""Beaucoup de clients cherchent un prestataire le soir, une fois leur journée finie. À cette heure-là, vous ne répondez pas au téléphone. Votre site, si.

Il doit dire clairement ce que vous faites, rassurer, et permettre de vous écrire en un geste. Le lendemain matin, la demande vous attend.

{H_SITE}"""),

    # 52 · ven 11/12
    dict(template="constat", photo_fichier="site-bureau-sombre#2", label="Réseaux sociaux",
         texte="Un beau post par mois\nne fait pas un compte.", chute="La régularité, si.",
         legende=f"""On attend souvent l'idée parfaite, la photo parfaite, le bon moment. Pendant ce temps, le compte se tait.

Vos clients remarquent surtout une chose : que vous êtes là, semaine après semaine. Mieux vaut un post simple chaque semaine qu'un chef-d'œuvre par trimestre.

{H_RESEAUX}"""),

    # 53 · sam 12/12
    dict(template="carte", serie="astuce", photo_fichier="design-papeterie#4", label=ASTUCE,
         titre="Affichez le code wifi\n*là où on le cherche.*",
         texte="Une petite carte près de l'entrée ou sur la table. C'est une question qu'on ne vous posera plus.",
         legende=f"""L'astuce du samedi, côté accueil.

Le wifi fait partie des toutes premières questions, et c'est la plus simple à éviter. Une carte élégante, bien placée, avec le nom du réseau et le mot de passe.

Un message de moins pour vous, une première minute plus fluide pour le voyageur.

{H_ACC}"""),

    # 54 · dim 13/12
    dict(template="plein", photo_fichier="saison-noel#3",
         phrase="Les fêtes approchent.\n*Les messages aussi.*",
         legende=f"""Arrivées pendant les fêtes, horaires modifiés, questions sur les commerces ouverts : décembre concentre les demandes au moment où tout le monde voudrait souffler.

Préparez les réponses maintenant. Elles serviront pendant que vous serez à table.

{H_CONC}"""),

    # 55 · lun 14/12
    dict(template="terrain_photo", serie="terrain", photo_fichier="details-cles#1", label=TERRAIN,
         titre="Un filtre oublié, et l'assistant\n*répond avec le mauvais logement.*",
         texte="Le logiciel envoie les messages de tous les logements d'un compte au même endroit. Sans filtre, tout se mélange.",
         chute="Chaque logement a son filtre.",
         legende=f"""Une découverte faite en conditions réelles.

Un même compte gère souvent plusieurs logements, et les messages de tous les voyageurs arrivent par la même porte. Sans filtre, un assistant pourrait répondre à un voyageur de la maison A avec les informations de l'appartement B.

Chaque logement a donc son filtre, vérifié avant chaque réponse. Ce détail ne se voit jamais en démonstration. Il se voit le jour où il manque.

{H_CONC}"""),

    # 56 · mer 16/12 · carrousel
    dict(template="carrousel", label="Automatisation",
         couverture=dict(template="constat", photo_fichier="strategie-echecs#3", label="Automatisation",
                         texte="Automatiser\nvotre entreprise ?", chute="Commencez par\nune seule tâche."),
         pages=pages(
             ("Listez\n*ce qui se répète.*", "Pendant une semaine, notez chaque tâche faite plus de trois fois. La liste est toujours plus longue qu'on ne croit."),
             ("Décrivez\n*le processus réel.*", "Pas celui de la procédure. Celui qui se passe vraiment, avec ses exceptions et ses raccourcis."),
             ("Automatisez\n*la plus petite étape utile.*", "Une relance, une recopie, un tri. Un résultat visible en quelques jours, pas en six mois."),
             ("Mesurez,\n*puis élargissez.*", "Le temps gagné sur la première étape justifie la suivante. On avance par preuves, pas par promesses."),
         ),
         fin=dict(titre="Pas de grand projet.\n*Une première tâche qui disparaît.*", fond=FIN),
         legende=f"""Les projets d'automatisation qui échouent ont souvent un point commun : ils voulaient tout changer d'un coup.

Ceux qui réussissent commencent petit. Une tâche, un résultat visible, puis la suivante.

Voici la méthode que j'applique.

{CONTACT}

{H_PME2}"""),

    # 57 · ven 18/12
    dict(template="terrain_photo", serie="design", photo_fichier="design-nuancier#6", label=DESIGN,
         titre="Une palette courte\n*se retient.*",
         texte="Trois à cinq couleurs, avec leurs codes exacts. Au-delà, plus personne ne sait lesquelles sont les vôtres.",
         chute="On reconnaît une marque avant de lire son nom.",
         legende=f"""Note de design numéro deux.

Une identité forte se reconnaît de loin, avant même de lire le nom. Ce n'est pas une question de talent, c'est une question de discipline : peu de couleurs, toujours les mêmes, avec leurs codes exacts.

{H_DESIGN}"""),

    # 58 · sam 19/12
    dict(template="carte", serie="astuce", photo_fichier="saison-noel#2", label=ASTUCE,
         titre="Vos posts de fêtes,\n*écrits dès maintenant.*",
         texte="Fermetures, horaires, vœux : rédigés aujourd'hui, programmés pour la bonne date. Et vous profitez des fêtes.",
         legende=f"""L'astuce du samedi, côté réseaux.

Les annonces de fin d'année s'écrivent souvent le 24 au soir, dans l'urgence. Écrites dès maintenant et programmées, elles partent au bon moment sans vous.

{H_RESEAUX}"""),

    # 59 · dim 20/12
    dict(template="plein", photo_fichier="saison-noel#4",
         phrase="Noël arrive.\n*Vos voyageurs aussi.*",
         legende=f"""Arrivées tardives, marchés de Noël, restaurants ouverts le 25 : les questions de décembre ne ressemblent à aucune autre.

Le bon moment pour y penser, c'est avant qu'elles arrivent.

{H_CONC}"""),

    # 60 · lun 21/12
    dict(template="constat", photo_fichier="porte-lumiere#2", label="Le quotidien d'une conciergerie",
         texte="24 décembre, 21h.", chute="« La porte ne s'ouvre pas. »",
         legende=f"""Certains messages peuvent attendre le lendemain. Celui-là, non.

Dans ce cas, l'assistant que je configure ne cherche pas à régler le problème seul. Il rassure le voyageur immédiatement et vous alerte, avec le détail de la situation.

Automatiser, ce n'est pas disparaître. C'est être prévenu au bon moment.

{H_CONC}"""),

    # 61 · mer 23/12
    dict(template="constat", photo_fichier="design-sceau#2", label="Coulisses",
         texte="Ce post a été écrit\nen septembre.", chute="Il arrive pile pour Noël.",
         legende=f"""Oui, ce post a été préparé il y a trois mois, comme tout le calendrier de ce compte jusqu'au printemps.

C'est ce qui permet de publier régulièrement pendant les semaines chargées, les fêtes et les vacances. Le compte continue de vivre pendant que vous vivez aussi.

Joyeuses fêtes.

{H_RESEAUX}"""),

    # 62 · ven 25/12
    dict(template="plein", photo_fichier="saison-noel#1",
         phrase="Joyeux Noël.\n*Le téléphone peut attendre.*",
         legende="""Joyeux Noël à toutes les équipes, sur le terrain ou à table.

Aujourd'hui, rien n'est plus urgent que ceux qui sont autour de vous.

#joyeuxnoel #conciergerie #entrepreneur"""),

    # 63 · sam 26/12
    dict(template="carte", serie="astuce", photo_fichier="porte-lumiere#3", label=ASTUCE,
         titre="Un bon séjour\n*se termine par un au revoir.*",
         texte="Un message le jour du départ, un merci, une invitation à revenir. C'est souvent ce qui déclenche un bel avis.",
         legende=f"""L'astuce du samedi, côté accueil.

On soigne l'arrivée, on oublie souvent le départ. Pourtant c'est le dernier souvenir du séjour, juste avant que le voyageur ouvre l'application pour laisser son avis.

{H_ACC}"""),

    # 64 · dim 27/12
    dict(template="plein", photo_fichier="region-paris#3",
         phrase="Entre deux fêtes,\n*préparez l'année.*",
         legende=f"""La semaine entre Noël et le Nouvel An est souvent la plus calme de l'année. C'est le moment idéal pour regarder ce qui vous a pris le plus de temps en 2026.

Il y a de bonnes chances que ce soit la même chose l'an prochain. Sauf si on s'en occupe.

{H_PME}"""),

    # 65 · lun 28/12
    dict(template="constat", photo_fichier="design-papeterie#3", label="Identité visuelle",
         texte="Nouvelle année,\nnouveau logo ?", chute="Pas forcément.\nUne charte, sûrement.",
         legende=f"""Changer de logo n'est pas toujours nécessaire. Souvent, le problème n'est pas le logo lui-même, mais la façon dont il est utilisé : étiré, recoloré, remplacé selon les supports.

Une charte graphique remet de l'ordre sans tout jeter. Et vos clients vous reconnaissent toujours.

{CONTACT}

{H_DESIGN}"""),

    # 66 · mer 30/12 · carrousel
    dict(template="carrousel", label="Bilan",
         couverture=dict(template="constat", photo_fichier="temps-sablier#3", label="Bilan",
                         texte="Ce que 2026\nm'a appris.", chute="Quatre leçons,\nsans filtre."),
         pages=pages(
             ("Un oui sans date\n*est un non différé.*", "Un accord en rendez-vous ne vaut rien sans une date de mise en place fixée avant de raccrocher."),
             ("Une démonstration dit\n*ce que l'outil ne sait pas faire.*", "Un enthousiasme fondé sur une capacité imaginaire se retourne en déception le premier jour."),
             ("Un test incomplet\n*ne prouve rien.*", "Le bug le plus coûteux de l'année n'apparaissait qu'avec une vraie réservation. Aucune n'existait en test."),
             ("Le silence\n*est le pire des échecs.*", "Une réponse imparfaite vaut mieux qu'aucune réponse. Tout ce que je construis part de cette idée."),
         ),
         fin=dict(titre="Merci d'avoir suivi.\n*On continue en 2027.*", fond=FIN),
         legende="""Première année de DelorIA. Quelques réussites, quelques incidents, et beaucoup d'apprentissages.

Voici les quatre leçons que je garde, celles qui ont changé ma façon de travailler.

Merci à celles et ceux qui m'ont fait confiance cette année.

#entrepreneur #automatisation #conciergerie #bilan"""),

    # ─────────────── Janvier ───────────────
    # 67 · ven 01/01
    dict(template="plein", photo_fichier="porte-lumiere#1",
         phrase="Bonne année.\n*Déléguez ce qui se répète.*",
         legende="""Bonne année à toutes et à tous.

Un vœu simple pour 2027 : que votre temps aille à ce que vous faites de mieux, et que le reste parte tout seul.

#bonneannee #entrepreneur #automatisation"""),

    # 68 · sam 02/01
    dict(template="carte", serie="astuce", photo_fichier="pme-dossiers#1", label=ASTUCE,
         titre="Un tableau partagé\n*vaut mieux que dix fichiers.*",
         texte="Une seule source pour les clients, les devis ou les réservations. Tout ce qui s'automatise part de là.",
         legende=f"""L'astuce du samedi, côté organisation.

Dix versions d'un même fichier, ce sont dix vérités différentes. Un seul tableau partagé, tenu à jour, devient la mémoire de l'entreprise.

C'est aussi le point de départ de presque toutes les automatisations : on n'automatise que ce qui est rangé quelque part.

{H_PME}"""),

    # 69 · dim 03/01
    dict(template="plein", photo_fichier="region-corse#4",
         phrase="Janvier.\n*On réserve déjà l'été.*",
         legende=f"""Pendant que l'hiver s'installe, beaucoup de voyageurs réservent déjà leurs vacances d'été. Les premières questions arrivent : disponibilités, équipements, accès.

Une annonce claire et des réponses rapides, dès maintenant, font la différence.

{H_CONC}"""),

    # 70 · lun 04/01
    dict(template="constat", photo_fichier="temps-sablier#5", label="Réseaux sociaux",
         texte="Bonne résolution :\npublier chaque semaine.", chute="Elle tient\njusqu'à février.",
         legende=f"""Chaque janvier, beaucoup d'entreprises décident de publier régulièrement. En février, le rythme s'essouffle. En mars, le compte se tait.

Ce n'est pas un manque de volonté. C'est un manque de système. Un calendrier préparé d'avance tient la résolution pour vous.

{CONTACT}

{H_RESEAUX}"""),

    # 71 · mer 06/01
    dict(template="terrain_photo", serie="terrain", photo_fichier="details-cafe#5", label=TERRAIN,
         titre="Savoir répondre,\n*et savoir se taire.*",
         texte="Un merci, un pouce levé : certains messages n'appellent aucune réponse. L'assistant sait désormais ne rien envoyer.",
         chute="Une réponse inutile est déjà une erreur.",
         legende=f"""Une note de terrain, apprise à mes dépens.

Un assistant à qui l'on dit « ne réponds pas si ce n'est pas utile », mais qui n'a aucun moyen technique de se taire, finira toujours par écrire quelque chose. Et ce quelque chose partira au voyageur.

Aujourd'hui, se taire est une réponse prévue, vérifiée avant chaque envoi. Toute consigne de ne rien faire doit avoir son mécanisme.

{H_CONC}"""),

    # 72 · ven 08/01
    dict(template="constat", photo_fichier="pme-dossiers#3", label="En entreprise",
         texte="Votre meilleur commercial\nrecopie des tableaux.", chute="Est-ce vraiment\nson métier ?",
         legende=f"""Dans beaucoup d'entreprises, les personnes les plus précieuses passent une partie de leur semaine sur des tâches sans valeur : recopier un mail dans un tableau, mettre à jour un fichier, relancer à la main.

Chaque heure rendue à ces personnes retourne à ce qu'elles font de mieux : vendre, conseiller, fabriquer.

{H_PME}"""),

    # 73 · sam 09/01
    dict(template="carte", serie="astuce", photo_fichier="secteur-bureau#4", label=ASTUCE,
         titre="Une page,\n*un seul objectif.*",
         texte="Appeler, réserver, demander un devis : choisissez une action par page et rendez-la évidente.",
         legende=f"""L'astuce du samedi, côté site.

Une page qui propose dix choses n'en fait faire aucune. Décidez ce que le visiteur doit faire en arrivant, et placez ce bouton partout où son regard passe.

{H_SITE}"""),

    # 74 · dim 10/01
    dict(template="plein", photo_fichier="temps-sablier#4",
         phrase="Une heure par jour,\n*c'est six semaines par an.*",
         legende=f"""Une heure par jour passée sur des tâches répétitives, sur une année de travail, représente plus de six semaines à temps plein.

Six semaines de mails, de recopies et de relances. Six semaines qui pourraient aller à votre métier.

{H_PME}"""),

    # 75 · lun 11/01
    dict(template="service", photo_fichier="reseaux-telephone#2", label="Réseaux sociaux",
         titre="Ce que je prépare\n*pour votre compte.*",
         points=["Un calendrier de publications sur plusieurs mois",
                 "Des visuels à vos couleurs, prêts à partir",
                 "Une publication automatique, au jour prévu"],
         legende=f"""Un compte qui vit toute l'année ne demande pas d'y passer ses soirées. Il demande une préparation sérieuse, une fois, puis un système qui tient le rythme.

C'est exactement ce que je mets en place, à vos couleurs et avec votre ton.

{CONTACT}

{H_RESEAUX}"""),

    # 76 · mer 13/01 · carrousel
    dict(template="carrousel", label="Pour les conciergeries",
         couverture=dict(template="constat", photo_fichier="details-cles#2", label="Pour les conciergeries",
                         texte="Quatre questions\nreviennent sans cesse.", chute="Elles ont toutes\nune réponse prête."),
         pages=pages(
             ("Où est-ce que\n*je me gare ?*", "La question la plus pressante, souvent posée en route. La réponse doit être précise et immédiate."),
             ("À quelle heure\n*peut-on arriver ?*", "Et parfois : peut-on arriver plus tôt ? Celle-là, l'assistant vous la transmet. C'est votre décision."),
             ("Quel est\n*le code du wifi ?*", "Donné au bon moment, au voyageur dont le séjour commence. Pas des semaines avant."),
             ("Qu'y a-t-il\n*autour du logement ?*", "Boulangerie, pharmacie, restaurant. L'assistant ne connaît que les adresses que vous lui avez confiées. Il n'invente rien."),
         ),
         fin=dict(titre="Des réponses justes,\n*à toute heure.*", fond=FIN),
         legende=f"""Quatre questions reviennent dans presque toutes les conversations avec les voyageurs. Aucune n'est difficile. Toutes arrivent au mauvais moment.

Voici comment l'assistant que je configure y répond, et où il s'arrête.

{CONTACT}

{H_CONC}"""),

    # 77 · ven 15/01
    dict(template="constat", photo_fichier="pme-courrier#2", label="En entreprise",
         texte="« Je me permets de vous\nrelancer au sujet du devis. »", chute="Qui l'écrit, chez vous ?",
         legende=f"""La relance est l'une des tâches les plus rentables et les plus oubliées d'une entreprise. Un devis sans réponse n'est pas un refus : c'est souvent un client qui a oublié.

Une relance qui part seule, au bon moment, poliment, et qui s'arrête dès que le client répond. C'est simple à mettre en place, et ça se voit vite.

{CONTACT}

{H_PME}"""),

    # 78 · sam 16/01
    dict(template="carte", serie="astuce", photo_fichier="interieur-salle-bain#3", label=ASTUCE,
         titre="Relisez votre annonce\n*avant chaque saison.*",
         texte="Équipements, horaires, règles, photos : ce qui était vrai l'an dernier ne l'est peut-être plus.",
         legende=f"""L'astuce du samedi, côté accueil.

Une annonce qui promet un équipement disparu, c'est un voyageur déçu et un avis moyen. Une relecture par saison suffit à l'éviter.

C'est aussi ce qui garantit des réponses justes : l'assistant répond avec les informations que vous lui donnez.

{H_ACC}"""),

    # 79 · dim 17/01
    dict(template="plein", photo_fichier="temps-horlogerie#3",
         phrase="Les meilleurs outils\n*sont ceux qu'on oublie.*",
         legende=f"""Un bon outil ne demande pas d'attention. Il fait son travail, toujours de la même façon, et ne se rappelle à vous que lorsqu'il le faut.

C'est la seule définition de l'automatisation qui compte.

{H_PME}"""),

    # 80 · lun 18/01
    dict(template="terrain_photo", serie="design", photo_fichier="design-typographie#5", label=DESIGN,
         titre="Un logo doit tenir\n*en noir et blanc.*",
         texte="Tampon, gravure, document photocopié : sans ses couleurs, il doit rester reconnaissable.",
         chute="La couleur est un bonus, pas une béquille.",
         legende=f"""Note de design numéro trois.

Un logo qui ne fonctionne qu'en couleur est fragile. Imprimé en noir sur un devis, gravé, brodé, il doit rester lisible et reconnaissable.

Le test : imprimez-le en noir et blanc, en petit. Ce qui reste, c'est votre vrai logo.

{H_DESIGN}"""),

    # 81 · mer 20/01
    dict(template="constat", photo_fichier="region-alpes#3", label="Pour les conciergeries",
         texte="Un voyageur allemand\nvous écrit à minuit.", chute="Il aura sa réponse\nen allemand.",
         legende=f"""Répondre à un voyageur étranger en pleine nuit, dans sa langue, avec les bonnes informations : pour une petite équipe, ce n'est pas tenable. Pour un assistant bien configuré, c'est la base.

Il détecte la langue du message et répond dans la même, avec votre ton et les informations du logement.

{H_CONC}"""),

    # 82 · ven 22/01
    dict(template="terrain_photo", serie="ingenieur", photo_fichier="bureau-nuit#5", label=INGE,
         titre="Une automatisation sans alerte\n*est une panne qui attend.*",
         texte="Chaque système que je livre prévient dès qu'une étape échoue, et un test vérifie chaque matin que tout répond.",
         chute="Le jour où ça casse, on le sait.",
         legende=f"""Une note d'ingénieur, sur ce qu'on ne voit jamais en démonstration.

Un système automatique qui tombe en panne en silence est pire qu'aucun système : tout le monde croit que le travail est fait. Chaque automatisation que je livre prévient donc dès qu'une étape échoue.

Le jour où ça casse, on le sait. Le reste du temps, on n'y pense pas.

{H_PME2}"""),

    # 83 · sam 23/01
    dict(template="carte", serie="astuce", photo_fichier="reseaux-appareil#4", label=ASTUCE,
         titre="Une photo de vous\n*vaut dix logos.*",
         texte="Sur les réseaux, on suit plus volontiers une personne qu'une marque. Montrez qui travaille derrière.",
         legende=f"""L'astuce du samedi, côté réseaux.

Un visage inspire confiance plus vite qu'un logo. Une photo de vous au travail, de temps en temps, rappelle qu'il y a une personne derrière le compte.

Pas besoin d'en faire trop. Une fois par mois suffit.

{H_RESEAUX}"""),

    # 84 · dim 24/01
    dict(template="plein", photo_fichier="region-bretagne#1",
         phrase="On regrette rarement\n*d'avoir délégué trop tôt.*",
         legende=f"""Déléguer fait peur au début : peur de perdre le contrôle, peur que ce soit moins bien fait. Puis on découvre le temps retrouvé, et on se demande pourquoi on a attendu.

Commencez par une seule tâche. Celle qui vous agace le plus.

{H_PME}"""),

    # 85 · lun 25/01
    dict(template="edito", photo_fichier="design-nuancier#3", label="Identité visuelle",
         titre="Logo, couleurs, typographies. *Une seule image.*",
         texte="Je crée ou je remets en ordre votre identité visuelle, avec des fichiers propres pour chaque usage.",
         pictos=[dict(icone="pinceau", texte="Logo et\nversions"), dict(icone="palette", texte="Palette\ncourte"),
                 dict(icone="document", texte="Règles\nécrites")],
         cta="Écrivez-moi en privé",
         legende=f"""Une identité visuelle, ce n'est pas seulement un logo. C'est un ensemble de règles simples qui font que votre site, vos réseaux, vos devis et votre vitrine se ressemblent.

Je la crée pour les entreprises qui démarrent, et je la remets en ordre pour celles qui ont grandi sans elle.

{CONTACT}

{H_DESIGN}"""),

    # 86 · mer 27/01 · carrousel
    dict(template="carrousel", label="Réseaux sociaux",
         couverture=dict(template="constat", photo_fichier="reseaux-appareil#2", label="Réseaux sociaux",
                         texte="Quatre erreurs qui font\nfuir vos futurs clients.", chute="Aucune ne coûte\nun centime à corriger."),
         pages=pages(
             ("Publier\n*par à-coups.*", "Dix posts en une semaine, puis trois mois de silence. Le visiteur retient le silence."),
             ("Des visuels\n*sans cohérence.*", "Une couleur par post, une police par humeur. Le fil ne ressemble à rien, donc pas à vous."),
             ("Des textes\n*qui disent tout.*", "Un long post qui explique tout n'est pas lu. Une idée par post, dite simplement."),
             ("Aucun moyen\n*de vous joindre.*", "Pas de lien, pas de numéro, une bio vague. L'intérêt retombe avant d'avoir trouvé comment vous écrire."),
         ),
         fin=dict(titre="Régulier, cohérent, clair.\n*Le reste est un bonus.*", fond=FIN),
         legende=f"""Un compte Instagram n'a pas besoin d'être spectaculaire pour attirer des clients. Il a surtout besoin d'éviter quatre erreurs, très courantes et faciles à corriger.

Faites glisser, et regardez votre propre compte avec ces quatre questions en tête.

{CONTACT}

{H_RESEAUX}"""),

    # 87 · ven 29/01
    dict(template="constat", photo_fichier="astuce-chargeur#2", label="Le quotidien d'une conciergerie",
         texte="Dix logements.", chute="Un seul téléphone.",
         legende=f"""Dans beaucoup de conciergeries, tout converge vers un seul appareil : celui du gérant. Les voyageurs, les propriétaires, les équipes de ménage, les plateformes.

Ce n'est pas un problème de téléphone. C'est un goulot d'étranglement. Et chaque logement de plus le resserre.

{H_CONC}"""),

    # 88 · sam 30/01
    dict(template="carte", serie="astuce", photo_fichier="pme-dossiers#5", label=ASTUCE,
         titre="Un modèle de devis,\n*et on ne retape plus rien.*",
         texte="Mentions, conditions, mise en page : ce qui ne change jamais ne devrait jamais se retaper.",
         legende=f"""L'astuce du samedi, côté organisation.

Un bon modèle de devis contient déjà tout ce qui ne change pas : vos mentions, vos conditions, votre mise en page, votre logo. Il ne reste qu'à remplir ce qui change.

C'est aussi la première brique d'un devis qui se prépare tout seul.

{H_PME}"""),

    # 89 · dim 31/01
    dict(template="plein", photo_fichier="region-alpes#5",
         phrase="Février approche.\n*Les stations se remplissent.*",
         legende=f"""Vacances d'hiver en vue. Dans les stations, les arrivées vont s'enchaîner chaque samedi, avec leur lot de questions : routes, équipements, local à skis, heure d'arrivée.

Chaque réponse préparée maintenant, c'est une soirée de libre en février.

{H_CONC} #montagne"""),

    # ─────────────── Février ───────────────
    # 90 · lun 01/02
    dict(template="service", photo_fichier="auto-engrenages#2", label="Coulisses",
         titre="Ce compte\n*en trois chiffres.*",
         points=["7 publications par semaine",
                 "17h30, tous les jours",
                 "187 posts préparés d'avance"],
         legende=f"""Quelques chiffres sur ce compte, pour ceux qui se demandent comment il tient le rythme.

Sept publications par semaine, toujours à la même heure, préparées des mois à l'avance. Les posts du calendrier partent tout seuls.

Le même système peut fonctionner pour votre entreprise.

{CONTACT}

{H_RESEAUX}"""),

    # 91 · mer 03/02
    dict(template="terrain_photo", serie="design", photo_fichier="interieur-salon#2", label=DESIGN,
         titre="Vos photos parlent\n*avant vos textes.*",
         texte="Sur un site, l'œil va d'abord aux images. Floues, sombres ou empruntées, elles décrédibilisent tout le reste.",
         chute="Une bonne photo remplace un paragraphe.",
         legende=f"""Note de design numéro quatre.

Sur une page, le regard se pose d'abord sur les images. Si elles sont floues, mal cadrées ou vues ailleurs, le visiteur doute avant d'avoir lu une ligne.

Quelques bonnes photos de vos locaux, de votre travail ou de vos logements valent mieux que dix pages de texte.

{H_DESIGN}"""),

    # 92 · ven 05/02
    dict(template="constat", photo_fichier="strategie-echecs#4", label="En entreprise",
         texte="Vos procédures sont\ndans une seule tête.", chute="Et quand elle part\nen vacances ?",
         legende=f"""Dans beaucoup de PME, une personne sait tout : comment traiter telle demande, où trouver tel document, quoi répondre à tel client. Tant qu'elle est là, tout va bien.

Documenter ces procédures, puis les rendre accessibles à toute l'équipe, parfois par une simple question posée à un outil, c'est protéger l'entreprise contre une absence ou un départ.

{CONTACT}

{H_PME2}"""),

    # 93 · sam 06/02
    dict(template="carte", serie="astuce", photo_fichier="secteur-atelier#4", label=ASTUCE,
         titre="Votre plus belle réalisation\n*en haut de la page.*",
         texte="Pas votre histoire, pas votre équipe. Ce que vous faites de mieux, visible sans faire défiler.",
         legende=f"""L'astuce du samedi, côté site.

Le haut de la page d'accueil est le seul endroit que tous les visiteurs voient. Beaucoup n'iront pas plus loin.

Ce qui doit s'y trouver : ce que vous faites, votre plus belle preuve, et un moyen de vous contacter.

{H_SITE}"""),

    # 94 · dim 07/02
    dict(template="plein", photo_fichier="temps-sablier#1",
         phrase="Le temps ne se trouve pas.\n*Il se libère.*",
         legende=f"""On attend souvent d'avoir du temps pour s'occuper de ce qui en ferait gagner. C'est un cercle qui ne se casse jamais tout seul.

Libérer une heure par semaine, puis une autre. C'est comme ça que ça commence.

{H_PME}"""),

    # 95 · lun 08/02
    dict(template="service", photo_fichier="accueil-sonnette#1", label="Pour les conciergeries",
         titre="Ce que l'assistant\n*vous transmet.*",
         points=["Un vrai problème signalé par un voyageur",
                 "Une question dont il n'a pas la réponse",
                 "Un intérêt pour l'un de vos services"],
         legende=f"""Un bon assistant ne répond pas à tout. Il sait quand vous passer la main.

Trois situations déclenchent une alerte avec le détail de la conversation : un problème réel, une information qu'il n'a pas, et un voyageur intéressé par un service. Le reste, il le traite seul.

{CONTACT}

{H_CONC}"""),

    # 96 · mer 10/02 · carrousel
    dict(template="carrousel", label="Identité visuelle",
         couverture=dict(template="constat", photo_fichier="design-typographie#1", label="Identité visuelle",
                         texte="Votre logo est-il\nvraiment bon ?", chute="Quatre tests,\ndix minutes."),
         pages=pages(
             ("Le test\n*de l'ongle.*", "Réduisez-le à la taille d'une photo de profil. S'il reste lisible, il le sera partout."),
             ("Le test\n*du noir et blanc.*", "Sans couleur, le reconnaît-on encore ? Imprimé en noir, il doit tenir."),
             ("Le test\n*du fond sombre.*", "Posé sur une photo ou un fond foncé, reste-t-il net ? Sinon, il lui faut une version claire."),
             ("Le test\n*des trois secondes.*", "Montrez-le trois secondes à quelqu'un, puis demandez-lui de le décrire. Ce qu'il retient, c'est votre logo."),
         ),
         fin=dict(titre="Un logo qui passe les quatre tests\n*travaille pour vous partout.*", fond=FIN),
         legende=f"""Pas besoin d'être graphiste pour évaluer un logo. Quatre tests simples suffisent à voir s'il tiendra sur tous vos supports.

Faites-les sur le vôtre. Si deux échouent, il est temps d'en parler.

{CONTACT}

{H_DESIGN}"""),

    # 97 · ven 12/02
    dict(template="constat", photo_fichier="design-croquis#4", label="Réseaux sociaux",
         texte="Le post parfait\nn'existe pas.", chute="Le post publié, si.",
         legende=f"""Beaucoup d'entreprises repoussent leurs publications en attendant la bonne photo, la bonne formule, le bon moment. Le compte reste vide, et personne ne voit le travail accompli.

Un post correct publié aujourd'hui vaut mieux qu'un post parfait publié jamais.

{H_RESEAUX}"""),

    # 98 · sam 13/02
    dict(template="carte", serie="astuce", photo_fichier="secteur-boulangerie#1", label=ASTUCE,
         titre="Laissez vos bonnes adresses,\n*pas celles d'un guide.*",
         texte="Boulangerie, pharmacie, restaurant du soir : ce sont ces adresses-là qu'on vous demandera.",
         legende=f"""L'astuce du samedi, côté accueil.

Les voyageurs demandent rarement le monument le plus proche. Ils demandent où acheter du pain demain matin et où dîner ce soir.

Vos adresses, notées une fois dans le livret, servent toute l'année. Et l'assistant peut les donner à son tour, parce que vous les lui avez confiées.

{H_ACC}"""),

    # 99 · dim 14/02
    dict(template="plein", photo_fichier="design-typographie#6",
         phrase="Un compte qu'on aime,\n*c'est un compte qu'on retrouve.*",
         legende=f"""Bonne Saint-Valentin.

Sur les réseaux, on s'attache aux comptes qu'on retrouve régulièrement, avec la même voix, le même soin. La régularité est une forme d'attention.

{H_RESEAUX}"""),

    # 100 · lun 15/02
    dict(template="terrain_photo", serie="terrain", photo_fichier="details-cles#4", label=TERRAIN,
         titre="Le jour où le voyageur réserve,\n*tout change.*",
         texte="Avant la réservation, la conversation vit à une adresse. Après, à une autre. Le bug n'apparaissait qu'avec une vraie réservation.",
         chute="Tester chaque cas, pas seulement le plus simple.",
         legende=f"""Une note de terrain, la plus coûteuse de l'année.

Pour un logiciel de location, une demande d'information et une réservation confirmée ne vivent pas au même endroit. Tant qu'un voyageur se renseigne, tout fonctionne. Dès qu'il réserve, l'ancienne adresse ne répond plus.

En test, aucune réservation réelle n'existait. Le bug est apparu en production. Depuis, chaque état possible d'une conversation a son test.

{H_CONC}"""),

    # 101 · mer 17/02
    dict(template="constat", photo_fichier="secteur-bureau#5", label="Site internet",
         texte="Changer un horaire\nsur votre site ?", chute="Vous ne devriez\nappeler personne.",
         legende=f"""Beaucoup de sites sont construits de telle façon qu'il faut rappeler le prestataire pour changer un horaire, une photo ou un texte. Résultat : le site n'est jamais à jour.

Je construis des sites dont vous modifiez vous-même le contenu, simplement, sans toucher au code.

{CONTACT}

{H_SITE}"""),

    # 102 · ven 19/02
    dict(template="constat", photo_fichier="secteur-atelier#1", label="En entreprise",
         texte="Le même tableau,\nrempli trois fois.", chute="Par trois personnes\ndifférentes.",
         legende=f"""Une commande arrive par mail. Quelqu'un la note dans un tableau. Quelqu'un d'autre la recopie dans le logiciel de facturation. Un troisième la reporte dans le planning.

Trois saisies, trois risques d'erreur, pour une seule information. Une seule saisie, reprise automatiquement partout ailleurs, suffit.

{CONTACT}

{H_PME}"""),

    # 103 · sam 20/02
    dict(template="carte", serie="astuce", photo_fichier="design-sceau#4", label=ASTUCE,
         titre="Une bonne idée\n*mérite plusieurs vies.*",
         texte="En story le jour même, en carrousel un mois plus tard, en rappel à la saison suivante.",
         legende=f"""L'astuce du samedi, côté réseaux.

Produire du contenu prend du temps. Le publier une seule fois, c'est le gaspiller. Une bonne idée peut revivre sous plusieurs formes, à plusieurs moments, sans lasser personne.

{H_RESEAUX}"""),

    # 104 · dim 21/02
    dict(template="plein", photo_fichier="auto-engrenages#5",
         phrase="Une machine répète.\n*Vous, vous décidez.*",
         legende=f"""C'est toute la répartition du travail que je propose. Ce qui se répète à l'identique part à une machine. Ce qui demande un jugement, une relation ou une décision reste à vous.

Bon dimanche.

{H_PME}"""),

    # 105 · lun 22/02
    dict(template="constat", photo_fichier="design-nuancier#4", label="Coulisses",
         texte="Ce visuel n'a été\ndessiné par personne.", chute="Il a été généré,\nà mes couleurs.",
         legende=f"""Chaque visuel de ce compte est produit par un programme à partir de mes gabarits : mes typographies, ma palette, mes règles de mise en page. Je n'ouvre aucun logiciel de dessin.

Résultat : une cohérence parfaite d'un post à l'autre, et des visuels prêts en quelques secondes.

{H_RESEAUX} #design"""),

    # 106 · mer 24/02 · carrousel
    dict(template="carrousel", label="Pour les conciergeries",
         couverture=dict(template="constat", photo_fichier="astuce-lampe#3", label="Pour les conciergeries",
                         texte="23h04.\nUn message arrive.", chute="Voici ce qui se passe\nensuite."),
         pages=pages(
             ("Il lit\n*toute la conversation.*", "Pas seulement le dernier message, pour ne jamais répéter ce qui a déjà été dit."),
             ("Il vérifie\n*le logement.*", "Les informations de la fiche, le calendrier, le wifi. Uniquement ce que vous lui avez confié."),
             ("Il répond\n*dans la bonne langue.*", "Avec votre ton, sans formule toute faite, sans lien ni numéro que la plateforme bloquerait."),
             ("Ou il vous passe\n*la main.*", "Un problème, une information manquante, une demande de service : vous êtes prévenu avec le détail."),
         ),
         fin=dict(titre="Une réponse juste,\n*même quand vous dormez.*", fond=FIN),
         legende=f"""Que se passe-t-il quand un voyageur écrit à 23h04 à une conciergerie équipée ? En quelques instants, quatre étapes s'enchaînent.

Rien de magique. Des règles précises, testées sur de vraies conversations.

{CONTACT}

{H_CONC}"""),

    # 107 · ven 26/02
    dict(template="constat", photo_fichier="design-papeterie#6", label="Identité visuelle",
         texte="Votre carte de visite\net votre site", chute="ne se connaissent pas.",
         legende=f"""Une couleur sur la carte de visite, une autre sur le site, une troisième sur les réseaux. Chaque support a été fait à un moment différent, par une personne différente.

Pour un client, ce sont trois entreprises. Une charte graphique les réunit.

{H_DESIGN}"""),

    # 108 · sam 27/02
    dict(template="carte", serie="astuce", photo_fichier="astuce-rue#4", label=ASTUCE,
         titre="Le stationnement\n*se décrit avec précision.*",
         texte="Gratuit ou payant, à quelle distance, dans quelle rue. C'est souvent la toute première question.",
         legende=f"""L'astuce du samedi, côté accueil.

« Stationnement facile » ne veut rien dire pour quelqu'un qui arrive de nuit dans une ville inconnue. Le nom de la rue, la distance à pied, le prix s'il y en a un : trois informations qui évitent un appel depuis la voiture.

{H_ACC}"""),

    # 109 · dim 28/02
    dict(template="plein", photo_fichier="saison-printemps#5",
         phrase="Le printemps approche.\n*Votre site est prêt ?*",
         legende=f"""Avec les beaux jours, les recherches reprennent : des voyageurs, des clients, des projets. Beaucoup commencent par regarder votre site.

S'il date, c'est maintenant qu'il faut s'en occuper. Pas en juin.

{H_SITE}"""),

    # ─────────────── Mars ───────────────
    # 110 · lun 01/03
    dict(template="terrain_photo", serie="ingenieur", photo_fichier="auto-engrenages#1", label=INGE,
         titre="Une automatisation\n*doit s'expliquer en une phrase.*",
         texte="Si personne ne comprend ce qu'elle fait, personne ne saura la corriger le jour où elle se trompe.",
         chute="Simple à expliquer, simple à réparer.",
         legende=f"""Une note d'ingénieur, sur ce qui fait durer un système.

Une automatisation que seul son créateur comprend est une dépendance, pas un gain. Chaque étape doit pouvoir se dire simplement : quand ceci arrive, on fait cela.

Si l'explication tient en une phrase, l'entreprise garde la main.

{H_PME2}"""),

    # 111 · mer 03/03
    dict(template="constat", photo_fichier="interieur-lit#6", label="Pour les conciergeries",
         texte="Le voyageur ne sait pas\nque vous dormiez.", chute="Il sait seulement\nqu'on lui a répondu.",
         legende=f"""Pour un voyageur, il n'y a pas d'heure de bureau. Il y a une question, et une réponse qui arrive, ou pas.

Ce qu'il retient de votre conciergerie se joue souvent là, à une heure où vous avez tous les droits de dormir.

{H_CONC}"""),

    # 112 · ven 05/03
    dict(template="constat", photo_fichier="strategie-echecs#6", label="Réseaux sociaux",
         texte="Vos concurrents n'ont pas\nplus de temps que vous.", chute="Ils ont un système.",
         legende=f"""Quand un concurrent publie chaque semaine, on imagine une équipe dédiée ou des soirées sacrifiées. C'est rarement le cas.

La différence tient presque toujours à une organisation : des contenus préparés d'avance, et une publication qui ne dépend pas de l'humeur du jour.

{CONTACT}

{H_RESEAUX}"""),

    # 113 · sam 06/03
    dict(template="carte", serie="astuce", photo_fichier="design-croquis#2", label=ASTUCE,
         titre="Décrivez vos images\n*pour ceux qui ne les voient pas.*",
         texte="Un texte alternatif sur chaque photo : les lecteurs d'écran le lisent, les moteurs de recherche aussi.",
         legende=f"""L'astuce du samedi, côté site.

Une courte description sur chaque image rend votre site accessible aux personnes malvoyantes. Et elle aide les moteurs de recherche à comprendre ce que vous montrez.

Deux raisons de le faire, pour quelques secondes par photo.

{H_SITE}"""),

    # 114 · dim 07/03
    dict(template="plein", photo_fichier="porte-lumiere#4",
         phrase="Déléguer,\n*ce n'est pas disparaître.*",
         legende=f"""Confier une partie du travail à un système ne vous éloigne pas de vos clients. Ça vous rend disponible pour ce qui compte vraiment : les décisions, les imprévus, la relation.

Bon dimanche.

{H_PME}"""),

    # 115 · lun 08/03
    dict(template="service", photo_fichier="secteur-bureau#2", label="Site internet",
         titre="Ce que votre site\n*doit dire d'emblée.*",
         points=["Ce que vous faites, en une phrase",
                 "Pour qui vous le faites",
                 "Comment vous joindre, en un geste"],
         legende=f"""Un visiteur décide très vite s'il reste ou s'il repart. Pendant ces premières secondes, votre page d'accueil doit répondre à trois questions, sans qu'il ait à chercher.

Tout le reste, l'histoire, l'équipe, les détails, peut venir après.

{CONTACT}

{H_SITE}"""),

    # 116 · mer 10/03 · carrousel
    dict(template="carrousel", label="Automatisation",
         couverture=dict(template="constat", photo_fichier="auto-engrenages#6", label="Automatisation",
                         texte="Quatre automatisations\nqui changent une semaine.", chute="Aucune ne remplace\npersonne."),
         pages=pages(
             ("Les relances\n*de devis.*", "Elles partent au bon moment, poliment, et s'arrêtent dès que le client répond."),
             ("La prise\n*de rendez-vous.*", "Le client choisit parmi vos créneaux réels. Plus d'allers-retours pour trouver une date."),
             ("La recopie\n*d'une demande.*", "Un mail ou un formulaire arrive, les informations rejoignent le bon tableau sans être retapées."),
             ("Les questions\n*qui reviennent.*", "Horaires, délais, documents : une réponse juste, à toute heure, et vous êtes prévenu pour le reste."),
         ),
         fin=dict(titre="Moins de répétitions.\n*Plus de métier.*", fond=FIN),
         legende=f"""Pas besoin d'un grand projet pour sentir la différence. Ces quatre automatisations, prises une par une, rendent déjà des heures chaque semaine.

Aucune ne remplace une personne. Toutes lui rendent du temps.

{CONTACT}

{H_PME}"""),

    # 117 · ven 12/03
    dict(template="constat", photo_fichier="region-nice#5", label="Pour les conciergeries",
         texte="L'été dernier, combien\nde messages après 23h ?", chute="Cet été peut être différent.",
         legende=f"""Les réservations d'été arrivent. Dans quelques mois, les journées commenceront tôt et les messages finiront tard.

Ce qui se prépare en mars se ressent en août : des réponses justes, à toute heure, et des soirées qui redeviennent les vôtres.

{CONTACT}

{H_CONC}"""),

    # 118 · sam 13/03
    dict(template="carte", serie="astuce", photo_fichier="details-carnet#1", label=ASTUCE,
         titre="Laissez vos clients\n*réserver seuls.*",
         texte="Un lien de prise de rendez-vous avec vos vrais créneaux. Plus d'allers-retours pour trouver une date.",
         legende=f"""L'astuce du samedi, côté organisation.

Trouver un créneau par téléphone ou par mail prend souvent plus de temps que le rendez-vous lui-même. Un lien de réservation, relié à votre agenda, règle la question en quelques secondes.

{H_PME}"""),

    # 119 · dim 14/03
    dict(template="plein", photo_fichier="interieur-chambre#4",
         phrase="Votre métier, c'est accueillir.\n*Pas répéter le code wifi.*",
         legende=f"""Accueillir, c'est anticiper, rassurer, faire plaisir. Répéter la même information vingt fois par semaine, ce n'est pas accueillir. C'est une tâche.

Et une tâche qui se répète peut se confier.

{H_CONC}"""),

    # 120 · lun 15/03
    dict(template="terrain_photo", serie="design", photo_fichier="texture-papier#5", label=DESIGN,
         titre="L'espace vide\n*n'est pas du vide.*",
         texte="Des marges généreuses, peu d'éléments par page : c'est ce qui donne l'impression de qualité.",
         chute="Le luxe respire.",
         legende=f"""Note de design numéro cinq.

On a souvent envie de tout montrer, et donc de tout serrer. L'effet est inverse : une page chargée paraît bon marché, une page aérée paraît soignée.

Retirez un élément de chaque page. Vous verrez la différence.

{H_DESIGN}"""),

    # 121 · mer 17/03
    dict(template="constat", photo_fichier="commerce-vitrine#2", label="Réseaux sociaux",
         texte="Avant de vous appeler,\non regarde votre compte.", chute="Qu'y trouve-t-on ?",
         legende=f"""Un compte Instagram est devenu une seconde vitrine. Beaucoup de clients y jettent un œil avant de vous contacter, pour voir si vous êtes actif, sérieux, et si votre travail leur plaît.

Un compte vivant rassure. Un compte abandonné fait douter.

{H_RESEAUX}"""),

    # 122 · ven 19/03
    dict(template="constat", photo_fichier="design-sceau#5", label="En entreprise",
         texte="Un devis sans réponse\nn'est pas un non.", chute="C'est souvent un oubli.",
         legende=f"""Un client qui ne répond pas a souvent simplement été pris par autre chose. Sans relance, le devis dort, et le client finit par signer ailleurs, parfois par simple commodité.

Une relance polie, au bon moment, ramène une partie de ces devis à la vie. Elle peut partir toute seule.

{CONTACT}

{H_PME}"""),

    # 123 · sam 20/03
    dict(template="carte", serie="astuce", photo_fichier="accueil-sonnette#6", label=ASTUCE,
         titre="Répondez aux avis,\n*même aux bons.*",
         texte="Un merci personnalisé montre qu'il y a quelqu'un derrière l'annonce. Les futurs voyageurs lisent aussi vos réponses.",
         legende=f"""L'astuce du samedi, côté accueil.

On répond volontiers aux avis négatifs, pour se défendre. On oublie les bons. Pourtant une réponse chaleureuse à un bel avis est lue par tous ceux qui hésitent encore à réserver.

{H_ACC}"""),

    # 124 · dim 21/03
    dict(template="plein", photo_fichier="saison-printemps#6",
         phrase="Le printemps est là.\n*Les voyageurs aussi.*",
         legende=f"""Premier week-end de printemps. Les demandes reprennent, les séjours courts se multiplient, les questions reviennent.

C'est le moment de vérifier que tout est prêt pour la saison.

{H_CONC}"""),

    # 125 · lun 22/03
    dict(template="service", photo_fichier="normandie-deauville#4", label="Avant la saison",
         titre="Trois vérifications\n*avant l'été.*",
         points=["Vos annonces sont-elles à jour ?",
                 "Vos réponses types sont-elles justes ?",
                 "Qui répond pendant vos congés ?"],
         legende=f"""La saison se prépare maintenant, pas le premier samedi de juillet.

Des annonces fidèles, des réponses vérifiées, et une solution pour les jours où vous ne serez pas joignable. Trois vérifications simples qui évitent les pires semaines de l'été.

{CONTACT}

{H_CONC}"""),

    # 126 · mer 24/03 · carrousel
    dict(template="carrousel", label="Site internet",
         couverture=dict(template="constat", photo_fichier="commerce-vitrine#1", label="Site internet",
                         texte="Un site qui fait appeler\ntient en quatre blocs.", chute="Dans cet ordre."),
         pages=pages(
             ("Ce que vous faites,\n*en une phrase.*", "Pas un slogan. Une phrase qu'un client pourrait répéter à quelqu'un d'autre."),
             ("Pour qui,\n*précisément.*", "Le visiteur doit se reconnaître immédiatement. Sinon, il pense que ce n'est pas pour lui."),
             ("La preuve.", "Vos réalisations, vos photos, les mots de vos clients. Ce qui rend vos promesses crédibles."),
             ("Comment\n*vous joindre.*", "Un bouton visible, un numéro qui lance l'appel, une réponse rapide. Le dernier pas doit être le plus facile."),
         ),
         fin=dict(titre="Quatre blocs,\n*et un site qui travaille pour vous.*", fond=FIN),
         legende=f"""Beaucoup de sites empilent les rubriques sans ordre précis. Ceux qui font réellement appeler suivent presque toujours la même logique.

Ce que vous faites, pour qui, la preuve, et comment vous joindre. Faites glisser pour le détail.

{CONTACT}

{H_SITE}"""),

    # 127 · ven 26/03
    dict(template="constat", photo_fichier="region-corse#5", label="Réseaux sociaux",
         texte="Cet été, votre compte\nva-t-il se taire ?", chute="Il peut publier sans vous.",
         legende=f"""L'été, c'est souvent le moment où les comptes des entreprises s'arrêtent : trop de travail, puis les congés. C'est aussi le moment où beaucoup de clients ont le temps de regarder.

Un calendrier préparé au printemps publie tout l'été, même pendant vos vacances.

{CONTACT}

{H_RESEAUX}"""),

    # 128 · sam 27/03
    dict(template="carte", serie="astuce", photo_fichier="astuce-rue#5", label=ASTUCE,
         titre="Testez votre site\n*dehors, sur votre téléphone.*",
         texte="En 4G, au soleil, d'une main. C'est dans ces conditions que vos clients le découvrent.",
         legende=f"""L'astuce du samedi, côté site.

On vérifie son site sur un grand écran, au bureau, avec une bonne connexion. Vos clients, eux, le découvrent souvent dans la rue, sur un petit écran, avec une main libre.

Faites le test. Tout ce qui est difficile là est à corriger.

{H_SITE}"""),

    # 129 · dim 28/03
    dict(template="plein", photo_fichier="saison-printemps#2",
         phrase="Joyeuses Pâques.\n*Un dimanche pour vous.*",
         legende="""Joyeuses Pâques à toutes et à tous.

Aujourd'hui, que les questions attendent et que le téléphone reste dans la poche.

#paques #entrepreneur #conciergerie"""),

    # 130 · lun 29/03
    dict(template="service", photo_fichier="secteur-atelier#2", label="Pourquoi DelorIA",
         titre="Un ingénieur,\n*pas une plateforme.*",
         points=["Je configure tout avec vous",
                 "Je surveille ce que j'installe",
                 "Je réponds quand vous m'écrivez"],
         signature="PARTOUT EN FRANCE",
         legende=f"""Une plateforme vous vend un abonnement et vous laisse seul avec les réglages. Je fais l'inverse : je comprends votre façon de travailler, je configure, je teste, et je reste joignable.

Des conciergeries et des entreprises partout en France, un seul interlocuteur.

{CONTACT}

#automatisation #conciergerie #siteinternet #reseauxsociaux #pme"""),

    # ─────────────── Avril ───────────────
    # 131 · mer 31/03
    dict(template="constat", photo_fichier="secteur-artisan#3", label="En entreprise",
         texte="Qu'est-ce qui vous prend encore\ndu temps chaque semaine ?", chute="Commençons par là.",
         legende=f"""Pas besoin de tout revoir. La bonne question tient en une ligne : quelle tâche revient chaque semaine et vous agace à chaque fois ?

C'est presque toujours la meilleure première automatisation.

{CONTACT}

{H_PME}"""),

    # 132 · ven 02/04
    dict(template="plein", photo_fichier="region-nice#4",
         phrase="Six mois de posts.\n*Tous partis seuls.*",
         legende=f"""Il y a six mois, j'ai préparé le calendrier de ce compte. Depuis, chaque publication prévue est partie seule, à l'heure, sans que j'y pense.

Ce n'est pas un exploit. C'est un système. Et il peut fonctionner pour votre entreprise.

{CONTACT}

{H_RESEAUX}"""),

    # 133 · sam 03/04
    dict(template="carte", serie="astuce", photo_fichier="interieur-chambre#5", label=ASTUCE,
         titre="Dormez une nuit\n*dans votre logement.*",
         texte="Ou demandez à un proche. On découvre toujours un détail : un store qui coince, une lampe trop faible.",
         legende=f"""L'astuce du samedi, côté accueil.

Vous connaissez votre logement par cœur, et c'est justement le problème. Une nuit sur place, avec les yeux d'un voyageur, révèle ce qu'aucune visite rapide ne montre.

{H_ACC}"""),

    # 134 · dim 04/04
    dict(template="plein", photo_fichier="normandie-cote#1",
         phrase="La saison commence.\n*Cette fois, vous êtes prêts.*",
         legende=f"""Les beaux jours sont là, les voyageurs arrivent. Cette année, les réponses partent à l'heure, les annonces sont à jour et vos soirées vous appartiennent.

Bonne saison à toutes les conciergeries.

{H_CONC}"""),
]


# ─────────────────────────────────────────────────────────────────────────────
# Publication quotidienne : deux séries ajoutées le mardi et le jeudi.
# MARDIS : développement d'entreprise. JEUDIS : « L'automatisation du jeudi »,
# une tâche concrète par semaine, avant et après. Dans l'ordre des dates.
# ─────────────────────────────────────────────────────────────────────────────

H_DEV = "#developpement #entrepreneur #pme #strategie"
JEUDI = "L'automatisation du jeudi"


def jeudi(photo, titre, avant, apres, chute, legende):
    return dict(template="terrain_photo", serie="jeudi", label=JEUDI, photo_fichier=photo,
                titre=titre, avant=avant, apres=apres, chute=chute, legende=legende)


MARDIS = [
    # 06/10
    dict(template="constat", photo_fichier="dev-boussole#3", label="Développement",
         texte="Vos meilleurs clients\nvous ont trouvé par hasard ?", chute="Le hasard n'est pas\nune stratégie.",
         legende=f"""Un ami qui recommande, une recherche tombée au bon moment, un passage devant la vitrine. Beaucoup d'entreprises doivent leurs meilleurs clients à la chance.

La chance ne se planifie pas. Une présence régulière, un site clair et des réponses rapides, si.

{CONTACT}

{H_DEV}"""),
    # 13/10
    dict(template="constat", photo_fichier="dev-poignee#2", label="Développement",
         texte="Le bouche-à-oreille\nest votre meilleur canal.", chute="Jusqu'au jour\noù il s'arrête.",
         legende=f"""Le bouche-à-oreille est précieux : il amène des clients qui ont déjà confiance. Mais il ne se commande pas, il ne se prévoit pas, et il s'arrête sans prévenir.

Les entreprises qui durent le complètent par une présence visible et régulière, qui travaille même quand personne ne parle d'elles.

{H_DEV}"""),
    # 20/10
    dict(template="constat", photo_fichier="dev-telephone#4", label="Développement",
         texte="Le premier qui répond\npart avec une longueur d'avance.", chute="Souvent, c'est lui\nqui signe.",
         legende=f"""Quand un client demande plusieurs devis, il les compare. Mais il compare aussi, sans le dire, la rapidité, la clarté et le soin de chaque réponse.

Une réponse rapide dit : ici, on s'occupe de vous. C'est souvent ce qui fait pencher la balance.

{CONTACT}

{H_DEV}"""),
    # 27/10
    dict(template="constat", photo_fichier="dev-escalier#3", label="Développement", voile=0.72,
         texte="Dire oui à tout le monde,", chute="c'est ne parler à personne.",
         legende=f"""Une entreprise qui fait tout pour tout le monde a du mal à dire ce qu'elle fait de mieux. Et un client qui hésite choisit celui qui semble fait pour lui.

Choisir pour qui vous travaillez, c'est rendre votre message évident pour ceux-là.

{H_DEV}"""),
    # 03/11
    dict(template="constat", photo_fichier="dev-calcul#3", label="Développement",
         texte="Baisser votre prix\nne règle pas le problème.", chute="Le client ne voyait\npas la valeur.",
         legende=f"""Quand un devis ne se signe pas, le premier réflexe est souvent de baisser le prix. Parfois c'est justifié. Souvent, le vrai problème est ailleurs : le client n'a pas compris ce qu'il obtenait.

Une offre mieux expliquée se vend mieux qu'une offre moins chère.

{H_DEV}"""),
    # 10/11
    dict(template="constat", photo_fichier="dev-matin#6", label="Développement",
         texte="Un client satisfait\nne revient pas tout seul.", chute="Il revient quand\non pense à lui.",
         legende=f"""Un client content vous oublie rarement par déception. Il vous oublie parce qu'il a autre chose à faire.

Un message au bon moment, une nouvelle utile, une attention un an après : garder le lien ne demande pas beaucoup, à condition d'y penser. Ou de laisser un système y penser.

{H_DEV}"""),
    # 17/11
    dict(template="constat", photo_fichier="dev-signature#5", label="Développement",
         texte="Vos clients contents\nne laissent pas d'avis.", chute="Sauf si on\nle leur demande.",
         legende=f"""Les clients mécontents écrivent spontanément. Les clients satisfaits, rarement. Résultat : vos avis ne reflètent pas vraiment votre travail.

Une demande simple, envoyée au bon moment après la prestation, change l'équilibre. Et elle peut partir toute seule.

{H_DEV}"""),
    # 24/11
    dict(template="plein", photo_fichier="details-cafe#2",
         phrase="Vous travaillez dans votre entreprise.\n*Quand travaillez-vous dessus ?*",
         legende=f"""Répondre, produire, livrer, facturer : le quotidien remplit toutes les heures. Et il ne reste plus de temps pour ce qui ferait grandir l'entreprise.

Chaque tâche répétitive confiée à une machine, c'est du temps rendu pour réfléchir, prospecter, améliorer.

{H_DEV}"""),
    # 01/12
    dict(template="constat", photo_fichier="dev-salle#1", label="Développement",
         texte="Tout passe par vous ?", chute="Alors tout vous attend.",
         legende=f"""Les devis, les questions, les validations, les imprévus : dans beaucoup de petites entreprises, tout remonte au dirigeant. C'est rassurant, jusqu'au jour où il n'est pas disponible.

Déléguer, à une personne ou à un système, commence par une question : qu'est-ce qui pourrait se faire sans moi ?

{H_DEV}"""),
    # 08/12
    dict(template="constat", photo_fichier="dev-signature#1", label="Développement",
         texte="Si ce n'est écrit nulle part,", chute="ça n'existe pas.",
         legende=f"""Une procédure qui n'existe que dans une tête se perd au premier départ, au premier congé, au premier nouveau salarié.

L'écrire, c'est la rendre transmissible. Et une procédure écrite est aussi la première étape pour l'automatiser.

{H_PME}"""),
    # 15/12
    dict(template="service", photo_fichier="dev-calcul#5", label="Développement",
         titre="Trois chiffres\n*à suivre chaque mois.*",
         points=["Le nombre de demandes reçues",
                 "Le délai moyen de réponse",
                 "Le nombre de devis signés"],
         legende=f"""Pas besoin d'un tableau de bord compliqué pour piloter une petite entreprise. Trois chiffres suffisent pour voir si les choses avancent : ce qui arrive, la vitesse à laquelle vous répondez, et ce qui se signe.

Et ces trois chiffres peuvent se calculer tout seuls.

{CONTACT}

{H_DEV}"""),
    # 22/12
    dict(template="plein", photo_fichier="interieur-cheminee#3",
         phrase="Janvier se prépare\n*en décembre.*",
         legende=f"""Les semaines de fin d'année sont souvent plus calmes. C'est le bon moment pour poser ce qui fera gagner du temps toute l'année prochaine : une offre plus claire, un site à jour, une première tâche automatisée.

En janvier, il sera déjà temps d'en profiter.

{H_DEV}"""),
    # 29/12
    dict(template="constat", photo_fichier="auto-colis#3", label="Développement",
         texte="Qu'avez-vous refait\ncinquante fois cette année ?", chute="Voilà votre première\nautomatisation de 2027.",
         legende=f"""Avant de fermer l'année, une question simple : quelle tâche avez-vous répétée le plus souvent ? Un mail, une relance, une recopie, un document à préparer.

C'est presque toujours la meilleure candidate pour une première automatisation.

{CONTACT}

{H_PME}"""),
    # 05/01
    dict(template="constat", photo_fichier="dev-matin#1", label="Développement",
         texte="Un objectif sans système", chute="reste une bonne intention.",
         legende=f"""Publier chaque semaine, relancer chaque devis, répondre dans l'heure : les résolutions de janvier sont souvent les bonnes. Ce qui manque, c'est le moyen de les tenir quand le quotidien reprend le dessus.

Un système ne remplace pas la volonté. Il la rend inutile.

{H_DEV}"""),
    # 12/01
    dict(template="constat", photo_fichier="dev-telephone#2", label="Développement",
         texte="Vos clients ne veulent pas\nun outil de plus.", chute="Ils veulent une réponse.",
         legende=f"""Une application à télécharger, un espace client à créer, un formulaire de plus : ce qui simplifie votre travail complique parfois celui de vos clients.

La bonne automatisation est invisible pour eux. Ils posent une question, ils obtiennent une réponse.

{H_DEV}"""),
    # 19/01
    dict(template="constat", photo_fichier="auto-machine#2", label="Développement",
         texte="Grandir sans s'organiser,", chute="c'est multiplier les urgences.",
         legende=f"""Plus de clients, c'est plus de demandes, plus de devis, plus de relances. Si tout se fait encore à la main, chaque nouveau client ajoute du désordre autant que du chiffre d'affaires.

S'organiser avant de grandir, c'est grandir sans s'épuiser.

{H_DEV}"""),
    # 26/01
    dict(template="constat", photo_fichier="commerce-vitrine#5", label="Développement",
         texte="Vous vendez de la qualité ?", chute="Votre image doit\nle montrer d'abord.",
         legende=f"""Un client juge la qualité de votre travail avant de l'avoir vu : sur votre site, vos réseaux, vos documents. Une image négligée fait douter d'un travail soigné.

L'image n'est pas un luxe. C'est la première preuve.

{H_DESIGN}"""),
    # 02/02
    dict(template="constat", photo_fichier="dev-phare#4", label="Développement",
         texte="On oublie vite\nune entreprise silencieuse.", chute="Même quand elle\ntravaille bien.",
         legende=f"""Entre deux commandes, beaucoup d'entreprises disparaissent de l'esprit de leurs clients. Non pas parce qu'ils sont déçus, mais parce qu'ils n'y pensent plus.

Une présence régulière, même discrète, suffit à rester la première idée quand le besoin revient.

{H_RESEAUX}"""),
    # 09/02
    dict(template="constat", photo_fichier="dev-telephone#3", label="Développement",
         texte="Vos clients sont\ndans votre téléphone ?", chute="Ils devraient être\ndans un fichier.",
         legende=f"""Les coordonnées dans le téléphone, l'historique dans les mails, les devis dans un dossier : l'information existe, mais elle est éparpillée. Et elle part avec le téléphone.

Un fichier clients, même simple, est la mémoire de l'entreprise. C'est aussi lui qui rend possibles les relances et les suivis automatiques.

{H_PME}"""),
    # 16/02
    dict(template="constat", photo_fichier="dev-poignee#4", label="Développement",
         texte="Un nouveau client,\nce sont toujours les mêmes étapes.", chute="Pourquoi les refaire\nà la main ?",
         legende=f"""Message de bienvenue, documents à envoyer, informations à demander, rendez-vous à fixer : l'arrivée d'un client suit presque toujours le même chemin.

Ce chemin peut se dérouler tout seul, étape par étape, avec votre ton. Vous n'intervenez que là où vous êtes utile.

{CONTACT}

{H_PME}"""),
    # 23/02
    dict(template="constat", photo_fichier="auto-colis#2", label="Développement",
         texte="Promettez moins.", chute="Livrez plus tôt.",
         legende=f"""Un délai tenu rassure. Un délai battu marque. À l'inverse, une promesse trop ambitieuse transforme un bon travail en déception.

Mieux vaut annoncer un délai réaliste et surprendre que l'inverse.

{H_DEV}"""),
    # 02/03
    dict(template="service", photo_fichier="dev-escalier#1", label="Développement",
         titre="Trois questions\n*avant de grandir.*",
         points=["Qu'est-ce qui dépend encore de vous seul ?",
                 "Qu'est-ce qui se répète chaque semaine ?",
                 "Qu'est-ce qui se perd entre deux outils ?"],
         legende=f"""Avant de chercher plus de clients, il vaut la peine de vérifier que l'entreprise peut les absorber. Trois questions suffisent à repérer ce qui craquera en premier.

Les réponses donnent souvent la liste des premières choses à organiser, ou à automatiser.

{CONTACT}

{H_DEV}"""),
    # 09/03
    dict(template="constat", photo_fichier="auto-clavier#2", label="Développement",
         texte="Répondre vite", chute="ne veut pas dire répondre mal.",
         legende=f"""La vitesse compte, mais une réponse rapide et approximative coûte plus cher qu'une réponse juste arrivée un peu plus tard.

L'objectif n'est pas de répondre à tout, tout de suite. C'est de répondre juste, vite, et de savoir quand passer la main.

{H_DEV}"""),
    # 16/03
    dict(template="constat", photo_fichier="details-cafe#4", label="Développement",
         texte="Un client qui vous recommande", chute="est votre meilleur commercial.",
         legende=f"""Aucune publicité n'a la force d'une recommandation. Encore faut-il la faciliter : un client satisfait recommande plus volontiers quand on le lui demande, au bon moment, simplement.

C'est un geste commercial. Et un geste qui peut se programmer.

{H_DEV}"""),
    # 23/03
    dict(template="edito", photo_fichier="dev-salle#6", label="Développement",
         titre="Une entreprise *qui tourne sans vous.*",
         texte="Des réponses qui partent, des relances qui se font, des publications qui sortent. Vous gardez les décisions.",
         pictos=[dict(icone="message", texte="Réponses\nautomatiques"), dict(icone="fleche", texte="Relances\nprogrammées"),
                 dict(icone="calendrier", texte="Publications\nplanifiées")],
         cta="Écrivez-moi en privé",
         legende=f"""C'est l'objectif de tout ce que je construis : une entreprise où le répétitif avance sans vous, et où votre temps va aux décisions, aux clients et au métier.

Pas en une fois. Une tâche après l'autre.

{CONTACT}

{H_PME}"""),
    # 30/03
    dict(template="constat", photo_fichier="dev-phare#6", label="Développement",
         texte="Votre prochain client\nvous cherche peut-être déjà.", chute="Êtes-vous facile\nà trouver ?",
         legende=f"""Au printemps, les projets reprennent et les recherches aussi. Un site clair, un compte actif, une réponse rapide : trois conditions pour être trouvé, et choisi.

{CONTACT}

{H_DEV}"""),
]

JEUDIS = [
    # 01/10
    jeudi("dev-signature#6", "La relance d'un devis\n*sans réponse.*",
          "on y pense trop tard, ou jamais.", "elle part seule au bon moment, et s'arrête dès que le client répond.",
          "Un devis qui dort n'est pas un refus.",
          f"""Nouvelle série : chaque jeudi, une tâche concrète qu'on peut confier à une machine.

Première de la liste, la relance de devis. Elle rapporte, elle est simple à mettre en place, et c'est pourtant l'une des tâches les plus souvent oubliées.

{CONTACT}

{H_PME}"""),
    # 08/10
    jeudi("temps-horloge#4", "La confirmation\n*de rendez-vous.*",
          "un appel pour confirmer, un oubli de temps en temps.", "une confirmation immédiate, puis un rappel la veille.",
          "Moins d'oublis, moins de créneaux perdus.",
          f"""L'automatisation du jeudi.

Un rendez-vous oublié, c'est un créneau perdu pour vous et un client gêné. Une confirmation au moment de la prise de rendez-vous, puis un rappel la veille, règlent la question sans que personne n'ait à y penser.

{H_PME}"""),
    # 15/10
    jeudi("design-sceau#6", "La demande\n*d'avis client.*",
          "on n'ose pas, ou on oublie.", "un message poli part quelques jours après la prestation, avec le lien direct.",
          "Les clients contents écrivent quand on le leur demande.",
          f"""L'automatisation du jeudi.

Un avis se demande au bon moment : assez tôt pour que le souvenir soit frais, assez tard pour que le client ait profité du résultat. Ce moment se programme une fois pour toutes.

{H_PME}"""),
    # 22/10
    jeudi("auto-clavier#1", "Le formulaire\n*de contact.*",
          "un mail à recopier dans un tableau.", "la demande rejoint le tableau, et le client reçoit un accusé de réception immédiat.",
          "Rien ne se perd, personne n'attend.",
          f"""L'automatisation du jeudi.

Chaque demande qui arrive par votre site mérite deux choses : être notée quelque part, et rassurer celui qui l'a envoyée. Les deux peuvent se faire à la seconde, sans vous.

{H_PME}"""),
    # 29/10
    jeudi("dev-calcul#6", "La facture\n*après le devis signé.*",
          "on retape les mêmes lignes.", "la facture se prépare à partir du devis, il ne reste qu'à vérifier et envoyer.",
          "Une seule saisie, aucune recopie.",
          f"""L'automatisation du jeudi.

Tout ce qui figure sur la facture existe déjà dans le devis. Le retaper, c'est perdre du temps et risquer une erreur. Une seule saisie suffit.

{H_PME}"""),
    # 05/11
    jeudi("auto-colis#5", "Le tri\n*des e-mails entrants.*",
          "tout arrive au même endroit, l'urgent se noie.", "chaque demande est classée, et la bonne personne est prévenue.",
          "L'urgent reste visible.",
          f"""L'automatisation du jeudi.

Devis, réclamations, factures, publicités : quand tout arrive pêle-mêle, ce qui compte se perd. Un tri automatique range chaque message au bon endroit, dès son arrivée.

{H_PME}"""),
    # 12/11
    jeudi("auto-dominos#4", "Les questions\n*qui reviennent.*",
          "la même réponse écrite vingt fois.", "une réponse juste part aussitôt, et vous êtes prévenu pour ce qui sort du cadre.",
          "Vous ne répondez plus qu'à l'inédit.",
          f"""L'automatisation du jeudi.

Horaires, délais, documents à fournir, modalités : une grande partie des questions reçues ont toujours la même réponse. Elle peut partir tout de suite, à toute heure.

{CONTACT}

{H_PME}"""),
    # 19/11
    jeudi("dev-matin#2", "Le point\n*du lundi matin.*",
          "on ouvre cinq outils pour savoir où on en est.", "un résumé de la semaine arrive dans votre boîte mail.",
          "Les chiffres viennent à vous.",
          f"""L'automatisation du jeudi.

Demandes reçues, devis envoyés, factures en attente : les chiffres de la semaine peuvent se rassembler seuls et vous attendre le lundi matin, dans un seul message.

{H_PME}"""),
    # 26/11
    jeudi("dev-matin#4", "Les publications\n*sur les réseaux.*",
          "on publie quand on y pense.", "un calendrier préparé d'avance, et chaque post part seul, au jour prévu.",
          "Ce compte en est la preuve.",
          f"""L'automatisation du jeudi.

Ce post est parti tout seul. Le calendrier de ce compte est écrit des mois à l'avance, et un programme publie chaque jour à 17h30.

{CONTACT}

{H_RESEAUX}"""),
    # 03/12
    jeudi("dev-poignee#3", "L'accueil\n*d'un nouveau client.*",
          "les mêmes mails et documents renvoyés à chaque fois.", "un parcours de bienvenue qui se déroule tout seul.",
          "Un bon départ, à chaque fois.",
          f"""L'automatisation du jeudi.

Les premiers jours d'une relation client donnent le ton. Un parcours d'accueil prévu une fois, avec votre ton, assure que personne n'est oublié et que rien ne manque.

{H_PME}"""),
    # 10/12
    jeudi("dev-calcul#1", "La relance\n*d'une facture impayée.*",
          "on hésite, on attend, on oublie.", "un rappel courtois part à l'échéance, puis un second si besoin.",
          "Votre trésorerie ne dépend plus de votre mémoire.",
          f"""L'automatisation du jeudi.

Relancer un client pour un paiement n'est agréable pour personne. Un rappel automatique, poli et à la bonne date, enlève la gêne et accélère les règlements.

{H_PME}"""),
    # 17/12
    jeudi("dev-salle#4", "Le compte rendu\n*de réunion.*",
          "des notes éparpillées, rarement envoyées.", "un résumé clair et les actions de chacun, envoyés à tous.",
          "Ce qui a été décidé ne se perd plus.",
          f"""L'automatisation du jeudi.

Une réunion sans compte rendu est souvent une réunion à refaire. Un résumé préparé automatiquement, avec qui fait quoi, garde la trace de chaque décision.

{H_PME}"""),
    # 24/12
    jeudi("astuce-deux-verres#2", "Le message d'absence\n*pendant les fêtes.*",
          "on oublie, les clients attendent sans savoir.", "une réponse avec votre date de retour et un contact en cas d'urgence.",
          "Vous fermez, vos clients savent.",
          f"""L'automatisation du jeudi, version fêtes.

Un message d'absence bien écrit rassure vos clients pendant que vous êtes à table. Il se prépare en cinq minutes, et il peut s'activer et se désactiver tout seul.

Joyeux réveillon.

{H_PME}"""),
    # 31/12
    jeudi("temps-horloge#5", "Le bilan\n*de l'année.*",
          "des heures à rassembler les chiffres.", "les demandes, devis et ventes de l'année, déjà réunis.",
          "Le 31 décembre, tout est prêt.",
          f"""L'automatisation du jeudi, dernier jour de l'année.

Quand les informations sont rangées au fil de l'eau, le bilan annuel n'est plus une corvée. Il se prépare tout seul.

Belle fin d'année à toutes et à tous.

{H_PME}"""),
    # 07/01
    jeudi("dev-signature#3", "Le devis\n*préparé à partir d'un formulaire.*",
          "chaque devis recommence de zéro.", "le client renseigne ses besoins, le devis se prépare, vous le relisez.",
          "Vous validez, vous ne retapez plus.",
          f"""L'automatisation du jeudi.

Pour les entreprises qui vendent des produits ou des prestations sur mesure, un formulaire bien pensé peut préparer le devis, le descriptif et le mail d'envoi. Il ne reste qu'à vérifier.

{CONTACT}

{H_PME2}"""),
    # 14/01
    jeudi("auto-entrepot#3", "L'alerte\n*de stock bas.*",
          "on découvre la rupture le jour où il faut la pièce.", "un seuil atteint déclenche une alerte et une commande à valider.",
          "Plus de mauvaise surprise.",
          f"""L'automatisation du jeudi.

Une rupture de stock coûte rarement le prix de la pièce. Elle coûte l'attente, le chantier arrêté, le client déçu. Un seuil surveillé en continu évite tout ça.

{H_PME2}"""),
    # 21/01
    jeudi("astuce-lampe#5", "Les messages\n*des voyageurs.*",
          "les mêmes questions, à toute heure, sur votre téléphone.", "une réponse juste, dans leur langue, et vous êtes prévenu pour le reste.",
          "Vos soirées redeviennent les vôtres.",
          f"""L'automatisation du jeudi, côté conciergerie.

Parking, arrivée, wifi : la plupart des messages de voyageurs ont une réponse connue. Un assistant bien configuré y répond avec les informations du logement, et vous alerte dès qu'il faut une décision.

{CONTACT}

{H_CONC}"""),
    # 28/01
    jeudi("details-linge#3", "Le planning\n*des équipes de ménage.*",
          "on recopie les réservations pour prévenir l'équipe.", "chaque arrivée et chaque départ mettent leur planning à jour.",
          "Personne n'apprend un départ au dernier moment.",
          f"""L'automatisation du jeudi, côté conciergerie.

Les réservations existent déjà dans votre logiciel de location. Les recopier pour l'équipe de ménage, c'est une source d'oubli. Le planning peut se mettre à jour tout seul.

{H_CONC}"""),
    # 04/02
    jeudi("auto-entrepot#2", "La recherche\n*d'un document interne.*",
          "on fouille les dossiers ou on demande au collègue.", "on pose la question, l'outil répond avec le bon document.",
          "Le savoir de l'entreprise, accessible à tous.",
          f"""L'automatisation du jeudi.

Procédures, fiches techniques, modèles : le savoir d'une entreprise est souvent là, mais introuvable. Un outil qui répond aux questions à partir de vos propres documents le rend accessible à toute l'équipe.

{CONTACT}

{H_PME2}"""),
    # 11/02
    jeudi("dev-boussole#4", "La veille\n*des appels d'offres.*",
          "on consulte les plateformes quand on y pense.", "chaque nouvelle offre qui vous correspond arrive dans votre boîte mail.",
          "Vous ne ratez plus les bonnes occasions.",
          f"""L'automatisation du jeudi.

Les marchés intéressants existent, mais ils se perdent parmi des centaines d'annonces. Une veille automatique filtre selon vos critères et vous prévient dès qu'une offre correspond.

{H_PME2}"""),
    # 18/02
    jeudi("dev-escalier#4", "Les nouveaux avis\n*en ligne.*",
          "on découvre un avis des semaines plus tard.", "chaque nouvel avis est signalé, avec une proposition de réponse à relire.",
          "Chaque client a sa réponse.",
          f"""L'automatisation du jeudi.

Répondre à un avis montre qu'il y a quelqu'un derrière l'entreprise. Encore faut-il le voir passer. Une alerte, et une réponse préparée à relire, et c'est fait en une minute.

{H_DEV}"""),
    # 25/02
    jeudi("auto-machine#1", "Le rappel\n*d'entretien annuel.*",
          "le client oublie, vous aussi.", "un an après l'intervention, un message propose un rendez-vous.",
          "Un client fidèle, ça se garde.",
          f"""L'automatisation du jeudi.

Chaudière, machine, installation, contrôle : beaucoup d'interventions reviennent chaque année. Un rappel au bon moment fait revenir le client, sans démarchage.

{H_PME2}"""),
    # 04/03
    jeudi("details-carnet#3", "Les pièces\n*pour le comptable.*",
          "une course aux justificatifs en fin de mois.", "factures et reçus rangés au fil de l'eau, envoyés chaque mois.",
          "La fin de mois devient une formalité.",
          f"""L'automatisation du jeudi.

Chaque facture reçue peut être rangée et transmise au moment où elle arrive. En fin de mois, il n'y a plus rien à chercher.

{H_PME}"""),
    # 11/03
    jeudi("dev-salle#5", "L'arrivée\n*d'un nouveau salarié.*",
          "on oublie un accès, un document, une présentation.", "une liste qui se déroule seule, étape par étape.",
          "Le premier jour se passe bien, à chaque fois.",
          f"""L'automatisation du jeudi.

Comptes à créer, documents à signer, personnes à présenter : l'arrivée d'un salarié suit toujours les mêmes étapes. Une liste automatique s'assure que rien n'est oublié.

{H_PME}"""),
    # 18/03
    jeudi("dev-matin#5", "Le récapitulatif\n*du matin.*",
          "on découvre les demandes de la veille une par une.", "un seul message résume ce qui est arrivé et ce qui attend.",
          "Vous commencez la journée en sachant tout.",
          f"""L'automatisation du jeudi.

Plutôt que dix notifications dispersées, un seul message chaque matin : les demandes reçues, celles qui attendent une réponse, et ce qui est urgent.

{H_PME}"""),
    # 25/03
    jeudi("auto-colis#1", "Le suivi\n*après une prestation.*",
          "une fois le travail livré, on n'a plus de nouvelles.", "une semaine plus tard, un message vérifie que tout va bien.",
          "Le service continue après la facture.",
          f"""L'automatisation du jeudi.

Un message une semaine après la livraison montre que vous vous souciez du résultat, pas seulement de la vente. Et il ouvre souvent la porte à la suite.

{H_DEV}"""),
    # 01/04
    jeudi("interieur-salon#1", "Le rapport\n*aux propriétaires.*",
          "chaque mois, des heures à compiler réservations et revenus.", "un rapport clair, préparé automatiquement pour chaque propriétaire.",
          "Vos propriétaires savent, sans vous appeler.",
          f"""L'automatisation du jeudi, côté conciergerie.

Vos propriétaires veulent savoir comment se porte leur logement. Un rapport mensuel préparé automatiquement répond à leurs questions avant qu'ils ne les posent.

{CONTACT}

{H_CONC}"""),
]
