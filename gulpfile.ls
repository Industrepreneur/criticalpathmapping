'use strict'

exec             = require 'child_process' .exec
gulp             = require 'gulp'
cache            = require 'gulp-cached'
browser-sync     = require 'browser-sync' .create!
sourcemaps       = require 'gulp-sourcemaps'
sass             = require 'gulp-sass'
#gulp-livescript = require 'gulp-livescript'
#exec            = require 'gulp-exec'
# plumber        = require 'gulp-plumber'
# notifier       = require 'node-notifier'


/**
 * Clear the console
 **/
gulp.task 'clear_screen', ->
    exec 'clear', (err, stdout, stderr) -> console.log(stdout)


/**
 * Lint python project files
 */
gulp.task 'lint_python', ->
    exec 'flake8 --max-complexity 10 mapping',  (err, stdout, stderr) ->
        console.log stdout
        /*if (stdout.length > 10) {
        notifier.notify
          'title': 'Linting Errors',
          'message': 'some message for me'
        }*/
        /*exec 'arc lint --everything --ansi',  (err, stdout, stderr) ->
           # if (stdout.length > 10) {
          notifier.notify
            'title': 'Linting Errors',
            'message': 'some message for me'
          # }
          console.log stdout*/


/**
 * Run Unit Tests
 * @requires pytest and django-pytest
 */
gulp.task 'pytest', ->
    exec 'envdir envs/test py.test --color=yes --tb=short -r w mapping/', (err, stdout, stderr) ->
        console.log stdout
        console.log stderr


/**
 * Compile Application SASS code
 * @requires gulp-sass
 */
gulp.task 'sass', ->
    return gulp.src 'mapping/frontend/static/styles/**/*.scss'
    .pipe cache 'styles'
    .pipe sourcemaps.init!
        .pipe sass!on 'error', sass.logError
    .pipe sourcemaps.write!
    # .pipe gulp.dest 'mapping/frontend/static/styles'
    .pipe gulp.dest 'static_final/styles'
    .pipe browser-sync.stream!

#gulp.task 'sass:watch', ->
#    gulp.watch 'mapping/frontend/static/**/*.scss', ['sass']


/**
 * Compile Application SASS code
 * @requires livescript, gulp-livescript
 */
#gulp.task 'livescript', ->
#    return gulp.src 'mapping/frontend/static/scripts/**/*.ls'
#    .pipe cache 'livescript'
#    .pipe gulp-livescript bare: true, map: 'embedded' .on 'error' -> console.log 'LS ERRROR!'
#    #/*.pipe exec 'lsc -bc --map embedded "<%= file.path %>"'*/
#    .pipe gulp.dest 'mapping/frontend/static/scripts'
#    .pipe browser-sync.stream!


/**
 * Generate model graph
 * @requires django-extensions and graphviz
 */
gulp.task 'graph_models', ->
    exec 'python3 manage.py graph_models | dot -odocs/models.png -Tpng', (err, stdout, stderr) ->


gulp.task 'watch', ->
    browser-sync.init do
        proxy: 'dev.mapping.mymanufacturing.org'
        open: false


    #gulp.watch ['**/models/*.py', '**/models.py'], ['graph_models']
    #gulp.watch ['**/*.py'], <[clear_screen lint_python]>

    #gulp.watch 'mapping/frontend/static/scripts/**/*.ls', ['livescript']
    gulp.watch 'mapping/frontend/static/styles/**/*.scss', ['sass']

    #gulp.watch 'mapping/frontend/static/**/*.html' .on 'change', browser-sync.reload
    gulp.watch [
        'mapping/frontend/static/**/*.html'
        'mapping/frontend/static/**/*.ls'
    ], browser-sync.reload


gulp.task 'default', <[sass watch]>
