import React, { Component } from "react";
import {NavLink, Switch, Route} from 'react-router-dom';
import MyPageEdit from "./editModal"
import Charge from "../charge/charge"
import axios from "axios";


class MyPage extends Component {
/*TODO - add contents */
    constructor(props){
        super(props);

        this.state = {
            info: {
                user_id: "aa",
                email:"",
                user_name:"",
                user_pw:"bb",
                credit:99999,
                credit_used:0,
            }
        }
    }

    componentDidMount() {
        this.resetState();
    }


    getInfo = () => {
        axios.get('mypage/2').then(res => this.setState({ info: res.data }));
      };

    resetState = () => {
       this.getInfo(this.props.pk);
     };



    render() {
        this.resetState()
        return(
        <div>
            {this.state.user_name} NAME
            <li>{this.state.user_pw}</li>
            <li>{this.state.info.credit}</li>
            <li>{this.state.info.credit_used}</li>
         </div>
         );
         }
    }

 export default MyPage;


 /*
            matched_mentors:[]
            searched_mentors:[]
            matched_mentees:[]
- 이부분은 쿼리로 해결. 필요 시 백앤드에서 views함수에 추가. */

            // {user_name} 님 안녕하세요!
            // 보유 매칭권 수      |     현재 매칭된 멘토/멘티     |        내가 찾아본 멘토
            // (Link)충전하기     |       김신(LINE) 멘토       |       백승호 (KAKAO) 멘토

            //내 프로필
            //ID - ade
            // email - ade@adedata.com
            // 이름  -  권기남
            // (Modal link) 수정하기