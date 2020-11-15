CREATE TABLE task (
    id int,
    name varchar(256),
    code_path varchar(512),
);

CREATE TABLE task_param (
    task_id int
};

CREATE TABLE task_result (
    task_id int
};