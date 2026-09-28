"""Contenu éditorial DelorIA, 6 mois, du lundi 5 octobre 2026 au vendredi 2 avril 2027.

POSTS : lundi, mercredi, vendredi, dans l'ordre. WEEKEND : samedi puis dimanche, dans l'ordre.
"photo" désigne un dossier de photos/pexels/ : construire.py choisit une photo
non encore utilisée dans ce dossier, sauf si "photo_fichier" impose un fichier.
Règles : faits réels uniquement, aucun tiret long ou moyen, vouvoiement,
aucun nom de client, jamais "à leur place".
"""

H_CONC = "#conciergerie #conciergerieairbnb #locationcourteduree #airbnb #hotes"
H_NORM = "#normandie"
H_PME = "#pme #automatisation #entrepreneur #france"
H_DESIGN = "#identitevisuelle #chartegraphique #siteinternet #design"
H_RESEAUX = "#reseauxsociaux #instagram #automatisation #communication"

CONTACT = "Une question ? Écrivez-moi en message privé."

POSTS = [
    # ─────────────── OCTOBRE 2026 ───────────────
    dict(template="plein", photo_fichier="photos/pexels/normandie-falaises/6395435_adrien-olichon.jpg",
         lieu="Étretat, Normandie", phrase="La côte ne dort jamais.\n*Vos voyageurs non plus.*", decalage=-230,
         legende=f"""Bienvenue chez DelorIA.

Je m'appelle Tom, je suis ingénieur, basé en Normandie, et je travaille avec des conciergeries et des entreprises partout en France. Je construis des outils qui répondent aux voyageurs des conciergeries comme vous le feriez, de jour comme de nuit.

Ici, je partage ce que j'apprends sur le terrain : ce qui marche, ce qui casse, et ce qu'on ne devrait jamais automatiser.

{H_CONC} #etretat {H_NORM}"""),

    dict(template="constat", label="Le quotidien d'une conciergerie",
         texte="Un voyageur écrit à 22h43 pour savoir où se garer.\nQuelqu'un répond forcément.", chute="Aujourd'hui, c'est vous.",
         legende=f"""Un voyageur qui cherche où se garer n'attend pas le lendemain. Il écrit maintenant, et il attend une réponse maintenant.

Dans beaucoup de conciergeries, cette réponse part du téléphone personnel du gérant, entre deux autres choses. C'est ce quotidien que je veux alléger.

{H_CONC}"""),

    dict(template="terrain_photo", photo="details-telephone", cadrage="center 85%", label="Note de terrain",
         titre="Airbnb refuse tout message qui contient *un lien.*",
         texte="Un nom de site, une adresse e-mail, un numéro de téléphone : le message entier est bloqué. Le voyageur ne reçoit rien.",
         chute="Ce qui répond à vos voyageurs doit le savoir.",
         legende=f"""Airbnb bloque les messages qui contiennent une coordonnée, pour éviter qu'on sorte de la plateforme. Ce n'est pas seulement le lien qui saute : c'est tout le message.

Quand vous écrivez vous-même, l'application vous prévient. Un outil automatique, lui, peut ne jamais le savoir.

C'est pour ça que l'assistant que je configure n'écrit aucune coordonnée. Pour une adresse précise, il vous passe la main.

{H_CONC}"""),

    dict(template="edito", photo_fichier="photos/pexels/interieur-chambre/29435313_yunus-tug.jpg", cadrage="30% center",
         label="Pour les conciergeries", titre="Un assistant qui répond *comme vous le feriez.*",
         texte="Il connaît le logement, le calendrier et votre façon de parler aux voyageurs. Il vous prévient dès qu'on a besoin de vous.",
         pictos=[dict(icone="globe", texte="Langue du\nvoyageur"), dict(icone="lune", texte="Jour\net nuit"), dict(icone="cloche", texte="Alerte si\nproblème")],
         cta="Écrivez-moi en privé",
         legende=f"""Ce que je construis pour les conciergeries : un assistant branché sur votre messagerie de location, qui répond aux voyageurs avec les vraies informations de chaque logement.

Il répond dans la langue du voyageur, à toute heure. Et dès qu'un vrai problème se présente, il ne le règle pas seul : il rassure le voyageur et vous alerte.

{CONTACT}

{H_CONC}"""),

    dict(template="plein", photo="interieur-lit", phrase="Un bon accueil commence\n*avant l'arrivée.*",
         legende=f"""Où se garer, à quelle heure arriver, comment récupérer les clés : la plupart des questions tombent dans les jours qui précèdent le séjour.

Une réponse claire à ce moment-là, c'est un voyageur qui arrive serein. Et un séjour qui commence bien.

{H_CONC}"""),

    dict(template="terrain_photo", photo="details-cles", photo_fichier="photos/pexels/details-cles/17026019_esra-erdem.jpg", cadrage="center 60%",
         label="Note de terrain", titre="Le code de la boîte à clés *ne passe jamais par l'assistant.*",
         texte="Il part tout seul la veille de l'arrivée, depuis le logiciel de gestion. Personne ne le recopie, personne ne l'envoie trop tôt.",
         chute="Automatiser, c'est aussi choisir ce qu'on n'automatise pas.",
         legende=f"""On pourrait laisser l'assistant donner le code d'accès. J'ai fait le choix inverse.

Le code est l'information la plus sensible d'un logement. Les logiciels de location savent déjà l'envoyer automatiquement la veille de l'arrivée. Le confier à un deuxième outil n'apporte rien, sauf un risque de code périmé envoyé au mauvais moment.

Si un voyageur le demande trop tôt, l'assistant lui explique simplement quand il arrivera.

{H_CONC}"""),

    dict(template="constat", label="Le quotidien d'une conciergerie",
         texte="Dimanche soir, pendant le dîner.\nUn voyageur demande le code wifi.", chute="Encore une fois.",
         legende=f"""Le code wifi est sans doute la question la plus posée en location courte durée. Elle n'est jamais difficile. Elle arrive juste toujours au mauvais moment.

Ce genre de question peut recevoir une réponse juste, immédiate, sans vous.

{H_CONC}"""),

    dict(template="edito", photo="secteur-bureau", label="Coulisses",
         titre="Ce post a été publié *sans que personne n'appuie sur un bouton.*",
         texte="Visuel, texte, date de publication : tout part automatiquement, cinq fois par semaine. Je peux mettre en place la même chose pour votre compte.",
         pictos=[dict(icone="calendrier", texte="5 posts\npar semaine"), dict(icone="pinceau", texte="À vos\ncouleurs"), dict(icone="engrenage", texte="Sans y\npenser")],
         cta="Écrivez-moi en privé",
         legende=f"""Petit aveu : ce compte tourne tout seul.

Les visuels sont générés à mes couleurs, les textes sont préparés à l'avance, et un automate publie cinq jours par semaine. Je n'ouvre Instagram que pour répondre à vos messages.

Si vous voulez la même chose pour votre activité, parlons-en.

{H_RESEAUX}"""),

    dict(template="plein", photo_fichier="region-paris#6", lieu="Paris", phrase="Paris s'éveille.\n*Vos messages aussi.*",
         legende=f"""Les premiers messages de la journée arrivent souvent avant le premier café : une heure d'arrivée, une question sur le petit-déjeuner, un train en retard.

Un peu de Paris pour commencer le week-end.

#paris #conciergerie #locationcourteduree"""),

    dict(template="terrain", label="Note de terrain",
         titre="Le prix affiché par l'outil *n'est pas celui que paie le voyageur.*",
         texte="Frais de ménage, frais de service, suppléments selon le nombre de voyageurs : le total final change tout.",
         chute="L'assistant ne donne jamais de prix. Il renvoie vers l'annonce.",
         legende=f"""Une leçon apprise en conditions réelles.

Le prix par nuit qu'un logiciel de location transmet n'est pas le montant que le voyageur verra au moment de payer. Entre les deux : ménage, frais de service, suppléments.

Un assistant qui annonce un prix finit donc par se tromper, et un voyageur qui se sent trompé au paiement, c'est un litige. La règle est simple : aucun prix, jamais. Le total exact s'affiche sur l'annonce.

{H_CONC}"""),

    dict(template="service", label="Ce que l'assistant ne fait jamais", titre="Savoir ce qu'il ne faut *pas automatiser.*",
         points=["Annoncer un prix", "Donner le code d'accès", "Inventer une réponse qu'il n'a pas"],
         signature="CONCIERGERIES · PARTOUT EN FRANCE",
         legende=f"""Un bon assistant se définit aussi par ce qu'il refuse de faire.

Pas de prix, parce que le total final dépend de trop de paramètres. Pas de code d'accès, parce qu'il part déjà automatiquement au bon moment. Et pas d'invention : quand il ne sait pas, il vous passe la main.

{H_CONC}"""),

    dict(template="plein", photo="interieur-salon", phrase="Le luxe, c'est de n'avoir\n*rien à demander.*",
         legende=f"""Un logement bien préparé répond à la moitié des questions avant qu'elles soient posées. Le reste, c'est une affaire de réponses claires et rapides.

Bon week-end.

{H_CONC}"""),

    # ─────────────── NOVEMBRE 2026 ───────────────
    dict(template="edito", photo="secteur-bureau", label="Sites internet",
         titre="Un site qui inspire confiance *dès la première seconde.*",
         texte="Des pages claires, vos vraies photos, un contact en un geste. Pensé d'abord pour le téléphone, là où l'on vous découvre.",
         pictos=[dict(icone="mobile", texte="Pensé pour\nle mobile"), dict(icone="pinceau", texte="À vos\ncouleurs"), dict(icone="message", texte="Contact\nen un geste")],
         cta="Écrivez-moi en privé",
         legende=f"""Je conçois aussi des sites internet.

Pas de modèle générique : une présentation qui vous ressemble, lisible sur téléphone, avec un moyen simple de vous contacter. Pour une conciergerie, une PME ou un indépendant.

{CONTACT}

{H_DESIGN}"""),

    dict(template="constat", label="Hors saison",
         texte="Novembre.\nLes messages ralentissent enfin.", chute="C'est le moment de préparer la suite.",
         legende=f"""La basse saison est le meilleur moment pour mettre en place un nouvel outil. On le teste au calme, on corrige, et il est rodé quand les réservations repartent.

Mettre en route un assistant en plein mois d'août, c'est l'inverse de ce qu'il faut faire.

{H_CONC}"""),

    dict(template="plein", photo_fichier="normandie-cote#2", lieu="Côte normande", phrase="En novembre, la côte respire.\n*Vous aussi.*",
         legende=f"""Moins de monde sur les plages, moins de messages sur le téléphone. Profitez-en.

{H_NORM} #cotenormande #conciergerie"""),

    dict(template="terrain_photo", photo="details-carnet", label="Note de terrain",
         titre="Du 19 au 20, *c'est une seule nuit.*",
         texte="Évident pour vous. Beaucoup moins pour un outil qui compte des jours au lieu de nuits.",
         chute="Chaque automatisme se teste sur des cas réels, pas sur des cas faciles.",
         legende=f"""Une erreur que j'ai vue passer : un séjour du 19 au 20 compté comme deux nuits.

Pour une personne, c'est évident. Pour un programme, tout dépend de la façon dont on lui décrit les dates. C'est typiquement le genre de détail qui ne se voit qu'en conditions réelles.

C'est aussi pour ça que l'assistant ne fait jamais de calcul de prix.

{H_CONC}"""),

    dict(template="edito", photo="secteur-atelier", label="Identité visuelle",
         titre="Une identité qui se reconnaît *au premier regard.*",
         texte="Logo, couleurs, typographies, règles d'usage : un cadre simple pour que chaque support vous ressemble, du site aux réseaux.",
         pictos=[dict(icone="pinceau", texte="Logo"), dict(icone="etoile", texte="Charte\ngraphique"), dict(icone="document", texte="Règles\nd'usage")],
         cta="Écrivez-moi en privé",
         legende=f"""Je crée des logos et des chartes graphiques.

Une identité claire, c'est des visuels cohérents partout : site, réseaux, devis, cartes de visite. Et c'est aussi ce qui permet d'automatiser ensuite des publications qui restent belles.

{CONTACT}

{H_DESIGN}"""),

    dict(template="plein", photo_fichier="region-corse#2", lieu="Bonifacio, Corse", phrase="Certains paysages\n*se passent de description.*",
         legende=f"""Pas de conseil aujourd'hui. Juste la Corse.

#corse #bonifacio #france"""),

    dict(template="terrain_photo", photo="interieur-fenetre", label="Note de terrain",
         titre="Le silence *est le pire des échecs.*",
         texte="Un voyageur sans réponse réécrit, s'inquiète, puis se plaint. Une réponse imparfaite vaut mieux que pas de réponse.",
         chute="Quand l'assistant hésite, il fait patienter et vous prévient.",
         legende=f"""Une conviction forgée en production : ne rien envoyer est pire qu'envoyer une réponse imparfaite.

C'est pour ça que, lorsque l'assistant n'a pas l'information, il ne se tait pas. Il répond au voyageur qu'on revient vers lui très vite, et il vous alerte avec le détail de la demande.

{H_CONC}"""),

    dict(template="constat", label="Le quotidien d'une conciergerie",
         texte="Vous avez créé une conciergerie\npour être plus libre.", chute="Votre téléphone n'est pas au courant.",
         legende=f"""Beaucoup de conciergeries sont nées d'une envie d'indépendance. Et beaucoup de gérants passent aujourd'hui leurs soirées à répondre aux mêmes questions.

Ce n'est pas une fatalité.

{H_CONC}"""),

    dict(template="plein", photo="normandie-mont", lieu="Baie du Mont-Saint-Michel", phrase="Tout le monde veut voir la baie.\n*Tout le monde a une question.*",
         legende=f"""Horaires des marées, accès, parkings, restaurants : autour des lieux très visités, les voyageurs posent beaucoup de questions. Les mêmes, souvent.

C'est exactement là qu'un assistant bien renseigné fait gagner du temps.

#montsaintmichel {H_NORM} #conciergerie"""),

    dict(template="edito", photo="details-telephone", label="Google Business",
         titre="Votre fiche Google *est votre première vitrine.*",
         texte="C'est souvent là qu'on vous découvre, avant votre site. Horaires, photos, avis : tout doit être juste et à jour.",
         pictos=[dict(icone="horloge", texte="Horaires\nà jour"), dict(icone="photo", texte="Photos\nsoignées"), dict(icone="etoile", texte="Avis\nsuivis")],
         cta="Écrivez-moi en privé",
         legende=f"""Je m'occupe aussi des fiches Google Business.

Une fiche incomplète ou mal tenue fait fuir avant même le premier contact. Des horaires justes, de belles photos et des avis auxquels on répond : c'est simple, et ça change la première impression.

{CONTACT}

#googlebusiness #referencementlocal {H_PME}"""),

    dict(template="terrain", label="Note de terrain",
         titre="Parfois, la bonne réponse *c'est de ne rien envoyer.*",
         texte="Un merci auquel on a déjà répondu, un message déjà traité : répondre encore sonne faux. Un bon assistant sait aussi se taire.",
         chute="Encore faut-il lui en donner les moyens.",
         legende=f"""Demander à un assistant de ne pas répondre quand ce n'est pas nécessaire, c'est facile à écrire. Encore faut-il que le système puisse réellement ne rien envoyer.

J'ai appris à le prévoir dès la construction : toute consigne de silence doit avoir son mécanisme technique derrière.

{H_CONC}"""),

    dict(template="plein", photo_fichier="interieur-cheminee#4", phrase="Les soirées d'hiver\n*méritent mieux qu'un code wifi.*",
         legende=f"""Le feu dans la cheminée, le téléphone retourné sur la table. Voilà l'objectif.

Bon week-end.

{H_CONC}"""),

    dict(template="service", label="Pour les PME", titre="Automatiser ce qui se répète, *garder ce qui compte.*",
         points=["Des devis préparés à partir de vos paramètres", "Des réponses aux mails qui reviennent sans cesse", "Vos procédures retrouvées en une question"],
         signature="PME · PARTOUT EN FRANCE",
         legende=f"""DelorIA ne travaille pas qu'avec des conciergeries.

J'accompagne aussi des PME, notamment industrielles : préparer des devis, trier et préparer des réponses aux mails, retrouver une information dans une documentation technique. Tout ce qui se répète peut être allégé.

Je suis ingénieur, ce sont des sujets que je connais de l'intérieur.

{CONTACT}

{H_PME}"""),

    # ─────────────── DÉCEMBRE 2026 ───────────────
    dict(template="constat", label="Décembre",
         texte="Les réservations des fêtes arrivent.", chute="Les questions aussi.",
         legende=f"""Arrivées tardives, départs le 1er janvier, sapin ou pas sapin : décembre a ses questions bien à lui.

Préparer les réponses maintenant, c'est passer les fêtes un peu plus tranquille.

{H_CONC}"""),

    dict(template="plein", photo="saison-hiver-mer", phrase="L'hiver au bord de la mer\n*a ses fidèles.*",
         legende=f"""Il y a ceux qui ne viennent qu'en été, et ceux qui préfèrent la mer en hiver. Ces voyageurs-là méritent le même accueil.

#mer #hiver #france"""),

    dict(template="terrain_photo", photo_fichier="details-cafe#4", cadrage="center 60%", label="Note de terrain",
         titre="Deux voix dans la même conversation *sèment le doute.*",
         texte="Messages programmés d'un côté, réponses de l'assistant de l'autre : si personne ne décide qui dit quoi, le voyageur reçoit des doublons.",
         chute="On fait la liste avant de lancer, pas après.",
         legende=f"""Beaucoup de conciergeries utilisent déjà des messages programmés : bienvenue, instructions d'arrivée, rappel de départ. C'est très bien.

Mais dès qu'un assistant répond aussi, il faut décider qui dit quoi. Sinon le voyageur reçoit deux fois la même information, ou pire, deux informations différentes.

Avant chaque mise en route, on fait ensemble la liste de vos messages automatiques.

{H_CONC}"""),

    dict(template="edito", photo="interieur-salon", label="Réseaux sociaux",
         titre="Vos logements méritent *d'être vus.*",
         texte="Des publications régulières, à vos couleurs, qui mettent en avant vos biens et votre région. Vous validez, le reste se fait seul.",
         pictos=[dict(icone="calendrier", texte="Rythme\nrégulier"), dict(icone="pinceau", texte="À vos\ncouleurs"), dict(icone="check", texte="Validé\npar vous")],
         cta="Écrivez-moi en privé",
         legende=f"""Publier régulièrement sur Instagram prend un temps que peu de conciergeries ont.

Je prépare des publications à vos couleurs, avec vos photos, publiées automatiquement après votre validation. Vous gardez la main sur ce qui sort, sans y passer vos soirées.

{CONTACT}

{H_RESEAUX} #conciergerie"""),

    dict(template="plein", photo="saison-noel", phrase="Les fêtes se préparent\n*dans les détails.*",
         legende=f"""Une table dressée, un logement décoré, un message d'accueil soigné. Les voyageurs de décembre s'en souviennent.

{H_CONC}"""),

    dict(template="terrain_photo", photo="interieur-lit", label="Note de terrain",
         titre="Un voyageur de plus, un chien de plus : *le séjour change.*",
         texte="Quand un voyageur parle d'une future réservation, l'assistant lui rappelle une fois d'indiquer le nombre exact de personnes et d'animaux.",
         chute="Une phrase qui évite bien des malentendus à l'arrivée.",
         legende=f"""Un détail qui compte : le nombre de voyageurs et la présence d'un animal modifient souvent le tarif, et parfois les règles du logement.

L'assistant le rappelle naturellement, une seule fois, quand un voyageur évoque sa réservation. Pas de sermon, juste une phrase utile.

{H_CONC}"""),

    dict(template="constat", label="Le quotidien d'une conciergerie",
         texte="Un voyageur allemand écrit à minuit.", chute="Il attend une réponse dans sa langue.",
         legende=f"""Une clientèle internationale, c'est une chance. C'est aussi des messages en anglais, en allemand ou en néerlandais, à toute heure.

L'assistant répond dans la langue de chaque voyageur, avec les informations du logement.

{H_CONC}"""),

    dict(template="plein", photo_fichier="region-nice#3", lieu="Nice", phrase="Les plus beaux ports\n*ne ferment jamais.*",
         legende=f"""Nice en décembre. Bon week-end à tous.

#nice #cotedazur #france"""),

    dict(template="service", label="Comment on démarre", titre="Commencer petit, *pour bien commencer.*",
         points=["Un appel pour comprendre votre quotidien", "Un premier logement pour tester", "On élargit quand tout fonctionne"],
         signature="CONCIERGERIES · PARTOUT EN FRANCE",
         legende=f"""Je ne branche jamais un assistant sur tout un parc d'un coup.

On commence par un échange sur votre façon de travailler, puis un seul logement, le temps de vérifier que les réponses sont justes et que le ton vous ressemble. Ensuite seulement, on étend.

{CONTACT}

{H_CONC}"""),

    dict(template="plein", photo="saison-noel", phrase="Chez vous aussi,\n*c'est bientôt les fêtes.*",
         legende=f"""Derniers jours avant Noël. Pensez à vous accorder quelques soirées sans téléphone.

{H_CONC}"""),

    dict(template="plein", photo_fichier="interieur-cheminee#6", phrase="Joyeux Noël.\n*Le téléphone peut attendre.*",
         legende="""Joyeux Noël à toutes les conciergeries, à leurs équipes, et à tous ceux qui travaillent pendant que les autres sont en vacances.

#joyeuxnoel #conciergerie #hotes"""),

    dict(template="terrain_photo", photo="accueil-panier", label="Note de terrain",
         titre="Un voyageur intéressé par un service, *c'est un revenu.*",
         texte="Vélos, petit-déjeuner, ménage en plus : quand un voyageur montre un intérêt, l'assistant le transmet tout de suite à la conciergerie.",
         chute="Un assistant peut aussi rapporter.",
         legende=f"""On parle souvent d'un assistant comme d'un moyen de gagner du temps. C'est aussi un moyen de ne plus rater de ventes.

Quand un voyageur s'intéresse à un service de la conciergerie, l'assistant vous le signale immédiatement, avec le service concerné, les dates et le nombre de personnes. À vous de conclure.

{H_CONC}"""),

    dict(template="constat", label="Bilan de l'année",
         texte="Cette année, combien de soirées ont fini sur votre téléphone ?", chute="L'an prochain peut être différent.",
         legende=f"""Pas besoin de répondre en commentaire. Juste d'y penser un instant avant la nouvelle année.

{H_CONC}"""),

    # ─────────────── JANVIER 2027 ───────────────
    dict(template="plein", photo="normandie-cote", phrase="Belle année.\n*Plus de soirées pour vous.*",
         legende=f"""Bonne année 2027 à toutes et à tous.

Je vous souhaite des voyageurs ravis, des logements pleins, et des soirées où le téléphone reste dans la poche.

#bonneannee {H_CONC} {H_NORM}"""),

    dict(template="edito", photo="interieur-cuisine", label="Pour les conciergeries",
         titre="Les questions reviennent. *Les réponses aussi.*",
         texte="Wifi, parking, arrivée, poubelles : l'essentiel des messages se ressemble. L'assistant y répond avec les informations de chaque logement.",
         pictos=[dict(icone="maison", texte="Fiche\nlogement"), dict(icone="calendrier", texte="Calendrier\nà jour"), dict(icone="message", texte="Réponse\nimmédiate")],
         cta="Écrivez-moi en privé",
         legende=f"""La plupart des messages de voyageurs portent sur les mêmes sujets. Ce ne sont pas des questions difficiles, ce sont des questions répétées.

L'assistant lit la fiche du logement et le calendrier à chaque conversation. Si une information change, elle change aussi dans ses réponses.

{CONTACT}

{H_CONC}"""),

    dict(template="terrain_photo", photo="secteur-boulangerie", label="Note de terrain",
         titre="L'assistant ne connaît *que ce que vous lui donnez.*",
         texte="Il ne cherche pas sur internet. La boulangerie, la pharmacie, le bon restaurant du coin : il faut les lui transmettre, avec les vraies adresses.",
         chute="Sinon, il vous passe la main. Il n'invente pas.",
         legende=f"""Une précision importante, que je donne à chaque rendez-vous.

L'assistant ne navigue pas sur internet et n'a pas de carte. Il ne connaît que les informations qu'on lui a confiées. C'est pour ça qu'on remplit ensemble une rubrique « autour du logement », avec vos adresses à vous.

Mieux vaut un assistant qui dit « je me renseigne » qu'un assistant qui invente une boulangerie.

{H_CONC}"""),

    dict(template="plein", photo_fichier="region-alpes#1", phrase="En montagne,\n*la saison bat son plein.*",
         legende=f"""Pendant que le littoral se repose, les stations tournent à plein. Pour les conciergeries de montagne, janvier, c'est la haute saison.

Bon courage à toutes celles qui enchaînent les arrivées ce week-end.

#montagne #ski {H_CONC}"""),

    dict(template="edito", photo="secteur-industrie", label="Pour les PME industrielles",
         titre="Un devis prêt *avant la fin de l'appel.*",
         texte="Votre client choisit ses paramètres, l'outil prépare le devis, le descriptif et le mail. Vous relisez, vous envoyez.",
         pictos=[dict(icone="engrenage", texte="Vos\nparamètres"), dict(icone="document", texte="Devis\nen PDF"), dict(icone="message", texte="Mail\nprêt")],
         cta="Écrivez-moi en privé",
         legende=f"""Pour les entreprises qui vendent des produits configurables, je construis des configurateurs sur mesure.

Le client saisit ses besoins, l'outil génère le devis, le descriptif technique et le mail d'accompagnement. Vous gardez la relecture et la décision.

Ingénieur de métier, je parle le même langage que vos équipes techniques.

{CONTACT}

{H_PME} #industrie"""),

    dict(template="constat", label="Le quotidien d'une conciergerie",
         texte="Chaque message a l'air urgent.", chute="Très peu le sont vraiment.",
         legende=f"""Tout le problème est là : pour savoir qu'un message n'est pas urgent, il faut déjà l'avoir lu.

Un assistant trie pour vous. Il répond à ce qui peut l'être, et ne vous dérange que pour ce qui compte vraiment.

{H_CONC}"""),

    dict(template="plein", photo="interieur-salle-bain", phrase="Le calme se voit\n*dans les détails.*",
         legende=f"""Une serviette pliée, une lumière douce, un logement impeccable. Le reste, ce sont des réponses claires.

Bon week-end.

{H_CONC}"""),

    dict(template="terrain_photo", photo="accueil-sonnette", label="Note de terrain",
         titre="Un vrai problème *remonte tout de suite.*",
         texte="Une fuite, un chauffage en panne, un voyageur mécontent : l'assistant ne tente pas de régler seul. Il rassure et vous alerte.",
         chute="Déléguer les questions, pas les problèmes.",
         legende=f"""La frontière est claire : l'assistant répond aux questions, il ne gère pas les incidents.

Dès qu'un voyageur signale un problème, il lui répond avec sérieux, sans minimiser, et vous envoie une alerte avec le détail. S'il relance sur le même sujet, l'assistant fait le suivi sans vous déranger une seconde fois.

{H_CONC}"""),

    dict(template="edito", photo="secteur-artisan", label="Exemple · Artisan",
         titre="Le soir, *le devis est déjà parti.*",
         texte="Quelques informations saisies sur le chantier, un devis mis en forme automatiquement, envoyé au client après votre relecture.",
         pictos=[dict(icone="mobile", texte="Saisie sur\nle chantier"), dict(icone="document", texte="Devis mis\nen forme"), dict(icone="check", texte="Relu\npar vous")],
         cta="Écrivez-moi en privé",
         legende=f"""Un exemple de ce qui est possible pour un artisan.

Le devis, c'est souvent ce qui se fait le soir, fatigué, après la journée. Une partie peut se préparer automatiquement à partir de quelques informations saisies sur place. Vous vérifiez, vous envoyez.

Chaque métier a ses tâches répétitives. Parlons des vôtres.

{H_PME} #artisan"""),

    dict(template="plein", photo_fichier="region-lyon#6", lieu="Lyon", phrase="Où que vous soyez,\n*tout se fait à distance.*",
         legende=f"""Je travaille avec des conciergeries et des entreprises dans toute la France.

Un premier appel en visio suffit pour comprendre votre activité. La configuration, les tests et le suivi se font ensuite à distance, sans que vous ayez à vous déplacer.

{CONTACT}

#lyon #france"""),

    dict(template="terrain_photo", photo="details-carnet", label="Note de terrain",
         titre="Une information, *un seul endroit.*",
         texte="Le code wifi change ? On le met à jour là où vous gérez déjà vos logements, et l'assistant le lit à chaque conversation.",
         chute="Deux sources, c'est la garantie qu'une des deux sera fausse.",
         legende=f"""Un principe que j'applique partout : chaque information vit à un seul endroit.

Si le wifi est écrit à la fois dans votre logiciel de location et dans l'assistant, un jour l'un des deux sera oublié. Alors l'assistant va chercher l'information là où vous la tenez déjà à jour.

{H_CONC}"""),

    dict(template="service", label="Ce que je fais", titre="Un seul interlocuteur *pour tout ce qui se répète.*",
         points=["Les réponses à vos voyageurs", "Vos sites et votre identité visuelle", "Vos publications sur les réseaux"],
         signature="PARTOUT EN FRANCE",
         legende=f"""En résumé, DelorIA, c'est :

Un assistant qui répond à vos voyageurs comme vous le feriez.
Des sites, logos et chartes graphiques à votre image.
Des publications automatisées sur vos réseaux, comme ce compte.

Et un interlocuteur unique, qui vous répond directement.

{CONTACT}

{H_CONC} {H_DESIGN}"""),

    dict(template="plein", photo_fichier="region-biarritz#3", lieu="Biarritz", phrase="Biarritz hors saison.\n*Le temps de tout préparer.*",
         legende=f"""L'océan est calme en janvier. Dans quelques semaines, les réservations du printemps arriveront.

#biarritz #paysbasque #france"""),

    # ─────────────── FÉVRIER 2027 ───────────────
    dict(template="edito", photo="secteur-restaurant", label="Exemple · Restaurant",
         titre="Les questions du soir, *répondues pendant le service.*",
         texte="Horaires, accès, réservations de groupe : les messages arrivent quand vous êtes en cuisine. Un assistant peut répondre avec vos informations.",
         pictos=[dict(icone="horloge", texte="Horaires"), dict(icone="message", texte="Messages"), dict(icone="cloche", texte="Vous alerte\nsi besoin")],
         cta="Écrivez-moi en privé",
         legende=f"""Un exemple de ce qui est possible pour un restaurant.

Pendant le service, personne n'a le temps de répondre aux messages. Un assistant peut prendre en charge les questions simples et vous transmettre les demandes qui méritent votre attention, comme une réservation de groupe.

{H_PME} #restaurant"""),

    dict(template="terrain", label="Note de terrain",
         titre="Ouvrir la messagerie à tout le monde, *c'est doubler les réponses.*",
         texte="Propriétaires, équipe, assistant : si chacun peut répondre, le voyageur reçoit deux messages différents.",
         chute="On partage le calendrier. On garde une seule voix.",
         legende=f"""Une recommandation que je fais aux conciergeries qui ouvrent leur outil à leurs propriétaires.

Partager le calendrier et les réservations, oui. Ouvrir la messagerie, non : sinon un propriétaire peut répondre en même temps que l'assistant, et le voyageur ne sait plus qui croire.

{H_CONC}"""),

    dict(template="plein", photo="interieur-fenetre", phrase="Dehors, il pleut.\n*Dedans, tout est prêt.*",
         legende=f"""Février en Normandie. Le bon temps pour un plaid, un livre, et un téléphone silencieux.

{H_CONC}"""),

    dict(template="constat", label="Vacances d'hiver",
         texte="Les vacances d'hiver commencent.\nLes réservations repartent.", chute="Et les questions avec elles.",
         legende=f"""Petit avant-goût de la saison. Si les messages de ces deux semaines vous pèsent déjà, imaginez juillet.

C'est maintenant qu'il faut s'organiser.

{H_CONC}"""),

    dict(template="edito", photo="interieur-chambre", label="Vidéo",
         titre="Vos photos *deviennent une vidéo.*",
         texte="Un court film de votre logement ou de votre activité, monté à partir de vos images, pour les réseaux et votre site.",
         pictos=[dict(icone="video", texte="Format\nréseaux"), dict(icone="photo", texte="À partir de\nvos photos"), dict(icone="pinceau", texte="À vos\ncouleurs")],
         cta="Écrivez-moi en privé",
         legende=f"""Je réalise aussi de courtes vidéos pour les réseaux, à partir de vos photos.

Un format qui attire l'œil, sans organiser de tournage. Idéal pour présenter un logement, une activité ou une nouveauté.

{CONTACT}

{H_RESEAUX} #video"""),

    dict(template="plein", photo="details-cafe", phrase="Un café, une vue,\n*aucune notification.*",
         legende=f"""C'est tout ce qu'on vous souhaite pour ce week-end.

{H_CONC}"""),

    dict(template="terrain_photo", photo="details-carnet", label="Note de terrain",
         titre="Un code transmis à l'oral *est un code perdu.*",
         texte="Mot de passe, accès, identifiant : on les envoie par écrit, sur un canal qu'on retrouve. Jamais seulement dans le chat d'une visio.",
         chute="Une règle simple, apprise à mes dépens.",
         legende=f"""Petite histoire vraie : un accès transmis dans le chat d'une visio, et plus rien à la fin de l'appel. Le chat avait disparu avec la réunion. Un jour de perdu.

Depuis, la règle est simple : tout ce qui est important passe par écrit, par e-mail ou par SMS. C'est valable pour vos équipes aussi.

{H_CONC} {H_PME}"""),

    dict(template="constat", label="Le quotidien d'une conciergerie",
         texte="La question la plus posée\nn'est jamais la plus difficile.", chute="C'est la plus répétée.",
         legende=f"""Faites l'exercice : notez pendant une semaine les questions que vous posent les voyageurs. Vous verrez que la moitié se ressemblent.

Ce sont celles-là qui s'automatisent le mieux.

{H_CONC}"""),

    dict(template="plein", photo="normandie-mont", lieu="Mont-Saint-Michel", phrase="Chaque marée\n*apporte ses voyageurs.*",
         legende=f"""La baie, entre deux saisons. Bon week-end.

#montsaintmichel {H_NORM}"""),

    dict(template="edito", photo="secteur-bureau", label="Pour les PME",
         titre="Vos procédures, *retrouvées en une question.*",
         texte="Normes, modes opératoires, fiches techniques : un assistant interne qui répond à partir de vos documents, et cite sa source.",
         pictos=[dict(icone="document", texte="Vos\ndocuments"), dict(icone="loupe", texte="Une\nquestion"), dict(icone="check", texte="Source\ncitée")],
         cta="Écrivez-moi en privé",
         legende=f"""Dans beaucoup d'entreprises, l'information existe mais personne ne la retrouve. Elle dort dans des dossiers partagés, des classeurs, des versions successives.

Un assistant interne peut répondre à partir de vos propres documents, en indiquant d'où vient la réponse. Vos équipes gagnent du temps, et la bonne version fait foi.

{CONTACT}

{H_PME}"""),

    dict(template="terrain_photo", photo="interieur-lit", label="Note de terrain",
         titre="Une heure de départ, *la même partout.*",
         texte="10h sur l'annonce, 11h dans les messages : le voyageur retiendra celle qui l'arrange. L'assistant répète ce qu'on lui donne.",
         chute="Automatiser oblige à mettre de l'ordre.",
         legende=f"""Mettre en place un assistant révèle souvent de petites incohérences : une heure de départ différente selon le support, un équipement annoncé qui n'existe plus.

C'est un effet secondaire très utile. Avant la saison, tout ce que vous dites à vos voyageurs devient enfin cohérent.

{H_CONC}"""),

    dict(template="plein", photo="saison-printemps", phrase="Le printemps\n*se prépare maintenant.*",
         legende=f"""Les premiers beaux jours arrivent bientôt. Les voyageurs aussi.

{H_CONC}"""),

    # ─────────────── MARS 2027 ───────────────
    dict(template="service", label="Avant la saison", titre="Trois choses *à vérifier maintenant.*",
         points=["Vos annonces disent exactement la vérité", "Vos messages programmés ne se contredisent pas", "Vos réponses aux questions courantes sont prêtes"],
         signature="CONCIERGERIES · PARTOUT EN FRANCE",
         legende=f"""Une petite liste avant le printemps.

Une annonce fidèle évite les mauvaises surprises. Des messages cohérents évitent les confusions. Et des réponses prêtes vous évitent de retaper les mêmes phrases tout l'été.

{H_CONC}"""),

    dict(template="edito", photo="accueil-sonnette", label="Pour les conciergeries",
         titre="La saison arrive. *Votre téléphone le sait déjà.*",
         texte="Mettre en place l'assistant avant le rush, c'est le tester au calme et arriver en été avec des réponses rodées.",
         pictos=[dict(icone="calendrier", texte="Mise en\nplace"), dict(icone="check", texte="Tests\nau calme"), dict(icone="lune", texte="Été\nserein")],
         cta="Écrivez-moi en privé",
         legende=f"""Mars est le dernier moment confortable pour mettre en place un assistant avant l'été.

Le temps de configurer un premier logement, de vérifier les réponses et d'ajuster le ton. En juillet, tout sera rodé.

{CONTACT}

{H_CONC}"""),

    dict(template="plein", photo_fichier="region-bretagne#2", lieu="Bretagne", phrase="La côte se réveille.\n*Vos réservations aussi.*",
         legende=f"""Les premières réservations de printemps arrivent. Bon week-end.

#bretagne #france"""),

    dict(template="terrain_photo", photo="details-carnet", label="Note de terrain",
         titre="Un outil sans surveillance *tombe en panne en silence.*",
         texte="Alerte en cas d'erreur, journal de chaque échange, test automatique chaque matin : si quelque chose casse, je le sais avant vous.",
         chute="La confiance se construit sur ce qu'on ne voit pas.",
         legende=f"""Installer un assistant, c'est la moitié du travail. L'autre moitié, c'est de savoir quand il ne fonctionne pas.

Chaque système que j'installe est surveillé : une alerte dès qu'une erreur survient, un journal de tous les échanges, et un test automatique chaque matin. Pas de panne silencieuse.

{H_CONC}"""),

    dict(template="constat", label="Le quotidien d'une conciergerie",
         texte="Répondre vite, c'est bien.", chute="Répondre juste, c'est mieux.",
         legende=f"""La rapidité compte, mais une réponse fausse coûte plus cher qu'une réponse lente. Un prix inventé, une adresse approximative, et c'est la confiance qui part.

C'est pour ça que l'assistant préfère vous passer la main plutôt que deviner.

{H_CONC}"""),

    dict(template="plein", photo_fichier="interieur-chambre#5", phrase="La lumière du matin\n*ne demande rien.*",
         legende=f"""Un logement lumineux, un lit fait, un séjour qui commence sans question. Bon week-end.

{H_CONC}"""),

    dict(template="edito", photo="interieur-salon", label="Sites internet",
         titre="Vos propriétaires vous jugent *sur votre site.*",
         texte="Avant de vous confier leur bien, ils regardent comment vous vous présentez. Un site clair et rassurant fait une partie du travail.",
         pictos=[dict(icone="maison", texte="Vos\nlogements"), dict(icone="etoile", texte="Vos\navis"), dict(icone="message", texte="Contact\nsimple")],
         cta="Écrivez-moi en privé",
         legende=f"""Pour une conciergerie, le site ne sert pas qu'aux voyageurs. Il sert surtout à convaincre de nouveaux propriétaires.

Des logements bien présentés, des avis visibles, un contact simple : c'est ce qui rassure quelqu'un qui hésite à vous confier son bien.

{CONTACT}

{H_DESIGN} #conciergerie"""),

    dict(template="terrain", label="Note de terrain",
         titre="Un test qui ne couvre pas un cas *ne prouve rien sur ce cas.*",
         texte="Voyageur qui se renseigne, voyageur qui a réservé, propriétaire qui écrit : chaque situation se teste avant la mise en route.",
         chute="La plupart des pannes viennent du cas qu'on n'avait pas imaginé.",
         legende=f"""Une leçon d'ingénieur, réapprise sur le terrain.

Tester avec une seule situation, même dix fois, ne dit rien des autres. Avant chaque mise en route, je liste tous les cas possibles d'une conversation et je vérifie qu'au moins un test couvre chacun.

{H_CONC} {H_PME}"""),

    dict(template="plein", photo_fichier="region-provence#4", lieu="Provence", phrase="Les beaux jours\n*se préparent dès maintenant.*",
         legende=f"""Les terrasses rouvrent, les voyageurs reviennent. Partout en France, la saison se lance.

#provence #france {H_CONC}"""),

    dict(template="edito", photo="secteur-boulangerie", label="Exemple · Commerce",
         titre="Vos horaires, vos produits, *toujours à jour.*",
         texte="Une fiche Google soignée, des publications régulières, des réponses aux questions courantes : ce qui fait venir les clients.",
         pictos=[dict(icone="etoile", texte="Fiche\nGoogle"), dict(icone="calendrier", texte="Posts\nréguliers"), dict(icone="message", texte="Réponses\nrapides")],
         cta="Écrivez-moi en privé",
         legende=f"""Un exemple de ce qui est possible pour un commerce de proximité.

Des horaires justes sur Google, des publications régulières sans y penser, des réponses aux questions qu'on vous pose tous les jours. De quoi rester visible sans y passer vos soirées.

{H_PME} #commercelocal"""),

    dict(template="constat", label="Ce que je vous propose",
         texte="Une soirée tranquille,\nsans vérifier votre téléphone.", chute="C'est tout. Et c'est beaucoup.",
         legende=f"""Au fond, tout ce que je construis sert à ça.

{CONTACT}

{H_CONC}"""),

    dict(template="plein", photo="saison-printemps", phrase="Les beaux jours reviennent.\n*Vos voyageurs aussi.*",
         legende=f"""Bon week-end, et bonne saison à toutes les conciergeries.

{H_CONC}"""),

    dict(template="service", label="Pourquoi DelorIA", titre="Un ingénieur, *pas une plateforme.*",
         points=["Je configure tout avec vous", "Je surveille ce que j'installe", "Je réponds quand vous m'écrivez"],
         signature="PARTOUT EN FRANCE",
         legende=f"""Les grands logiciels vendent des fonctionnalités. Je propose un accompagnement.

Je configure chaque outil avec vous, je surveille ce que j'installe, et vous avez quelqu'un à appeler. Où que vous soyez en France.

{CONTACT}

{H_CONC}"""),

    dict(template="terrain", label="Note de terrain",
         titre="Deux logements, *deux fiches.*",
         texte="Même conciergerie, même ville, mais pas le même parking ni le même wifi. L'assistant répond avec la fiche du bon logement.",
         chute="Le détail qui évite la pire des erreurs.",
         legende=f"""Quand une conciergerie gère plusieurs logements, tous les messages arrivent souvent au même endroit.

Avant de répondre, l'assistant vérifie de quel logement il s'agit et ne répond qu'avec ses informations. Répondre avec le code wifi du voisin, c'est exactement ce qu'on doit rendre impossible.

{H_CONC}"""),

    # ─────────────── AVRIL 2027 ───────────────
    dict(template="plein", photo_fichier="region-nice#4", phrase="Six mois de posts.\n*Aucun publié à la main.*",
         legende=f"""Depuis octobre, chaque publication de ce compte est partie toute seule, cinq fois par semaine. Visuels, textes, dates : tout était prêt à l'avance.

Si vous voulez la même tranquillité pour votre activité, sur vos réseaux ou avec vos voyageurs, écrivez-moi.

{H_RESEAUX} {H_CONC}"""),
]


