import React, { Component } from "react";
import {NavLink, Switch, Route} from 'react-router-dom';
import MyPageEdit from "./editModal"
import Charge from "../charge/charge"
import axios from "axios";

class MyPage extends Component {
/*TODO - add contents */
    render() {

    state = {
        info: {
            user_id: ''
            email:''
            user_name:''
            user_pw:''
            credit:''
            credit_used:''
        }
    }

/*
            matched_mentors:[]
            searched_mentors:[]
            matched_mentees:[]
- 이부분은 쿼리로 해결. 필요 시 백앤드에서 views함수에 추가. */

/*
    getInfo = () => {
        axios.get('/api/profiles/<int: profile_id>/').then(res => this.setState({ info: res.data })); //이부분 아마 수정 필요
      };
  유저의 프로필 정보 가져오는 함수
  */

    //
        return(
            // {user_name} 님 안녕하세요!
            // 보유 매칭권 수      |     현재 매칭된 멘토/멘티     |        내가 찾아본 멘토
            // (Link)충전하기     |       김신(LINE) 멘토       |       백승호 (KAKAO) 멘토

            //내 프로필
            //ID - ade
            // email - ade@adedata.com
            // 이름  -  권기남
            // (Modal link) 수정하기
        )
    }
 }

 export default MyPage;