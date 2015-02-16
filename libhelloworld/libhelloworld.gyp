{
    'includes': [
    'libhelloworld.gypi',
    ],
    'targets': [
        {
            'target_name': 'libhelloworld',
            'product_prefix': '',
            'product_extension': 'dll',
            'type': 'shared_library',
            'sources': [ '<@(src)' ],
            'include_dirs' : [
                '.',
            ],
            'cflags': [
                '<@(shared_library_cflags)',
            ],
        },
    ],
}
