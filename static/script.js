// console.log($);
/* global $ */


(function() {
    var nextUrl;
    var clickedMore = false;
    var userInput;

    $('#submit-button').on('click', function(){
        //reset results div after previous search:
        $('#results-container').empty();
        $('#more').removeClass('show');
        $('#loading-gif').show();
        //new search:
        userInput = $('input[name=user-input]').val();
        var albumOrArtist = $('select').val();

        $.ajax({
            url: 'https://elegant-croissant.glitch.me/spotify',
            method: 'GET',
            // any sort of data we need to send to the API so we get a response
            data: {
                query: userInput,
                type: albumOrArtist
            },
            success: function(response) {
                // success runs when we get a response from the API
                showResults(response);
                $('#loading-gif').hide();
            }
        });
    });

    $('#more').on('click', function() {
        clickedMore = true;
        $.ajax({
            url: nextUrl,
            method: 'GET',
            success: function(response){
                showResults(response);
            }
        });
    });

    

}());
