$('#clear').click(function(){
    inputs = $('#fields').find('input');
    inputs.each(function() {
        this.value = '';
    })
    error = $('.error').first();
    if(! error.hasClass('d-none')) error.toggleClass('d-none');
});

$('#count').click(function(){
    inputs = $('#fields').find('input');
    if(inputs.first().val() == "") {
        $('.error').first().toggleClass('d-none');
    }
    else {
        if(inputs.first().attr('id') == 'm') {
            inputs.last().val(+inputs.first().val() / 1000);
        } else inputs.last().val(+inputs.first().val() * 1000);
    }
});

$('#swap').click(function(){
    inputs = $('#fields').find('input');
    error = $('.error').first();
    if(! error.hasClass('d-none')) error.toggleClass('d-none');
    temp = inputs.first().parent().html();
    inputs.first().parent().html(inputs.last().parent().html());
    inputs.last().parent().html(temp);
    inputs = $('#fields').find('input');
    inputs.last().prop('readonly',true);
    inputs.first().prop('readonly',false);
    inputs.each(function() {
        this.value = '';
    })
});
