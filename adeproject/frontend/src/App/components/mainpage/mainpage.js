import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import {NavLink, Switch, Route} from 'react-router-dom';
import ProfileList from "./ProfileList";
//import LeadBanner from "../banner/leadbanner";
import axios from "axios";

class Mainpage extends Component {
    state = {
        profile: []
    }

     componentDidMount() {
    this.resetState();
  }

    getProfiles = () => {
        axios.get('/api/profiles/').then(res => this.setState({ profiles: res.data }));
      };

    resetState = () => {
       this.getProfiles();
       };

    render() {
        return (
        <>
        <h5> This is Mainpage page </h5>
        // big banner
            <ProfileList
               profiles={this.state.profiles}
               resetState={this.resetState}
             />
         </>
        );
    }
}

export default Mainpage;