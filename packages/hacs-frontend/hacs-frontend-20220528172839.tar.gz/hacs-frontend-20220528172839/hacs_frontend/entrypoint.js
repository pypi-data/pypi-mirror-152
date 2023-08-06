
try {
  new Function("import('/hacsfiles/frontend/main-f003dcaa.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-f003dcaa.js';
  el.type = 'module';
  document.body.appendChild(el);
}
  