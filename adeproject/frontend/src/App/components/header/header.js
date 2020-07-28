import React, { Component } from "react";
import {NavLink, Switch, Route} from 'react-router-dom';
import Mainpage from "../mainpage/mainpage";
import MyPage from '../mypage/mypagemain';
//import Login from '../login/login';
//import Register from '../register/register';
import  { Link } from 'react-router-dom';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav, NavDropdown, Form, FormControl, Button } from 'react-bootstrap';



class Header extends Component {
    render() {
        return(
        <div>
            <Navbar bg="light" expand="lg">
              <Navbar.Brand href="/">ADE-beta</Navbar.Brand>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                  <Nav.Link href="/">Home</Nav.Link>
                  <Nav.Link href="/mypage/1">마이페이지</Nav.Link>
                  {
                    this.props.isAuthenticated?
                    <Nav.Link href="/"> Logout</Nav.Link> :
                    <Nav.Link href="/Login">Login</Nav.Link>
                  }
                  <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                  </NavDropdown>
                </Nav>
                <Form inline>
                  <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                  <Button variant="outline-success">Search</Button>
                </Form>
              </Navbar.Collapse>
            </Navbar>
           </div>
        );
    }
}


export default Header;