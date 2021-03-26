function initMap(){

    // Map Center
    var options = {
      zoom:12,
      center:{lat:33.7743,lng:-117.9380}
    }

    var map = new google.maps.Map(document.getElementById('map'),options);

    // Search Autocomplete
    
    const autocomplete = new google.maps.places.Autocomplete(document.getElementById('search_bar'));
    autocomplete.addListener('place_changed', onPlaceChanged);


    // idk if we need this -> optional argument in autocomplete object 

    // const aOptions = {
    //     bounds: defaultBounds,
    //     componentRestrictions: { country: "us" },
    //     fields: ["place_id", "geometry", "name"],
    //     types: ["geocode"],
    //   };



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

  // erm not sure what this does
  function onPlaceChanged(){
      var place = autocomplete.getPlace();

      if(!place.geometry){
          document.getElementById('autocomplete').placeholder = 'Enter a place';
      }
      else {
          document.getElementById('details').innerHTML = place.name;
      }
  }

  
  
