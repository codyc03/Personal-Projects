from email.policy import default
import tkinter as tk
from tkinter import ANCHOR, CENTER, NSEW, ttk
from turtle import bgcolor
import Main as db

def on_resize(event):
    # Update the size of the root window when resized
    root.grid_rowconfigure(0, weight=6)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=12)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=12)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=12)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)
    

def exit_program(event=None):
    root.destroy()

def get_all_in_category(category) :
    all_in_category = db.get_reminders(category, "user_entries")
    all_category_string = "\n".join(str(entry) for entry in all_in_category)
    return all_category_string


def update_previous_entries() :
    date_label = ttk.Label(results_frame,text="DATE", anchor="center")
    date_label.grid(row=0,column=0, sticky='nsew')
    
    mood_label = ttk.Label(results_frame,text="MOOD", anchor="center")
    mood_label.grid(row=0,column=1, sticky='nsew')
    
    energy_level_label = ttk.Label(results_frame,text="ENERGY LEVEL", anchor="center")
    energy_level_label.grid(row=0,column=2, sticky='nsew')
    
    sleep_duration_label = ttk.Label(results_frame,text="SLEEP DURATION", anchor="center")
    sleep_duration_label.grid(row=0,column=3, sticky='nsew')
    
    sleep_quality_label = ttk.Label(results_frame,text="SLEEP QUALITY", anchor="center")
    sleep_quality_label.grid(row=0,column=4, sticky='nsew')

    physical_symptoms_label = ttk.Label(results_frame,text="PHYSICAL SYMPTOMS", anchor="center")
    physical_symptoms_label.grid(row=0,column=5, sticky='nsew')
    
    social_interaction_label = ttk.Label(results_frame,text="SOCIAL INTERACTION", anchor="center")
    social_interaction_label.grid(row=0,column=6, sticky='nsew')

    physical_activity_label = ttk.Label(results_frame,text="PHYSICAL ACTIVITY", anchor="center")
    physical_activity_label.grid(row=0,column=7, sticky='nsew')
    
    test = get_all_in_category("entry_date")

    last_10_entries_dates = ttk.Label(results_frame, text = get_all_in_category("entry_date"), anchor='center')
    last_10_entries_dates.grid(row=1,column=0, sticky = 'n')
    
    last_10_entries_moods = ttk.Label(results_frame, text = get_all_in_category("mood"), anchor='center')
    last_10_entries_moods.grid(row=1,column=1, sticky = 'n')
    
    last_10_entries_energy_levels = ttk.Label(results_frame, text = get_all_in_category("energy_level"), anchor='center')
    last_10_entries_energy_levels.grid(row=1,column=2, sticky = 'n')

    last_10_entries_sleep_durations = ttk.Label(results_frame, text = get_all_in_category("sleep_duration"), anchor='center')
    last_10_entries_sleep_durations.grid(row=1,column=3, sticky = 'n')
    
    last_10_entries_sleep_qualities = ttk.Label(results_frame, text = get_all_in_category("sleep_quality"), anchor='center')
    last_10_entries_sleep_qualities.grid(row=1,column=4, sticky = 'n')
    
    last_10_entries_physical_symptoms = ttk.Label(results_frame, text = get_all_in_category("physical_symptoms"), anchor='center')
    last_10_entries_physical_symptoms.grid(row=1,column=5, sticky = 'n')
    
    last_10_entries_social_interactions = ttk.Label(results_frame, text = get_all_in_category("social_interaction"), anchor='center')
    last_10_entries_social_interactions.grid(row=1,column=6, sticky = 'n')
    
    last_10_entries_physical_activities = ttk.Label(results_frame, text = get_all_in_category("physical_activity"), anchor='center')
    last_10_entries_physical_activities.grid(row=1,column=7, sticky = 'n')
    
    
def update_output(output_widgets, all_outputs, default_output):
    num_outputs = len(all_outputs)
    progress = 0
    
    for i in range(min(num_outputs, 3)) :
         progress = i + 1
         output_text = f"{i+1}. {all_outputs[i]}"
        
         if i == 0:
             output_widgets[i].config(text=output_text, font=("Arial", 12))
         elif i == 1:
             output_widgets[i].config(text=output_text, font=("Arial", 12))
         elif i == 2:
             output_widgets[i].config(text=output_text, font=("Arial", 12))
       
    for i in range(progress,3) :
         if i == 0:
             output_widgets[i].config(text=default_output, font=("Arial", 12))
         elif i == 1:
             output_widgets[i].config(text=default_output, font=("Arial", 12))
         elif i == 2:
             output_widgets[i].config(text=default_output, font=("Arial", 12))

