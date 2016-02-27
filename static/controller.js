/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var popsciquiz = {
    hello : function() {
        var test_el = $("#test");
        test_el.html('hello');
        console.log('test');
    },
    setPlayerCount : function() {
        jQuery.get('player_count', function(data) {
            $('#players_count').html(data);
        });
    }
};

window.onload = function() {
    window.setInterval(popsciquiz.setPlayerCount, 100);
};
