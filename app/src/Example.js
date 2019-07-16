import React, { Component } from 'react';

export default class Example extends Component {
  onClick = () => {
    this.props.setExample(this.props.value);
    this.props.onClick();
  }
  render() {
    const classes = `example column`;
    return (
      <div className={classes} onClick={this.onClick}>
        <h3>{this.props.name}</h3>
      </div>
    );
  }
}
