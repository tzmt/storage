import React, { Component } from 'react';

const query = 'http://localhost:5000/boop';

export default class InfoForm extends Component {
    constructor(){
        super()

        this.state = {
            currentValue: '',
            planet: 0
        };

        this.changeHandler = this.changeHandler.bind(this);
        this.submitButton = this.submitButton.bind(this);
    }

    changeHandler(event) {
        this.setState({currentValue: event.target.value})
    }
    submitButton() {
        fetch(query, {
            method: 'POST',
            body: JSON.stringify({
                firstParam: this.state.currentValue
            })

        })
        .then(results => results.json())
        .then(resultsJson => this.setState({planet: JSON.stringify(resultsJson)}))
    }

    render() {
        return (
            <div>
                <form>
                    <label>
                        Name:
                        <input type='text' onChange={this.changeHandler} value={this.state.currentValue} />
                    </label>
                        <input type='button' value='boop!' onClick={this.submitButton} />
                </form>
                <div>{this.state.planet}</div>
            </div>
        )
    }  
}
