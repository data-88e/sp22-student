test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> assert data.num_rows == 12810\n>>> assert data.num_columns == 52\n>>> assert type(data) == Table\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert data.group("countrycode").num_rows == 183\n>>> assert data.group("year").num_rows == 70\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert data.where("countrycode", "USA").where("year", 1956).column("hc")[0] == \'2,662317276\'\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
