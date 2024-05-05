document.addEventListener("DOMContentLoaded", function() {
	function parallax(e) {
	  const bg = document.querySelector("body");
	  let w = window.innerWidth / 2;
	  let h = window.innerHeight / 2;
	  let mouseX = e.clientX;
	  let mouseY = e.clientY;
	  let pos = `${50 - (mouseX - w) * 0.08}% ${50 - (mouseY - h) * 0.03}%`;
	  bg.style.backgroundPosition = pos;
	}
 
	function shapeParallax(a) {
	  const shapes = document.querySelectorAll(".shape_img");
	  shapes.forEach(shape => {
		 const speed = shape.getAttribute("data-speed");
		 let w = (window.innerWidth - a.pageX * speed) / 150;
		 let h = (window.innerHeight - a.pageY * speed) / 150;
		 shape.style.transform = `translateX(${w}px) translateY(${h}px)`;
	  });
	}
 
	document.addEventListener("mousemove", parallax);
	document.addEventListener("mousemove", shapeParallax);
 });
 