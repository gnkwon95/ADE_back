import React, { Component, Fragment } from 'react';
import Mainpage from "./App/components/mainpage/mainpage";
import Header from "./App/components/header/header";
// import './App.css';


class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <Mainpage />
            </Fragment>
        )
    }
}



/* - to jump around paths
const Main = () => (
    <Switch>
        <Route exact path='/profiles' component = {Mainpage}></Route>
        <Route exact path='/mypage' component = {MyPage}></Route>
    </Switch>
);
*/


export default App;
