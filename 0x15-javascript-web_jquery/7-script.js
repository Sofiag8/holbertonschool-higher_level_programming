#!/usr/bin/node


$(document).ready(function () {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
        $('#character').text(data.name);
    });
});