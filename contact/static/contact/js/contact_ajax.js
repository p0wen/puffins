$( document ).ready(function() {
    $('#contactform').on('submit', function(event){
        event.preventDefault();
        form = $('#contactform').closest("form");
        var serializedData = $(this).serialize();
        $.ajax({
            url : form.attr("data-sent-to-url"), // the endpoint
            type : "POST", // http method
            data : serializedData, // data sent with the post request
            // handle a successful response
            success : function(html) {
                $('#contactformouter').html(html)
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
            }
        });
    });
});