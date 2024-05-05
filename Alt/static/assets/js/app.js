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

	if (prevButton && nextButton) {
		 prevButton.addEventListener('click', handlePrevClick);
		 nextButton.addEventListener('click', handleNextClick);
	}

	showBlock(currentIndex);
}

function textAnimation(){
	const animatedElements = document.querySelectorAll('.anim');

    // Функция для добавления класса 'show' с задержкой
    function animateElements(elements, index) {
        if (index < elements.length) {
            elements[index].classList.add('show_anim_txt');
            setTimeout(function() {
                animateElements(elements, index + 1);
            }, 200); 
        }
    }

    setTimeout(function() {
        animateElements(animatedElements, 0);
    }, 500); 
}


function init() {
	handleNavigation();
}

document.addEventListener("DOMContentLoaded", function() {
	textAnimation();
 });

 init();