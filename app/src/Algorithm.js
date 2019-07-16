import React, { Component } from 'react';

import './css/Algorithm.css';

export default class Algorithm extends Component {
  handleClick = () => {
    this.props.setAlgorithm(this.props.value);
  }

  render() {
    const classes = `algorithm ${this.props.color}`;
    return (
      <div onClick={this.handleClick} className={classes}>
        <h2>{this.props.name}</h2>
      </div>
    );
  }
}
