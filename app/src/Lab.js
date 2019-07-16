import React, { Component } from 'react';

import './css/Lab.css';

export default class Lab extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: ''
    };
  }
  handleChange = (event) => {
    this.setState({
        prediction: event.target.value
    });
  }
  handleClick = (event) => {
      this.props.predict(this.state.prediction);
  }
  render() {
    return (
      <div className="lab">
        <h1>Apprentice's Lab</h1>
        <h2>Experiment with your ML model here</h2>
        <div className="statistics">
            <h3>Statistics</h3>
            <div>
                <h1> {this.props.rows} </h1>
                <h2> rows </h2>
            </div>
            <div>
                <h1> {this.props.size} </h1>
                <h2> mB </h2>
            </div>
            <div>
                <h1> {this.props.time} </h1>
                <h2> ms </h2>
            </div>
        </div>
        <textarea placeholder="Enter comma separated test data here" value={this.state.prediction} onChange={this.handleChange}>
        </textarea>
        <div onClick={this.handleClick} className="submit">
          <h3 >Submit</h3>
        </div>
      </div>
    );
  }
}
