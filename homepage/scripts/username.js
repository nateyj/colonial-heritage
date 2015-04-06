/**
 * Created by Nate on 2/24/15.
 */
$(function () {
    // grabs element from off the page, we want to pull our form element from off the page
    $('#usernameform').ajaxForm(function (data) {
        $('#jquery-loadmodal-js').find('.modal-body').html(data);
    });
}); //ready