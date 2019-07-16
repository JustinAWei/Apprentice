import React, { Component } from 'react';

import './css/Loading.css';

import Bar from './Bar';

export default class Loading extends Component {
  constructor(props) {
    super(props);
    let bars = [];
    for (let i=0; i<props.bars; i++) {
      const offset = Math.floor(Math.random()*props.maxOffset);
      bars.push([offset, 0]);
    }
    this.state = {
      current: 0,
      bars
    };
  }
  componentDidMount() {
    setInterval(function() {
      if (this.state.current >= this.props.bars) {
        this.setState({
          current: (this.state.current+1) > (this.props.bars+5) ? 0 : (this.state.current+1)
        });
      } else {
        let bars = this.state.bars.slice();
        bars[this.state.current][1] = 1;
        let updates = [
          [this.state.current-3, 0],
          [this.state.current-2, 0.3],
          [this.state.current-1, 0.7],
          [this.state.current+1, 0.7],
          [this.state.current+2, 0.3]
        ];
        if (this.state.current+1 >= this.props.bars) {
          updates[0][1] = 0;
          updates[1][1] = 0;
          updates[2][1] = 0;
          bars[this.state.current][1] = 0;
        }
        for (let update of updates) {
          if (update[0] >= 0 && update[0] < this.props.bars) {
            bars[update[0]][1] = update[1];
          }
        }
        this.setState({
          bars,
          current: this.state.current+1
        });
      }
    }.bind(this), 87.5);
  }
  render() {
    const bars = this.state.bars.map((element, index) => {
      return <Bar key={index} offset={element[0]} opacity={element[1]} />
    });
    return (
        <div className="loading">
          <h1>Hold tight! We're generating your custom ML model</h1>
          <div className="bars">
            {bars}
          </div>
        </div>
    );
  }
}