def startup() :
    all_goals = db.get_reminders("goal","goals_new")
    default_goal = "Please Add Goal"
    goals_output_widgets = [goals_output_1, goals_output_2, goals_output_3]
    update_output(goals_output_widgets, all_goals, default_goal)

    all_accomplishments = db.get_reminders("accomplishment", "accomplishments_new")
    default_accomplishment = "Please Add Accomplishment"
    accomplishments_output_widgets = [accomplishments_output_1, accomplishments_output_2, accomplishments_output_3]
    update_output(accomplishments_output_widgets, all_accomplishments, default_accomplishment)

    all_coping_strategies = db.get_reminders("coping_strategy", "coping_strategies_new")
    default_coping_strategy = "Please Add Coping Strategy"
    coping_strategys_output_widgets = [coping_strategies_output_1, coping_strategies_output_2, coping_strategies_output_3]
    update_output(coping_strategys_output_widgets, all_coping_strategies, default_coping_strategy)
    
    all_gratitudes = db.get_reminders("gratitude", "gratitudes_new")
    default_gratitude = "Please Add Gratitude"
    gratitudes_output_widgets = [gratitudes_output_1, gratitudes_output_2, gratitudes_output_3]
    update_output(gratitudes_output_widgets, all_gratitudes, default_gratitude)

    all_reflections = db.get_reminders("reflection", "reflections_new")
    default_reflection = "Please Add reflection"
    reflections_output_widgets = [reflections_output_1, reflections_output_2, reflections_output_3]
    update_output(reflections_output_widgets, all_reflections, default_reflection)

    all_self_care_activities = db.get_reminders("self_care_activity", "self_care_activities_new")
    default_self_care_activity = "Please Add Self Care Activity"
    self_care_activitys_output_widgets = [self_care_activities_output_1, self_care_activities_output_2, self_care_activities_output_3]
    update_output(self_care_activitys_output_widgets, all_self_care_activities, default_self_care_activity)

    update_previous_entries()

def clicked() :
    mood = user_entry_mood.get()
    energy_level = user_entry_energy.get()
    sleep_duration = user_entry_sleep.get()
    sleep_quality = user_entry_sleep_quality.get()
    physical_symptoms = user_entry_physical_symptoms.get()
    social_interaction = user_entry_social_interaction.get()
    physical_activity = user_entry_physical_activity.get()
    db.add_entry(mood,energy_level,sleep_duration,sleep_quality,physical_symptoms,social_interaction,physical_activity)

    update_previous_entries()
 
root = tk.Tk()
root.title("Main Window")

# Set the window attributes to fullscreen
root.attributes("-fullscreen", True)

# Bind the resize event to the on_resize function
root.bind("<Configure>", on_resize)

# Bind the Escape key to exit the program
root.bind("<Escape>", exit_program)

greeting = ttk.Label(root, text="Hello, welcome to MyHealth!", font=("Arial", 20, "bold"),anchor="center")
greeting.grid(row=0, column=1, sticky='nsew')

button = ttk.Button(root, text="Add Daily Entry", command = clicked)
button.grid(row=5, column=1, sticky = 'ns')

goals_header = ttk.Label(root, text = "Goals", anchor= "center", font=("Arial", 14, "bold"))
goals_header.grid(row=1, column=0, sticky= NSEW)

goals_label = ttk.Labelframe(root)
goals_label.grid(row=2, column=0, sticky='nsew')

goals_label.grid_columnconfigure(0,weight=1)
goals_label.grid_rowconfigure(0,weight=1)
goals_label.grid_rowconfigure(1,weight=1)
goals_label.grid_rowconfigure(2,weight=1)

goals_output_1 = ttk.Label(goals_label, text="First goal", anchor=CENTER)
goals_output_1.grid(row=0, column=0, sticky = 'nsew')

goals_output_2 = ttk.Label(goals_label, text="Second goal", anchor=CENTER)
goals_output_2.grid(row=1, column=0,sticky='nsew')

goals_output_3 = ttk.Label(goals_label, text="Third goal", anchor=CENTER)
goals_output_3.grid(row=2, column=0, sticky='nsew')

accomplishments_header = ttk.Label(root, text = "Accomplishments", anchor= "center", font=("Arial", 14, "bold"))
accomplishments_header.grid(row=3, column=0, sticky= NSEW)

accomplishments_label = ttk.Labelframe(root)
accomplishments_label.grid(row=4, column=0, sticky='nsew')

accomplishments_label.grid_columnconfigure(0,weight=1)
accomplishments_label.grid_rowconfigure(0,weight=1)
accomplishments_label.grid_rowconfigure(1,weight=1)
accomplishments_label.grid_rowconfigure(2,weight=1)

