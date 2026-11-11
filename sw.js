// Service worker "pembersih": menggantikan versi lama, menghapus cache, lalu melepas diri
// supaya HP yang pernah membuka link lama ikut pindah ke https://vanisyanrklh.github.io/belajar-volume-kubus-balok/
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      const kunci = await caches.keys();
      await Promise.all(kunci.map((k) => caches.delete(k)));
      await self.registration.unregister();
      const klien = await self.clients.matchAll({ type: 'window' });
      klien.forEach((c) => c.navigate('https://vanisyanrklh.github.io/belajar-volume-kubus-balok/'));
    })(),
  );
});
