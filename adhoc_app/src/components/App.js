import React, {Component} from 'react';
import PropTypes from 'prop-types';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Input from '@material-ui/core/Input';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import {fade} from '@material-ui/core/styles/colorManipulator';
import {withStyles} from '@material-ui/core/styles';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Paper from '@material-ui/core/Paper';
import AccountCircle from '@material-ui/icons/AccountCircle';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';
import './App.css';
import Message from './Message';
import Dashboard from './Dashboard';

const styles = theme => ({
  root: {
    width: '100%'
  },
  grow: {
    flexGrow: 1
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20
  },
  title: {
    display: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'block'
    }
  },
  layout: {
    width: 'auto',
    display: 'block', // Fix IE11 issue.
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    [theme.breakpoints.up(400 + theme.spacing.unit * 3 * 2)]: {
      width: 400,
      marginLeft: 'auto',
      marginRight: 'auto'
    }
  },
  paper: {
    marginTop: theme.spacing.unit * 8,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: `${theme.spacing.unit * 2}px ${theme.spacing.unit * 3}px ${theme.spacing.unit * 3}px`
  },

  icon: {
    margin: theme.spacing.unit
  },
  form: {
    width: '100%',
    marginTop: theme.spacing.unit
  },
  submit: {
    marginTop: theme.spacing.unit * 3
  }
});

const style = {
  color: "inherit",
  fontSize: "0.875rem",
  textTransform: "uppercase",
  fontWeight: "500",
  color: "white",
  textDecoration: "none"
};

class App extends Component {



  render() {
    const {classes} = this.props;

    return (<div>
      <CssBaseline/>
      <Router>
        <div>
          <div className={classes.root}>
            <AppBar position="static">
              <Toolbar>
                <Typography variant="title" color="inherit" className={classes.grow} align="center">
                  Distress Relief App
                </Typography>

                <Link to={'/Message'} className="Link">
                    <Button style={style}  color="primary">
                      Send Message
                    </Button>
                </Link>

                <Link to={'/Dashboard'} className="Link">
                    <Button style={style}  color="primary">
                      Dashboard
                    </Button>
                </Link>

              </Toolbar>
            </AppBar>
          </div>

          <Switch>
            <Route exact="exact" path='/Message' component={Message}/>
            <Route exact="exact" path='/Dashboard' component={Dashboard}/>
          </Switch>
        </div>
      </Router>
    </div>);
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(App);
