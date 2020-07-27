import React, { Component } from "react";
import {NavLink, Switch, Route} from 'react-router-dom';
import Mainpage from "../mainpage/mainpage";
import MyPage from '../mypage/mypagemain';
//import Login from '../login/login';
//import Register from '../register/register';
import  { Link } from 'react-router-dom';
import axios from "axios";



class Header extends Component {
    render(){
        return(
            <nav>
                <ul>
                    <li><Link to="/profiles" className= {Mainpage}>홈</Link></li>
                    <li><Link to="/mypage" className= {MyPage}>내페이지</Link></li>
                </ul>
            </nav>
        );
    }
}

/*
class Header extends Component {
    render(){
        return(

            <nav>
                <ul>
                    <li><NavLink exact activeClassName="current" to='/profiles'>메인페이지</NavLink></li>
                    <li><NavLink exact activeClassName="current" to='/mypage'>마이페이지</NavLink></li>
                    <li><NavLink exact activeClassName="current" to='/Login'>로그인</NavLink></li>
                    <li><NavLink exact activeClassName="current" to='/Register'>회원등록</NavLink></li>
                    <li><NavLink exact activeClassName="current" to='/RegisterMentor'>멘토등록하기</NavLink></li>
                </ul>
            </nav>
            );
    }
}
*/

export default Header;