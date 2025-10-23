from rtde_control import RTDEControlInterface as RTDEControl
from rtde_io import RTDEIOInterface
from rtde_receive import RTDEReceiveInterface as RTDEReceive
import time
import threading
from compas_fab.robots.robot import Configuration
import math
from compas_fab.robots import JointTrajectory


def get_config(ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    robot_joints = ur_r.getActualQ()
    config = Configuration.from_revolute_values(robot_joints)
    return config

def get_tcp_offset(ip="127.0.0.1"):
    ur_c = RTDEControl(ip)
    tcp = ur_c.getTCPOffset()
    return tcp

def set_tcp_offset(pose, ip = "127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.setTcp(pose)

def normalize_joint_values_to_pi(config):
    for i,v in enumerate(config.joint_values):
        if v>math.pi:
            v-=2*math.pi
        if v<-math.pi:
            v+=2*math.pi
        config.joint_values[i]=v
    return config

def move_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool

    ur_c = RTDEControl(ip)
    ur_c.moveJ(config.joint_values, speed, accel, nowait)

def movel_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    ur_c.moveL_FK(config.joint_values, speed, accel, nowait)

def move_to_target(frame, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    pose = frame.point.x, frame.point.y, frame.point.z, *frame.axis_angle_vector
    ur_c = RTDEControl(ip)
    ur_c.moveL(pose ,speed, accel, nowait)
    return pose

def move_in_z_until_contact(config, speed, accel, nowait, ip):
    ur_r = RTDEReceive(ip)
    ur_c = RTDEControl(ip)
    #tcp_force = ur_r.getActualTCPForce()
    # # ur_c.forceMode(([0, 0, 1, 0, 0, 0], [0.0, 0.0, max_force, 0.0, 0.0, 0.0], [0.01, 0.01, max_speed, 0.01, 0.01, 0.01]))
    # # ur_c.forceModeStop()

    move_to_joints(config, speed, accel, nowait, ur_c)
    ur_c.startContactDetection()
    contact_detected = ur_c.readContactDetection()
    if contact_detected:
        ur_c.stopContactDetection()

    return contact_detected

def stopL(accel, ip = "127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.stopL(accel)

def get_digital_io(signal, ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    return ur_r.getDigitalOutState(signal)

def set_digital_io(signal, value, ip="127.0.0.1"):
    io = RTDEIOInterface(ip)
    io.setStandardDigitalOut(signal, value)

def set_tool_digital_io(signal, value, ip="127.0.0.1"):
    io = RTDEIOInterface(ip)
    io.setToolDigitalOut(signal, value)

def get_tcp_frame(ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    tcp = ur_r.getActualTCPPose()
    frame = Frame.from_axis_angle_vector(tcp[3:], point=tcp[0:3])
    return frame

def start_teach_mode(ip="127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.teachMode()

def stop_teach_mode(ip="127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_c.endTeachMode()

def measure_frame_from_3_points(ip="127.0.0.1"):
    ur_c = RTDEControl(ip)
    ur_r = RTDEReceive(ip)

    tcp = ur_c.getTCPOffset()
    print("Hello, your current TCP offset is:")
    print(tcp)

    print("The robot is in free drive mode now")
    print()

    print("1. Move the robot tip to the origin of the calibration frame and press Enter")
    ur_c.teachMode()
    input()
    ur_c.endTeachMode()

    frame_origin = ur_r.getActualTCPPose()
    print("Frame origin:")
    print(frame_origin)

    print("2. Move the robot tip to the X-axis of the calibration frame and press Enter")
    ur_c.teachMode()
    input()
    ur_c.endTeachMode()

    frame_point_on_xaxis = ur_r.getActualTCPPose()
    print("Frame on X-axis:")
    print(frame_point_on_xaxis)

    print("3. Move the robot tip to the Y-axis of the calibration frame and press Enter")
    ur_c.teachMode()
    input()
    ur_c.endTeachMode()

    frame_point_on_yaxis = ur_r.getActualTCPPose()
    print("Frame on Y-axis:")
    print(frame_point_on_yaxis)

    frame = Frame.from_points(
        point=frame_origin[0:3], point_xaxis=frame_point_on_xaxis[0:3], point_xyplane=frame_point_on_yaxis[0:3]
    )

    return frame

def send_trajectory(trajectory, speed, accel, stop_before=0, stop_after=0, ip="127.0.0.1"):

    time.sleep(stop_before)
    #Convert points of trajectory to configurations
    for i in range(len(trajectory.points)):

        #Trajectory points
        point = trajectory.points[i].joint_values
        print (type(point))

        #move to configuration
        move_to_joints(point, speed, accel, False , ip)
    
    time.sleep(stop_after)

    
def send_trajectory_radius(trajectory, speed, accel, radius, stop_before=0, stop_after=0, ip="127.0.0.1"):

    configurations = trajectory.points
    print(f"Move trajectory of {len(configurations)} points with speed {speed}, accel {accel} and blend {radius}")
    path = []
  
    for config in configurations:
        path.append(config.joint_values + [speed, accel, radius])

    time.sleep(stop_before)

    if len(path):
        ur_c = RTDEControl(ip)
        ur_c.moveJ(path)

    time.sleep(stop_after)
