{
  "name": "sqrtrading",
  "version": "1.0.0",
  "main": "index.js",
  "server": "stockscreener",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "css-compile": "node-sass sqrtrading/static/scss -o sqrtrading/static/css",
    "css-watch": "node-sass sqrtrading/static/scss -o sqrtrading/static/css --watch",
    "browser-sync": "browser-sync start --files \"stockscreener/static/*.css, sqrtrading/static/js/*.js, stockscreener/static/images/*.*, sqrtrading/*.py, stockscreener/*.py, stockscreener/templates/*.html\" --proxy 127.0.0.1:8000 --reload-delay=300 --reload-debounce=500",
    "start": "concurrently --kill-others \"python manage.py runserver\" \"npm run css-watch\" \"npm run browser-sync\" "
  },
  "repository": {
    "type": "git",
    "url": "sqrtrading.github:/alexbid/sqrtrading.git"
  },
  "author": "AB",
  "license": "ISC",
  "devDependencies": {
    "browser-sync": "^2.18.5",
    "concurrently": "^3.1.0",
    "node-sass": "^4.1.1"
  },
  "dependencies": {
    "browser-sync": "^2.18.5",
    "concurrently": "^3.1.0",
    "node-sass": "^4.1.1"
  },
  "server": {
    "baseDir": "stockscreener/",
    "directory": true
  },
  "description": ""
}
