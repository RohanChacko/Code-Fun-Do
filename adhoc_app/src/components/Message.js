import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import FormControl from '@material-ui/core/FormControl';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import LockIcon from '@material-ui/icons/LockOutlined';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import withStyles from '@material-ui/core/styles/withStyles';

const styles = theme => ({
  layout: {
    width: 'auto',
    display: 'block',
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
  form: {
    width: '100%',
    marginTop: theme.spacing.unit
  },
  submit: {
    marginTop: theme.spacing.unit * 3
  }
});

class Message extends Component {
  render() {
    const {classes} = this.props;
    return (<div>
      <CssBaseline/>
      <div className={classes.layout}>
        <Paper className={classes.paper}>
          <Typography variant="headline">
            Send Message
          </Typography>
          <form className={classes.form}>
            <FormControl margin="normal" required="required" fullWidth="fullWidth">
              <InputLabel htmlFor="text">
                Message
              </InputLabel >
              <Input name="firstname" type="text" id="firstname" autoComplete="firstname"/>
            </FormControl>

            <Button type="submit" fullWidth="fullWidth" variant="raised" color="primary" className={classes.submit}>
              Send
            </Button>
          </form>
        </Paper>
      </div>
    </div>);
  }

}

Message.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Message);
