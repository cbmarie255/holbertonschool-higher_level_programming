$('#toggle_header').click( function() {
    $('#toggle_header').toggleClass('green red');
    if ($('#toggle_header').hasClass('green')) {
        $('#toggle_header').toggleClass('red');
    }
});