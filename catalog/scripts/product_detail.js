$(function () {
    $('#detail_add_to_cart_btn').on('click', function () {

        var product_id = $(this).attr('data-product_id');
        var qty = $('#qty').val();

        $.loadmodal({
            url: '/catalog/shopping_cart.add/' + product_id + '/' + qty,
            title: 'Shopping Cart',
            width: '700px'
        }); //loadmodal
    }); //click
}); //ready
