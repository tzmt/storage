import React, { Component } from 'react';
import Cleave from 'cleave.js/react';

const query = 'http://localhost:5000/query';

export default class DateForm extends Component {
    constructor(){
        super()

        this.state = {
            inputDate: null,
            inputTime: null,
            inputLocation: null,
            data: null
        };
    }

    onDateChange(event) {
        this.setState({inputDate: event.target.value});
    }

    onTimeChange(event) {
        this.setState({inputTime: event.target.value});
    }

    onLocationChange(event) {
        this.setState({inputLocation: event.target.value});
    }

    submitButton() {
        fetch(query, {
            method: 'POST',
            body: JSON.stringify({
                inputDate: this.state.inputDate,
                inputTime: this.state.inputTime,
                inputLocation: this.state.inputLocation
            })

        }) 
        .then(results => results.json())
        .then(resultsJson => {
            this.setState({data: JSON.stringify(resultsJson)});
            console.log(this.state.data);
        })
    }

    render() {
        return (
            <div>
                <label>
                    Date
                    <Cleave placeholder="MM/DD/YYYY"
                    options={{date: true, datePattern: ['m', 'd', 'Y']}}
                    onChange={this.onDateChange.bind(this)} />
                </label>
                <p />
                <label>
                    Time 
                    <Cleave placeholder="HH:mm"
                    options={{time: true, timePattern: ['h', 'm']}}
                    onChange={this.onTimeChange.bind(this)} />
                </label>
                <p />
                <label>
                    Location 
                    <input onChange={this.onLocationChange.bind(this)} />
                </label>
                
                <p />
                <input type='button' value='bleep!' 
                    onClick={this.submitButton.bind(this)} />
            </div>
        );
    }  
}


