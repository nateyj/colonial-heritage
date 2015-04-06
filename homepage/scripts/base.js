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

    //$('#sign_out').on('click', function() {
    //
    //    $.ajax({
    //        url: '/homepage/login.logout_view'
    //    });//ajax
    //});//click
}); //ready