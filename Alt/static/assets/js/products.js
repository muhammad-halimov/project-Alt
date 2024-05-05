
function handleNavigation() {
 const blocks = document.querySelectorAll('.block');
 const navLinks = document.querySelectorAll('.profile_nav a');
 const prevButton = document.getElementById('prevCartButton');
 const nextButton = document.getElementById('nextCartButton');
  
 let currentIndex = 0;
  
 function showBlock(index) {
   blocks.forEach((block) => {
   block.classList.remove("active_block");
   });
   blocks[index].classList.add("active_block");
  
   // calculateTotalSum();
 }
  
 function handleNavClick(e) {
   e.preventDefault();
   const index = Array.from(navLinks).indexOf(e.target);
   currentIndex = index;
   showBlock(currentIndex);
  
   navLinks.forEach((link) => {
   link.classList.remove('active_nav_link');
   });
   e.target.classList.add('active_nav_link');
 }
  
 function handlePrevClick() {
   currentIndex--;
   if (currentIndex < 0) {
   currentIndex = blocks.length - 1;
   }
   showBlock(currentIndex);
  
   navLinks.forEach((link, index) => {
   if (index === currentIndex) {
   link.classList.add('active_nav_link');
   } else {
   link.classList.remove('active_nav_link');
   }
   });
 }
  
 function handleNextClick() {
   currentIndex++;
   if (currentIndex >= blocks.length) {
   currentIndex = 0;
   }
   showBlock(currentIndex);
  
   navLinks.forEach((link, index) => {
   if (index === currentIndex) {
   link.classList.add('active_nav_link');
   } else {
   link.classList.remove('active_nav_link');
   }
   });
 }
  
 navLinks.forEach((link) => {
   link.addEventListener('click', handleNavClick);
 });
  
 prevButton.addEventListener('click', handlePrevClick);
 nextButton.addEventListener('click', handleNextClick);
  
 showBlock(currentIndex);
  }
  
  function productsAnimation() {
 const products = document.querySelector(".products");
 let productsWidth = products.offsetWidth;
 let amountToScroll = productsWidth - window.innerWidth * 0.67;
 gsap.registerPlugin(ScrollTrigger);
  
 gsap.to(products, {
   x: -amountToScroll,
   ease: "none",
   scrollTrigger: {
   trigger: ".products_block",
   start: "top 30%",
   end: "+=" + amountToScroll,
   pin: true,
   scrub: true,
   },
 });
  }
  
  function rafLoop() {
 function loop(time) {
   lenis.raf(time);
   requestAnimationFrame(loop);
 }
 requestAnimationFrame(loop);
  }
  
  function init() {
 rafLoop();
 productsAnimation();
 handleNavigation();
  }
  
  function pageTransition() {
 const tl = gsap.timeline();
  
 tl.to(".transition", {
   duration: 0.5,
   scaleY: 1,
   transformOrigin: "bottom",
   ease: "power4.inOut",
 });
  
 tl.to(".transition", {
   duration: 1,
   scaleY: 0,
   transformOrigin: "top",
   ease: "power4.inOut",
   delay: 0.4,
   onComplete: function() {
   productsAnimation();
   }
 });
  }
  
  function contentAnimation() {
	const animElements = document.querySelectorAll('.anim');
	
	// Проверяем, есть ли анимируемые элементы
	if (animElements.length === 0) {
	  return;
	}
  
	// Анимационная линия времени
	const tl = gsap.timeline();
  
	// Добавляем анимации к каждому анимируемому элементу
	animElements.forEach((element, index) => {
	  tl.fromTo(element, {
		 translateY: 30,
		 opacity: 0
	  }, {
		 translateY: 0,
		 opacity: 1,
		 duration: 0.5, // Подстраиваем длительность при необходимости
		 delay: index * 0.1, // Задержка для каждой анимации
		 ease: "power2.out" // Подстраиваем функцию смягчения при необходимости
	  });
	});
  }
  

  
  function btnAnimation() {
 const tl = gsap.timeline();
 tl.to(".bounce", {
   y: 20,
   duration: 0.7,
   ease: "power1.inOut",
   repeat: -1,
   yoyo: true
 });
  }
  
  function delay(n) {
 n = n || 0;
 return new Promise((done) => {
   setTimeout(() => {
   done();
   }, n);
 });
  }
  
  function handleNavigationOnEnter() {
 handleNavigation();
  }
  
  function init() {
 handleNavigation();
 contentAnimation();
 productsAnimation();
  }
  
  document.addEventListener('DOMContentLoaded', function() {
 init();
 });