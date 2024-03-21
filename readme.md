
<div align="center">

# Facetracker for PILLAR-Robots 

[![Project WebPage](https://img.shields.io/badge/Project-webpage-blue)](https://pillar-robots.eu)

</div>


This package provides ROS integration for real-time face tracking used in the [PILLAR-Robots project](https://pillar-robots.eu) by [ARC](https://www.athenarc.gr). This package includes a ROS node for publishing face tracking data from video streams and a standalone demo for users who prefer not to use ROS.

<p align="center"> 
<img width="600px" src="assets/face_tracking.jpg">
</p>


## Prerequisites

- ROS Noetic (other versions may require adjustments)
- Python 3.x
- OpenCV
- cv_bridge ROS package
- [ultralytics](https://github.com/ultralytics/ultralytics)

Ensure ROS Noetic is properly installed on your system. Instructions can be found on the [official ROS installation page](http://wiki.ros.org/noetic/Installation).

## Installation

1. **Create or navigate to your ROS workspace**:

    ```bash
    cd ~/my_ros_workspace/src
    ```

2. **Clone the package into your workspace's `src` directory** (assuming this package is available in a Git repository):

    ```bash
    git clone https://github.com/filby89/facetracker_pillar
    ```

    Replace `https://github.com/filby89/facetracker_pillar` with the actual repository URL.

3. **Build the package**:

    Navigate back to the root of your workspace and build it:

    ```bash
    cd ~/my_ros_workspace
    catkin_make
    ```

4. **Source your workspace**:

    Each new terminal session requires sourcing your workspace:

    ```bash
    source ~/my_ros_workspace/devel/setup.bash
    ```

## Usage

### Running the ROS Node

1. **Start the ROS master** (if not already running):

    ```bash
    roscore
    ```

2. **Launch the `FaceTrackerNode`**:

    ```bash
    roslaunch facetracker_pillar facetracker.launch
    ```

    Ensure you have the `facetracker.launch` file set up as described in the package documentation.

### Running the Standalone Demo

If you prefer not to use ROS, a standalone `demo.py` is included. This script demonstrates basic face tracking functionality without the need for ROS infrastructure.

1. **Navigate to the script's directory**:

    Assuming `demo.py` is located in the `scripts` directory of the package:

    ```bash
    cd ~/my_ros_workspace/src/facetracker_pillar
    ```

2. **Run the demo**:

    ```bash
    python scripts/demo.py
    ```



## Acknowledgements
We acknowledge the following repositories for providing the face detection and tracking models:
* https://github.com/akanametov/yolov8-face
* https://github.com/ultralytics/ultralytics
