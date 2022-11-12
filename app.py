import gradio as gr

def sentence_builder(quantity, animal, place, activity_list, morning):
    return f"""The {quantity} {animal}s went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}"""

demo = gr.Interface(
    sentence_builder,
    [
        gr.Radio(["park", "zoo", "road"], label="Gender" ),
        gr.Dropdown(["South Asian, North Asian, White, African American, African, American Indian, Hispanic"], label="Ethnicity"),
        gr.Dropdown(["Black", "Brown", "Yellow", "Peach","Tan","Beige", "White", "Grey"], label="Skin color" ),
        gr.Dropdown(["Black","Dark brown", "Light", "brown", "Blonde", "Red", "Grey", "Blue", "Pink"], label="Hair color" ),
        gr.Dropdown(["Black", "Dark Brown", "Light Brown", "Green", "Blue", "Hazel", "Amber", "Red", "Pink"], label="Eye color" ),
        gr.CheckboxGroup(["Nose", "Ear", "Eyebrow", "Tongue", "Lips", "Cheeks"], label="Piercings"),
        gr.Checkbox(label="Is it the morning?"),
    ],
    "text",
    examples=[
        [2, "cat", "park", ["ran", "swam"], True],
        [4, "dog", "zoo", ["ate", "swam"], False],
        [10, "bird", "road", ["ran"], False],
        [8, "cat", "zoo", ["ate"], True],
    ],
)

if __name__ == "__main__":
    demo.launch()
