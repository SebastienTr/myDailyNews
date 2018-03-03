# =============
# User settings
# =============

LANGUAGE = 'french'
LANGUAGE_KEY = 'fr'
LANGUAGE_VOICE = 'Thomas' # 'Aurelie' 'Audrey' 'Thomas'

NEWS_WEBSITES = {
	'Le Monde': {
		'url': 'http://www.lemonde.fr/rss/une.xml',
		'type': 'International',
	},
	'BFMTV': {
		'url': 'http://www.bfmtv.com/rss/info/flux-rss/flux-toutes-les-actualites/',
		'type': 'International',
	},
	# 'Nice Matin': {
	# 	'url': 'http://www.nicematin.com/ville/nice/rss',
	# 	'type': 'Local',
	# },
}
NEWS_RESUME_LEN = 3

OUTPUT_VIEW_PATH = "browser/chrome/MyDailyNews/index.html"

AERIAL_URL = "http://a1.phobos.apple.com/us/r1000/000/Features/atv/AutumnResources/videos/entries.json"

# =====================
# Translations settings
# =====================

DAY_PLACEMENT = {
	0: 'Aujourd\'hui',
	1: 'Demain',
	2: 'Après demain',
	3: 'Dans trois jours',
	4: 'Dans quatres jours',
}

NEWS_TYPE = {
	'international': 'internationales',
	'local': 'locales'
}

CONDITIONS = {
	'Ensoleillé': 'Le temps sera Ensoleillé',
	'Nuit claire': 'La nuit sera claire',
	'Ciel voilé': 'Le ciel sera voilé',
	'Nuit légèrement voilée': 'La nuit sera légèrement voilée',
	'Faibles passages nuageux': 'Il y aura de faibles passages nuageux',
	'Nuit bien dégagée': 'La nuit sera bien dégagée',
	'Brouillard': 'Il y aura du brouillard',
	'Stratus': 'Il y aura du stratus',
	'Stratus se dissipant': 'Le stratus vas se dissiper',
	'Nuit claire et stratus': 'La nuit sera claire et il y aura du stratus',
	'Eclaircies': 'Il y aura des éclaircies',
	'Nuit nuageuse': 'La nuit sera nuageuse',
	'Faiblement nuageux': 'Le temps vas être faiblement nuageux',
	'Fortement nuageux': 'Le temps vas être fortement nuageux',
	'Averses de pluie faible': 'Il y aura quelques averses de pluie faible',
	'Nuit avec averses': 'Il y aura quelques averses dans la nuit',
	'Averses de pluie modérée': 'Il y aura des averses de pluie modérée',
	'Averses de pluie forte': 'Il y aura des averses de pluie forte',
	'Couvert avec averses': 'Le temps sera couvert avec quelques averses',
	'Pluie faible': 'Il vas y avoir une pluie faible',
	'Pluie forte': 'Il vas y avoir uen pluie forte',
	'Pluie modérée': 'Il vas y avoir une pluie modérée',
	'Développement nuageux': 'Les nuages vont se développés',
	'Nuit avec développement nuageux': 'Les nuages vont se développés dans la nuit',
	'Faiblement orageux': 'Il vas y avoir quelques orages',
	'Nuit faiblement orageuse': 'Il vas y avoir quelques orages dans la nuit',
	'Orage modéré': 'Il y aura des orages',
	'Fortement orageux': 'Il vas y avoir beaucoup d\'orages',
	'Averses de neige faible': 'Il y aura quelques averses de neige faible',
	'Nuit avec averses de neige faible': 'Il y aura quelques averses de neige faible cette nuit',
	'Neige faible': 'Il vas y avoir de la neige faiblement',
	'Neige modérée': 'Il vas y avoir de la neige modérément',
	'Neige forte': 'Il vas y avoir de la neige fortement',
	'Pluie et neige mêlée faible': 'Il vas y avoir de la pluie en plus de neige mêlée faiblement',
	'Pluie et neige mêlée modérée': 'Il vas y avoir de la pluie en plus de neige mêlée modérément',
	'Pluie et neige mêlée forte': 'Il vas y avoir de la pluie en plus de neige mêlée fortement',
}