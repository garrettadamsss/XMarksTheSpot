let marker;

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
    marker = new google.maps.Marker({
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

  // This changes the text in the search bar to the selection from autocomplete
  function onPlaceChanged(){
      var place = autocomplete.getPlace();

      if(!place.geometry){
          document.getElementById('autocomplete').placeholder = 'Enter a place';
      }
      else {
          document.getElementById('details').innerHTML = place.name;
      }
  }


//   const toggleMarkerDescrip = () => {
//       document.querySelector('.descrip_modal')
//         .classList.toggle('descrip_modal--hidden');
//   };

//   document.querySelector()
  
//get modal element
var modal = document.getElementById('locationModal');
var modalBtn = document.getElementById('modalBtn');
var closeBtn = document.getElementsByClassName('closeBtn')[0];

modalBtn.addEventListener('click',openModal);
closeBtn.addEventListener('click',closeModal);
window.addEventListener('click',clickOutside);
//open modal
function openModal(){
    modal.style.display = 'block';
}

//close modal

function closeModal(){
    modal.style.display = 'none';
}

function clickOutside(e){
    if(e.target == modal){
        modal.style.display = 'none';
    }
}