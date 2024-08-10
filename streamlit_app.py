import streamlit as st
import random
from PIL import Image
import pandas as pd

# Define image, word, sentence, and audio data for English
english_data = {
    "apple.jpg": {"word": "apple", "sentence": "I like to eat apples.", "audio": "apple.mp3", "sentence_audio": "apple_sentence.mp3"},
    "ball.jpg": {"word": "ball", "sentence": "The children are playing with a ball.", "audio": "ball.mp3", "sentence_audio": "ball_sentence.mp3"},
    "cat.jpg": {"word": "cat", "sentence": "The cat is sleeping.", "audio": "cat.mp3", "sentence_audio": "cat_sentence.mp3"},
    "dog.jpg": {"word": "dog", "sentence": "The dog is chasing its tail.", "audio": "dog.mp3", "sentence_audio": "dog_sentence.mp3"},
    "frog.jpg": {"word": "frog", "sentence": "The frog is sitting on a leaf.", "audio": "frog.mp3", "sentence_audio": "frog_sentence.mp3"},
    "bird.jpg": {"word": "bird", "sentence": "The bird is singing in the tree.", "audio": "bird.mp3", "sentence_audio": "bird_sentence.mp3"},
    "bus.jpg": {"word": "bus", "sentence": "The bus is waiting at the stop.", "audio": "bus.mp3", "sentence_audio": "bus_sentence.mp3"},
    "car.jpg": {"word": "car", "sentence": "The car is parked on the street.", "audio": "car.mp3", "sentence_audio": "car_sentence.mp3"},
    "giraffe.jpg": {"word": "giraffe", "sentence": "The giraffe is eating leaves from a tree.", "audio": "giraffe.mp3", "sentence_audio": "giraffe_sentence.mp3"},
    "elephant.jpg": {"word": "elephant", "sentence": "The elephant is spraying water with its trunk.", "audio": "elephant.mp3", "sentence_audio": "elephant_sentence.mp3"},
    "running.jpg": {"word": "running", "sentence": "The children are running in the park.", "audio": "running.mp3", "sentence_audio": "running_sentence.mp3"},
    "painting.jpg": {"word": "painting", "sentence": "The artist is painting a landscape.", "audio": "painting.mp3", "sentence_audio": "painting_sentence.mp3"},
    "sing.jpg": {"word": "singing", "sentence": "The girl is singing a song.", "audio": "singing.mp3", "sentence_audio": "singing_sentence.mp3"},
    "swimming.jpg": {"word": "swimming", "sentence": "The children are swimming in the pool.", "audio": "swimming.mp3", "sentence_audio": "swimming_sentence.mp3"},
    "taking pictures.jpg": {"word": "taking pictures", "sentence": "The photographer is taking pictures of the landscape.", "audio": "taking_pictures.mp3", "sentence_audio": "taking_pictures_sentence.mp3"},
    "train.jpg": {"word": "train", "sentence": "The train is traveling through the countryside.", "audio": "train.mp3", "sentence_audio": "train_sentence.mp3"},
    "sheep.jpg": {"word": "sheep", "sentence": "The sheep are grazing in the field.", "audio": "sheep.mp3", "sentence_audio": "sheep_sentence.mp3"},
    "tree.jpg": {"word": "tree", "sentence": "The tree is growing tall in the forest.", "audio": "tree.mp3", "sentence_audio": "tree_sentence.mp3"},
    "walking.jpg": {"word": "walking", "sentence": "The family is walking in the park.", "audio": "walking.mp3", "sentence_audio": "walking_sentence.mp3"},
}

math_problems = [
    {"problem": "What is 2 + 3?", "solution": "5", "hint": "Add the numbers together.", "video": "2+3.mp4"},
    {"problem": "What is 2 + 2?", "solution": "4", "hint": "Add the numbers together.", "video": "2+2.mp4"},
    {"problem": "What is 1 + 2?", "solution": "3", "hint": "Add the numbers together.", "video": "1+2.mp4"},
    {"problem": "What is 5 + 3?", "solution": "8", "hint": "Add the numbers together.",  "video": "5+3.mp4"},
    {"problem": "What is 8 - 6?", "solution": "2", "hint": "Start with the larger number and subtract.",  "video": "8-6.mp4"},
    {"problem": "What is 6 - 4?", "solution": "2", "hint": "Start with the larger number and subtract.", "video": "6-4.mp4"},
    {"problem": "What is 6 + 4?", "solution": "10","hint": "Add the numbers together.", "video": "6+4.mp4"},
    {"problem": "What is 4 - 2?", "solution": "2", "hint": "Start with the larger number and subtract.", "video": "4-2.mp4"},
    {"problem": "What is 4 + 2?", "solution": "6","hint": "Add the numbers together.", "video": "4+2.mp4"},
    {"problem": "What is 7 - 4?", "solution": "3", "hint": "Start with the larger number and subtract.", "video": "7-4.mp4"},
]

