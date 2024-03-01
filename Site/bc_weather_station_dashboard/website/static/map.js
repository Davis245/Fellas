// Initialize map to open a focus around startup weather station
const map = L.map('map').setView([51, -121], 7);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

const markerIcon = L.icon({
    iconUrl: '../static/marker-icon.png',
    shadowUrl: "../static/marker-shadow.png",

    iconSize:    [25, 41],
    iconAnchor:  [12, 41],
    popupAnchor: [1, -34],
    shadowSize:  [41, 41]
});

// Fetch data from Django backend
fetch('/weather_stations_data/')
    .then(response => response.json())
    .then(data => {
        data.forEach(station => {
            var marker = L.marker([station.latitude, station.longitude], {icon: markerIcon})
                .addTo(map)
                .bindPopup(
                    `<b>Station ID: ${station.id}</b><br>` +
                    `<b>Station Name: ${station.name}</b><br>` +
                    `<b>Latitude: ${station.latitude}</b><br>` +
                    `<b>Longitude: ${station.longitude}</b><br>` +
                    `<b>Elevation: ${station.elevation}m</b><br>` +
                    `<b>Install Date: ${station.install_date}</b>`
                );
             // Set HTML elements to show information of weather station with id of 100 on start
            if(station['id'] == 100) {
                document.getElementById('station-name').innerText = station['name'] + " - #" + station['id'];
                document.getElementById('latitude').innerText = 'Latitude: ' + station['latitude'];
                document.getElementById('longitude').innerText = 'Longitude: ' + station['longitude'];
                document.getElementById('elevation').innerText = 'Elevation: ' + station['elevation'] + "m";
                // Show popup of that station on display
                marker.fire('click');
            }
            // Add click event listener to update station information on click
            marker.on('click', function() {
                document.getElementById('station-name').innerText = station.name + " - #" + station.id;
                document.getElementById('latitude').innerText = 'Latitude: ' + station.latitude;
                document.getElementById('longitude').innerText = 'Longitude: ' + station.longitude;
                document.getElementById('elevation').innerText = 'Elevation: ' + station.elevation + "m";
            });
        });
    })
    .catch(error => console.error('Error fetching weather station data:', error));