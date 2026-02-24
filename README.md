# eduApp
The educational application for preschoolers

eduApp is a lightweight Streamlit-based educational application designed for preschool learners.
It supports vocabulary learning with images + audio, simple math practice, color matching, and a word scramble activity.
This app is used as the tablet interface module in a broader Child–Robot Interaction (CRI) / Robot-Assisted Language Learning (RALL) workflow.

### The application is focused on several skills:
- Using the images (20 of them) for learning English;
- Various number of the Math problems;
- Color matching task;
- Scramble words game to consolidate knowledge of the first part of the application English Vocabulary

## Dependencies

- Python 3.8+
- Streamlit
- Pillow
- Pandas

## To run the application you can follow next steps

### Install Streamlit locally:
(use the docs of streamlit [here](https://pages.github.com/))

    $ pip install streamlit
    $ streamlit hello

After cloning the application and installing all necessary libraries, you can run through the terminal the application:

    $ streamlit run streamlit_app.py

In the browser you'll see this application 
<img width="840" alt="screenshot" src="https://github.com/AnastasiyaRybakova/eduApp/assets/37059842/7f10a5ed-df15-4317-b859-c085caebe201">

## The next stage is the integration to ROS system: 

1. Set up ROS Environment, you can create one using the following commands:
   
        $ mkdir -p ~/catkin_ws/src
        $ cd ~/catkin_ws/
        $ catkin_make
        $ source devel/setup.bash
   
2. Create a Ros package for youe streamlit application:
   Navigate to the 'scr' directory in your ROS workspace and create a new package:

        $ cd ~/catkin_ws/src
        $ catkin_create_pkg streamlit_app rospy std_msgs

3. Add Your streamlit application to the ROS Package:
   Copy your streamlit application files into the newly created package directory:

        $ cp -r path_to_your_streamlit_app ~/catkin_ws/src/streamlit_app/

## Project Structure

- `streamlit_app.py` — Main Streamlit application file
- `assets/` — Images, audio, and media files used in learning tasks

## Research Context

This application was developed as part of a multi-modal Robot-Assisted Language Learning (RALL) framework.
It is used in structured experimental sessions combining tablet interaction and embodied robot-based activities.
The repository contains software only and does not include participant data.


## Related Publications

The development and evaluation of this application and the broader Child–Robot Interaction / Robot-Assisted Language Learning framework are described in the following peer-reviewed works:

- **Rybakova, A., & Choi, J. (2025).** *Evaluating the Effectiveness of Social Robots in Enhancing English Language Acquisition and Educational Engagement: A Study with Adults and Its Implications for Korean Kindergarten Children.* In *HCI International 2025 (HCII 2025)*, Springer. https://doi.org/10.1007/978-3-031-93861-0_21

- **Rybakova, A., & Choi, J. (2025).** *A multi-modal embodied robot framework for English as a second language learning in preschoolers: Design and evaluation.* *Robotica.* Published online 29 Oct 2025. https://doi.org/10.1017/S0263574725102646 

- **Rybakova, A., & Choi, J. (2026).** *From traditional to robot-assisted learning: A multimodal robot-assisted learning framework for enhancing English acquisition in Korean preschoolers.* *Intelligent Service Robotics, 19*, 30. https://doi.org/10.1007/s11370-025-00685-z
