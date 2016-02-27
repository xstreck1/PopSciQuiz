/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var popsciquiz = {
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
    msPerQuestion: 1000,
    questionNo: 0,
    questionCount: 2,
    questions: ["Who made the song Space Oddity?", "What do we scientifically call a rock, that landed on Earth from outer space?"],
    answers: [["David Bowie", "Michael Jackson", "Madonna", "Tina Turner"], ["Asteroid", "Meteor", "Meteorite", "Rolling Stone"]],
    setNewQuestion: function () {
        if (popsciquiz.questionNo < popsciquiz.questionCount) {
            $("#question_text").html(popsciquiz.questions[popsciquiz.questionNo]);
            for (var i = 1; i < 5; i++) {
                var name = "#answer_" + i + "_text";
                var ele = $(name);
                ele.html("&nbsp" + i + ") " + popsciquiz.answers[popsciquiz.questionNo][i - 1]);
            }
            popsciquiz.questionNo++;
        }
        else {
            window.location.href = "result.html";
        }
    }
};
