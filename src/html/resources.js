
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

  // Handle click on "Give" button
  $(".give-button").click(function () {
    var supplyName = $(this).data("supply");
    $("#selectedSupply").text("Selected Supply: " + supplyName);
  });

  // Handle click on "Decrement" button
  $("#decrementButton").click(function () {
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