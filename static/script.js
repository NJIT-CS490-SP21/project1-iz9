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

    function showResults(response){

        response = response.artists || response.albums;
        var myHtml = ''; //to add result 
        if (response.items.length > 0) {
            for (var i = 0; i < response.items.length; i++) {
                var spotifyUrl = response.items[i].external_urls.spotify;
                var myName = '<a target="_blank" rel="noopener noreferrer" href="'+spotifyUrl+'"><div class="annoying">' + response.items[i].name + '</div></a>';
                var imageUrl = 'static/no-image.jpg';
                
                if (response.items[i].images[0]) {
                    imageUrl = response.items[i].images[0].url;
                }
                var myImage = '<a target="_blank" rel="noopener noreferrer" href="'+spotifyUrl+'"><img src="'+imageUrl+'" alt="result image"></a>';
                myHtml += '<div class = "result-box">' + myImage + myName + '</div>';
            }
            if (clickedMore) {
                $('#results-container').append(myHtml);
            } else {
                var searchTerm = '<h2>Results for "'+userInput+'"</h2>';
                $('#search-term').html(searchTerm);
                $('#results-container').html(myHtml);
            }
            // get next set of 20 results ("more" button):
            // only use replace if there is a url to replace on:
            nextUrl = response.next && response.next.replace('https://api.spotify.com/v1/search', 'https://elegant-croissant.glitch.me/spotify');
            // console.log('corrected nextUrl: ', nextUrl);
            if (nextUrl) {
                $('#more').addClass('show');
            } else {
                $('#more').removeClass('show');
            }
        } else {
            var nonexistent = '<h2>Sorry, there are no results for "'+ userInput +'"</h2>';
            $('#search-term').html(nonexistent);
        }

    }

}());
