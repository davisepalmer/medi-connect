console.log('test0')
$(document).ready(function() {
  // Attach click event handler to all tab links
  $('.nav-link').on('click', function() {
    // Get the ID of the target tab content
    var targetTab = $(this).attr('href');
    
    // Hide all tab contents except the target tab
    $('.tab-pane').not(targetTab).removeClass('show active').addClass('fade');
    
    // Show the target tab content
    $(targetTab).addClass('show active').removeClass('fade');
  });
});

console.log('test1')
$(document).ready(function () {
  // Handle form submission
  $("#submitRequest").click(function () {
    var supplyName = $("#supplyName").val();
    var quantity = $("#quantity").val();
    var requestedBy = $("#requestedBy").val();

    $.ajax({
      type: "POST",
      url: "/create_supply",
      contentType: "application/json",
      data: JSON.stringify({
        supplyName: supplyName,
        quantity: quantity,
        requestedBy: requestedBy,
      }),
      success: function (response) {
        alert(response.message);
        // Optionally, update the table with the new supply data
      },
      error: function (xhr, status, error) {
        alert("Error creating supply: " + xhr.responseText);
      },
    });
  });

  console.log('test2')
  // Handle form submission
  $("#submitGiving").click(function () {
    var givingName = $("#givingName").val();
    var quantityb = $("#quantityb").val();
    var givenBy = $("#givenBy").val();

    $.ajax({
      type: "POST",
      url: "/create_supply",
      contentType: "application/json",
      data: JSON.stringify({
        givingName: givingName,
        quantityb: quantityb,
        givenBy: givenBy,
      }),
      success: function (response) {
        alert(response.message);
        // Optionally, update the table with the new supply data
      },
      error: function (xhr, status, error) {
        alert("Error sss supply: " + xhr.responseText);
      },
    });
  });

console.log('test3')
  // Handle click on "Decrement" button
  $("#Decrement").click(function () {
    var supplyName = $("#selectedSupply").text().split(": ")[1];
    var count = parseInt($("#decrementCount").val());

    if (count <= 0) {
      alert("Please enter a valid decrement count.");
      return;
    }

    var quantityElement = $("td:contains(" + supplyName + ")").next();
    var quantity = parseInt(quantityElement.text());

    if (count > quantity) {
      alert("Error: Decrement count exceeds available quantity.");
      return;
    }

    $.ajax({
      type: "POST",
      url: "/decrement_supply",
      data: { supplyName: supplyName, count: count },
      success: function (response) {
        alert("Quantity decremented successfully!");
        var newQuantity = quantity - count;
        quantityElement.text(newQuantity >= 0 ? newQuantity : 0);
      },
      error: function (xhr, status, error) {
        alert("Error decrementing quantity: " + xhr.responseText);
      },
    });
    $("#giveSupplyModal").modal("hide");
  });
});

// Handle form submission when the form inside the modal is submitted
$("#confirmDecrement").submit(function (event) {
  event.preventDefault(); // Prevent the default form submission

  // Retrieve supply name and decrement count from form inputs
  var supplyName = $("#supplyName").val();
  var decrementCount = $("#decrementCount").val();

  // Perform form validation here (e.g., check if input fields are not empty)

  // Make AJAX request to decrement endpoint
  $.ajax({
    type: "POST",
    url: "/decrement",
    contentType: "application/json",
    data: JSON.stringify({
      supplyName: supplyName,
      decrementCount: decrementCount,
    }),
    success: function (response) {
      alert(response.message);
      // Optionally, update the table with the new supply data
    },
    error: function (xhr, status, error) {
      alert("" + xhr.responseText);
    },
  });
});
