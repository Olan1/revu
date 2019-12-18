// Initialize mobile collapse menu
$(".button-collapse").sideNav();

// Search users in search bar
$("#searchBar").keyup(() => {
    search();
    noResultsFound();
});

// Call Delete User Modal
$("#delete-ac").click(() => {
    myModal('#myModal');
});

// Initialize MaterializeCSS form text area input
$('#textarea1').val('New Text');
$('#textarea1').trigger('autoresize');

// Search Bar function
function search() {
    // Get search bar input value
    let input = document.getElementById('searchBar').value;
    // Change input to lowercase
    input = input.toLowerCase();
    // Get all li's with class outerLi (users)
    let x = document.getElementsByClassName('outer');
    let z, i, j;
    // Loop through outerLi's (users)
    for (i = 0; i < x.length; i++) {
        // Set z to false for every iteration
        z = false;
        // Get all li's with class userLi (user data)
        let y = x[i].getElementsByClassName('inner');
        // Loop through userLi's (user data)
        for (j = 0; j < y.length; j++) {
            // If the userLi contains the input value, set z to true
            if (y[j].innerHTML.toLowerCase().includes(input)) {
                z = true;
            }
        }
        // If z is false, outerLi displayed as none
        if (z === false) {
            x[i].style.display = "none";
        }
        // Else if z is true, outerLi displayed as list-item
        else {
            x[i].style.display = "block";
        }
    }
}

// No Search Results Found
function noResultsFound() {
    let x = document.getElementsByClassName('outer');
    let z = true;
    // If no review sections are found, z is true
    for (let i = 0; i < x.length; i++) {
        if (x[i].style.display == 'block') {
            z = false;
        }
    }
    // If z is true, display "No results found" to user
    if (z === true && $(".no-result").length === 0) {
        $(".main-body").append(`<h1 class="center-align text-grey no-result">No results found</h1>`);
    }
    // If z is false, remove "No results found" from screen
    else if (z === false) {
        $(".no-result").remove();
    }
}

// Modal Function
function myModal(modalId) {
    // Modal appears
    $(modalId).fadeIn(500);
    $(".modal-content").fadeIn(500);
    // Close modal on "X" click
    $(".closeModal").click(function() {
        closeModal(modalId);
    });
    // Close Modal on "No" click
    $("#cancel").click(function() {
        closeModal(modalId);
    });
}

// Close modal function
function closeModal(modalId) {
    $(modalId).fadeOut(500);
}
