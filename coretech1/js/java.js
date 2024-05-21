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

function aumentarCard(cardId) {
    const card = document.getElementById(cardId);
    card.style.transform = "scale(1.1)";
    card.style.transition = "transform 0.3s ease-in-out";
    card.style.boxShadow = "10px 10px 30px rgba(0, 0, 0, 0.3)";
}

function reducirCard(cardId) {
    const card = document.getElementById(cardId);
    card.style.transform = "scale(1)";
    card.style.boxShadow = "none";
}

document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseover', function() {
            card.style.transform = "scale(1.1)";
            card.style.transition = "transform 0.3s ease-in-out";
            card.style.boxShadow = "10px 10px 30px rgba(0, 0, 0, 0.3)";
        });

        card.addEventListener('mouseout', function() {
            card.style.transform = "scale(1)";
            card.style.boxShadow = "none";
        });
    });
});


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
