const version = "0.1.18";
const cacheName = `festivalg-${version}`;
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(cacheName).then(cache => {
      return cache.addAll([
        `/`,
        `/static/img/192logo.png`,
        `/static/img/512logo.png`,
        `/static/img/boyband.jpg`,
        `/static/img/Distortion.png`,
        `/static/img/dude.jpg`,
        `/static/img/favicon.ico`,
        `/static/img/grnt_tr_logo1000.png`,
        `/static/img/groen.png`,
        `/static/img/marley.jpg`,
        `/static/img/marsboiis.jpg`,
        `/static/img/mekdes.jpg`,
        `/static/img/northside.png`,
        `/static/img/rapman.jpg`,
        `/static/img/roskilde.png`,
        `/static/img/saveus.jpg`,
        `/static/img/skive.png`,
        `/static/img/smukfest.png`,
        `/static/img/soleima.jpg`,
        `/static/img/spot.png`,
        `/static/img/tinderbox.png`,
        `/static/fonts/Miss Rhinetta.ttf`,
        `/static/fonts/Miss Rhinetta.otf`,
        `/static/css/main.css`,
        `/static/css/normalize.css`,
        `/static/css/skeleton.css`,
        `/static/js/autocomplete.js`
      ])
          .then(() => self.skipWaiting());
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(cacheName)
      .then(cache => cache.match(event.request, {ignoreSearch: true}))
      .then(response => {
      return response || fetch(event.request);
    })
  );
});