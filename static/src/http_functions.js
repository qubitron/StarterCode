import axios from "axios";

export function add_task(task) {
    return axios.post("/api/v1/add_task", {
        task
    })
}

export function get_all_tasks() {
    return axios.get("/api/v1/get_all_tasks")
}