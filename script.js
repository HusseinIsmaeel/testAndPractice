// document.addEventListener('DOMContentLoaded', function() {
//     const taskInput = document.getElementById('taskInput');
//     const addTaskBtn = document.getElementById('addTaskBtn');
//     const taskList = document.getElementById('taskList');


//     addTaskBtn.addEventListener('click', function() {
//         const taskText = taskInput.value.trim();

//         if (taskText !== '') {
//             const taskItem = document.createElement('li');
//             taskItem.innerText = taskText;

//             const deleteBtn = document.createElement('button');
//             deleteBtn.innerText = 'Delete';
//             deleteBtn.className = 'deleteBtn';

//             deleteBtn.addEventListener('click', function() {
//                 taskItem.remove();
//             });

//             taskItem.appendChild(deleteBtn);

//             taskItem.addEventListener('click', function() {
//                 taskItem.classList.toggle('completed');
//             });

//             taskList.appendChild(taskItem);
//             taskInput.value = '';
//         }
//     });
// });


document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    // Load tasks from local storage
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.forEach(taskText => addTask(taskText));

    addTaskBtn.addEventListener('click', function() {
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            addTask(taskText);
            // Save tasks to local storage
            tasks.push(taskText);
            localStorage.setItem('tasks', JSON.stringify(tasks));
            taskInput.value = '';
        }
    });

    function addTask(taskText) {
        const taskItem = document.createElement('li');
        taskItem.innerText = taskText;

        const deleteBtn = document.createElement('button');
        deleteBtn.innerText = 'Delete';
        deleteBtn.className = 'deleteBtn';
        deleteBtn.addEventListener('click', function() {
            taskItem.remove();
            // Remove task from local storage
            const index = tasks.indexOf(taskText);
            tasks.splice(index, 1);
            localStorage.setItem('tasks', JSON.stringify(tasks));
        });

        const editBtn = document.createElement('button');
        editBtn.innerText = 'Edit';
        editBtn.className = 'editBtn';
        editBtn.addEventListener('click', function() {
            const newTaskText = prompt('Edit task', taskText);
            if (newTaskText !== null) {
                taskItem.innerText = newTaskText;
                // Update task in local storage
                const index = tasks.indexOf(taskText);
                tasks[index] = newTaskText;
                localStorage.setItem('tasks', JSON.stringify(tasks));
            }
        });

        taskItem.appendChild(deleteBtn);
        taskItem.appendChild(editBtn);

        taskItem.addEventListener('click', function() {
            taskItem.classList.toggle('completed');
        });

        taskList.appendChild(taskItem);
    }

    clearAllBtn.addEventListener('click', function() {
        // Clear all tasks from the task list
        while (taskList.firstChild) {
            taskList.removeChild(taskList.firstChild);
        }
        // Clear tasks from local storage
        tasks.length = 0;
        localStorage.setItem('tasks', JSON.stringify(tasks));
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    addTaskBtn.addEventListener('click', function() {
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            const taskItem = document.createElement('li');
            taskItem.innerText = taskText;

            taskItem.addEventListener('click', function() {
                taskItem.classList.toggle('completed');
            });

            taskList.appendChild(taskItem);
            taskInput.value = '';
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');
    const dateTimeDisplay = document.getElementById('dateTimeDisplay'); // Assuming you have an element with id 'dateTimeDisplay'

    addTaskBtn.addEventListener('click', function() {
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            const taskItem = document.createElement('li');
            taskItem.innerText = taskText;

            const dateTime = new Date();
            const dateTimeText = dateTime.toLocaleString(); // Convert the date and time to a string
            taskItem.innerText += ' (' + dateTimeText + ')'; // Append the date and time to the task text

            taskList.appendChild(taskItem);
            taskInput.value = '';
        }
    });

    // Update the date and time display every second
    setInterval(function() {
        const dateTime = new Date();
        dateTimeDisplay.innerText = dateTime.toLocaleString();
    }, 1000);
});


document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput'); // New search input field
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    addTaskBtn.addEventListener('click', function() {
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            const taskItem = document.createElement('li');
            taskItem.innerText = taskText;
            taskList.appendChild(taskItem);
            taskInput.value = '';
        }
    });

    searchInput.addEventListener('input', function() { // New input event listener
        const searchTerm = searchInput.value.trim().toLowerCase();
        const tasks = taskList.getElementsByTagName('li');
        for (let i = 0; i < tasks.length; i++) {
            const taskText = tasks[i].innerText.toLowerCase();
            tasks[i].style.display = taskText.includes(searchTerm) ? '' : 'none';
        }
    });
});