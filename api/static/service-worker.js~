const CACHE_NAME = 'pwa-flask-cache-v1';
const urlsToCache = [
  '/',
  '/static/manifest.json',
  '/static/images/icon-192x192.png',
  '/static/images/icon-512x512.png'
];

// Instalação do Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Interceptar requisições
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});

