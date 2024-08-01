document.addEventListener('DOMContentLoaded', function () {
    let currentPage = 1;
    const restaurantsPerPage = 10;

    function fetchRestaurants(page) {
        fetch(`http://localhost:5000/api/restaurants?page=${page}&limit=${restaurantsPerPage}`)
            .then(response => response.json())
            .then(data => {
                displayRestaurants(data.restaurants);
                updatePaginationControls(data.totalPages);
            })
            .catch(error => console.error('Error fetching restaurant data:', error));
    }

    function displayRestaurants(restaurants) {
        const restaurantList = document.getElementById('restaurant-list');
        restaurantList.innerHTML = '';

        restaurants.forEach(restaurant => {
            const card = document.createElement('div');
            card.className = 'restaurant-card';
            card.innerHTML = `
                <h2>${restaurant.restaurant_name}</h2>
                <p>${restaurant.city}</p>
                <p>${restaurant.cuisines}</p>
                <a href="restaurant.html?id=${restaurant.restaurant_id}">View Details</a>
            `;
            restaurantList.appendChild(card);
        });
    }

    function updatePaginationControls(totalPages) {
        document.getElementById('current-page').textContent = currentPage;
        document.getElementById('prev-page').disabled = currentPage === 1;
        document.getElementById('next-page').disabled = currentPage === totalPages;
    }

    document.getElementById('prev-page').addEventListener('click', function () {
        if (currentPage > 1) {
            currentPage--;
            fetchRestaurants(currentPage);
        }
    });

    document.getElementById('next-page').addEventListener('click', function () {
        currentPage++;
        fetchRestaurants(currentPage);
    });

    fetchRestaurants(currentPage);
});
