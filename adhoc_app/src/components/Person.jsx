import React, { Component } from 'react';


function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

class Person extends Component {
    state = {
        id : null,
        x_coordinate = getRandomInt(0, area_width+1),
        y_coordinate = getRandomInt(0, area_height+1),
        center_of_motion = [x_coordinate, y_coordinate], //not sure if this syntax is correct
        displacement_x = getRandomInt(1,6),
        displacement_y = getRandomInt(1,6),
        range_of_motion = getRandomInt(50,200),
        wifi_range = getRandomInt(15,30),
        cell_connectivity = null,
        connected_people = [],
        message = null,
        chat = []
    }
    render() { 
        return (  );
    }
}
 
export default Person;