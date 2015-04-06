$(function () {
    //this button is located for each item on the list of products page. If a user were to add it to the cart, only
    //one of that product will be added with the option to edit the quantity once viewing the cart
    $('.add_to_cart_btn').on('click', function () {
        var product_id = $(this).attr('data-product_id');

        $.loadmodal({

            url: '/catalog/shopping_cart.add/' + product_id + '/1',
            title: 'Shopping Cart',
            width: '700px'
        }); //loadmodal
    }); //click

    // search is case sensitive
    $('#search').on('keypress', function () {

        // grabs user's input search criteria
        var input = $('#search').val();


        // function will iterate through each item_container. Every item_container contains the product picture and name in text
        $('.item_container').each(function () {
            // text refers to ANY text in the item_container, including button name, etc.
            if ($(this).text().indexOf(input) == -1)    // -1 means that if it's false or returns false
                $(this).hide()  //if the item_container text doesn't match the user's criteria, then hide it
            else
                $(this).show()
        }); //each
    }); //keypress

    $('#search_btn').on('click', function () {
        $('#search').val('');

        $('.item_container').each(function () {
            $(this).show()
        }); //each
    }); //click

    //$('#search').ajaxForm(function(data) {
    //    $('#search_results_container').html(data)
    //});// ajaxForm
}); //ready
