total_hw = 4
original_count = total_hw
print("Today's task #: ", original_count)
completed_count = 0
task_num = 1
next_task = "The first task is Math homework"

while task_num <= total_hw: 
    ans = input(f"Did you finish, {next_task}? Y/N:")
    if task_num == 1:
        next_task = "The next task is English homework."
    elif task_num == 2:
        next_task = "The next task is Science homework."
    elif task_num == 3:
        next_task = "The next task is History homework."
    else:
        next_task = "The next task is Band practice."

    if ans == "Y":
        completed_count += 1
        task_num += 1
        print("Task complete")
    else:
        print("Finish it and come back here after you are done.")

    print("Total hw remaining: ", total_hw - completed_count)
    print()
