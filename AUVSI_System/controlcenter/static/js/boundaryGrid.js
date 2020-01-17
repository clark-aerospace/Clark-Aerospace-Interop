function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: {lat: 38.1462694444444, lng: -76.4281638888889},
      mapTypeId: 'terrain'
    });

    var boundaryCoordinates = [
      {lat: 38.1462694444444, lng: -76.4281638888889},
      {lat: 38.151625, lng: -76.4286833333333},
      {lat: 38.1518888888889, lng: -76.4314666666667},
      {lat: 38.1505944444444, lng: -76.4353611111111},

      {lat: 38.1475666666667, lng: -76.4323416666667},
      {lat: 38.1446666666667, lng: -76.4329472222222},
      {lat: 38.1432555555556, lng: -76.4347666666667},
      {lat: 38.1404638888889, lng: -76.4326361111111},

      {lat: 38.1407194444444, lng: -76.4260138888889},
      {lat: 38.1437611111111, lng: -76.4212055555556},
      {lat: 38.1473472222222, lng: -76.4232111111111},
      {lat: 38.1461305555556, lng: -76.4266527777778},
    ];
    var flightPath = new google.maps.Polyline({
      path: boundaryCoordinates,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });

    flightPath.setMap(map);
  }