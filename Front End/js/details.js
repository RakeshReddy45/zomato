document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const restaurantId = urlParams.get('id');

    // Fetch and display restaurant details (Replace the URL with your API endpoint)
    fetch(`http://localhost:5000/api/restaurants/${restaurantId}`)
        .then(response => response.json())
        .then(restaurant => {
            const restaurantDetails = document.getElementById('restaurant-details');
            restaurantDetails.innerHTML = `
                <h2>${restaurant.restaurant_name}</h2>
                <p><strong>Address:</strong> ${restaurant.address}</p>
                <p><strong>City:</strong> ${restaurant.city}</p>
                <p><strong>Cuisines:</strong> ${restaurant.cuisines}</p>
                <p><strong>Average Cost for Two:</strong> ${restaurant.average_cost_for_two} ${restaurant.currency}</p>
                <p><strong>Rating:</strong> ${restaurant.aggregate_rating} (${restaurant.rating_text})</p>
            `;
        });
});
