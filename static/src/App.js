import React, { Component } from 'react';
import './App.css';
import { get_all_tasks, add_task } from './http_functions';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import Checkbox from '@material-ui/core/Checkbox';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';


const styles = {
  img: {
    height: '150px',
    width: '150px'
  },
  white: {
    color: 'white'
  }
};


class App extends Component {
  state = {
    tasks: [],
    taskToAdd: ""
  }

  componentDidMount() {
    get_all_tasks()
      .then(res => {
        const tasks = res.data.tasks;
        this.setState({
          tasks: tasks
        });
      })
      .catch(error => {
        console.log(error);
      })
  }

  addTask() {
    const task = this.state.taskToAdd;
    add_task(task)
      .then(res => {
        this.state.tasks.push(task);
        this.setState({
          tasks: this.state.tasks
        })
      })
      .catch(error => {
        console.log(error);
      });
  }

  handleChange(event) {
    this.state.taskToAdd = event.target.value;
    this.setState({
      taskToAdd: event.target.value
    });

    if (event.key === "Enter") {
      this.addTask();
      event.target.value = "";
    }
  }

  render() {
    return (
      <div className="App">
        <Typography style={styles.white} variant="h2" gutterBottom>
          Steps To Deploy To Azure
        </Typography>

        <FormControl>
          <TextField
            error
            id="task-input"
            label="Add A Task"
            onKeyPress={(e) => this.handleChange(e)}
            margin="normal"
            variant="outlined"
          />
          { 
            this.state.tasks.map(task => 
              (<FormControlLabel
                control={
                  <Checkbox style={styles.white}/>
                }
                label={<Typography style={styles.white}>{task}</Typography>}
              />)
            )
          }
        </FormControl>
      </div>
    );

  }
}

export default App;
