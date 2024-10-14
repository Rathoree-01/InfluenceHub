// script.js
const viewDetailsButtons = document.querySelectorAll('.view-details');
const template2 = document.getElementById('template2');
const closeButton = document.querySelector('.close-details');

viewDetailsButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Get the text content of the campaign title
        const campaignTitle = button.parentNode.querySelector('.campaign-title').textContent;
        // Populate template2 with the ad details (example)
        template2.querySelector('.ad-title').textContent = campaignTitle + " Ad"; 
        // ... (Populate other details based on your data source)
        // Show template2
        template2.classList.remove('hidden'); 
    });
});

closeButton.addEventListener('click', () => {
    template2.classList.add('hidden'); 
});