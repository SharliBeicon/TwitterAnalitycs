def cargarweb(jsonLocalizacion):
	return '''
            <html>
            <head>
			<title>Twitter Analylics</title>
	        <link rel="stylesheet" href="estilo.css" type="text/css"/>
              <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css" />
              <script src="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js"></script>
              <script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
              <!-- this goes in the <head> -->
              <style>
              #map {
                height: 600px;
              }
              </style>
            </head>
            <body>
			<img id = "titulo" src="titulo.png"  style="position:relative; left: 23%; width: 50%; height: 50%;" >
              <!-- this goes in the <body> -->
              <div id="map"></div>
              <script>
                // Load the tile images from OpenStreetMap
              var mytiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              });
              // Initialise an empty map
              var map = L.map('map');
              // Read the GeoJSON data with jQuery, and create a circleMarker element for each tweet
              // Each tweet will be represented by a nice red dot
              $.getJSON("'''+jsonLocalizacion+'''", function(data) {
                  var myStyle = {
                      radius: 2,
                      fillColor: "red",
                      color: "red",
                      weight: 1,
                      opacity: 1,
                      fillOpacity: 1
                  };

                  var geojson = L.geoJson(data, {
                      pointToLayer: function (feature, latlng) {
                          return L.circleMarker(latlng, myStyle);
                      }
                  });
                  geojson.addTo(map)
              });
              // Add the tiles to the map, and initialise the view in the middle of Europe
              map.addLayer(mytiles).setView([50.5, 5.0], 5);
              </script>
            </body>
            </html>
        '''
