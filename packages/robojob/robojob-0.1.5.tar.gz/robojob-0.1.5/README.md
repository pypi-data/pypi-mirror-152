

# Features

- *Job definition in code:* Jobs are Python code wrapped in a context manager.
- *Job configuration in data:* Parameter values can be stored in a configuration file.
- *Dynamic parameter binding:* Parameter values are wired to tasks at runtime, so adding a parameter to a task (e.g. a stored procedure) will work with no change to the job definition code.
- *Logging*: Parameter values used and errors raised by tasks are logged, and so are error thrown by the orchestration parts of the job.

# Quickstart

Install robojob using `pip install robojob`.

## Hello, world

Save and run the following:

~~~python
import robojob

def greet(name):
    print(f"Hello, {name}!")

with robojob.go("hello") as ctx:
    ctx.execute(greet, name="world")
~~~

The result should be the same as running `greet(name="world")`.

Set up logging to see what's happening behind the scenes:

~~~python
import logging

logging.basicConfig(level="INFO", format="%(levelname)s %(message)s")
~~~

Here we can see the job and task execution numbers - but until you connect robojob to a proper backend, the numbers will be assigned sequentially and task and job executions will not be logged.

## Setting a context parameter

Try moving a parameter value to the job execution context:

~~~python
with robojob.go("hello") as ctx:
    ctx["name"] = "world"
    ctx.execute(greet)
~~~

Note that the parameter value still gets used, even though it is not passed directly.

## Setting parameter values in a configuration file

Now try moving the parameter value to a configuration file called `robojob.yml`, in the same directory as the script:

~~~yaml
parameters:
  name: fileworld
~~~

Then remove the parameter value from the job definition:

~~~python
with robojob.go("hello") as ctx:
    ctx.execute(greet)
~~~

## Using the job execution id

Try adding a new task:

~~~python
def greet_again(name, job_execution_id):
    print(f"Hello again from {job_execution_id}, {name}!")
~~~

Then add it to the job:

~~~python
with robojob.go("hello") as ctx:
    ctx.execute(greet)
    ctx.execute(greet_again)
~~~

Notice that `greet_again` can access the job execution ID even though it was not passed or added explicitly anywhere.

## Exiting early from a job

You can use the `exit()` method of the job execution context to exit early from a job.

~~~python
with robojob.go("hello") as ctx:
    ctx.execute(greet)
    ctx.exit("Skipped")
    ctx.execute(greet_again)
~~~

`exit()` is primarily useful for jobs that sometimes run without doing anything other than checking if they should do something.

You can supply a custom status to make it clear that the job ended abnormally, but
`exit()` should not be used when an error has occurred. In this case, you should throw 
an exception, which will propagate to whatever invokes the job.

# Details

## Job Execution

1) The job execution passes itself to the backend where it is logged and assigned a job execution id.
1) Orchestration code and tasks are executed, with parameter values and logging being  managed by the job execution.
1) When control passes out of the context, the job execution checks how the job ended:
- If a `UserExitException` was thrown, the status of the job is changed to the status passed with exception and the error is suppressed.
- If any other exception was thrown, the status is changed to "Failed" and the error is rethrown.
- Otherwise, the status is changed to "Completed". In any case, the job execution finally passes itself to the backend for logging.

## Task execution

The `execute()` method executes Python functions in the parameter and logging context of a job execution. There are several other job 
- `execute_procedure()` executes SQL Server stored procedures
- `execute_r()` executes an R script, passing the parameters named in the first line of the script. Parameter names are all sequences of alphanumerical characters and underscores.
- `execute_powershell()` executed a PowerShell script, passing the parameters passed in the `param()` declaration of the script (which must be kept on the first line).

These are all convenience methods that set up a `TaskExecution` instance and pass it to `process_task_execution()`, which performs parameter binding and starts the task, catching exceptions and logging along the way. 

1) The client creates a Task Execution instance that hold the details of the task being executed and passes it to the `process_task_execution` of the Job Execution context.
1) Parameter binding:
  - The Job Execution context creates a Parameter Collection holding the parameter values that will be accessible to the task execution. This is a combination of global variables and local variables supplied for this particular task execution.
  - The Task Execution instance uses the Parameter Collection to bind specific 
1) Logging: The job and task execution instances are passed to the backend, which logs 
   The task execution id is assigned after parameter binding and is therefore not accessible to tasks.
1) Execution:
  - The job execution context tries to execute the task execution instance
  - If an exception is raised, the status of the task is changed to "Failed" and the error is message is attached to the task execution instance before it is passed to the backend for logging and the error is rethrown.
  - If no error is thrown, the status of the task is changed to "Completed" before it is passed to the backend for logging

