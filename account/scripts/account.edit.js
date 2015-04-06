$(function () {
    // form automatically generates ID's with the syntax 'id_formfieldname'
    $('#id_username').on('change', function () {
        //call the server with the username the user typed
        var username = $('#id_username').val();
        var site_user_id = $('.submit_btn').attr('data-site_user_id');

        $.ajax({
            url: '/account/account.check_username/' + site_user_id,
            type: 'POST',
            data: {
                'u': username
            },
            // query the server to see if the username is already taken
            success: function (resp) {
                $('#id_username_message').remove();
                //server replies with a yes/no
                //username not available (bad)
                if (resp == 'No') {
                    $('#id_username').after('<span id="id_username_message" style="color: red;">Username not available</span>');
                }
            }//success
        });//ajax
    });//change
});//ready