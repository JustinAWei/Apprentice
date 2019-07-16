import React, { Component } from 'react';
import {
  BrowserRouter,
  Route,
  Link
} from 'react-router-dom';

import Landing from './Landing';

class Router extends Component {
  render() {
    return (
        <BrowserRouter>
          <Route exact path="/" component={Landing} />
        </BrowserRouter>
    );
  }
}

export default Router;
