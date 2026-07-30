CITY_ENTITIES = {
    # Asia-Pacific
    "bangkok": {"wifi_speed": "120 Mbps", "avg_cost": "$1,400/mo", "country": "Thailand", "region": "Asia", "top_spot": "HUBBA Ekkamai", "matcha_spot": "Peace Oriental Teahouse", "app": "Grab / Bolt", "related": ["chiang-mai", "da-nang", "bali"]},
    "chiang-mai": {"wifi_speed": "95 Mbps", "avg_cost": "$1,100/mo", "country": "Thailand", "region": "Asia", "top_spot": "Punspace Tha Phae", "matcha_spot": "Ristr8to", "app": "Grab / Bolt", "related": ["bangkok", "da-nang", "bali"]},
    "bali": {"wifi_speed": "85 Mbps", "avg_cost": "$1,300/mo", "country": "Indonesia", "region": "Asia", "top_spot": "Dojo Bali", "matcha_spot": "Matcha Cafe Bali", "app": "Gojek / Grab", "related": ["bangkok", "chiang-mai", "da-nang"]},
    "tokyo": {"wifi_speed": "210 Mbps", "avg_cost": "$2,800/mo", "country": "Japan", "region": "Asia", "top_spot": "Biolab Tokyo", "matcha_spot": "Ippodo Tea Marunouchi", "app": "GO App / Suica", "related": ["bangkok", "lisbon", "berlin"]},
    "da-nang": {"wifi_speed": "80 Mbps", "avg_cost": "$900/mo", "country": "Vietnam", "region": "Asia", "top_spot": "Enouvo Space", "matcha_spot": "43 Factory Coffee", "app": "Grab", "related": ["bangkok", "chiang-mai", "bali"]},
    "kuala-lumpur": {"wifi_speed": "110 Mbps", "avg_cost": "$1,250/mo", "country": "Malaysia", "region": "Asia", "top_spot": "Colony Coworking", "matcha_spot": "Matcha Hero Kyoto", "app": "Grab", "related": ["bangkok", "bali", "singapore"]},
    "singapore": {"wifi_speed": "240 Mbps", "avg_cost": "$3,800/mo", "country": "Singapore", "region": "Asia", "top_spot": "The Working Capitol", "matcha_spot": "Hvala Craig Rd", "app": "Grab / MRT", "related": ["kuala-lumpur", "tokyo", "bangkok"]},

    # Europe
    "lisbon": {"wifi_speed": "150 Mbps", "avg_cost": "$2,100/mo", "country": "Portugal", "region": "Europe", "top_spot": "LACS Conde d'Óbidos", "matcha_spot": "Matcha Mama Lisbon", "app": "Bolt / Uber", "related": ["barcelona", "berlin", "tbilisi"]},
    "barcelona": {"wifi_speed": "180 Mbps", "avg_cost": "$2,600/mo", "country": "Spain", "region": "Europe", "top_spot": "Aticco Urquinaona", "matcha_spot": "HanSo Cafe", "app": "Cabify / Uber", "related": ["lisbon", "berlin", "medellin"]},
    "berlin": {"wifi_speed": "130 Mbps", "avg_cost": "$2,400/mo", "country": "Germany", "region": "Europe", "top_spot": "Factory Berlin", "matcha_spot": "The Barn Roastery", "app": "FreeNow / Uber", "related": ["lisbon", "barcelona", "tokyo"]},
    "tbilisi": {"wifi_speed": "90 Mbps", "avg_cost": "$1,200/mo", "country": "Georgia", "region": "Europe", "top_spot": "Impact Hub Tbilisi", "matcha_spot": "Coffee LAB", "app": "Yandex Go / Bolt", "related": ["lisbon", "chiang-mai", "medellin"]},
    "porto": {"wifi_speed": "140 Mbps", "avg_cost": "$1,800/mo", "country": "Portugal", "region": "Europe", "top_spot": "Porto i/o", "matcha_spot": "Epoca Cafe", "app": "Bolt / Uber", "related": ["lisbon", "barcelona", "madrid"]},
    "budapest": {"wifi_speed": "130 Mbps", "avg_cost": "$1,500/mo", "country": "Hungary", "region": "Europe", "top_spot": "KAPTÁR Coworking", "matcha_spot": "Kontakt Coffee", "app": "Bolt", "related": ["prague", "berlin", "tbilisi"]},

    # Americas
    "medellin": {"wifi_speed": "90 Mbps", "avg_cost": "$1,100/mo", "country": "Colombia", "region": "Americas", "top_spot": "Selah Coworking", "matcha_spot": "Teahouse El Poblado", "app": "Uber / InDrive", "related": ["mexico-city", "bali", "tbilisi"]},
    "new-york": {"wifi_speed": "250 Mbps", "avg_cost": "$4,200/mo", "country": "United States", "region": "Americas", "top_spot": "WeWork 450 Lexington", "matcha_spot": "Cha Cha Matcha", "app": "Uber / Lyft / UberEats", "related": ["tokyo", "london", "barcelona"]},
    "mexico-city": {"wifi_speed": "110 Mbps", "avg_cost": "$1,600/mo", "country": "Mexico", "region": "Americas", "top_spot": "Público Condesa", "matcha_spot": "Matcha Kaori", "app": "Uber / DiDi", "related": ["medellin", "barcelona", "lisbon"]},
    "buenos-aires": {"wifi_speed": "85 Mbps", "avg_cost": "$1,000/mo", "country": "Argentina", "region": "Americas", "top_spot": "AreaTres Soho", "matcha_spot": "Lattente", "app": "Cabify / Uber", "related": ["medellin", "mexico-city", "lima"]}
}