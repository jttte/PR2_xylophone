# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "mesh_builder: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/hydro/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/hydro/share/sensor_msgs/cmake/../msg;-Imoveit_msgs:/opt/ros/hydro/share/moveit_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/hydro/share/geometry_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/hydro/share/actionlib_msgs/cmake/../msg;-Itrajectory_msgs:/opt/ros/hydro/share/trajectory_msgs/cmake/../msg;-Ishape_msgs:/opt/ros/hydro/share/shape_msgs/cmake/../msg;-Iobject_recognition_msgs:/opt/ros/hydro/share/object_recognition_msgs/cmake/../msg;-Ioctomap_msgs:/opt/ros/hydro/share/octomap_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(mesh_builder_generate_messages ALL)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(mesh_builder
  "/home/cl3295/robot-test/src/mesh_builder/srv/MeshCloud.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mesh_builder
)

### Generating Module File
_generate_module_cpp(mesh_builder
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mesh_builder
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(mesh_builder_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(mesh_builder_generate_messages mesh_builder_generate_messages_cpp)

# target for backward compatibility
add_custom_target(mesh_builder_gencpp)
add_dependencies(mesh_builder_gencpp mesh_builder_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mesh_builder_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(mesh_builder
  "/home/cl3295/robot-test/src/mesh_builder/srv/MeshCloud.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mesh_builder
)

### Generating Module File
_generate_module_lisp(mesh_builder
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mesh_builder
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(mesh_builder_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(mesh_builder_generate_messages mesh_builder_generate_messages_lisp)

# target for backward compatibility
add_custom_target(mesh_builder_genlisp)
add_dependencies(mesh_builder_genlisp mesh_builder_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mesh_builder_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(mesh_builder
  "/home/cl3295/robot-test/src/mesh_builder/srv/MeshCloud.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mesh_builder
)

### Generating Module File
_generate_module_py(mesh_builder
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mesh_builder
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(mesh_builder_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(mesh_builder_generate_messages mesh_builder_generate_messages_py)

# target for backward compatibility
add_custom_target(mesh_builder_genpy)
add_dependencies(mesh_builder_genpy mesh_builder_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mesh_builder_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mesh_builder)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mesh_builder
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(mesh_builder_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(mesh_builder_generate_messages_cpp sensor_msgs_generate_messages_cpp)
add_dependencies(mesh_builder_generate_messages_cpp moveit_msgs_generate_messages_cpp)
add_dependencies(mesh_builder_generate_messages_cpp geometry_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mesh_builder)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mesh_builder
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(mesh_builder_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(mesh_builder_generate_messages_lisp sensor_msgs_generate_messages_lisp)
add_dependencies(mesh_builder_generate_messages_lisp moveit_msgs_generate_messages_lisp)
add_dependencies(mesh_builder_generate_messages_lisp geometry_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mesh_builder)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mesh_builder\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mesh_builder
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(mesh_builder_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(mesh_builder_generate_messages_py sensor_msgs_generate_messages_py)
add_dependencies(mesh_builder_generate_messages_py moveit_msgs_generate_messages_py)
add_dependencies(mesh_builder_generate_messages_py geometry_msgs_generate_messages_py)
