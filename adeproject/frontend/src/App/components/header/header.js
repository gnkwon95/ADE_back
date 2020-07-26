import React, { Component } from "react";
import {NavLink, Switch, Route} from 'react-router-dom';
import Mainpage from "./App/components/mainpage/mainpage";
import MyPage from '../mypage/mypagemain';
//import Login from '../login/login';
//import Register from '../register/register';
import  { Redirect } from 'react-router-dom';
import axios from "axios";

class Header extends Component {
/*TODO - 배너 모양으로 바꾸기*/
    render(){
        <nav>
            <ul>
                <li><NavLink exact activeClassName="current" to='/profiles'>메인페이지</NavLink></li> //메인페이지 가기 버튼
                <li><NavLink exact activeClassName="current" to='/mypage'>마이페이지</NavLink></li> // 마이페이지 가기 버튼
                <li><NavLink exact activeClassName="current" to='/Login'>로그인</NavLink></li> // 로그인 가기 버튼
                <li><NavLink exact activeClassName="current" to='/Register'>회원등록</NavLink></li> // 로그인 가기 버튼, if 로그인상태 아니면
                <li><NavLink exact activeClassName="current" to='/RegisterMentor'>멘토등록하기</NavLink></li> // 멘토 등록 버튼, if 로그인상태 & id_identity != 멘토
            </ul>
        </nav>
    }
}