accomplishments_output_1 = ttk.Label(accomplishments_label, text="First accomplishment", anchor=CENTER)
accomplishments_output_1.grid(row=0, column=0)

accomplishments_output_2 = ttk.Label(accomplishments_label, text="Second accomplishment", anchor=CENTER)
accomplishments_output_2.grid(row=1, column=0)

accomplishments_output_3 = ttk.Label(accomplishments_label, text="Third accomplishment", anchor=CENTER)
accomplishments_output_3.grid(row=2, column=0)

coping_strategies_header = ttk.Label(root, text = "Coping Strategies", anchor= "center", font=("Arial", 14, "bold"))
coping_strategies_header.grid(row=5, column=0, sticky= NSEW)

coping_strategies_label = ttk.Labelframe(root)
coping_strategies_label.grid(row=6, column=0, sticky='nsew')

coping_strategies_label.grid_columnconfigure(0,weight=1)
coping_strategies_label.grid_rowconfigure(0,weight=1)
coping_strategies_label.grid_rowconfigure(1,weight=1)
coping_strategies_label.grid_rowconfigure(2,weight=1)

coping_strategies_output_1 = ttk.Label(coping_strategies_label, text="First coping strategy", anchor=CENTER)
coping_strategies_output_1.grid(row=0, column=0)

coping_strategies_output_2 = ttk.Label(coping_strategies_label, text="Second coping strategy", anchor=CENTER)
coping_strategies_output_2.grid(row=1, column=0)

coping_strategies_output_3 = ttk.Label(coping_strategies_label, text="Third coping strategy", anchor=CENTER)
coping_strategies_output_3.grid(row=2, column=0)

gratitudes_header = ttk.Label(root, text = "Gratitudes", anchor= "center", font=("Arial", 14, "bold"))
gratitudes_header.grid(row=1, column=2, sticky= NSEW)

gratitudes_label = ttk.Labelframe(root)
gratitudes_label.grid(row=2, column=2, sticky='nsew')

gratitudes_label.grid_columnconfigure(0,weight=1)
gratitudes_label.grid_rowconfigure(0,weight=1)
gratitudes_label.grid_rowconfigure(1,weight=1)
gratitudes_label.grid_rowconfigure(2,weight=1)

gratitudes_output_1 = ttk.Label(gratitudes_label, text="First gratitude", anchor=CENTER)
gratitudes_output_1.grid(row=0, column=0)

gratitudes_output_2 = ttk.Label(gratitudes_label, text="Second gratitude", anchor=CENTER)
gratitudes_output_2.grid(row=1, column=0)

gratitudes_output_3 = ttk.Label(gratitudes_label, text="Third gratitude", anchor=CENTER)
gratitudes_output_3.grid(row=2, column=0)

reflections_header = ttk.Label(root, text = "Reflections", anchor= "center", font=("Arial", 14, "bold"))
reflections_header.grid(row=3, column=2)

reflections_label = ttk.Labelframe(root)
reflections_label.grid(row=4, column=2, sticky='nsew')

reflections_label.grid_columnconfigure(0,weight=1)
reflections_label.grid_rowconfigure(0,weight=1)
reflections_label.grid_rowconfigure(1,weight=1)
reflections_label.grid_rowconfigure(2,weight=1)

reflections_output_1 = ttk.Label(reflections_label, text="First reflection", anchor=CENTER)
reflections_output_1.grid(row=0, column=0)

reflections_output_2 = ttk.Label(reflections_label, text="Second reflection", anchor=CENTER)
reflections_output_2.grid(row=1, column=0)

reflections_output_3 = ttk.Label(reflections_label, text="Third reflection", anchor=CENTER)
reflections_output_3.grid(row=2, column=0)

self_care_activities_header = ttk.Label(root, text = "Self Care Activities", anchor= "center", font=("Arial", 14, "bold"))
self_care_activities_header.grid(row=5, column=2, sticky= NSEW)

self_care_activities_label = ttk.Labelframe(root)
self_care_activities_label.grid(row=6, column=2, sticky='nsew')

self_care_activities_label.grid_columnconfigure(0,weight=1)
self_care_activities_label.grid_rowconfigure(0,weight=1)
self_care_activities_label.grid_rowconfigure(1,weight=1)
self_care_activities_label.grid_rowconfigure(2,weight=1)

self_care_activities_output_1 = ttk.Label(self_care_activities_label, text="First self-care activity", anchor=CENTER)
self_care_activities_output_1.grid(row=0, column=0)

