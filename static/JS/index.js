// Copy Ban
document.addEventListener("copy", (event) =>{
    const selectedData= window.getSelection().toString();
    event.clipboardData.setData(
        "text/plain",
        "🚫"
    );
    event.preventDefault();
});

                    // Portfolio Section
// card More Button images
const cardRow = document.getElementById('card-row');
const loadMoreBtn = document.getElementById('load-more');

// List of additional images to load
const additionalCards = [
    { front: '/static/images/02.jpg', back: '/static/images/03.jpg' },
    { front: '/static/images/04.jpg', back: '/static/images/05.jpg' },
    { front: '/static/images/08.jpg', back: '/static/images/15.jpg' },
    { front: '/static/images/27.jpg', back: '/static/images/29.jpg' },
    { front: '/static/images/08.jpg', back: '/static/images/15.jpg' },
    { front: '/static/images/27.jpg', back: '/static/images/29.jpg' },
];
loadMoreBtn.addEventListener('click', () => {

    additionalCards.forEach(card => {
        const col = document.createElement('div');
        col.className = 'col-6 col-sm-6 col-md-4 col-lg-2';
        col.innerHTML = `
            <div class="card-container">
                <div class="gallery-card" data-rotation="0">
                    <div class="card-face front" style="background-image: url('${card.front}');" loading="lazy"></div>
                    <div class="card-face back" style="background-image: url('${card.back}');" loading="lazy"></div>
                </div>
            </div>`;
        cardRow.appendChild(col);
    });
    loadMoreBtn.style.display = 'none';

});

// card hover effect
    // Select all cards
    const cards = document.querySelectorAll('.gallery-card');

    cards.forEach(card => {
        // Initialize a variable to track the current state
        let showingBack = false;
        let isFlipping    = false;

        // Add hover event listeners
        card.addEventListener('mouseenter', () => {
            if (isFlipping) return; // Prevent another flip if the card is already flipping
            isFlipping = true;

           if (!card.classList.contains('flipped')) {
                card.style.transform = 'rotateY(180deg)';
                card.classList.add('flipped');
            } else {
                card.style.transform = 'rotateY(0deg)';
                card.classList.remove('flipped');
            }
        });
        card.addEventListener('transitionend', () => {
            isFlipping = false; // Allow new flips after the animation is complete
        });
    });

    // Lazy Loading images increase performance
const cardFaces = document.querySelectorAll('.card-face');

const observerOptions = {
    rootMargin: '0px 0px 100px 0px', // Load image when it comes near the viewport
    threshold: 0.1 // Load when at least 10% of the image is visible
};

const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const cardFace = entry.target;
            const imageUrl = cardFace.getAttribute('static/images');
            // cardFace.style.backgroundImage = url(${'static/images'}); // Set the background image

            // Add a class to make the image visible
            cardFace.classList.add('visible');

            observer.unobserve(cardFace);  // Stop observing after image is loaded
        }
    });
}, observerOptions);

// Start observing each image
cardFaces.forEach(face => imageObserver.observe(face));

    // Booking-Popup Form
        // Get references to DOM elements 
const popup = document.getElementById("popup");
const openBookingForm = document.getElementById("openBookingForm");
const closePopup = document.getElementById("closePopup");
const body = document.body;

        // Open popup
openBookingForm.addEventListener("click", (event) => {
    event.preventDefault(); // Prevent the default link behavior
        popup.style.display = "flex";
        body.classList.add("popup-active");
});

        // Close popup
closePopup.addEventListener("click", () => {
    popup.style.display = "none";
    body.classList.remove("popup-active");
});

        // Close popup when clicking outside the form
window.addEventListener("click", (event) => {
    if (event.target === popup) {
        popup.style.display = "none";
        body.classList.remove("popup-active");
    }
});

    //Rent Booking Form
    // Get references to DOM elements
    const rent_popup = document.getElementById("rent-popup");
    const rent_BookingForm = document.getElementById("RentBookingForm");
    const rent_close_Popup = document.getElementById("rent-close-Popup");
    const rent_body = document.body;
    
            // Open popup
    rent_BookingForm.addEventListener("click", (event) => {
        event.preventDefault(); // Prevent the default link behavior
            rent_popup.style.display = "flex";
            rent_body.classList.add("popup-active");
    });
    
            // Close popup
    rent_close_Popup.addEventListener("click", () => {
        rent_popup.style.display = "none";
        rent_body.classList.remove("popup-active");
    });
    
            // Close popup when clicking outside the form
    window.addEventListener("click", (event) => {
        if (event.target === rent_popup) {
            rent_popup.style.display = "none";
            rent_body.classList.remove("rent_popup-active");
        }
    });

//Message form validation
$(document).ready(function(){
    $('#bookingForm').on('submit', function(event){
        event.preventDefault();  // Prevent the default form submission
        $.ajax({
            url: '{% url "booking" %}',  // URL to which the form will be submitted
            type: 'POST',
            data: $(this).serialize(),  // Serialize the form data
            success: function(response){
                // If the form is valid and submission is successful
                $('#bookingModal').modal('hide');  // Hide the modal
                alert('Booking Successful!');  // Display success message (you can customize this)
            },
            error: function(response){
                // If there are any errors during submission
                alert('There was an error with the booking!');
            }
        });
    });
});