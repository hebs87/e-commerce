$(function() {
    /* Send payment form info to Stripe when form is submitted */
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };
    
    /* Stripe token */
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            // Prevent the credit card details from being submitted
            // to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            /* Submit the form */
            form.submit();
        } else {
            /* If we don't get 200 status code, we want to post error message */
            $("#stripe-error-message").text(response.error.message);
            /* Stripe API IDs - have to stick to them or it won't work */
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});