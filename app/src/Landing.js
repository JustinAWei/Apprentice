import React, {
  Component
} from 'react';
import $ from 'jquery';

import './css/Landing.css';

import Masthead from './Masthead';
import Algorithms from './Algorithms';
import Data from './Data';
import Loading from './Loading';
import Lab from './Lab';

export default class Landing extends Component {
  constructor(props) {
    super(props);
    this.state = {
      example: '',
      hyperparams: {},
      time: 0,
      rows: 0,
      size: 0,
    };
  }

  setAlgorithm = (algorithm) => {
    this.setState({algorithm});
    $('html, body').animate({
      scrollTop: $('.data').offset().top
    }, 600);
  }

  setExample = (example) => {
    this.setState({example}, () => {
      fetch('/example', {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.state)
        })
        .then(res => res.json())
        .then(json => {
          this.setState({id: json.id}, this.fit);
        });
    });
  }

  fit = () => {
    console.log(this.state)
    fetch('/fit', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.state)
      })
      .then(res => res.json())
      .then(json => {
        this.setState({
            time: json.time,
            rows: json.rows,
            size: json.size,
          },
          () => {
            $('html, body').animate({
              scrollTop: $('.lab').offset().top
            }, 1600);
          })
      });
  }

  predict = (prediction) => {
    this.setState({
      X: prediction
    }, () => {
      fetch('/predict', {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.state)
        })
        .then(res => res.json())
        .then(json => {
          this.setState({result: json}, () => console.log(this.state))
        })
    })
  }

  render() {
    return (
      <div className="landing">
          <Masthead/>
          <Algorithms setAlgorithm={this.setAlgorithm}/>
          <Data setExample={this.setExample}/>
          <Loading bars={70} maxOffset={30}/>
          <Lab predict={this.predict} time={this.state.time} rows={this.state.rows} size={this.state.size}/>
      </div>
    );
  }
}

