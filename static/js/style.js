prev_pic = function() {
    var pic = document.getElementById("display_photo");
    var pic_name = pic.src;
    var temp = pic_name.split('/');
    var name = temp[temp.length - 1].split('.')[0];

    // asdf = int(name) - 1

    pic.src = "/static/" + asdf + ".jpg";

}

//if asdf = 1, then hide button//