# Placeholder for merged math problems
merged_math_problems = []
merged_math_problems.extend(math_problems)

# Function to select a random word and its corresponding data
def select_word():
    selected_image = random.choice(list(english_data.keys()))
    selected_data = english_data[selected_image]
    return selected_image, selected_data

# Function to scramble a word
def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return word

# Function to display the learning English application
def learn_english_application():
    st.header("Learn English Application")
    st.write("Match Images, Words, and Sentences")

    # Display images and play corresponding audio
    selected_image = st.selectbox("Select an Image", list(english_data.keys()), format_func=lambda x: english_data[x]["word"])
    selected_word = english_data[selected_image]["word"]
    selected_sentence = english_data[selected_image]["sentence"]
    selected_audio = english_data[selected_image]["audio"]
    selected_sentence_audio = english_data[selected_image]["sentence_audio"]

    st.image(selected_image)
    st.write(f"Word: {selected_word}")
    st.write(f"Sentence: {selected_sentence}")

    # Play corresponding audio
    st.audio(selected_audio, format="audio/mp3", start_time=0)
    st.audio(selected_sentence_audio, format="audio/mp3", start_time=0)

# Function to display the math application
def math_application():
    st.header("Math Application")
    st.write("Solve Math Problems and Learn")

    # Display math problems and play corresponding audio
    selected_problem = st.selectbox("Select a Math Problem", [problem_data["problem"] for problem_data in merged_math_problems])
    selected_solution = [problem_data["solution"] for problem_data in merged_math_problems if problem_data["problem"] == selected_problem][0]
    selected_hint = [problem_data["hint"] for problem_data in merged_math_problems if problem_data["problem"] == selected_problem][0]
    explanation = f"The solution is {selected_solution}."
    video_path = [problem_data["video"] for problem_data in merged_math_problems if problem_data["problem"] == selected_problem][0]

    st.write(f"Problem: {selected_problem}")

    user_answer = st.text_input("Your Answer:")
    if st.button("Submit"):
        if user_answer == selected_solution:
            st.success("Correct!")
        else:
            st.error("Incorrect!")
            st.write(f"Hint: {selected_hint}")
        st.write(f"Explanation: {explanation}")
        st.audio(f"{selected_solution}_solution.mp3", format="audio/mp3", start_time=0)
        st.video(video_path)

