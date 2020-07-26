import React, { Component } from "react";
import {NavLink, Switch, Route} from 'react-router-dom';
import Mainpage from "./App/components/mainpage/mainpage";
import MyPage from '../mypage/mypagemain';
import Register from '../register/register';
import  { Redirect } from 'react-router-dom';
import axios from "axios";

class Login extends Component {
    render(){
    /*TODO - 로그인 창으로 만들기. UI 상황 봐서 별도 페이지 아닌 Modal로 가져갈 수 있음*/
        <NavLink exact activeClassName="current" to="/register">회원가입</NavLink> // 아이디 없으면 회원가입 유도
        <NavLink exact activeClassName="current" to="/profiles">메인 화면으로 돌아가기</NavLink> // 메인화면으로 돌아가는 버튼 (메이비. 뒤로가기로 대체 가능)
    }
}