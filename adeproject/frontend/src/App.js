import React, { Component, Fragment } from 'react';
import Mainpage from "./App/components/mainpage/mainpage";
import Header from "./App/components/header/header";
import MyPage from "./App/components/mypage/mypagemain";
import {NavLink, Switch, Route, BrowserRouter as Router} from 'react-router-dom';
// import './App.css';




class App extends Component {
    render() {
        return (
            <Router>
                <Header />
                <div>
                    <Route exact path="/" component={Mainpage} />
                    <Route path="/profiles" component={ Mainpage } />
                    <Route path="/mypage/:pk" component={ MyPage } />
                </div>
            </Router>
        )
    }
}


//  <li><NavLink exact activeClassName="current" to='/profiles'>메인페이지</NavLink></li>
/*
const Main = () => (
    <Switch>
        <Route exact path='/profiles' component = {Mainpage}></Route>
        <Route exact path='/mypage' component = {MyPage}></Route>
    </Switch>
);
*/


export default App;
