This is a repo for training and learning concepts about the whole flask Python framework.

This proyect consist in a basic API that lets you create, modify, and check todo's lists.

The data structure of the todo lists are these:

{
  "header":["task1","task2","task3" ... ]
}

Where the header is the name of the list


It has the next endpoints:

/todo/set/ that allows you to add a task to a list or to add a new header. The form has 2 inputs: 'todoHeader' -> Header to add , and 'todoinput' -> Task to add.
/todo/delete/ lets you delete a task from a specific header. The inputs of the form are 'todoHeader' -> header and 'taskToDelete' -> The task of the header that you want to delete
/todo/showAll/ it returns the dict with all the todo lists
/todo/changeTask/ that lets you change a task from a header with the input that the user desires. Form inputs are: 'todoHeader' -> Header, 'swapouttask' -> The name of the task you want to change, and 'swapintask' -> The task that you want to subsitute for swapouttask


For trying it out i recommend you to use something like postman.
