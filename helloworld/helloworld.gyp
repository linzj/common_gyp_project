{
    'includes': [
    'helloworld.gypi',
    ],
    'targets': [
        {
            'target_name': 'generate_src',
            'type': 'none',
            'actions': [{
                'action_name': 'generate_src',
                'inputs': ['<(script)'],
                'outputs': ['<@(generated_src)'],
                'action': [
                '<(script)', 
                '<@(generated_src)',
                ]
            },
            ],
            'message': 'generating source file.'
        },
        {
            'target_name': 'helloworld',
            'type': 'executable',
            'sources': [ '<@(generated_src)' ],
            'dependencies' : [
                'generate_src',
            ],
            'include_dirs' : [
                '.',
            ],
        },
    ],
}
