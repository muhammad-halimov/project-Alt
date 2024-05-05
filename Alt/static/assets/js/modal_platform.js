
var modal = document.getElementById("modal_add_platform");
var images = document.getElementsByClassName("myImg");
var platformName = document.querySelector(".platform_name");
var span = document.getElementsByClassName("close")[0];


for (var i = 0; i < images.length; i++) {
    images[i].onclick = function() {
        modal.style.display = "block";
        var altText = this.alt; 
        platformName.textContent = altText; 
    }
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
