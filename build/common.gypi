{
    'variables': {
        'variables': {
            'clang%': 0
        },
        'conditions': [
        ['clang == 1', {
                'make_global_settings': [
                ['CXX','/usr/bin/clang++'],
                ['LINK','/usr/bin/clang++'],
              ],
        }, {}
        ]
      ],
  },
  'target_defaults': {
      'default_configuration': 'Debug',
      'configurations': {
          'Common_Base': {
              'abstract': 1,
          },
          'Debug_Base': {
              'abstract': 1,
              'defines': [
                  'DEBUG=1',
                  'LOG_LEVEL=5',
              ],
              'cflags': [
                '-O0'
              ]
           },
           'Debug':  {
               'inherit_from': ['Common_Base', 'Debug_Base'],
           },
      },
  },
}
