function autoplayCarousel() {
  const carouselEl = document.getElementById("carousel");
  const slideContainerEl = carouselEl.querySelector("#slide-container");
  const slideEl = carouselEl.querySelector(".slide");
  let slideWidth = slideEl.offsetWidth;
  let autoplay; // Variable para guardar el intervalo de autoplay

  // Función para iniciar el autoplay
  function startAutoplay() {
    autoplay = setInterval(() => navigate("forward"), 3000);
  }

  // Función para detener el autoplay
  function stopAutoplay() {
    clearInterval(autoplay);
  }

  // Iniciar autoplay al cargar la página
  startAutoplay();

  // Add click handlers
  document
    .querySelector("#back-button")
    .addEventListener("click", () => navigate("backward"));
  document
    .querySelector("#forward-button")
    .addEventListener("click", () => navigate("forward"));
  document.querySelectorAll(".slide-indicator").forEach((dot, index) => {
    dot.addEventListener("click", () => navigate(index));
    dot.addEventListener("mouseenter", stopAutoplay);
  });

  // Add keyboard handlers
  document.addEventListener("keydown", (e) => {
    if (e.code === "ArrowLeft") {
      stopAutoplay();
      navigate("backward");
    } else if (e.code === "ArrowRight") {
      stopAutoplay();
      navigate("forward");
    }
  });

  // Add resize handler
  window.addEventListener("resize", () => {
    slideWidth = slideEl.offsetWidth;
  });

  // Stop autoplay when mouse enters the slide container
  slideContainerEl.addEventListener("mouseenter", stopAutoplay);

  // Reanudar autoplay cuando el mouse sale del contenedor
  slideContainerEl.addEventListener("mouseleave", startAutoplay);

  // Slide transition
  const getNewScrollPosition = (arg) => {
    const gap = 10;
    const maxScrollLeft = slideContainerEl.scrollWidth - slideWidth;
    
    // Si es hacia adelante
    if (arg === "forward") {
      const x = slideContainerEl.scrollLeft + slideWidth + gap;
      // Si llegamos al final, volvemos al inicio
      return x <= maxScrollLeft ? x : 0;
    }
    // Si es hacia atrás
    else if (arg === "backward") {
      const x = slideContainerEl.scrollLeft - slideWidth - gap;
      // Si llegamos al inicio, volvemos al final
      return x >= 0 ? x : maxScrollLeft;
    }
    // Si el argumento es un número (índice de slide)
    else if (typeof arg === "number") {
      const x = arg * (slideWidth + gap);
      // Asegurarse de que no se salga de los límites
      return x <= maxScrollLeft ? x : 0;
    }
  };

  const navigate = (arg) => {
    slideContainerEl.scrollLeft = getNewScrollPosition(arg);
  };

  // Slide indicators
  const slideObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const slideIndex = entry.target.dataset.slideindex;
          carouselEl
            .querySelector(".slide-indicator.active")
            .classList.remove("active");
          carouselEl
            .querySelectorAll(".slide-indicator")
            [slideIndex].classList.add("active");
        }
      });
    },
    { root: slideContainerEl, threshold: 0.1 }
  );

  document.querySelectorAll(".slide").forEach((slide) => {
    slideObserver.observe(slide);
  });
}

autoplayCarousel();
