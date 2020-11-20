// jQuery for Cart

$(document).ready(function() {
    $('#add_to_cart').on('submit', function(event){
        event.preventDefault();
        addToCart();
        openSideCart();
    });
});

// Forward the form request with the productvariant
function addToCart() {
    form = $('#add_to_cart').closest("form");
    productvariant_value = $('#order_item').val()
    $.ajax({
        url: form.attr("data-sent-to-url"), // the endpoint
        type: "POST", // http method
        data: { productvariant: productvariant_value }, // data sent with the post request
        // handle a successful response
        success: function (html) {
            $('#sideDrawerContent').html(html)
        },
        // handle a non-successful response
        error: function (xhr, errmsg, err) {
        }
    });
};