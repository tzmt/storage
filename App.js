import React, { Component } from 'react';
import './App.css';
import DateForm from './DateForm.js';
//import AstroChart from './AstroChart.js';
import drawn from './ChartDrawer.js';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      aspects: [],
      boop: '' 
    };
  }


  render() {
    return (
      <div className="App">
      <svg id='horoscope'></svg>
        <div>It's kinda sorta working?</div>
        <p />
        <DateForm />
      </div>
    );
  }
}
