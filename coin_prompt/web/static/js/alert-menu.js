$(document).ready(function(){

    // Show / Hide % selector div
    $('input[name="set-alert-type"]').click(function(){
        const radio_id = $(this)[0].id;
        const price_ratio_container = $('#price-ratio-container');
        if(radio_id == 'price-at'){
            price_ratio_container.addClass('d-none');
        }
        else{
            price_ratio_container.removeClass('d-none');
            const base_price = $('input[name="selected-coin-price"]').val();
            console.log(base_price);
            $('#set-alert-target-price').val(base_price);
        }
    });

    // Change target price based on selected radio button
    $('.price-ratio').click(function(){
        const change = parseInt($(this).attr('data-change'));
        const base_price = parseFloat($('input[name="selected-coin-price"]').val());
        const radio_id = $('input[name="set-alert-type"]:checked')[0].id;

        let target_price = base_price;
        let factor = 100;
        if(radio_id == 'price-up'){
            factor = (factor+change)/100;
        }
        else if(radio_id == 'price-down'){
            factor = (factor-change)/100;
        }

        target_price *= factor;
        $('#set-alert-target-price').val(target_price);
    });

    $('#price-ratio-text').on('keyup', function(){
        const change = parseInt($(this).val());
        const base_price = parseFloat($('input[name="selected-coin-price"]').val());
        const radio_id = $('input[name="set-alert-type"]:checked')[0].id;

        let target_price = base_price;
        let factor = 100;
        if(radio_id == 'price-up'){
            factor = (factor+change)/100;
        }
        else if(radio_id == 'price-down'){
            factor = (factor-change)/100;
        }

        target_price *= factor;
        $('#set-alert-target-price').val(target_price);

    });
});