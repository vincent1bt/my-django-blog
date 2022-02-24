const gulp = require('gulp');
const cleanCSS = require('gulp-clean-css');
const sass = require('gulp-sass')(require('sass'));

const stylesRoute = './css/*.scss';
const stylesDest = './../static/css';

gulp.task('css', () => {
  return gulp.src(stylesRoute)
    .pipe(sass().on('error', sass.logError))
    .pipe(cleanCSS({compatibility: '*'}))
    .pipe(gulp.dest(stylesDest));
});

gulp.task('watch:css', () => {
  gulp.watch(stylesRoute, gulp.series('css'));
});
