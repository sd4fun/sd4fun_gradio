import gradio as gr
import requests

url = "https://api.newnative.ai/stable-diffusion?prompt="

def run(gender, height, weight, age, ethnicity, skin_color, hair_length, hair_color, eye_color, facial_hair, facial_hair_color):
    bmi = weight/(height/100)**2

    if bmi < 18.5:
        bodyShape = "slim"
    elif bmi < 25:
        bodyShape = "average" 
    elif bmi < 30:
        bodyShape = "overweight"
    else:
        bodyShape = "obese"

    prompt = f"""mugshot portrait, {age + " " if age else ""}{bodyShape} {skin_color} {ethnicity} {gender}{" with " + hair_length if hair_length else ""} {hair_color + " hair, " if hair_length and hair_color else ""}{eye_color + " eyes, " if eye_color else ""}{facial_hair_color + " " if facial_hair and facial_hair_color else ""}{facial_hair+ ", " if facial_hair else ""}canon EOS"""
    
    print (prompt.lower())
    return getImage(prompt.lower())

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
    fn = run,
    article = "<p>For better accuracy, please enter all the information about the person you want to generate a portrait for.</p><h3>Biases and content acknowledgment</h3><p>Beware to the fact that this is a pre-trained model that may output content that reinforces or exacerbates societal biases, as well as realistic faces, pornography and violence. The model was trained on the LAION-5B dataset, which scraped non-curated image-text-pairs from the internet (the exception being the removal of illegal content) and is meant for research purposes.</p><p>You can read more in the model card <a href=\"https://huggingface.co/CompVis/stable-diffusion-v1-4\" target=\"_blank\">HERE.</a></p>"
        ,
    inputs = [
        
        gr.Radio(["Male", "Female"], label="Gender" ),  #Gender
        gr.Slider(100,250,value=160, label="Height (cm)"), #Height
        gr.Slider(40,250,value=50, label="Weight (kg)"), #Weight
        gr.Radio(["Young", "Adult", "Middle-aged", "Old"], label="Age" ), #Age
        gr.Dropdown(sorted(["South Asian", "North Asian", "White", "African American", "American Indian", "Hispanic", "Latin"]), label="Race"), #Race
        gr.Dropdown(sorted(["Black", "Brown", "Yellow", "Peach","Tan","Beige", "White", "Grey"]), label="Skin color" ), #Skin color
        gr.Radio(sorted(["Short", "Long", "Bald", "Medium"]), label="Hair length" ), #Hair length
        gr.Dropdown(sorted(["Black","Dark Brown", "Light Brown", "Blond", "Red", "Grey"]), label="Hair color" ), #Hair color
        gr.Dropdown(sorted(["Black", "Dark Brown", "Light Brown", "Green", "Blue", "Hazel", "Amber", "Red", "Pink"]), label="Eye color" ), #Eye color
        gr.Radio(sorted(["Mustache", "Beard", "Unibrow"]), label="Facial hair" ), #Facial hair
        gr.Dropdown(sorted(["Ginger", "Black", "Brown", "Grey", "Yellow", "White"]), label="Facial hair color" ), #facial hair color
        # gr.CheckboxGroup(["Nose", "Ear", "Eyebrow", "Lips", "Cheeks"], label="Piercings"),
        #gr.Checkbox(label="Is it the morning?"),
    ],
    outputs = "image",
    title = "AI Portrait Generator",
    description = "Generate a portrait of a person with the given attributes",
    examples=[
        ["Male", 180, 80, "Adult", "White", "White", "Short", "Blond", "Blue", "Mustache", "Ginger"],
        ["Male", 160, 50, "Young", "Latin", "Brown", "Medium", "Dark Brown", "Dark Brown", "Beard", "Brown"],
        ["Female", 150, 70, "Old", "South Asian", "White", "Long", "Black", "Light Brown", "Unibrow", "Brown"],
        ["Female", 170, 60, "Middle-aged", "African american", "Black", "Medium", "Black", "Black", None, None],

    

    ],
)

if __name__ == "__main__":
    demo.launch()