self_care_activities_output_2 = ttk.Label(self_care_activities_label, text="Second self-care activity", anchor=CENTER)
self_care_activities_output_2.grid(row=1, column=0)

self_care_activities_output_3 = ttk.Label(self_care_activities_label, text="Third self-care activity", anchor=CENTER)
self_care_activities_output_3.grid(row=2, column=0)

# Create a frame
user_entry_frame = ttk.Frame(root)
user_entry_frame.grid(row=2, column=1, rowspan=3, sticky="nsew")

# Configure grid weights for the frame
user_entry_frame.grid_columnconfigure(0, weight=1)
user_entry_frame.grid_columnconfigure(1, weight=1)

user_entry_frame.grid_rowconfigure(0, weight=1)
user_entry_frame.grid_rowconfigure(1, weight=1)
user_entry_frame.grid_rowconfigure(2, weight=1)
user_entry_frame.grid_rowconfigure(3, weight=1)
user_entry_frame.grid_rowconfigure(4, weight=1)
user_entry_frame.grid_rowconfigure(5, weight=1)
user_entry_frame.grid_rowconfigure(6, weight=1)
user_entry_frame.grid_rowconfigure(7, weight=1)


# Create a label inside the frame
user_entry_label1 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how was your mood today?", anchor="center", background="blue", foreground="white")
user_entry_label2 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how was your energy level today?", anchor="center", background="yellow", foreground="white")
user_entry_label3 = ttk.Label(user_entry_frame, text="How long did you sleep for?", anchor="center", background="green", foreground="white")
user_entry_label4 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how was your sleep quality?", anchor="center", background="red", foreground="white")
user_entry_label5 = ttk.Label(user_entry_frame, text="On a scale of 1-10, how would you rate your physical symptoms today?", anchor="center", background="black", foreground="white")
user_entry_label6 = ttk.Label(user_entry_frame, text="How many hours of social interaction did you have today?", anchor="center", background="yellow", foreground="white")
user_entry_label7 = ttk.Label(user_entry_frame, text="How many hours of physical activity did you have today?", anchor="center", background="blue", foreground="white")

user_entry_mood = ttk.Entry(user_entry_frame, background="blue")
user_entry_energy = ttk.Entry(user_entry_frame, background="blue")
user_entry_sleep = ttk.Entry(user_entry_frame, background="blue")
user_entry_sleep_quality = ttk.Entry(user_entry_frame, background="blue")
user_entry_physical_symptoms = ttk.Entry(user_entry_frame, background="blue")
user_entry_social_interaction = ttk.Entry(user_entry_frame, background="blue")
user_entry_physical_activity = ttk.Entry(user_entry_frame, background="yellow")

# Configure grid weights for the label
user_entry_label1.grid(row=0, column=0, sticky='nsew')
user_entry_label2.grid(row=1,column=0, sticky='nsew')
user_entry_label3.grid(row=2, column=0, sticky='nsew')
user_entry_label4.grid(row=3,column=0, sticky='nsew')
user_entry_label5.grid(row=4, column=0, sticky='nsew')
user_entry_label6.grid(row=5,column=0, sticky='nsew')
user_entry_label7.grid(row=6, column=0, sticky='nsew')

user_entry_mood.grid(row=0, column=1, sticky='nsew')
user_entry_energy.grid(row=1,column=1, sticky='nsew')
user_entry_sleep.grid(row=2, column=1, sticky='nsew')
user_entry_sleep_quality.grid(row=3,column=1, sticky='nsew')
user_entry_physical_symptoms.grid(row=4, column=1, sticky='nsew')
user_entry_social_interaction.grid(row=5,column=1, sticky='nsew')
user_entry_physical_activity.grid(row=6, column=1, sticky='nsew')

# Create a frame
results_frame = ttk.Frame(root)
results_frame.grid(row=6, column=1, rowspan=2, sticky="nsew")

# Configure grid weights for the frame
results_frame.grid_columnconfigure(0, weight=1)
results_frame.grid_columnconfigure(1, weight=1)
results_frame.grid_columnconfigure(2, weight=1)
results_frame.grid_columnconfigure(3, weight=1)
results_frame.grid_columnconfigure(4, weight=1)
results_frame.grid_columnconfigure(5, weight=1)
results_frame.grid_columnconfigure(6, weight=1)
results_frame.grid_columnconfigure(7, weight=1)

results_frame.grid_rowconfigure(0, weight=1)
results_frame.grid_rowconfigure(1, weight=3)


# # Create a label inside the frame
# test_label = ttk.Label(results_frame, text="hello", background="green", foreground="white")

# # Configure grid weights for the label
# test_label.grid(row=0, column=0, sticky="nsew")

startup()

root.mainloop()
