#!/usr/bin/env python
import rospy
import sys
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32
from nav_msgs.msg import Path
from geometry_msgs.msg import Pose #PoseStamped
SAMPLE_HORIZ = 1.0 #s

#class OdometryRecorder:

    #def __init__(self):
        #rospy.init_node('traj_recorder', anonymous=True)
        #self.pub_dist = rospy.Publisher('total_distance', Float32, queue_size=1)
        #self.pub_traj = rospy.Publisher('traj_so_far', Path, queue_size=1)
        #self.sub = rospy.Subscriber("/vrep/ugv1/odom", Odometry, self.callback)

        #self.total_distance = 0.
        #self.previous_x = 0
        #self.previous_y = 0
        #self.traj = []
        #self.prev_time = rospy.get_time()
        
        #r = rospy.Rate(10)
        #while not rospy.is_shutdown():
            #r.sleep()

    #def __del__(self):
        #onsavetraj()

    #def callback(self, data):

        #x = data.pose.pose.position.x
        #y = data.pose.pose.position.y
        #d_increment =   ((x - self.previous_x) ** 2 +
                         #(y - self.previous_y) ** 2 ) ** 0.5
        #self.total_distance = self.total_distance + d_increment
        #print("Total distance traveled is (%f)m"%(self.total_distance) )
        
        #currpose = Pose()
        #currpose.position.x = x
        #currpose.position.y = y
        #currpose.position.z = 0
        
        #curr_time = rospy.get_time()
        #if abs(curr_time - self.prev_time) > SAMPLE_HORIZ:
           #print("time diff: %f \n"%(curr_time - self.prev_time) )
           #self.traj.append( currpose )
           #self.prev_time = curr_time
        
        #self.previous_x = data.pose.pose.position.x
        #self.previous_y = data.pose.pose.position.y
        #rospy.sleep(1.)

    
    #def onsavetraj(self):
        #outfile = '/home/hankm/results/nextbestview/traj.txt'
        #with open(outfile, 'w') as f:
            #for ii in range(0, len(self.traj) ):
                #data = self.traj[ii]
                #strline = '%d %f %f\n'%(ii, data.position.x, data.position.y)
                #f.write(strline)
        #f.close()

def onsavetraj():
    global traj
    outfile = '/home/hankm/results/nextbestview/traj.txt'
    with open(outfile, 'w') as f:
        for ii in range(0, len(traj) ):
            data = traj[ii]
            strline = '%d %f %f\n'%(ii, data.position.x, data.position.y)
            f.write(strline)
    f.close()

def callback(data):
    global traj, prev_time
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y

    currpose = Pose()
    currpose.position.x = x
    currpose.position.y = y
    currpose.position.z = 0
    
    curr_time = rospy.get_time()
    if abs(curr_time - prev_time) > SAMPLE_HORIZ:
       print("time diff: %f \n"%(curr_time - prev_time) )
       traj.append( currpose )
       prev_time = curr_time
    

def main(argv):
    global traj
    global prev_time
    traj = []
    prev_time = 0
    rospy.init_node('traj_recorder', anonymous=True)
    rospy.Subscriber("/vrep/ugv1/odom", Odometry, callback, queue_size=1)
    rospy.spin()
    onsavetraj()
    
    #odom = OdometryRecorder()
    
    #odom.onsavetraj()

if __name__ == '__main__':

    main(sys.argv)
    

        
    
