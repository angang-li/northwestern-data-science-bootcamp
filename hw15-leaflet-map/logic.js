// Function to determine marker size based on earthquake magnitude
function markerSize(feature) {
  return Math.sqrt(Math.abs(feature.properties.mag)) * 5;
}

// Function to determine marker color based on earthquake magnitude
var colors = ["#c6ffdd", "#dfedbe", "#eede9f", "#ecc089", "#eda287", "#f7797d"]
function fillColor(feature) {
  var mag = feature.properties.mag;
  if (mag <= 1) {
    return colors[0]
  }
  else if (mag <= 2) {
    return colors[1]
  }
  else if (mag <= 3) {
    return colors[2]
  }
  else if (mag <= 4) {
    return colors[3]
  }
  else if (mag <= 5) {
    return colors[4]
  }
  else {
    return colors[5]
  }
}

// Define variables for base layers
var attribution = "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>";

var satelliteMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: attribution,
  maxZoom: 18,
  id: "mapbox.satellite",
  accessToken: API_KEY
});

var lightMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: attribution,
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

var outdoorsMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: attribution,
  maxZoom: 18,
  id: "mapbox.outdoors",
  accessToken: API_KEY
});

// Create a baseMaps object
var baseMaps = {
  "Satellite": satelliteMap,
  "Grayscale": lightMap,
  "Outdoors": outdoorsMap
};

// Store API endpoint as queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

var platesPath = "GeoJSON/PB2002_boundaries.json";

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  d3.json(platesPath, function(platesData) {

    // console.log(data.features);
    console.log(platesData);

    // Earthquake layer
    var earthquakes = L.geoJSON(data, {

      // Create circle markers
      pointToLayer: function (feature, latlng) {
        var geojsonMarkerOptions = {
          radius: 8,
          fillColor: "#ff7800",
          radius: markerSize(feature),
          fillColor: fillColor(feature),
          color: "#000",
          weight: 1,
          opacity: 1,
          fillOpacity: 1
        };
        return L.circleMarker(latlng, geojsonMarkerOptions);
      },

      // Create popups
      onEachFeature: function (feature, layer) {
        return layer.bindPopup(`<strong>Place:</strong> ${feature.properties.place}<br><strong>Magnitude:</strong> ${feature.properties.mag}`);
      }
    });

    // Tectonic plates layer
    var platesStyle = {
      "color": "#ff7800",
      "weight": 2,
      "opacity": 1,
      fillOpacity: 0,
    };
    var plates = L.geoJSON(platesData, {
      style: platesStyle
    });

    // Create an overlay object
    var overlayMaps = {
      "Fault lines": plates,
      "Earthquakes": earthquakes,
    };

    // Define a map object
    var map = L.map("map", {
      center: [37.09, -95.71],
      zoom: 3,
      layers: [satelliteMap, plates, earthquakes]
    });

    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(map);

    // Setting up the legend
    var legend = L.control({ position: "bottomright" });
    legend.onAdd = function() {
      var div = L.DomUtil.create("div", "info legend");
      var limits = ["0-1", "1-2", "2-3", "3-4", "4-5", "5+"];
      var labelsColor = [];
      var labelsText = [];

      // Add min & max
      limits.forEach(function(limit, index) {
        labelsColor.push(`<li style="background-color: ${colors[index]};"></li>`); // <span class="legend-label">${limits[index]}</span>
        labelsText.push(`<span class="legend-label">${limits[index]}</span>`)
      });

      var labelsColorHtml =  "<ul>" + labelsColor.join("") + "</ul>";
      var labelsTextHtml = `<div id="labels-text">${labelsText.join("<br>")}</div>`;

      var legendInfo = "<h4>Earthquake<br>Magnitude</h4>" +
        "<div class=\"labels\">" + labelsColorHtml + labelsTextHtml
        "</div>";
      div.innerHTML = legendInfo;

      return div;
    };

    // Adding legend to the map
    legend.addTo(map);

  })
})