$(function () {
    $('.remove').on('click', function () {
        var product_id = $(this).attr('data-product_id');

        $.loadmodal({
            url: '/homepage/rental_cart.remove/' + product_id,
            title: 'Rental Shopping Cart',
            width: '700px'
        }); //loadmodal
    }); //click

    //$('#checkout').on('click', function() {
    //    var date_due = $("#datepicker").datepicker('getDate');
    //    var discount = $('#discount').val();
    //
    //    $.loadmodal ({
    //        url: '/homepage/rental_cart.enter_username/',
    //        ajax:
    //        {
    //            data:
    //            {
    //                date_due: date_due,
    //                discount: discount
    //            }
    //        },
    //        title: 'Enter Username',
    //        width: '700px'
    //    }); //loadmodal
    //}); //click
}); //ready
