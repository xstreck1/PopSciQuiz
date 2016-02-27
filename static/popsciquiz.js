/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var popsciquiz = {
    timer_id: 0,
    hello: function () {
        var test_el = $("#test");
        test_el.html('hello');
        console.log('test');
    },
    setPlayerCount: function () {
        jQuery.get('player_count', function (data) {
            $('#players_count').html(data);
        });
    },
    msPerQuestion: 25000,
    questionNo: 0,
    questionCount: 2,
    questions: [
        "Which astronaut played Space Oddity at the ISS on a guitar?", 
        "What do we scientifically call a rock, that landed on Earth from outer space?", 
        "Which specie does not do cooperative hunting?",
        "How do you call the process of making RNA based on DNA?",
        "What is the derivate of x<sup>2</sup>?"],
    answers: [
        ["Chris Hadfield", "Mark Whatney", "Matt Kowalski", "Hugh Mann"], 
        ["Asteroid", "Meteor", "Meteorite", "Rolling Stone"], 
        ["chimpanzees", "dolphins", "lions", "falcons"],
        ["translation", "transcription", "transmutation", "transmogrification"],
        ["x", "2x", "x<sup>2</sup>", "2x<sup>2</sup>"]
        
    ],
    setNewQuestion: function () {
        if (popsciquiz.questionNo < popsciquiz.questionCount) {
            $.post('/new_question');
            $("#question_text").html(popsciquiz.questions[popsciquiz.questionNo]);
            for (var i = 1; i < 5; i++) {
                var name = "#answer_" + i + "_text";
                var ele = $(name);
                ele.html("&nbsp" + i + ") " + popsciquiz.answers[popsciquiz.questionNo][i - 1]);
            }
            popsciquiz.questionNo++;
        }
        else {
            window.clearInterval(popsciquiz.timer_id);
            window.location.href = "result.html?" + Math.random();
        }
    },
    selected : function(i) {
        $.post('/answer/' + i);
    }
};
