//CONSUMO API
document.addEventListener('DOMContentLoaded', function() {
    fetchCharacters();
});

function fetchCharacters() {
    fetch('https://rickandmortyapi.com/api/character')
        .then(response => response.json())
        .then(data => {
            const characters = data.results.slice(0, 6); // Obtén los primeros 6 personajes
            const cards = document.querySelectorAll('.card.custom-size');

            characters.forEach((character, index) => {
                if (cards[index]) {
                    const img = cards[index].querySelector('img');
                    const title = cards[index].querySelector('.card-title');
                    const text = cards[index].querySelector('.card-text');

                    img.src = character.image;
                    img.alt = character.name;
                    title.textContent = character.name;
                    text.textContent = `Status: ${character.status}`;
                }
            });
        })
        .catch(error => console.error('Error fetching characters:', error));
}













// Animación de carga de página
function pageLoader() {
    const loader = document.getElementById('loader');
    const content = document.getElementById('content');
    setTimeout(function() {
        loader.style.opacity = '0';
        setTimeout(function() {
            loader.style.display = 'none';
            content.style.display = 'block';
            content.style.opacity = '0';
            setTimeout(function() {
                content.style.transition = 'opacity 1s';
                content.style.opacity = '1';
            }, 10);
        }, 500);
    }, 2000);
}

// Animaciones de desplazamiento (Scroll Animations)
function scrollAnimations() {
    const fadeIns = document.querySelectorAll('.fade-in');

    function checkVisibility() {
        const windowHeight = window.innerHeight;
        fadeIns.forEach(fadeIn => {
            const rect = fadeIn.getBoundingClientRect();
            if (rect.top < windowHeight - 100) {
                fadeIn.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', checkVisibility);
    window.addEventListener('load', checkVisibility);
}

// Animaciones de hover para botones
function buttonHoverAnimations() {
    const buttons = document.querySelectorAll('.button');

    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.backgroundColor = '#2980b9';
            button.style.transform = 'scale(1.1)';
        });

        button.addEventListener('mouseleave', () => {
            button.style.backgroundColor = '#3498db';
            button.style.transform = 'scale(1)';
        });
    });
}

// Animaciones de despliegue de menús
function menuAnimations() {
    const menus = document.querySelectorAll('.menu');

    menus.forEach(menu => {
        const menuContent = menu.querySelector('.menu-content');

        menu.addEventListener('mouseenter', () => {
            menuContent.style.display = 'block';
            setTimeout(() => {
                menuContent.style.opacity = '1';
                menuContent.style.transform = 'translateY(0)';
            }, 10);
        });

        menu.addEventListener('mouseleave', () => {
            menuContent.style.opacity = '0';
            menuContent.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                menuContent.style.display = 'none';
            }, 500);
        });
    });
}

// Animación de añadir al carrito
function addToCartAnimation(button) {
    const product = button.parentElement;
    const flyElement = document.createElement('div');
    flyElement.classList.add('fly-to-cart');
    product.appendChild(flyElement);
    setTimeout(() => {
        flyElement.remove();
    }, 1000);
}

// Inicializar todas las animaciones
function initAnimations() {
    if (document.getElementById('loader')) {
        pageLoader();
    }
    scrollAnimations();
    buttonHoverAnimations();
    menuAnimations();
}

// Inicializar animaciones al cargar la página
window.addEventListener('load', initAnimations);
