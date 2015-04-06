$(function () {
    //this event will occur on the .js file associated with the HTML file that has the agent enter the person's username
    //  and then presses the "View Rental Items" button
    $('#viewRentalItems').on('click', function () {
        var username = $('#username').val();

        $.post('/homepage/rental_items/' + username, function (data) {
            //I don't know what's supposed to go in here...
        });//post
    });//click

    $('.return').on('click', function () {
        var line_item_id = $(this).parent().parent().find('.rental_item_id').text();
        var damage_fee = $(this).parent().parent().find('.damage_fee').val();
        var damage_desc = $(this).parent().parent().find('.damage_desc').val();

        $.ajax({
            url: '/homepage/rental_return.update_session/',
            data: {
                'fee': damage_fee,
                'desc': damage_desc,
                'line_item_id': line_item_id
            },
            success: function (data) {
                if (data == 'Success!') {
                    $(this).replaceWith(data);
                }
            },
            context: this//success
        });
    });//click


    //$('.check_in').on('click', function() {
    //    $.ajax({
    //        url: '/homepage/rental_items.check_in/',
    //        success: function (resp) {
    //            console.log(resp);
    //            $('.button_cell').find('.check_in_btn_div').html(resp);
    //        }//success
    //    });
    //});//click
});//ready
