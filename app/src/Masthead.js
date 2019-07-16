import React, { Component } from 'react';
import $ from 'jquery';

import './css/Masthead.css';

import down from './img/down.png';

export default class Masthead extends Component {
  constructor(props) {
    super(props);

    this.state = {
      scrolled: false
    };
  }
  componentDidMount() {
    window.addEventListener('scroll', this.handleScroll);
  }

  componentWillUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  }

  handleScroll = (e) => {
    if (!this.state.scrolled && $(window).scrollTop() < 20) {
      $('html, body').animate({
          scrollTop: $('.algorithms').offset().top
      }, 600);
    }
    this.setState({
      scrolled: true
    });
  }

  nextPage = () => {
    $('html, body').animate({
        scrollTop: $('.algorithms').offset().top
    }, 600);
  }

  render() {
    return (
        <div className="masthead">
          <div className="wrapper">
            <h1>apprentice</h1>
            <h2>machine learning, trained for <span className="humans">humans</span></h2>
            <div className="bounce">
              <img className="down" onClick={this.nextPage} src={down} />
            </div>
          </div>
        </div>
    );
  }
}
