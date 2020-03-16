PIPELINE_COMPILERS = (
    'pipeline_compass.compiler.CompassCompiler',
    'pipeline.compilers.es6.ES6Compiler',
    'pipeline.compilers.livescript.LiveScriptCompiler',
)

PIPELINE_CSS = {
    'mapping': {
        'source_filenames': (
            'styles/mapping.scss',
            # 'styles/ui-grid.css',
        ),
        'output_filename': 'styles/mapping.css',
    },
    'vendor': {
        'source_filenames': {
            # 'normalize-3.0.2/normalize.css',
            'bootstrap/dist/css/bootstrap.min.css',
            'font-awesome/css/font-awesome.min.css',
            'angular-material/angular-material.min.css',
            'angular-ui-grid-3.0.4/ui-grid.min.css',
            'ez-dropdown/ez-dropdown.min.css',
            'ez-datetime-0.1.4/ez-datetime.css',
        },
        'output_filename': 'styles/vendor.css',
    }
}

PIPELINE_JS = {
    'mapping': {
        'source_filenames': (
            'scripts/mapping.es6',
            'scripts/mapping.config.es6',
            'scripts/mapping.controller.es6',
            'scripts/mapping.routes.es6',
            'scripts/**/*.es6',
            'scripts/**/*.ls',
            'scripts/**/**/*.es6',
            'scripts/**/**/*.ls',
            'scripts/**/**/**/*.es6',
            'scripts/**/**/**/*.ls',
        ),
        'output_filename': 'scripts/mapping.js',
    },
    'mapping-lite': {
        'source_filenames': (
            'scripts/mapping-lite.es6',
            'scripts/mapping.config.es6',
        ),
        'output_filename': 'scripts/mapping-lite.js',
    },
    'vendor': {
        'source_filenames': (
            'console-shim/console-shim.min.js',
            'lodash/lodash.min.js',
            'moment/min/moment.min.js',
            'moment-range/dist/moment-range.min.js',
            'angular/angular.min.js',
            'angular-animate/angular-animate.min.js',
            'angular-aria/angular-aria.min.js',
            'angular-cookies/angular-cookies.min.js',
            'angular-bootstrap/ui-bootstrap-tpls.min.js',
            'restangular/dist/restangular.min.js',
            'angular-material/angular-material.min.js',
            'angular-messages/angular-messages.min.js',
            'ui-router/release/angular-ui-router.min.js',
            'angular-ui-mask/dist/mask.min.js',
            'angular-ui-grid-3.0.4/ui-grid.min.js',
            'ocanvas/build/dist/ocanvas-2.8.1.min.js',
            # 'ez-transition-0.0.1/ez-transition.min.js',
            # 'ez-modal-0.0.5/ez-modal.min.js',
            # 'ez-modal-0.0.5/ez-modal-tpl.min.js',
            'ez-dropdown/dist/ez-dropdown.min.js',
            'ez-datetime-0.1.4/ez-datetime.js',
            'ez-datetime-0.1.4/ez-datetime-tpl.js',
        ),
        'output_filename': 'scripts/vendor.js',
    },
}

# PIPELINE_ENABLED = True
PIPELINE_DISABLE_WRAPPER = True
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

PIPELINE_LIVE_SCRIPT_ARGUMENTS = '--no-header '
