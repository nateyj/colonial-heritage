/**
 * Created by Nate on 2/24/15.
 */
$(function () {
    // grabs element from off the page, we want to pull our form element from off the page
    $('#login_dialog').modal({
        show: false
    });//modal

    $('#show_login_dialog').on('click', function () {

        $('#login_dialog').modal('show');
        $.ajax({
            url: '/homepage/login.loginform',
            success: function (data) {
                $('#login_dialog').find('.modal-body').html(data)
            }//success
        });//ajax
    });//click
}); //ready