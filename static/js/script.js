// Initialize mobile collapse menu
$(".button-collapse").sideNav();

// Search users in search bar
$("#searchBar").keyup(() => {
    search();
});

// Call Modal
$("#delete-ac").click(() => {
    myModal();
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
    let a = document.getElementsByClassName('outer-a');
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
            a[i].style.display = "none";
        }
        // Else if z is true, outerLi displayed as list-item
        else {
            x[i].style.display = "block";
            a[i].style.display = "block";
        }
    }
}

// Modal Function
function myModal() {
    // Modal appears
    $("#myModal").fadeIn(500);
    $(".modal-content").fadeIn(500);
    // Close modal on "X" click
    $(".closeModal").click(function() {
        closeModal();
    });
    // Close Modal on "No" click
    $("#cancel").click(function() {
        closeModal();
    });
}

// Close modal function
function closeModal() {
    $("#myModal").fadeOut(500);
}