# Function to display the color matching game
def color_matching_game():
    st.header("Color Matching Game")
    st.write("Match the colors by entering the correct color name.")

    # Define colors and corresponding hex codes
    colors = {
        "Red": "#FE1E1E",
        "Orange": "#F19111",
        "Yellow": "#F7DE25",
        "Green": "#89D50E",
        "Blue": "#1671AF",
        "Purple": "#8F12CD",
        "Brown": "#822909",
        "White": "#FFFCFC",
        "Black": "#000000",
        "Pink": "#FFB6C1"
    }

    # Create a DataFrame for color names and images
    color_df = pd.DataFrame(colors.items(), columns=["Color Name", "Color Hex"])
    # Shuffle the colors
    color_df = color_df.sample(frac=1).reset_index(drop=True)

    # Initialize session state variables if they don't exist
    if "total_matches" not in st.session_state:
        st.session_state.total_matches = 0
        st.session_state.correct_matches = 0
        st.session_state.color_df = color_df
        st.session_state.feedback = [""] * len(color_df)  # Initialize feedback list with empty strings

    # Ensure feedback list is not None and matches the length of color_df
    if st.session_state.feedback is None or len(st.session_state.feedback) != len(st.session_state.color_df):
        st.session_state.feedback = [""] * len(st.session_state.color_df)

    # Display color images and get user input for color names
    for index, row in st.session_state.color_df.iterrows():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(f"https://via.placeholder.com/100/{row['Color Hex'].replace('#', '')}/000000?text=", width=100)
        with col2:
            user_color = st.text_input(f"Enter color name:", key=f"user_color_{index}")

            if st.button(f"Submit", key=f"submit_{index}"):
                st.session_state.total_matches += 1
                if user_color.lower() == row["Color Name"].lower():
                    st.session_state.correct_matches += 1
                    st.session_state.feedback[index] = "Correct!"
                else:
                    st.session_state.feedback[index] = "Incorrect!"
                st.experimental_rerun()

    # Display matching results
    st.write("Matching Results:")
    st.write(f"Total Matches: {st.session_state.total_matches}")
    st.write(f"Correct Matches: {st.session_state.correct_matches}")

    # Display feedback for each color block
    for index, feedback in enumerate(st.session_state.feedback):
        st.write(f"Block {index+1}: {feedback}")

    # Option to reset game
    if st.button("Reset Game"):
        st.session_state.total_matches = 0
        st.session_state.correct_matches = 0
        st.session_state.color_df = color_df.sample(frac=1).reset_index(drop=True)
        st.session_state.feedback = [""] * len(st.session_state.color_df)  # Reset feedback list
        st.experimental_rerun()

def word_scramble_game():
    st.header("Word Scramble Game")
    st.write("Look at the image and unscramble the word below.")

    # Initialize session_state variables if they don't exist
    if "current_data" not in st.session_state:
        st.session_state.current_image, st.session_state.current_data = select_word()
        st.session_state.scrambled_word = scramble_word(st.session_state.current_data["word"])
        st.session_state.feedback = None
        st.session_state.user_guess = ""  # Initialize user guess
        st.session_state.answers = []  # Initialize answers list

    # Ensure all necessary session_state variables are initialized
    if "user_guess" not in st.session_state:
        st.session_state.user_guess = ""
    if "answers" not in st.session_state:
        st.session_state.answers = []

    original_word = st.session_state.current_data["word"]
    scrambled_word = st.session_state.scrambled_word

    st.image(st.session_state.current_image, caption="Image for reference")
    st.write(f"Scrambled Word: {' '.join(scrambled_word)}")

    user_guess = st.text_input("Unscramble the word:", value=st.session_state.user_guess)

    if st.button("Submit"):
        if user_guess.lower() == original_word.lower():
            st.session_state.feedback = "Correct! Well done!"
            st.session_state.answers.append({"word": original_word, "guess": user_guess, "correct": True})
        else:
            st.session_state.feedback = "Incorrect! Try again."
            st.session_state.answers.append({"word": original_word, "guess": user_guess, "correct": False})
        st.session_state.user_guess = user_guess  # Save user guess
        st.experimental_rerun()

    if st.session_state.feedback:
        st.write(st.session_state.feedback)
        if st.button("Next"):
            st.session_state.current_image, st.session_state.current_data = select_word()
            st.session_state.scrambled_word = scramble_word(st.session_state.current_data["word"])
            st.session_state.feedback = None
            st.session_state.user_guess = ""  # Clear previous user guess
            st.experimental_rerun()

    # Option to view collected data
    if st.button("View Data"):
        st.write("Collected Data:")
        st.write(pd.DataFrame(st.session_state.answers))

    # Option to reset game
    if st.button("Reset Game"):
        st.session_state.current_image, st.session_state.current_data = select_word()
        st.session_state.scrambled_word = scramble_word(st.session_state.current_data["word"])
        st.session_state.feedback = None
        st.session_state.user_guess = ""  # Clear previous user guess
        st.session_state.answers = []  # Clear collected data
        st.experimental_rerun()


# Main application logic
def main():
    st.title('Preschoolers\' STEM Tasks and English Learning')

    # Add a sidebar for navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the App Mode", ["Learn English", "Math", "Color Matching", "Word Scramble"])

    if app_mode == "Learn English":
        learn_english_application()
    elif app_mode == "Math":
        math_application()
    elif app_mode == "Color Matching":
        color_matching_game()
    elif app_mode == "Word Scramble":
        word_scramble_game()

# Run the main function
if __name__ == "__main__":
    main()
