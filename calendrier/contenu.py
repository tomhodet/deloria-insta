"""Contenu éditorial DelorIA, 6 mois, du lundi 5 octobre 2026 au vendredi 2 avril 2027.

Une entrée par post, dans l'ordre de publication (lundi, mercredi, vendredi).
"photo" désigne un dossier de photos/pexels/ : construire.py choisit une photo
non encore utilisée dans ce dossier, sauf si "photo_fichier" impose un fichier.
Règles : faits réels uniquement, aucun tiret long ou moyen, vouvoiement,
aucun nom de client, jamais "à leur place".
"""

H_CONC = "#conciergerie #conciergerieairbnb #locationcourteduree #airbnb #hotes"
H_NORM = "#normandie #lehavre"
H_PME = "#pme #automatisation #entrepreneur #normandie"
H_DESIGN = "#identitevisuelle #chartegraphique #siteinternet #normandie"
H_RESEAUX = "#reseauxsociaux #instagram #automatisation #normandie"

CONTACT = "Une question ? Écrivez-moi en message privé."

POSTS = [
    # ─────────────── OCTOBRE 2026 ───────────────
    dict(template="plein", photo_fichier="photos/pexels/normandie-falaises/6395435_adrien-olichon.jpg",
         lieu="Étretat, Normandie", phrase="La côte ne dort jamais.\n*Vos voyageurs non plus.*", decalage=-230,
         legende=f"""Bienvenue chez DelorIA.

Je m'appelle Tom, je suis ingénieur et je travaille depuis la région du Havre. Je construis des outils qui répondent aux voyageurs des conciergeries comme vous le feriez, de jour comme de nuit.

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
         texte="Visuel, texte, date de publication : tout part automatiquement, trois fois par semaine. Je peux mettre en place la même chose pour votre compte.",
         pictos=[dict(icone="calendrier", texte="3 posts\npar semaine"), dict(icone="pinceau", texte="À vos\ncouleurs"), dict(icone="engrenage", texte="Sans y\npenser")],
         cta="Écrivez-moi en privé",
         legende=f"""Petit aveu : ce compte tourne tout seul.

Les visuels sont générés à mes couleurs, les textes sont préparés à l'avance, et un automate publie chaque lundi, mercredi et vendredi. Je n'ouvre Instagram que pour répondre à vos messages.

Si vous voulez la même chose pour votre activité, parlons-en.

{H_RESEAUX}"""),

    dict(template="plein", photo="normandie-honfleur", lieu="Honfleur, Normandie", phrase="Honfleur s'éveille.\n*Vos messages aussi.*",
         legende=f"""Les premiers messages de la journée arrivent souvent avant le premier café : une heure d'arrivée, une question sur le petit-déjeuner, un train en retard.

Un petit bout de Normandie pour commencer le week-end.

#honfleur {H_NORM} #conciergerie"""),

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
         signature="CONCIERGERIES · NORMANDIE",
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

    dict(template="plein", photo="normandie-falaises", lieu="Étretat, Normandie", phrase="Certains paysages\n*se passent de description.*",
         legende=f"""Pas de conseil aujourd'hui. Juste Étretat.

#etretat {H_NORM} #cotedalbatre"""),

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

    dict(template="plein", photo="interieur-cheminee", phrase="Les soirées d'hiver\n*méritent mieux qu'un code wifi.*",
         legende=f"""Le feu dans la cheminée, le téléphone retourné sur la table. Voilà l'objectif.

Bon week-end.

{H_CONC}"""),

    dict(template="service", label="Pour les PME", titre="Automatiser ce qui se répète, *garder ce qui compte.*",
         points=["Des devis préparés à partir de vos paramètres", "Des réponses aux mails qui reviennent sans cesse", "Vos procédures retrouvées en une question"],
         signature="PME · NORMANDIE",
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

{H_NORM} #mer #hiver"""),

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

    dict(template="plein", photo="normandie-honfleur", lieu="Honfleur, Normandie", phrase="Les plus beaux ports\n*ne ferment jamais.*",
         legende=f"""Honfleur en décembre. Bon week-end à tous.

#honfleur {H_NORM}"""),

    dict(template="service", label="Comment on démarre", titre="Commencer petit, *pour bien commencer.*",
         points=["Un appel pour comprendre votre quotidien", "Un premier logement pour tester", "On élargit quand tout fonctionne"],
         signature="CONCIERGERIES · NORMANDIE",
         legende=f"""Je ne branche jamais un assistant sur tout un parc d'un coup.

On commence par un échange sur votre façon de travailler, puis un seul logement, le temps de vérifier que les réponses sont justes et que le ton vous ressemble. Ensuite seulement, on étend.

{CONTACT}

{H_CONC}"""),

    dict(template="plein", photo="saison-noel", phrase="Chez vous aussi,\n*c'est bientôt les fêtes.*",
         legende=f"""Derniers jours avant Noël. Pensez à vous accorder quelques soirées sans téléphone.

{H_CONC}"""),

    dict(template="plein", photo_fichier="interieur-cheminee#6", phrase="Joyeux Noël.\n*Le téléphone peut attendre.*",
         legende="""Joyeux Noël à toutes les conciergeries, à leurs équipes, et à tous ceux qui travaillent pendant que les autres sont en vacances.

#joyeuxnoel #conciergerie #normandie"""),

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

    dict(template="plein", photo="normandie-campagne", phrase="Hors saison.\n*Calme, enfin.*",
         legende=f"""Les chemins sont vides, les réservations plus rares. Le bon moment pour souffler, et pour préparer la saison.

{H_NORM} #campagne"""),

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

    dict(template="plein", photo="normandie-falaises", lieu="Étretat, Normandie", phrase="La Normandie,\n*c'est chez moi.*",
         legende=f"""DelorIA est basée tout près du Havre, à quelques kilomètres de ces falaises.

Travailler avec quelqu'un de proche, c'est pouvoir se rencontrer, s'appeler, et avoir un interlocuteur qui connaît votre région. En Normandie, un café est toujours possible.

#etretat {H_NORM}"""),

    dict(template="terrain_photo", photo="details-carnet", label="Note de terrain",
         titre="Une information, *un seul endroit.*",
         texte="Le code wifi change ? On le met à jour là où vous gérez déjà vos logements, et l'assistant le lit à chaque conversation.",
         chute="Deux sources, c'est la garantie qu'une des deux sera fausse.",
         legende=f"""Un principe que j'applique partout : chaque information vit à un seul endroit.

Si le wifi est écrit à la fois dans votre logiciel de location et dans l'assistant, un jour l'un des deux sera oublié. Alors l'assistant va chercher l'information là où vous la tenez déjà à jour.

{H_CONC}"""),

    dict(template="service", label="Ce que je fais", titre="Un seul interlocuteur *pour tout ce qui se répète.*",
         points=["Les réponses à vos voyageurs", "Vos sites et votre identité visuelle", "Vos publications sur les réseaux"],
         signature="DELORIA · NORMANDIE",
         legende=f"""En résumé, DelorIA, c'est :

Un assistant qui répond à vos voyageurs comme vous le feriez.
Des sites, logos et chartes graphiques à votre image.
Des publications automatisées sur vos réseaux, comme ce compte.

Et un interlocuteur unique, près de chez vous.

{CONTACT}

{H_CONC} {H_DESIGN}"""),

    dict(template="plein", photo="normandie-deauville", lieu="Deauville", phrase="Deauville hors saison.\n*Le temps de tout préparer.*",
         legende=f"""Les planches sont calmes en janvier. Dans quelques semaines, les réservations du printemps arriveront.

#deauville {H_NORM}"""),

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

{H_CONC} {H_NORM}"""),

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
         signature="CONCIERGERIES · NORMANDIE",
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

    dict(template="plein", photo="normandie-falaises", lieu="Côte d'Albâtre", phrase="La côte se réveille.\n*Vos réservations aussi.*",
         legende=f"""Les premières réservations de printemps arrivent. Bon week-end.

#cotedalbatre {H_NORM}"""),

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

    dict(template="plein", photo="normandie-honfleur", lieu="Honfleur", phrase="Honfleur,\n*à l'heure où tout commence.*",
         legende=f"""Les terrasses rouvrent, les voyageurs reviennent. La saison est lancée.

#honfleur {H_NORM}"""),

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

    dict(template="service", label="Pourquoi DelorIA", titre="Un ingénieur près du Havre, *pas une plateforme.*",
         points=["Je configure tout avec vous", "Je surveille ce que j'installe", "Je réponds quand vous m'écrivez"],
         signature="LE HAVRE · NORMANDIE",
         legende=f"""Les grands logiciels vendent des fonctionnalités. Je propose un accompagnement.

Je configure chaque outil avec vous, je surveille ce que j'installe, et vous avez quelqu'un à appeler. Près de chez vous.

{CONTACT}

{H_CONC} {H_NORM}"""),

    dict(template="terrain", label="Note de terrain",
         titre="Deux logements, *deux fiches.*",
         texte="Même conciergerie, même ville, mais pas le même parking ni le même wifi. L'assistant répond avec la fiche du bon logement.",
         chute="Le détail qui évite la pire des erreurs.",
         legende=f"""Quand une conciergerie gère plusieurs logements, tous les messages arrivent souvent au même endroit.

Avant de répondre, l'assistant vérifie de quel logement il s'agit et ne répond qu'avec ses informations. Répondre avec le code wifi du voisin, c'est exactement ce qu'on doit rendre impossible.

{H_CONC}"""),

    # ─────────────── AVRIL 2027 ───────────────
    dict(template="plein", photo="normandie-cote", phrase="Six mois de posts.\n*Aucun publié à la main.*",
         legende=f"""Depuis octobre, chaque publication de ce compte est partie toute seule, trois fois par semaine. Visuels, textes, dates : tout était prêt à l'avance.

Si vous voulez la même tranquillité pour votre activité, sur vos réseaux ou avec vos voyageurs, écrivez-moi.

{H_RESEAUX} {H_CONC}"""),
]