# ═══════════════════════ WEEK-END ═══════════════════════
# Samedi : « Astuce d'accueil », gabarit carte, série numérotée.
# Dimanche : alternance photo respiration et réflexion courte.
# Ordre : samedi 10 oct, dimanche 11 oct, samedi 17 oct, dimanche 18 oct, etc.

H_ACC = "#astuceaccueil #hote #locationcourteduree #conciergerie #airbnb"
ASTUCE = "Astuce d'accueil"

WEEKEND = [
    # 10 et 11 octobre
    dict(template="carte", photo_fichier="astuce-lampe#1", label=ASTUCE,
         titre="Une lampe allumée *pour une arrivée de nuit.*",
         texte="Un voyageur qui arrive tard cherche l'interrupteur dans le noir. Une lampe laissée allumée change la première impression.",
         legende=f"""Nouvelle série du samedi : une astuce d'accueil simple, applicable dès ce week-end.

La première minute dans un logement compte énormément. Arriver de nuit dans une pièce éclairée, c'est se sentir attendu.

{H_ACC}"""),
    dict(template="plein", photo="interieur-lit", phrase="Dimanche.\n*Le téléphone peut dormir aussi.*",
         legende=f"""Bon dimanche à toutes les conciergeries.

{H_CONC}"""),

    # 17 et 18 octobre
    dict(template="carte", photo_fichier="astuce-mot#3", label=ASTUCE,
         titre="Un mot écrit à la main *vaut toutes les attentions.*",
         texte="Quelques lignes, le prénom du voyageur, un conseil pour le soir même. Deux minutes, et un souvenir.",
         legende=f"""Dans un monde de messages automatiques, un mot manuscrit se remarque. C'est aussi ce qu'on retrouve souvent cité dans les avis.

L'automatisation sert justement à libérer du temps pour ce genre de détail.

{H_ACC}"""),
    dict(template="constat", label="Le dimanche soir",
         texte="Dimanche, 19h.\nLes départs du week-end sont faits.", chute="Les questions de la semaine arrivent déjà.",
         legende=f"""Le dimanche soir, c'est souvent le moment où tout se superpose : les avis des voyageurs partis, les questions de ceux qui arrivent.

{H_CONC}"""),

    # 24 et 25 octobre
    dict(template="carte", photo="details-telephone", label=ASTUCE,
         titre="Affichez le code wifi *là où on le cherche.*",
         texte="Une petite carte près de l'entrée ou sur la table. C'est une question que l'on ne vous posera plus.",
         legende=f"""La question la plus fréquente mérite la réponse la plus visible.

Une carte posée à l'entrée, et le message du soir disparaît.

{H_ACC}"""),
    dict(template="plein", photo_fichier="region-bordeaux#6", phrase="Un dimanche dans les vignes,\n*sans notification.*",
         legende=f"""Prenez le temps. Les messages attendront lundi.

#vignes #campagne #france"""),

    # 31 octobre et 1er novembre
    dict(template="carte", photo_fichier="astuce-parapluie#4", label=ASTUCE,
         titre="Un jour de pluie, *un parapluie dans l'entrée.*",
         texte="Le détail qui fait sourire les voyageurs, et qui leur sauve une journée de balade.",
         legende=f"""La météo ne se commande pas, même en vacances.

Un parapluie à disposition, c'est une attention qui coûte peu et que les voyageurs n'oublient pas.

{H_ACC}"""),
    dict(template="constat", label="Fin des vacances",
         texte="Les vacances se terminent.\nLes derniers voyageurs repartent.", chute="Les avis arrivent.",
         legende=f"""Après les départs, les avis. Pensez à remercier ceux qui en laissent, même quand tout s'est bien passé.

{H_CONC}"""),

    # 7 et 8 novembre
    dict(template="carte", photo="interieur-cuisine", label=ASTUCE,
         titre="Expliquez le tri *avant qu'on vous le demande.*",
         texte="Jours de collecte, bacs, conteneur à verre : trois lignes dans le livret évitent les sacs oubliés au départ.",
         legende=f"""Chaque commune a ses règles, et les voyageurs ne les connaissent pas. Trois lignes claires suffisent.

{H_ACC}"""),
    dict(template="plein", photo="saison-hiver-mer", phrase="Au bord de l'eau,\n*le calme de novembre.*",
         legende=f"""La mer hors saison a quelque chose d'unique. Bon dimanche.

#mer #hiver #france"""),

    # 14 et 15 novembre
    dict(template="carte", photo="interieur-chambre", label=ASTUCE,
         titre="Des photos fidèles *évitent les déceptions.*",
         texte="Mieux vaut un logement un peu plus beau que ses photos que l'inverse. Les avis s'en souviennent.",
         legende=f"""La tentation est grande de montrer le logement sous son meilleur jour. Mais un voyageur déçu à l'arrivée le dira dans son avis.

Des photos justes, c'est un séjour qui commence bien.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="Vous répondez à vos voyageurs depuis des années.", chute="Vous connaissez déjà toutes les réponses.",
         legende=f"""Tout ce savoir existe déjà, dans votre tête. Le transmettre une bonne fois à un assistant, c'est ne plus avoir à le répéter.

{H_CONC}"""),

    # 21 et 22 novembre
    dict(template="carte", photo_fichier="interieur-cheminee#1", label=ASTUCE,
         titre="Un plaid sur le canapé, *le chauffage déjà lancé.*",
         texte="En hiver, arriver dans un logement froid gâche la soirée. Programmer le chauffage avant l'arrivée change tout.",
         legende=f"""L'hiver, le confort commence par la température. Un thermostat programmable ou un passage avant l'arrivée, et le voyageur se sent chez lui.

{H_ACC}"""),
    dict(template="plein", photo_fichier="interieur-cheminee#3", phrase="Un dimanche au coin du feu.\n*Enfin.*",
         legende=f"""Bon dimanche.

{H_CONC}"""),

    # 28 et 29 novembre
    dict(template="carte", photo_fichier="astuce-livret#3", label=ASTUCE,
         titre="Un livret d'accueil *se lit en deux minutes.*",
         texte="Les voyageurs ne lisent pas vingt pages. L'essentiel d'abord : arrivée, wifi, départ, urgences.",
         legende=f"""Un livret trop long n'est pas lu. Commencez par ce dont le voyageur a besoin dans l'heure qui suit son arrivée, le reste peut venir après.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="La meilleure réponse à un voyageur ?", chute="Celle qu'il n'a pas eu à attendre.",
         legende=f"""La qualité d'une réponse, c'est aussi son délai.

{H_CONC}"""),

    # 5 et 6 décembre
    dict(template="carte", photo_fichier="astuce-machine-cafe#4", label=ASTUCE,
         titre="Un café prêt *pour le premier matin.*",
         texte="Quelques dosettes, du sucre, deux tasses propres. Le premier réveil dans un logement devient un bon souvenir.",
         legende=f"""Le premier matin, personne n'a envie de chercher une boulangerie ouverte. Un café à disposition, c'est une attention simple et très appréciée.

{H_ACC}"""),
    dict(template="plein", photo="normandie-deauville", lieu="Deauville", phrase="Un dimanche sur les planches.\n*Sans personne.*",
         legende=f"""Deauville en décembre, rien que pour vous. Bon dimanche.

#deauville {H_NORM}"""),

    # 12 et 13 décembre
    dict(template="carte", photo="details-linge", label=ASTUCE,
         titre="Des serviettes en plus, *bien en vue.*",
         texte="Une pile rangée en évidence dans la salle de bain évite un message à 22h.",
         legende=f"""Si le voyageur doit chercher, il écrit. Si c'est visible, il se sert.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="Déléguer, ce n'est pas disparaître.", chute="C'est choisir où vous êtes utile.",
         legende=f"""Confier les questions répétitives, c'est garder votre énergie pour ce qui compte : les propriétaires, les imprévus, les voyageurs qui ont vraiment besoin de vous.

{H_CONC}"""),

    # 19 et 20 décembre
    dict(template="carte", photo="saison-noel", label=ASTUCE,
         titre="Une touche de fête, *sans en faire trop.*",
         texte="Quelques branches de sapin, une bougie, une guirlande discrète. Les voyageurs de décembre y sont sensibles.",
         legende=f"""Décorer un logement pour les fêtes, oui. Le transformer en vitrine de grand magasin, non. La sobriété fonctionne toujours mieux.

{H_ACC}"""),
    dict(template="plein", photo="saison-noel", phrase="Dernier dimanche avant Noël.\n*Respirez.*",
         legende=f"""La semaine qui arrive sera chargée. Profitez de ce dimanche.

{H_CONC}"""),

    # 26 et 27 décembre
    dict(template="carte", photo_fichier="astuce-porte#1", label=ASTUCE,
         titre="Le départ *se prépare dès l'arrivée.*",
         texte="Heure de départ, clés, poubelles, volets : une liste courte près de la porte. Moins de questions le dernier jour.",
         legende=f"""Les questions du dernier jour se ressemblent toutes. Une liste de départ affichée près de la porte y répond d'avance.

{H_ACC}"""),
    dict(template="constat", label="Entre les fêtes",
         texte="Entre Noël et le Nouvel An, les voyageurs écrivent toujours.", chute="Vous, vous avez le droit de souffler.",
         legende=f"""Bonnes fêtes de fin d'année.

{H_CONC}"""),

    # 2 et 3 janvier
    dict(template="carte", photo_fichier="astuce-chargeur#4", label=ASTUCE,
         titre="Un chargeur de téléphone *près du lit.*",
         texte="C'est le plus oublié des bagages. Un chargeur universel coûte peu et évite une soirée compliquée.",
         legende=f"""Première astuce de l'année, et sans doute la plus rentable : un chargeur laissé sur la table de nuit.

{H_ACC}"""),
    dict(template="plein", photo="normandie-mont", lieu="Mont-Saint-Michel", phrase="Premier dimanche de l'année.\n*Premier vrai repos ?*",
         legende=f"""Bonne année, et bon dimanche.

#montsaintmichel {H_NORM}"""),

    # 9 et 10 janvier
    dict(template="carte", photo="accueil-sonnette", label=ASTUCE,
         titre="Répondez aux avis, *même aux bons.*",
         texte="Un merci personnalisé montre qu'il y a quelqu'un derrière l'annonce. Les futurs voyageurs lisent aussi vos réponses.",
         legende=f"""Un avis sans réponse, c'est une conversation laissée en suspens. Quelques mots suffisent, à condition qu'ils ne soient pas copiés-collés.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="Votre expérience est précieuse.", chute="Elle mérite d'être transmise, pas répétée.",
         legende=f"""Chaque réponse que vous tapez pour la dixième fois est une connaissance qui pourrait travailler pour vous.

{H_CONC}"""),

    # 16 et 17 janvier
    dict(template="carte", photo_fichier="astuce-porte#2", label=ASTUCE,
         titre="Une arrivée autonome *s'explique en images.*",
         texte="Une photo de la porte, une de la boîte à clés, une de l'interrupteur. Plus clair que trois paragraphes.",
         legende=f"""Pour une arrivée autonome, rien ne vaut quelques photos bien choisies. Le voyageur se repère tout de suite, même de nuit.

{H_ACC}"""),
    dict(template="plein", photo="interieur-fenetre", phrase="Un dimanche de pluie.\n*Rien d'urgent.*",
         legende=f"""Bon dimanche à tous.

{H_CONC}"""),

    # 23 et 24 janvier
    dict(template="carte", photo_fichier="astuce-rue#4", label=ASTUCE,
         titre="Le stationnement *se décrit avec précision.*",
         texte="Gratuit ou payant, à quelle distance, dans quelle rue. C'est souvent la toute première question.",
         legende=f"""« Où est-ce que je peux me garer ? » arrive souvent avant même « bonjour ». Une réponse précise dans l'annonce et dans le livret évite ce message.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="Un bon gérant ne répond pas à tout.", chute="Il s'organise pour que tout ait une réponse.",
         legende=f"""Nuance importante, et c'est toute la différence entre être disponible et être organisé.

{H_CONC}"""),

    # 30 et 31 janvier
    dict(template="carte", photo_fichier="astuce-machine-cafe#2", label=ASTUCE,
         titre="Les appareils compliqués *méritent une étiquette.*",
         texte="Plaque de cuisson, machine à café, chauffage : une petite étiquette évite les appels au mauvais moment.",
         legende=f"""Ce qui est évident pour vous ne l'est pas pour quelqu'un qui découvre le logement. Une étiquette discrète, et le mode d'emploi est là où on en a besoin.

{H_ACC}"""),
    dict(template="plein", photo="details-cafe", phrase="Le dimanche commence\n*par un café chaud.*",
         legende=f"""Bon dimanche.

{H_CONC}"""),

    # 6 et 7 février
    dict(template="carte", photo_fichier="astuce-enfants#5", label=ASTUCE,
         titre="Vous accueillez des familles ? *Dites-le avec des détails.*",
         texte="Lit parapluie, chaise haute, barrière d'escalier : les parents cherchent précisément ces mots dans l'annonce.",
         legende=f"""« Adapté aux familles » ne veut rien dire pour un parent. La liste précise de l'équipement, si.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="Combien de fois avez-vous écrit où se trouve le code wifi ?", chute="Une dernière fois suffit.",
         legende=f"""Écrire une réponse une fois, correctement, et ne plus jamais la retaper. C'est tout le principe.

{H_CONC}"""),

    # 13 et 14 février
    dict(template="carte", photo_fichier="astuce-deux-verres#4", label=ASTUCE,
         titre="Pour un séjour à deux, *un détail suffit.*",
         texte="Deux verres, une bougie, une bonne adresse de restaurant. Pas besoin de pétales de rose partout.",
         legende=f"""Le week-end de la Saint-Valentin, beaucoup de réservations sont des séjours à deux. Une petite attention fait toute la différence.

{H_ACC}"""),
    dict(template="plein", photo_fichier="astuce-deux-verres#3", phrase="Bonne Saint-Valentin.\n*Le téléphone reste dans le sac.*",
         legende=f"""Bon dimanche, et belle Saint-Valentin.

{H_CONC}"""),

    # 20 et 21 février
    dict(template="carte", photo_fichier="astuce-chien#2", label=ASTUCE,
         titre="Animaux acceptés ? *Précisez les règles.*",
         texte="Sur le canapé ou pas, gamelle fournie ou non, supplément éventuel. Des règles claires évitent les litiges.",
         legende=f"""Accepter les animaux ouvre votre logement à beaucoup de voyageurs. Encore faut-il que tout le monde parte avec les mêmes règles en tête.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="Un voyageur satisfait ne se souvient pas de la réponse.", chute="Il se souvient qu'elle est arrivée vite.",
         legende=f"""La rapidité est une forme d'attention.

{H_CONC}"""),

    # 27 et 28 février
    dict(template="carte", photo_fichier="astuce-menage#6", label=ASTUCE,
         titre="Une liste de contrôle *pour chaque ménage.*",
         texte="Les oublis se ressemblent : ampoule grillée, papier toilette, piles de télécommande. La même liste à chaque passage.",
         legende=f"""Ce n'est pas le grand ménage qui pose problème, ce sont les petits oublis. Une liste identique pour chaque passage, et ils disparaissent.

{H_ACC}"""),
    dict(template="plein", photo_fichier="region-annecy#3", phrase="Fin février.\n*Les jours rallongent.*",
         legende=f"""La saison approche doucement. Bon dimanche.

#lac #montagne #france"""),

    # 6 et 7 mars
    dict(template="carte", photo_fichier="astuce-jardin#4", label=ASTUCE,
         titre="Le jardin *fait partie du logement.*",
         texte="Salon de jardin sorti, pelouse tondue, éclairage extérieur vérifié : au printemps, les voyageurs vivent dehors.",
         legende=f"""Dès les premiers beaux jours, l'extérieur devient la pièce principale. Il mérite la même attention que l'intérieur.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="L'été dernier, combien de messages après 23h ?", chute="Cet été peut être différent.",
         legende=f"""Il reste quelques semaines pour s'organiser avant la saison.

{H_CONC}"""),

    # 13 et 14 mars
    dict(template="carte", photo="accueil-sonnette", cadrage="center 78%", label=ASTUCE,
         titre="Un contact d'urgence *clair et affiché.*",
         texte="Dans le livret et près de la porte : qui appeler en cas de souci, et pour quoi. Le voyageur ne doit jamais se sentir seul.",
         legende=f"""Une fuite, une coupure de courant, une serrure qui bloque : en cas de vrai problème, le voyageur doit savoir immédiatement vers qui se tourner.

{H_ACC}"""),
    dict(template="plein", photo="saison-printemps", phrase="Le printemps arrive\n*doucement.*",
         legende=f"""Bon dimanche.

{H_CONC}"""),

    # 20 et 21 mars
    dict(template="carte", photo="interieur-salle-bain", label=ASTUCE,
         titre="Testez votre logement *comme un voyageur.*",
         texte="Dormez-y une nuit, ou demandez à un proche. On découvre toujours un détail : un store qui coince, une lampe qui manque.",
         legende=f"""Rien ne remplace l'expérience réelle. Une nuit dans votre propre logement avant la saison vous apprendra plus qu'une longue liste de vérifications.

{H_ACC}"""),
    dict(template="constat", label="Réflexion du dimanche",
         texte="Ce que vous faites de mieux, c'est accueillir.", chute="Pas répéter le code wifi.",
         legende=f"""Gardez votre temps pour ce qui fait vraiment votre valeur.

{H_CONC}"""),

    # 27 et 28 mars
    dict(template="carte", photo_fichier="astuce-porte#5", label=ASTUCE,
         titre="Un bon séjour *se termine par un au revoir.*",
         texte="Un message le jour du départ, un merci, une invitation à revenir. C'est souvent ce qui déclenche un bel avis.",
         legende=f"""La dernière impression compte autant que la première. Un au revoir personnalisé, et le voyageur repart avec l'envie de revenir.

{H_ACC}"""),
    dict(template="plein", photo="saison-printemps", phrase="Joyeuses Pâques.\n*Un dimanche pour vous.*",
         legende=f"""Joyeuses Pâques à toutes et à tous.

{H_CONC}"""),

    # 3 et 4 avril
    dict(template="carte", photo="normandie-cote", label=ASTUCE,
         titre="Relisez votre annonce *avant chaque saison.*",
         texte="Équipements, horaires, règles, photos : ce qui était vrai l'an dernier ne l'est peut-être plus.",
         legende=f"""Dernière astuce de la série, et peut-être la plus importante. Une annonce à jour, c'est moins de questions, moins de surprises, et de meilleurs avis.

{H_ACC}"""),
    dict(template="constat", label="La saison commence",
         texte="Les beaux jours sont là.\nLes voyageurs arrivent.", chute="Cette fois, vous êtes prêts.",
         legende=f"""Bonne saison à toutes les conciergeries qui nous suivent.

{CONTACT}

{H_CONC}"""),
]


# ═══════════════════════ RÉÉQUILIBRAGE (28/09/2026) ═══════════════════════
# Tom réoriente DelorIA : moins de messagerie voyageurs, plus de sites, identité,
# réseaux et automatisation PME. Ces posts remplacent, à la même date, le post
# de semaine prévu initialement. Clé = date de publication.

H_PME2 = "#pme #automatisation #industrie #entrepreneur #france"
DESIGN = "Note de design"
INGE = "Note d'ingénieur"

REMPLACEMENTS = {
    "2026-10-19": dict(template="constat", label="Réseaux sociaux",
         texte="Votre dernier post date de quand ?", chute="Vos clients, eux, regardent.",
         legende=f"""Un compte Instagram ou une fiche Google qui ne bouge plus, c'est souvent la première chose qu'un client potentiel remarque.

La régularité rassure. Et elle peut s'automatiser, comme sur ce compte.

{H_RESEAUX}"""),

    "2026-11-04": dict(template="constat", label="En entreprise",
         texte="Combien de fois par semaine recopiez-vous la même information ?", chute="Une fois suffirait.",
         legende=f"""D'un mail vers un tableau, d'un tableau vers un devis, d'un devis vers une facture. Chaque recopie prend du temps et laisse passer des erreurs.

C'est typiquement ce qu'on automatise en premier.

{H_PME2}"""),

    "2026-11-09": dict(template="terrain_photo", serie="ingenieur", photo="secteur-atelier", label=INGE,
         titre="Automatiser un processus flou, *c'est automatiser le désordre.*",
         texte="Avant d'écrire une ligne, on décrit le processus tel qu'il est vraiment, avec ses exceptions et ses cas particuliers.",
         chute="La moitié du travail se fait sur papier.",
         legende=f"""Nouvelle série : des notes d'ingénieur sur l'automatisation en entreprise.

La première règle est simple. Un outil ne rend pas un processus plus clair, il le rend plus rapide. Si le processus est confus, il devient confus plus vite. On commence donc toujours par le décrire.

{H_PME2}"""),

    "2026-11-18": dict(template="terrain_photo", serie="design", photo_fichier="astuce-mot#4", label=DESIGN,
         titre="Deux typographies, *pas plus.*",
         texte="Une pour les titres, une pour le texte. Au-delà, un support perd sa cohérence et son élégance.",
         chute="La sobriété se voit avant de se lire.",
         legende=f"""Nouvelle série : des notes de design, pour des supports qui vous ressemblent.

Sur ce compte, il n'y a que deux polices : une élégante pour les titres, une simple pour le texte. C'est cette contrainte qui donne l'impression d'ensemble.

{H_DESIGN}"""),

    "2026-11-25": dict(template="edito", photo_fichier="astuce-mot#1", label="Pour les PME",
         titre="Les mails qui se ressemblent *peuvent se préparer seuls.*",
         texte="Demandes de prix, relances, confirmations : un outil prépare la réponse avec vos informations. Vous relisez, vous envoyez.",
         pictos=[dict(icone="message", texte="Mail\nreçu"), dict(icone="document", texte="Réponse\npréparée"), dict(icone="check", texte="Relue\npar vous")],
         cta="Écrivez-moi en privé",
         legende=f"""Dans beaucoup d'entreprises, une partie des mails reçus appelle toujours la même réponse, à quelques détails près.

Un outil peut les repérer, préparer la réponse avec les bonnes informations, et vous la proposer. La décision d'envoyer reste la vôtre.

{CONTACT}

{H_PME2}"""),

    "2026-12-02": dict(template="constat", label="Réseaux sociaux",
         texte="Un compte qui ne publie plus donne l'impression d'une activité qui s'arrête.", chute="Même quand ce n'est pas le cas.",
         legende=f"""Décembre est souvent le mois où l'on n'a plus le temps de publier. C'est aussi celui où beaucoup de clients préparent l'année suivante et regardent qui est actif.

{H_RESEAUX}"""),

    "2026-12-14": dict(template="terrain_photo", serie="design", photo_fichier="astuce-lampe#6", label=DESIGN,
         titre="Une couleur d'accent, *utilisée avec parcimonie.*",
         texte="Dans ma charte, l'or n'apparaît que sur quelques détails. C'est ce qui lui garde sa valeur.",
         chute="Ce qui est partout ne se remarque plus.",
         legende=f"""Une palette réussie repose souvent sur une couleur forte, réservée aux éléments importants.

Utilisée partout, elle devient du bruit. Utilisée avec retenue, elle guide le regard.

{H_DESIGN}"""),

    "2026-12-16": dict(template="constat", label="En entreprise",
         texte="L'information existe quelque part.", chute="Le problème, c'est de la retrouver.",
         legende=f"""Une procédure, une fiche technique, la bonne version d'un devis : tout est là, mais dans quel dossier ?

Un assistant interne peut répondre à partir de vos propres documents, en citant la source.

{H_PME2}"""),

    "2026-12-21": dict(template="service", label="Comment se passe un projet", titre="Commencer par une tâche, *pas par tout.*",
         points=["Un échange pour repérer ce qui se répète", "Un premier outil sur une seule tâche", "On mesure, puis on élargit"],
         signature="PME · PARTOUT EN FRANCE",
         legende=f"""Je ne propose jamais de tout automatiser d'un coup.

On part d'une seule tâche, celle qui revient le plus souvent. On la traite bien, on vérifie le gain, et seulement ensuite on passe à la suivante.

{CONTACT}

{H_PME2}"""),

    "2026-12-28": dict(template="service", label="Identité visuelle", titre="Ce que comprend *une identité visuelle.*",
         points=["Un logo en plusieurs versions", "Une palette et deux typographies", "Des règles d'usage simples"],
         signature="PARTOUT EN FRANCE",
         legende=f"""Un logo seul ne fait pas une identité.

Ce qui rend une marque reconnaissable, c'est la cohérence : les mêmes couleurs, les mêmes polices et les mêmes règles sur le site, les réseaux, les devis et les cartes de visite.

{CONTACT}

{H_DESIGN}"""),

    "2026-12-30": dict(template="service", label="Sites internet", titre="Un site en trois étapes, *sans jargon.*",
         points=["Un échange pour comprendre votre activité", "Une maquette à valider ensemble", "La mise en ligne et les réglages"],
         signature="PARTOUT EN FRANCE",
         legende=f"""Pour l'année qui vient, peut-être un nouveau site ?

Je travaille simplement : on parle de votre activité, je vous montre une maquette, on ajuste, puis je m'occupe de la mise en ligne.

{CONTACT}

{H_DESIGN}"""),

    "2027-01-04": dict(template="edito", photo_fichier="astuce-lampe#4", label="Réseaux sociaux",
         titre="Vos publications, *à vos couleurs, prêtes à l'avance.*",
         texte="Des modèles créés une fois dans votre charte, remplis automatiquement à chaque publication. Le rendu reste le même, post après post.",
         pictos=[dict(icone="pinceau", texte="Vos\nmodèles"), dict(icone="calendrier", texte="Prêts à\nl'avance"), dict(icone="check", texte="Rendu\nconstant")],
         cta="Écrivez-moi en privé",
         legende=f"""Nouvelle année, bonne résolution : publier régulièrement.

Le plus dur n'est pas de publier une fois, c'est de tenir. Avec des modèles à vos couleurs et un calendrier préparé, la régularité ne dépend plus de votre emploi du temps.

{CONTACT}

{H_RESEAUX}"""),

    "2027-01-13": dict(template="terrain_photo", serie="ingenieur", photo="secteur-artisan", label=INGE,
         titre="Garder l'humain *au moment de la décision.*",
         texte="L'outil prépare, trie, rédige. La validation d'un devis ou d'une réponse importante reste chez vous.",
         chute="Automatiser n'est pas abdiquer.",
         legende=f"""Une règle que j'applique à chaque projet : l'automatisme fait le travail répétitif, la personne garde la décision.

C'est plus sûr, et c'est aussi ce qui permet aux équipes d'adopter l'outil sans méfiance.

{H_PME2}"""),

    "2027-02-03": dict(template="terrain_photo", serie="design", photo_fichier="astuce-chargeur#2", label=DESIGN,
         titre="Un site se conçoit *d'abord pour le téléphone.*",
         texte="On part du petit écran, puis on adapte à l'ordinateur. L'inverse donne des pages illisibles dans la poche.",
         chute="C'est là que vos clients vous découvrent.",
         legende=f"""La plupart des visites commencent sur un téléphone, entre deux choses.

Concevoir le site pour ce petit écran en premier oblige à aller à l'essentiel. Et ce qui fonctionne sur téléphone fonctionne presque toujours sur ordinateur.

{H_DESIGN}"""),

    "2027-02-08": dict(template="edito", photo="secteur-industrie", label="Exemple · Maintenance",
         titre="Le rapport d'intervention, *rédigé avant de repartir.*",
         texte="Quelques notes prises sur place, un rapport mis en forme automatiquement, envoyé au client après votre relecture.",
         pictos=[dict(icone="mobile", texte="Notes\nsur place"), dict(icone="document", texte="Rapport\nmis en forme"), dict(icone="check", texte="Relu\npar vous")],
         cta="Écrivez-moi en privé",
         legende=f"""Un exemple de ce qui est possible pour une entreprise de maintenance.

Le rapport d'intervention se rédige souvent le soir, de mémoire. Il peut se préparer à partir de quelques notes prises sur place, dans un format propre et identique à chaque fois.

{H_PME2}"""),

    "2027-02-17": dict(template="constat", label="Coulisses",
         texte="Ces visuels sont générés automatiquement.", chute="La charte, elle, a été pensée à la main.",
         legende=f"""L'automatisation ne remplace pas le travail de conception. Elle le répète fidèlement.

Tout commence par une charte soignée : couleurs, polices, mises en page. Ensuite seulement, les publications peuvent se produire seules sans perdre en qualité.

{H_DESIGN} {H_RESEAUX}"""),

    "2027-02-24": dict(template="terrain_photo", serie="design", photo_fichier="astuce-porte#3", label=DESIGN,
         titre="Le contact, *à un geste sur chaque page.*",
         texte="Téléphone, formulaire, message : sur un site, le moyen de vous joindre doit se trouver sans chercher.",
         chute="Un visiteur qui cherche est un visiteur qui part.",
         legende=f"""Un détail qui change tout sur un site : l'accès au contact.

S'il faut remonter la page ou fouiller un menu pour vous joindre, beaucoup abandonnent. Un bouton visible partout, et la question ne se pose plus.

{H_DESIGN}"""),

    "2027-03-10": dict(template="terrain_photo", serie="ingenieur", photo="secteur-industrie", label=INGE,
         titre="Commencer par la tâche *la plus répétée.*",
         texte="Le meilleur premier projet est rarement le plus ambitieux. C'est une tâche simple, faite plusieurs fois par jour.",
         chute="Les gains visibles donnent envie d'aller plus loin.",
         legende=f"""Quand on démarre l'automatisation, la tentation est de s'attaquer au problème le plus complexe.

C'est souvent une erreur. Une petite tâche très fréquente, bien automatisée, fait gagner du temps dès la première semaine. C'est ce qui convainc les équipes.

{H_PME2}"""),

    "2027-03-24": dict(template="constat", label="En entreprise",
         texte="Le devis part le lendemain.", chute="Le client, lui, a déjà demandé ailleurs.",
         legende=f"""La réactivité est un argument commercial. Préparer un devis en quelques minutes au lieu de quelques heures, c'est parfois ce qui fait la différence.

{CONTACT}

{H_PME2}"""),

    "2027-03-31": dict(template="terrain_photo", serie="design", photo_fichier="secteur-atelier#2", label=DESIGN,
         titre="Un logo se teste *en tout petit.*",
         texte="Sur une photo de profil ou dans un onglet de navigateur, il ne fait que quelques millimètres.",
         chute="S'il reste lisible là, il le sera partout.",
         legende=f"""Un logo se juge souvent en grand, sur un écran d'ordinateur. Mais il vivra surtout en petit : sur les réseaux, dans un onglet, sur un tampon.

Le test le plus simple : le réduire à la taille d'un ongle et voir ce qu'il en reste.

{H_DESIGN}"""),
}
