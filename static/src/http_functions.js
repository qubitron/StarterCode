import axios from "axios";

export function add_task(task) {
    return axios.post("http://localhost:5000/api/v1/add_task", {
        task
    })
}

export function get_all_tasks() {
    return axios.get("http://localhost:5000/api/v1/get_all_tasks")
}