$(function () {
    // grabs element from off the page, we want to pull our form element from off the page
    $('#loginform').ajaxForm(function (data) {
        $('#login_dialog').find('.modal-body').html(data);
    });
}); //ready