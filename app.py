import gradio as gr
import requests

url = "https://api.newnative.ai/stable-diffusion?prompt="

def run(gender, ethnicity, skin_color, hair_length, hair_color, eye_color, piercings):
    prompt = f"""mugshot portrait, {ethnicity} {skin_color} {gender} with {hair_length} {hair_color} hair, {eye_color} eyes, {" piercing, ".join([*piercings, ""]) if piercings else ""}"""
    # return f"""The {quantity} {animal}s went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}"""
    return getImage(prompt)

def getImage(prompt):
    r = requests.get(url + prompt)
    # response = requests.request("GET", url+prompt)
    data = r.json()
    return(data["image_url"])

demo = gr.Interface(
    run,
    [
        gr.Radio(["Male", "Female"], label="Gender" ),
        gr.Dropdown(["South Asian", "North Asian", "White", "African American", "African", "American Indian", "Hispanic"], label="Ethnicity"),
        gr.Dropdown(["Black", "Brown", "Yellow", "Peach","Tan","Beige", "White", "Grey"], label="Skin color" ),
        gr.Radio(["Short", "Long"], label="Hair length" ),
        gr.Dropdown(["Black","Dark brown", "Light brown", "Blonde", "Red", "Grey", "Blue", "Pink"], label="Hair color" ),
        gr.Dropdown(["Black", "Dark Brown", "Light Brown", "Green", "Blue", "Hazel", "Amber", "Red", "Pink"], label="Eye color" ),
        gr.CheckboxGroup(["Nose", "Ear", "Eyebrow", "Lips", "Cheeks"], label="Piercings"),
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
