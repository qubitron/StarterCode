import React, { Component } from 'react';
import './App.css';
import { get_all_tasks, add_task } from './http_functions';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import Checkbox from '@material-ui/core/Checkbox';
import TextField from '@material-ui/core/TextField';


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
    // event.preventDefault();
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
        <FormControl>
          <TextField
            label="Add A Task"
            onKeyPress={(e) => this.handleChange(e)}
            margin="normal"
            variant="outlined"
          />
          { 
            this.state.tasks.map(task => 
              (<FormControlLabel
                control={
                  <Checkbox checked={true}/>
                }
                label={task}
              />)
            )
          }
        </FormControl>
      </div>
    );

  }
}

export default App;
