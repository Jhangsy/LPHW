provinces = {
    'Jilin': 'JL',
    'Heilongjiang': 'HLJ',
    'LiaoNing': 'LN',
    'Guangzhou': 'GZ',
}

cities = {
    'LN': 'Shenyang',
    'HLJ': 'Harbin',
    'JL': 'Changchun',
    'GZ': 'Dongguan'
}

for province in provinces.keys():
    print province

for abbrev in provinces.values():
    print abbrev

for province, abbrev in provinces.items():
    print "%s has a abbreviation: %s" % (province, abbrev)

for abbrev, city in cities.items():
    print "%s has %s." % (abbrev, city)

for province, abbrev in provinces.items():
    print "%s 's abbreviation is %s, %s is in it." % (province, abbrev, cities[abbrev])

province = provinces.get('Tianjin')
if province is None:
    print " Don't exits"
