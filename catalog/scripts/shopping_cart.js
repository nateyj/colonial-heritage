$(function () {
    $('.remove').on('click', function () {
        var product_id = $(this).attr('data-product_id');

        $.loadmodal({
            url: '/catalog/shopping_cart.remove/' + product_id,
            title: 'Shopping Cart',
            width: '700px'
        }); //loadmodal
    }); //click
}); //ready
