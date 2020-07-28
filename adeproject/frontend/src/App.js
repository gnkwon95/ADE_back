import React, { Component, Fragment } from 'react';
import Mainpage from "./App/components/mainpage/mainpage";
import Header from "./App/components/header/header";
import MyPage from "./App/components/mypage/mypagemain";
import Login from "./App/components/login/login"
import {NavLink, Switch, Route, BrowserRouter as Router} from 'react-router-dom';
import {connect} from 'react-redux';
 import './App.css';
import * as actions from './store/actions/auth';




class App extends Component {

    componentDidMount() {
        this.props.onTryAutoSignup();
    }

    render() {
        return (
            <Router>
                <Header {...this.props} >
                </Header>
                <div>
                    <Route exact path="/" component={Mainpage} />
                    <Route path="/profiles" component={ Mainpage } />
                    <Route path="/mypage/:pk" component={ MyPage } />
                    <Route path="/login" component = {Login} />
                </div>
            </Router>
        )
    }
}


const mapStateToProps = state => {
    return {
        isAuthenticated: state.token != null
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onTryAutoSignup: () => dispatch(actions.authCheckState())
    }
}


export default connect(mapStateToProps, mapDispatchToProps)(App);
