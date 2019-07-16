import React, { Component } from 'react';

import bar from './img/white-bar.png';

export default class Bar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      marginTop: this.props.offset,
      opacity: this.props.opacity
    };
  }
  componentWillReceiveProps(props) {
    this.setState({
      opacity: props.opacity
    });
  }
  render() {
    return (
      <div className="bar">
        <img style={this.state} src={bar} />
      </div>
    );
  }
}
