import React, { Component } from 'react';

import Algorithm from './Algorithm';

import './css/Algorithms.css';

export default class Algorithms extends Component {
  render() {
    return (
        <div className="algorithms">
          <h1>First, select a machine learning algorithm</h1>
          <div className="wrapper">
            <Algorithm color="red" value="tree" name="Decision Trees" setAlgorithm={this.props.setAlgorithm} />
            <Algorithm color="pink" value="svm" name="SVM" setAlgorithm={this.props.setAlgorithm} />
            <Algorithm color="purple" value="gnb" name="GNB" setAlgorithm={this.props.setAlgorithm} />
          </div>
        </div>
    );
  }
}
