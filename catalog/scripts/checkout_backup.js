$(function () {
    $('#place_order').on('click', function () {
        $.loadmodal({
            url: '/catalog/checkout.receipt',
            title: 'Thank You for Shopping with Us!',
            width: '700px'
        }); //loadmodal
    }); //click
}); //ready
