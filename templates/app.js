function initMap(){

    // Map Center
    var options = {
      zoom:12,
      center:{lat:33.7743,lng:-117.9380}
    }

    var map = new google.maps.Map(document.getElementById('map'),options);

    // Marker
    const marker = new google.maps.Marker({
        position: {lat:33.7743,lng:-117.9380},
        map: map
        // icon : "img"
    });

    // Info Window
    const detail = new google.maps.InfoWindow({
        content: '<h2>Yooooohoo</h2>'
    });

    marker.addListener("mouseover", () =>{
        detail.open(map, marker);
    })
  }


  
  function initAutocomplete(){

    const aOptions = {
        bounds: defaultBounds,
        componentRestrictions: { country: "us" },
        fields: ["address_components", "geometry", "icon", "name"],
        types: ["geocodet"],
      };

      const autocomplete = new google.maps.places.Autocomplete(document.getElementById('autocomplete'),aOptions);
  }