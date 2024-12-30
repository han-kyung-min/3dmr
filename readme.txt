last modified 2024/ 12/30


# How to install #

1. git clone https://github.com/luigifreda/3dmr.git

2. conda create env -n nbv python=3.8

3. pip install -r requirements.txt

4. conda activate nbv

5. then, follow the instruction written in https://github.com/luigifreda/3dmr.git

i.e.) ./install.sh   followed by  ./build.sh  followed by source source_all.bash


# Before running the SW #

1. Correct the output traj name by modifying arg: "traj_file_path" located in "/3dmr/nav_ws/src/nav/trajectory_control/launch/sim_trajectory_control_ugv1.launch" 

2. "max_sensor_range" is 10m by default. I modified this number to "2m" to guarrantee generating max coverage path planner for Matterport camera reconstruction later.

If you want to change the max_sensor_range back to original value, you need to change max_sensor_range values in

 i) 3dmr/exploration_ws/src/ugv_3dexplorer/launch/exploration.yaml
 ii) 3dmr/nav_ws/src/nav/path_planner/launch/sim_volumetric_mapping_ugv2.launch

3. "projected_max_zmax" and "projected_max_zmin" params in "3dmr/nav_ws/src/nav/path_planner/launch/sim_volumetric_mapping_ugv2.launch" are used to limit the height of 3D sensor in Octomap to generate 2d projected map. One coulde modify this number if the user is not happy with the generated 2d map.  


 
# To run #

1. cd to 3dmr
2. python main.py
3. select a world 

4. Make sure to finish the run manually if the map is 

5. You can save the map by

rosrun map_server map_saver map:=/volumetric_mapping_ugv1/projected_map -f  out_map

6. traj file is located in the directory that you specified in "/3dmr/nav_ws/src/nav/trajectory_control/launch/sim_trajectory_control_ugv1.launch"



# Modified files/items: #


1. TrajectoryControlActionServer.cpp ( /3dmr/nav_ws/src/nav/trajectory_control/src/TrajectoryControlActionServer.cpp)

 i) create output traj data file 
 ( traj_file path is set in   /3dmr/nav_ws/src/nav/trajectory_control/launch/sim_trajectory_control_ugv1.launch )
 
 ii) save robot traj data into the file

2. octomap_manager.cc and octomap_world.cc (/3dmr  )

 i) Independently creates 2d gridmap ( appended based on APIs from the original Octomap )
 
3. launching scripts and rviz files

4. Tried to save published goals, but this func has been deprecated, so as "travel_tracker.py"



