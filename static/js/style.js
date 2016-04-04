prev_pic = function() {
    var pic = document.getElementById("display_photo");
    var pic_name = pic.src;
    var temp = pic_name.split('/');
    var name = temp[temp.length - 1].split('.')[0];

    var num = Number(name) - 1
    if (num == 1) {
        document.getElementById("prev_button").style = "visibility: hidden;";
    }
    else{
        document.getElementById("next_button").style = "visibility: visible;";
    }

    pic.src = "/static/images/" + num + ".jpg";

}

next_pic = function(){
    var pic = document.getElementById("display_photo");
    var pic_name = pic.src;
    var temp = pic_name.split('/');
    var name = temp[temp.length - 1].split('.')[0];

    var num = Number(name) + 1
    if (num == 9) {
        document.getElementById("next_button").style = "visibility: hidden;";
    }
    else{
        document.getElementById("prev_button").style = "visibility: visible;";
    }
    pic.src = "/static/images/" + num + ".jpg";

}

function initMap() {
    var mapDiv = document.getElementById('map');
    var map = new google.maps.Map(mapDiv, {
      center: {lat: 44.540, lng: -78.546},
      zoom: 8
    });
}

//if asdf = 1, then hide button//