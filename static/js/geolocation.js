window.onload = function get_location() {
  navigator.geolocation.getCurrentPosition(show_map);
}

function show_map(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  // let's show a map or do something interesting!
}