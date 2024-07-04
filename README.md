# eduApp
The educational application for preschoolers

The application has been developed to help preschoolers learn English through CRI (Child-Robot interaction)

### The application is focused on several skills:
- Using the images (20 of them) for learning English;
- Various number of the Math problems;
- Color matching task;
- Scramble words game to consolidate knowledge of the first part of the application English Vocabulary

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

