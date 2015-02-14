{
    'variables': {
        'path_common_gyp': '<(DEPTH)/build/common.gypi',
    },
    'includes': [
    '../build/common.gypi',
    ],
    'variables': {
        'script': './generate_src.sh',
        'generated_src': [ '<(SHARED_INTERMEDIATE_DIR)/helloworld.cpp' ],
    }
}
