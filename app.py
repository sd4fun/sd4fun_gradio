import gradio as gr
import requests

url = "https://api.newnative.ai/stable-diffusion?prompt="

def run(gender, height, weight, age, ethnicity, skin_color, hair_length, hair_color, eye_color, facial_hair, facial_hair_color):
    prompt = f"""mugshot portrait, {ethnicity} {skin_color} {gender} with {hair_length} {hair_color} hair, {eye_color} eyes, {facial_hair} {facial_hair_color} facial hair, {age} years old, {getHeightInFeet(height)} tall, {getWeightInPounds(weight)}"""
    
    # prompt = f"""mugshot portrait, {ethnicity} {skin_color} {gender} with {hair_length} {hair_color} hair, {eye_color} eyes, {" piercing, ".join([*piercings, ""]) if piercings else ""}"""
    # return f"""The {quantity} {animal}s went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}"""
    print (prompt)
    return getImage(prompt)

def getHeightInFeet(height):
    feet = height*0.0328084
    inches = (feet - int(feet))*0.393701
    return str(int(feet)) + "'" + str(int(inches)) + '"'

def getWeightInPounds(weight):
    return str(int(weight*2.20462)) + " lbs"
    
def getImage(prompt):
    r = requests.get(url + prompt)
    data = r.json()
    return(data["image_url"])

demo = gr.Interface(
    run,
    [
        gr.Radio(["Male", "Female"], label="Gender" ),  #Gender
        gr.Slider(100,250,value=160, label="Height (cm)"), #Height
        gr.Slider(40,250,value=50, label="Weight (kg)"), #Weight
        gr.Radio(sorted(["Young", "Adult", "Middle-aged", "Old"]), label="Age" ), #Age
        gr.Dropdown(sorted(["South Asian", "North Asian", "White", "African American", "African", "American Indian", "Hispanic"]), label="Ethnicity"), #Ethnicity
        gr.Dropdown(sorted(["Black", "Brown", "Yellow", "Peach","Tan","Beige", "White", "Grey"]), label="Skin color" ), #Skin color
        gr.Radio(sorted(["Short", "Long", "Bald", "Medium"]), label="Hair length" ), #Hair length
        gr.Dropdown(sorted(["Black","Dark brown", "Light brown", "Blonde", "Red", "Grey"]), label="Hair color" ), #Hair color
        gr.Dropdown(sorted(["Black", "Dark Brown", "Light Brown", "Green", "Blue", "Hazel", "Amber", "Red", "Pink"]), label="Eye color" ), #Eye color
        gr.Radio(sorted(["Mustache", "Beard", "Unibrow"]), label="Facial hair" ), #Facial hair
        gr.Dropdown(sorted(["Ginger", "Black", "Brown", "Grey", "Yellow", "White"]), label="Facial hair color" ), #facial hair color
        # gr.CheckboxGroup(["Nose", "Ear", "Eyebrow", "Lips", "Cheeks"], label="Piercings"),
        #gr.Checkbox(label="Is it the morning?"),
    ],
    "image",
    # examples=[
    #     [2, "cat", "park", ["ran", "swam"], True],
    #     [4, "dog", "zoo", ["ate", "swam"], False],
    #     [10, "bird", "road", ["ran"], False],
    #     [8, "cat", "zoo", ["ate"], True],
    # ],
)

if __name__ == "__main__":
    demo.launch()
