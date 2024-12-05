document.addEventListener("scroll", () => {
  const header = document.getElementById("header");

  // Comprueba si el usuario se ha desplazado más de 50px
  if (window.scrollY > 50) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});


  //-----------------SLIDES-------------------------
$(function () {
  $(".rslides").responsiveSlides({
    nav: true, // Activar los botones de navegación
    /* prevText: "❮", */ // Texto para el botón "anterior"
    /* nextText: "❯", */ // Texto para el botón "siguiente"
    pauseControls: false, // No pausar al hacer hover en controles
  });
});

$(function () {
  $(".rslides-services").responsiveSlides({
    nav: true, // Activar los botones de navegación
    /* prevText: "❮", */ // Texto para el botón "anterior"
    /* nextText: "❯", */ // Texto para el botón "siguiente"
    pauseControls: false, // No pausar al hacer hover en controles
  });
});

//--------------MENU-----------------
$("#icon-menu").click(function () {
  $("#ul-menu").toggleClass("abrir_menu");
});

//--------------CLOSE-MENU-----------------
$(".close-a").click(function () {
  $("#ul-menu").toggleClass("abrir_menu");
});


//--------------------MENÚ BLOCK--------
// Manejador para los clics en los enlaces del menú
document.querySelectorAll('.menu-item > a').forEach(menuItem => {
  menuItem.addEventListener('click', function(event) {
      // Verificamos si el elemento tiene un atributo href
      if (this.hasAttribute('href') && this.getAttribute('href').trim() !== '') {
          return; // Si tiene href, salimos y permitimos el comportamiento predeterminado
      }

      event.preventDefault(); // Evitamos el comportamiento predeterminado del enlace
      
      const parent = this.parentElement; // Seleccionamos el elemento padre (menu-item)

      // Cerramos todos los submenús abiertos que no sean el actual
      document.querySelectorAll('.menu-item.active').forEach(activeItem => {
          if (activeItem !== parent) {
              activeItem.classList.remove('active');
          }
      });

      // Alternamos la clase active en el elemento actual
      parent.classList.toggle('active');
  });
});

// Manejador para cerrar submenús al hacer clic fuera del menú
document.addEventListener('click', function(event) {
  // Verificamos si el clic ocurrió dentro de un elemento del menú
  const clickedInsideMenu = event.target.closest('.menu-item');

  if (!clickedInsideMenu) {
      // Si el clic ocurrió fuera del menú, cerramos todos los submenús abiertos
      document.querySelectorAll('.menu-item.active').forEach(activeItem => {
          activeItem.classList.remove('active');
      });
  }
});


/* --------------modal  -----------------*/

// Abrir el modal y desactivar el scroll cuando se presiona el botón con la clase 'contact'
$(".contact").click(function () {
  $("#modal").addClass("show");
  toggleScroll(false); // Desactivar scroll
});

function toggleScroll(enable) {
  if (enable) {
    // Restaurar scroll
    document.body.style.overflow = '';
  } else {
    // Desactivar scroll
    document.body.style.overflow = 'hidden';
  }
}

// Cerrar el modal y restaurar el scroll cuando se presiona el botón con la clase 'close'
$(".close").click(function () {
  $("#modal").removeClass("show");
  toggleScroll(true); // Restaurar scroll
});

// Cerrar el modal al hacer clic fuera del diálogo
window.onclick = function (event) {
  if (event.target == document.getElementById("modal")) {
    $("#modal").removeClass("show");
    toggleScroll(true); // Restaurar scroll
  }
};

// Cerrar el modal al presionar la tecla Esc
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    $("#modal").removeClass("show");
    toggleScroll(true); // Restaurar scroll
  }
});


// Incrementar el contador en la sección Experience
document.addEventListener("DOMContentLoaded", function () {
  const counters = document.querySelectorAll('.counter');

  // Función para hacer el conteo progresivo
  const updateCount = (counter) => {
    const target = +counter.getAttribute('data-target');
    const current = +counter.innerText.replace(/[^0-9]/g, '');
    
    if (current < target) {
      counter.innerText = `[ ${Math.min(current + Math.ceil(target / 100), target)} ]`;
      setTimeout(() => updateCount(counter), 10); // Ajusta la velocidad de incremento
    } else {
      counter.innerText = `[ ${target} ]`; // Asegura que el número llegue al valor final
    }
  };

  // Configura el IntersectionObserver
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { // Si el contador es visible
        updateCount(entry.target); // Inicia el conteo
        observer.unobserve(entry.target); // Deja de observar una vez que se haya iniciado el conteo
      }
    });
  }, {
    threshold: 0.5 // El 50% del elemento debe estar visible para comenzar el conteo
  });

  // Empieza a observar cada elemento con la clase .counter
  counters.forEach(counter => {
    observer.observe(counter);
  });
});


//------------------MENÚ DE SERVICIOS--------------//

// Función para manejar la apertura y cierre de submenús
document.querySelectorAll('.item-service p').forEach(item => {
  item.addEventListener('click', function() {
    // Toggle (abrir/cerrar) el submenú del item seleccionado
    const submenu = this.nextElementSibling;
    if (submenu && submenu.classList.contains('item-subservice')) {
      submenu.classList.toggle('visible');
    }
  });
});
