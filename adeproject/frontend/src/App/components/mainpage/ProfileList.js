import React, { Component } from "react";
import { Table } from "reactstrap";
import {NavLink, Switch, Route} from 'react-router-dom';
import MyPage from '../mypage/mypagemain';
import axios from "axios";


class ProfileList extends Component {
    render() {
    const profiles = this.props.profiles;
        return(
        <Table dark>
        <thead>
          <tr>
            <th>title</th>
            <th>name</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!profiles || profiles.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            profiles.map(profile => (

              <tr key={profile.pk}>
                <td>YAAAAAAAAAAAY</td>
                <td>{profile.title}</td>
                <td>{profile.author}</td>
                <td align="center">
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
        )
    }
}

/*
class ProfileList extends Component {
    render() {
    const profiles = this.props.profiles;
        return(
            profiles.map(profile =>
                <tr key={profile.pk}>
                <li>{profile.title}</li>
                <li>{profile.author}</li>
                </tr>
            )
        );
    }
}
*/

export default ProfileList;