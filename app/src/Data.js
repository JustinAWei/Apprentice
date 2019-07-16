import React, { Component } from 'react';
import $ from 'jquery';

import './css/Data.css';

import Example from './Example';

export default class Data extends Component {
  handlePress = () => {
    $('html, body').animate({
        scrollTop: $('.loading').offset().top
    }, 600);
  }
  render() {
    return (
        <div className="data">
          <h1>Then, choose some training data</h1>
          <div className="examples">
            <div className="row">
              <Example onClick={this.handlePress} name="MNIST Digits" value="digits" setExample={this.props.setExample} />
              <Example onClick={this.handlePress} name="Boston Houses" value="boston" setExample={this.props.setExample} />
            </div>
            <div className="row">
              <Example onClick={this.handlePress} name="Diabetes Patients" value="diabetes" setExample={this.props.setExample} />
              <Example onClick={this.handlePress} name="Iris Flowers" value="iris" setExample={this.props.setExample} />
            </div>
            <div className="row">
              <div onClick={this.handlePress} className="full purple column">
                <h3>Upload your own training data</h3>
              </div>
            </div>
          </div>
        </div>
    );
  }
}