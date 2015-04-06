$(function () {
    $('#view_cart').on('click', function () {
        $.loadmodal({
            url: '/catalog/shopping_cart/',
            title: 'Shopping Cart',
            width: '700px'
        }); //loadmodal
    }); //click
}); //ready
