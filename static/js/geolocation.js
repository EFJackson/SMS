window.onload = function get_location() {
	navigator.geolocation.getCurrentPosition(show_map);
}

function show_map(position) {
	var latitude = position.coords.latitude;
	var longitude = position.coords.longitude;
	center: new google.maps.LatLng(latitude, longitude),
	zoom: 8,
    mapTypeId: google.maps.MapTypeId.ROADMAP
}