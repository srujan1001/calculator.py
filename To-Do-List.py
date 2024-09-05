import tkinter as tk
from datetime import datetime

tasks = []  # List to store the details of tasks

def add_task():
    # Function to add a new task to the list
    task_name = task_name_entry.get()
    description = description_entry.get()
    due_date = due_date_entry.get()

    # Convert the due date string to a datetime object for better handling
    due_date_obj = datetime.strptime(due_date, "%d/%m/%Y")

    # Create a formatted string with task details and add it to the tasks list
    task_details = f"{task_name: ^40}{description: ^40}{due_date_obj.strftime('%d/%m/%Y'): ^20}"
    tasks.append(task_details)
    tasks.sort(key=lambda x: datetime.strptime(x.split()[-1], '%d/%m/%Y'))  # Sort tasks based on due dates

    # Update the task list display and clear the input fields
    update_task_list()
    task_name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

def update_task_list():
    # Function to update the task list display in the GUI
    task_list_text.delete(0, tk.END)  # Clear the existing task list display

    # Insert each task with its index number into the task_list_text widget
    for i, task in enumerate(tasks, 1):
        task_list_text.insert(tk.END, f"{i}. {task}\n")

def delete_selected_task():
    # Function to delete the selected task from the tasks list
    selected_indices = task_list_text.curselection()
    if selected_indices:
        selected_indices = sorted(map(int, selected_indices), reverse=True)
        for index in selected_indices:
            if 0 <= index < len(tasks):
                del tasks[index]

        update_task_list()

def edit_selected_task():
    # Function to edit the selected task in the tasks list
    selected_index = task_list_text.curselection()
    if selected_index:
        index = int(selected_index[0])
        if 0 <= index < len(tasks):
            # Open a new window for editing the task details
            edit_window = tk.Toplevel(root)
            edit_window.title("Edit Task")

            # Get the details of the selected task
            task = tasks[index].split()
            task_name = task[0]
            description = task[1]
            due_date = task[2]

            def save_edited_task():
            # Function to save the edited task details and update the list
                new_due_date = due_date_entry.get()
    
                edited_task_details = f"{task_name_entry.get(): ^40}{description_entry.get(): ^40}{new_due_date: ^20}"
                tasks[index] = edited_task_details
                tasks.sort(key=lambda x: datetime.strptime(x.split()[-1], '%d/%m/%Y'))
                update_task_list()
                edit_window.destroy()


    # Create entry widgets to edit the task details
    font_style = ("Arial", 14)

    task_name_label = tk.Label(edit_window, text="Task Name:", font=font_style)
    task_name_label.grid(row=0, column=0, padx=5, pady=5)
    task_name_var = tk.StringVar()  # Create a StringVar for task name
    task_name_entry = tk.Entry(edit_window, font=font_style, textvariable=task_name_var)
    task_name_entry.grid(row=0, column=1, padx=5, pady=5)
    task_name_var.set(task_name)  # Set the initial value

    description_label = tk.Label(edit_window, text="Description:", font=font_style)
    description_label.grid(row=1, column=0, padx=5, pady=5)
    description_var = tk.StringVar()  # Create a StringVar for description
    description_entry = tk.Entry(edit_window, font=font_style, textvariable=description_var)
    description_entry.grid(row=1, column=1, padx=5, pady=5)
    description_var.set(description)  # Set the initial value

    due_date_label = tk.Label(edit_window, text="Due Date:", font=font_style)
    due_date_label.grid(row=2, column=0, padx=5, pady=5)
    due_date_entry = tk.Entry(edit_window, font=font_style)
    due_date_entry.grid(row=2, column=1, padx=5, pady=5)
    due_date_entry.insert(0, due_date)

    save_button = tk.Button(edit_window, text="Save", command=save_edited_task, font=font_style)
    save_button.grid(row=3, columnspan=2, padx=5, pady=5)

def deselect_task(event):
    # Function to clear the selection when clicking on the task list
    task_list_text.selection_clear(0, tk.END)

def create_task_frame(root):
     # Function to create the main GUI frame for task management
    global task_name_entry, description_entry, due_date_entry, task_list_text

    frame = tk.Frame(root, bg="#E0E0E0")
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Create input fields for adding a new task
    font_style = ("Comic Sans MS", 14)

    task_name_label = tk.Label(frame, text="Task Name:", bg="#E0E0E0", font=font_style)
    task_name_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    task_name_entry = tk.Entry(frame, font=font_style)
    task_name_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky='w')
    task_name_entry.config(width=40)

    description_label = tk.Label(frame, text="Description:", bg="#E0E0E0", font=font_style)
    description_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

    description_entry = tk.Entry(frame, font=font_style)
    description_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky='w')
    description_entry.config(width=40)

    due_date_label = tk.Label(frame, text="Due Date:", bg="#E0E0E0", font=font_style)
    due_date_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

    due_date_entry = tk.Entry(frame, font=font_style)
    due_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    due_date_entry.config(width=20)

    # Add button to create a new task
    add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#60BD4F", font=font_style)
    add_button.grid(row=0, column=3, padx=5, pady=5, sticky='e', rowspan=3)

    # Create a listbox to display the tasks and bind events for editing and deselecting
    task_list_text = tk.Listbox(frame, bg="#F0F0F0", selectbackground="#E6E6E6", selectforeground="#000000",
                                width=100, height=15, font=font_style)
    task_list_text.grid(row=3, columnspan=4, padx=5, pady=5, sticky='w')

    task_list_text.bind("<Double-Button-1>", lambda event: edit_selected_task())
    task_list_text.bind("<Button-1>", deselect_task)

    # Add buttons for deleting and editing tasks
    delete_button = tk.Button(frame, text="Delete Task", command=delete_selected_task, bg="#FF0000", font=font_style)
    delete_button.grid(row=4, column=1, padx=5, pady=5, sticky='e')

    edit_button = tk.Button(frame, text="Edit Task", command=edit_selected_task, bg="#FFA500", font=font_style)
    edit_button.grid(row=4, column=2, padx=5, pady=5, sticky='w')

if __name__ == "__main__":
    # Main program to create the root window and start the main loop
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("1300x650")
    root.config(bg="#E0E0E0")

    create_task_frame(root)

    root.mainloop()
