/**
 * Created by Nate on 2/24/15.
 */
$(function () {
    // grabs element from off the page, we want to pull our form element from off the page
    $('#login_dialog').modal({
        show: false
    });//modal

    $('#show_login_dialog_nav').on('click', function () {

        $('#login_dialog').modal('show');
        $.ajax({
            url: '/homepage/login.loginform',
            success: function (data) {
                $('#login_dialog').find('.modal-body').html(data)
            }//success
        });//ajax
    });//click

    $('#view_rental_cart').on('click', function () {
        $.loadmodal({
            url: '/homepage/rental_cart/',
            title: 'Rental Shopping Cart',
            width: '700px'
        }); //loadmodal
    }); //click

    var blue_clicks = 0;
    var green_clicks = 0;

    $('.color').on('click', function() {
        if ($(this).attr('id') == 'green') {
            green_clicks += 1;

            $('#green_clicks').html(green_clicks);
        }
        else {
            blue_clicks += 1;

            $('#blue_clicks').html(blue_clicks);
        }

        if (green_clicks > blue_clicks) {
            $('#winner').html('<strong> Green machine</strong>  is in the lead!')
        }
        else if (blue_clicks > green_clicks) {
            $('#winner').html('<strong>Blue goo</strong> does not want to lose!')
        }
        else {
            $('#winner').html('<em>Please end the suspense and break the tie!</em>')
        }
    });//blue click
}); //ready