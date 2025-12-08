#!/usr/bin/env python3
"""
Navigation Goal Sender for Medibot
Sends predefined navigation goals to the robot for hospital automation tasks.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import time

class MedibotNavigator:
    """
    A simple class to send navigation goals to predefined locations in the hospital.
    """
    
    # Predefined locations in the hospital
    LOCATIONS = {
        'pharmacy': {
            'x': -7.0,
            'y': -7.0,
            'z': 0.0
        },
        'patient_room_1': {
            'x': 7.0,
            'y': -7.0,
            'z': 0.0
        },
        'patient_room_2': {
            'x': 7.0,
            'y': 7.0,
            'z': 0.0
        },
        'corridor_center': {
            'x': 0.0,
            'y': 0.0,
            'z': 0.0
        }
    }
    
    def __init__(self):
        """Initialize the navigator"""
        self.navigator = BasicNavigator()
        
    def create_pose(self, location_name):
        """
        Create a PoseStamped message for a given location.
        
        Args:
            location_name: Name of the location (e.g., 'pharmacy', 'patient_room_1')
            
        Returns:
            PoseStamped message or None if location not found
        """
        if location_name not in self.LOCATIONS:
            print(f"Error: Location '{location_name}' not found!")
            print(f"Available locations: {', '.join(self.LOCATIONS.keys())}")
            return None
            
        loc = self.LOCATIONS[location_name]
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        goal_pose.pose.position.x = loc['x']
        goal_pose.pose.position.y = loc['y']
        goal_pose.pose.position.z = loc['z']
        goal_pose.pose.orientation.w = 1.0
        
        return goal_pose
    
    def go_to(self, location_name):
        """
        Navigate to a predefined location.
        
        Args:
            location_name: Name of the location
            
        Returns:
            True if navigation was successful, False otherwise
        """
        print(f"\n{'='*50}")
        print(f"Navigating to: {location_name}")
        print(f"{'='*50}")
        
        goal_pose = self.create_pose(location_name)
        if goal_pose is None:
            return False
        
        # Wait for navigation to activate
        self.navigator.waitUntilNav2Active()
        
        # Send goal
        print(f"Sending goal to ({goal_pose.pose.position.x}, {goal_pose.pose.position.y})")
        self.navigator.goToPose(goal_pose)
        
        # Monitor progress
        i = 0
        while not self.navigator.isTaskComplete():
            i += 1
            feedback = self.navigator.getFeedback()
            if feedback and i % 10 == 0:
                print(f"Distance remaining: {feedback.distance_remaining:.2f} meters")
            time.sleep(0.1)
        
        # Check result
        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print(f"✓ Successfully reached {location_name}!")
            return True
        elif result == TaskResult.CANCELED:
            print(f"✗ Navigation to {location_name} was canceled!")
            return False
        elif result == TaskResult.FAILED:
            print(f"✗ Failed to reach {location_name}!")
            return False
        else:
            print(f"✗ Unknown result: {result}")
            return False
    
    def shutdown(self):
        """Shutdown the navigator"""
        self.navigator.lifecycleShutdown()


def main():
    """Main function to demonstrate navigation"""
    rclpy.init()
    
    navigator = MedibotNavigator()
    
    print("\n" + "="*50)
    print("Medibot Hospital Navigation Demo")
    print("="*50)
    print("\nAvailable locations:")
    for loc_name in navigator.LOCATIONS.keys():
        coords = navigator.LOCATIONS[loc_name]
        print(f"  - {loc_name}: ({coords['x']}, {coords['y']})")
    print("\n")
    
    # Example navigation sequence
    try:
        # Example 1: Go from pharmacy to patient room 1
        print("Example 1: Pharmacy → Patient Room 1")
        if navigator.go_to('patient_room_1'):
            time.sleep(2)
            
            # Example 2: Go from patient room 1 to patient room 2
            print("\nExample 2: Patient Room 1 → Patient Room 2")
            if navigator.go_to('patient_room_2'):
                time.sleep(2)
                
                # Example 3: Return to pharmacy
                print("\nExample 3: Patient Room 2 → Pharmacy")
                navigator.go_to('pharmacy')
        
        print("\n" + "="*50)
        print("Navigation demo completed!")
        print("="*50 + "\n")
        
    except KeyboardInterrupt:
        print("\nNavigation interrupted by user")
    finally:
        navigator.shutdown()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
