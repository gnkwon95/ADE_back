import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import '../../../index.css';
import { Form, Input, Button, Checkbox } from 'antd';
import {NavLink} from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../../../store/actions/auth';

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

 const onFinish = values => {
    console.log('Success:', values);
  };

  const onFinishFailed = errorInfo => {
    console.log('Failed:', errorInfo);
  };

class Login extends Component  {
    handleSubmit = values => {
        this.props.onAuth(values.username, values.password);
        this.props.history.push('/');
      }

    render() {
        let errorMessage = null;
        if (this.props.error) {
            errorMessage = (
                <p>{this.props.error.message}</p>
            )
        }

  return (
  <div>
  {errorMessage}
    <Form  className = 'login-form'
      {...layout}
      name="basic"
      initialValues={{
        remember: true,
      }}
      onFinish={this.handleSubmit}
    //  onSubmit = {onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[
          {
            required: true,
            message: 'Please input your username!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },
        ]}
      >
        <Input.Password />
      </Form.Item>


      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit">
          로그인
        </Button>
         또는
        <NavLink to='/register'>
            회원가입
        </NavLink>

      </Form.Item>
    </Form>
    </div>
  );
  }
};

const mapStateToProps = (state) => {
    return {
        loading: state.loading,
        error: state.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, password) => dispatch(actions.authLogin(username, password))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Login);