# -*- coding: utf-8 -*-
"""
Created on Sun Feb 2 20:29:07 2020

This file reads the CAN_Message.csv output file.  It extracts, plots, and 
writes the decoded data to a Decoded_Messages.csv.

@author: Gus Lee
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cantools 
import matplotlib.animation as animation
from matplotlib import style
import DBC_Read_Tools as DBC

# Read in data
fileName = '../../Data/RAV-4_Giraffe_Data/2020_03_24/2020-03-24-16-42-54_CAN_Messages.csv'
can_data = pd.read_csv(fileName)

# Specify dbc file
db_file = cantools.db.load_file('newToyotacode.dbc')

###############################################################################

# Extract Data
KINEMATICS_Yaw_Rate = DBC.getNumpyData('KINEMATICS',0,can_data,db_file)
KINEMATICS_Steering_Torque = DBC.getNumpyData('KINEMATICS',1,can_data,db_file)
KINEMATICS_Accel_Y = DBC.getNumpyData('KINEMATICS',2,can_data,db_file)

STEER_ANGLE_SENSOR_Steer_Angle = DBC.getNumpyData('STEER_ANGLE_SENSOR',0,can_data,db_file)
STEER_ANGLE_SENSOR_Steer_Fraction = DBC.getNumpyData('STEER_ANGLE_SENSOR',1,can_data,db_file)
STEER_ANGLE_SENSOR_Steer_Rate = DBC.getNumpyData('STEER_ANGLE_SENSOR',2,can_data,db_file)

BRAKE_Brake_Amount = DBC.getNumpyData('BRAKE',0,can_data,db_file)
BRAKE_Brake_Pedal = DBC.getNumpyData('BRAKE',1,can_data,db_file)

WHEEL_SPEEDS_Wheel_Speed_FR = DBC.getNumpyData('WHEEL_SPEEDS',0,can_data,db_file)
WHEEL_SPEEDS_Wheel_Speed_FL = DBC.getNumpyData('WHEEL_SPEEDS',1,can_data,db_file)
WHEEL_SPEEDS_Wheel_Speed_RR = DBC.getNumpyData('WHEEL_SPEEDS',2,can_data,db_file)
WHEEL_SPEEDS_Wheel_Speed_RL = DBC.getNumpyData('WHEEL_SPEEDS',3,can_data,db_file)

SPEED_Encoder = DBC.getNumpyData('SPEED',0,can_data,db_file)
SPEED_Speed = DBC.getNumpyData('SPEED',1,can_data,db_file)
SPEED_Checksum = DBC.getNumpyData('SPEED',2,can_data,db_file)

UKNOWN186_1 = DBC.getNumpyData('UKNOWN186',0,can_data,db_file)

UKNOWN291_1 = DBC.getNumpyData('UKNOWN291',0,can_data,db_file)
UKNOWN291_2 = DBC.getNumpyData('UKNOWN291',1,can_data,db_file)
UKNOWN291_3 = DBC.getNumpyData('UKNOWN291',2,can_data,db_file)

UNKNOWN295_1 = DBC.getNumpyData('UKNOWN295',0,can_data,db_file)
UNKNOWN295_2 = DBC.getNumpyData('UKNOWN295',1,can_data,db_file)
UNKNOWN295_3 = DBC.getNumpyData('UKNOWN295',2,can_data,db_file)

UNKNOWN296_1 = DBC.getNumpyData('UKNOWN296',0,can_data,db_file)
UNKNOWN296_2 = DBC.getNumpyData('UKNOWN296',1,can_data,db_file)
UNKNOWN296_3 = DBC.getNumpyData('UKNOWN296',2,can_data,db_file)

# Unpack requires at least 64 bits to unpack (got 56)
# To resolve: Changed DSU_SPEED message in DBC file from 8 to 7 bytes
DSU_SPEED_Forward_Speed = DBC.getNumpyData('DSU_SPEED',0,can_data,db_file)

STEERING_IPAS_COMMA_State = DBC.getNumpyData('STEERING_IPAS_COMMA',0,can_data,db_file)
STEERING_IPAS_COMMA_Angle = DBC.getNumpyData('STEERING_IPAS_COMMA',1,can_data,db_file)
STEERING_IPAS_COMMA_Set_Me_X10 = DBC.getNumpyData('STEERING_IPAS_COMMA',2,can_data,db_file)
STEERING_IPAS_COMMA_Direction_Cmd = DBC.getNumpyData('STEERING_IPAS_COMMA',3,can_data,db_file)
STEERING_IPAS_COMMA_Set_Me_X40 = DBC.getNumpyData('STEERING_IPAS_COMMA',4,can_data,db_file)
STEERING_IPAS_COMMA_Set_Me_X00 = DBC.getNumpyData('STEERING_IPAS_COMMA',5,can_data,db_file)
STEERING_IPAS_COMMA_Checksum = DBC.getNumpyData('STEERING_IPAS_COMMA',6,can_data,db_file)

TRACK_A_0_Counter = DBC.getNumpyData('TRACK_A_0',0,can_data,db_file)
TRACK_A_0_Long_Dist = DBC.getNumpyData('TRACK_A_0',1,can_data,db_file)
TRACK_A_0_Lat_Dist = DBC.getNumpyData('TRACK_A_0',2,can_data,db_file)
TRACK_A_0_New_Track = DBC.getNumpyData('TRACK_A_0',3,can_data,db_file)
TRACK_A_0_Rel_Speed = DBC.getNumpyData('TRACK_A_0',4,can_data,db_file)
TRACK_A_0_Valid = DBC.getNumpyData('TRACK_A_0',5,can_data,db_file)
TRACK_A_0_Checksum = DBC.getNumpyData('TRACK_A_0',6,can_data,db_file)

TRACK_A_1_Counter = DBC.getNumpyData('TRACK_A_1',0,can_data,db_file)
TRACK_A_1_Long_Dist = DBC.getNumpyData('TRACK_A_1',1,can_data,db_file)
TRACK_A_1_Lat_Dist = DBC.getNumpyData('TRACK_A_1',2,can_data,db_file)
TRACK_A_1_New_Track = DBC.getNumpyData('TRACK_A_1',3,can_data,db_file)
TRACK_A_1_Rel_Speed = DBC.getNumpyData('TRACK_A_1',4,can_data,db_file)
TRACK_A_1_Valid = DBC.getNumpyData('TRACK_A_1',5,can_data,db_file)
TRACK_A_1_Checksum = DBC.getNumpyData('TRACK_A_1',6,can_data,db_file)

TRACK_A_2_Counter = DBC.getNumpyData('TRACK_A_2',0,can_data,db_file)
TRACK_A_2_Long_Dist = DBC.getNumpyData('TRACK_A_2',1,can_data,db_file)
TRACK_A_2_Lat_Dist = DBC.getNumpyData('TRACK_A_2',2,can_data,db_file)
TRACK_A_2_New_Track = DBC.getNumpyData('TRACK_A_2',3,can_data,db_file)
TRACK_A_2_Rel_Speed = DBC.getNumpyData('TRACK_A_2',4,can_data,db_file)
TRACK_A_2_Valid = DBC.getNumpyData('TRACK_A_2',5,can_data,db_file)
TRACK_A_2_Checksum = DBC.getNumpyData('TRACK_A_2',6,can_data,db_file)

TRACK_A_3_Counter = DBC.getNumpyData('TRACK_A_3',0,can_data,db_file)
TRACK_A_3_Long_Dist = DBC.getNumpyData('TRACK_A_3',1,can_data,db_file)
TRACK_A_3_Lat_Dist = DBC.getNumpyData('TRACK_A_3',2,can_data,db_file)
TRACK_A_3_New_Track = DBC.getNumpyData('TRACK_A_3',3,can_data,db_file)
TRACK_A_3_Rel_Speed = DBC.getNumpyData('TRACK_A_3',4,can_data,db_file)
TRACK_A_3_Valid = DBC.getNumpyData('TRACK_A_3',5,can_data,db_file)
TRACK_A_3_Checksum = DBC.getNumpyData('TRACK_A_3',6,can_data,db_file)

TRACK_A_4_Counter = DBC.getNumpyData('TRACK_A_4',0,can_data,db_file)
TRACK_A_4_Long_Dist = DBC.getNumpyData('TRACK_A_4',1,can_data,db_file)
TRACK_A_4_Lat_Dist = DBC.getNumpyData('TRACK_A_4',2,can_data,db_file)
TRACK_A_4_New_Track = DBC.getNumpyData('TRACK_A_4',3,can_data,db_file)
TRACK_A_4_Rel_Speed = DBC.getNumpyData('TRACK_A_4',4,can_data,db_file)
TRACK_A_4_Valid = DBC.getNumpyData('TRACK_A_4',5,can_data,db_file)
TRACK_A_4_Checksum = DBC.getNumpyData('TRACK_A_4',6,can_data,db_file)

TRACK_A_5_Counter = DBC.getNumpyData('TRACK_A_5',0,can_data,db_file)
TRACK_A_5_Long_Dist = DBC.getNumpyData('TRACK_A_5',1,can_data,db_file)
TRACK_A_5_Lat_Dist = DBC.getNumpyData('TRACK_A_5',2,can_data,db_file)
TRACK_A_5_New_Track = DBC.getNumpyData('TRACK_A_5',3,can_data,db_file)
TRACK_A_5_Rel_Speed = DBC.getNumpyData('TRACK_A_5',4,can_data,db_file)
TRACK_A_5_Valid = DBC.getNumpyData('TRACK_A_5',5,can_data,db_file)
TRACK_A_5_Checksum = DBC.getNumpyData('TRACK_A_5',6,can_data,db_file)

TRACK_A_6_Counter = DBC.getNumpyData('TRACK_A_6',0,can_data,db_file)
TRACK_A_6_Long_Dist = DBC.getNumpyData('TRACK_A_6',1,can_data,db_file)
TRACK_A_6_Lat_Dist = DBC.getNumpyData('TRACK_A_6',2,can_data,db_file)
TRACK_A_6_New_Track = DBC.getNumpyData('TRACK_A_6',3,can_data,db_file)
TRACK_A_6_Rel_Speed = DBC.getNumpyData('TRACK_A_6',4,can_data,db_file)
TRACK_A_6_Valid = DBC.getNumpyData('TRACK_A_6',5,can_data,db_file)
TRACK_A_6_Checksum = DBC.getNumpyData('TRACK_A_6',6,can_data,db_file)

TRACK_A_7_Counter = DBC.getNumpyData('TRACK_A_7',0,can_data,db_file)
TRACK_A_7_Long_Dist = DBC.getNumpyData('TRACK_A_7',1,can_data,db_file)
TRACK_A_7_Lat_Dist = DBC.getNumpyData('TRACK_A_7',2,can_data,db_file)
TRACK_A_7_New_Track = DBC.getNumpyData('TRACK_A_7',3,can_data,db_file)
TRACK_A_7_Rel_Speed = DBC.getNumpyData('TRACK_A_7',4,can_data,db_file)
TRACK_A_7_Valid = DBC.getNumpyData('TRACK_A_7',5,can_data,db_file)
TRACK_A_7_Checksum = DBC.getNumpyData('TRACK_A_7',6,can_data,db_file)

TRACK_A_8_Counter = DBC.getNumpyData('TRACK_A_8',0,can_data,db_file)
TRACK_A_8_Long_Dist = DBC.getNumpyData('TRACK_A_8',1,can_data,db_file)
TRACK_A_8_Lat_Dist = DBC.getNumpyData('TRACK_A_8',2,can_data,db_file)
TRACK_A_8_New_Track = DBC.getNumpyData('TRACK_A_8',3,can_data,db_file)
TRACK_A_8_Rel_Speed = DBC.getNumpyData('TRACK_A_8',4,can_data,db_file)
TRACK_A_8_Valid = DBC.getNumpyData('TRACK_A_8',5,can_data,db_file)
TRACK_A_8_Checksum = DBC.getNumpyData('TRACK_A_8',6,can_data,db_file)

TRACK_A_9_Counter = DBC.getNumpyData('TRACK_A_9',0,can_data,db_file)
TRACK_A_9_Long_Dist = DBC.getNumpyData('TRACK_A_9',1,can_data,db_file)
TRACK_A_9_Lat_Dist = DBC.getNumpyData('TRACK_A_9',2,can_data,db_file)
TRACK_A_9_New_Track = DBC.getNumpyData('TRACK_A_9',3,can_data,db_file)
TRACK_A_9_Rel_Speed = DBC.getNumpyData('TRACK_A_9',4,can_data,db_file)
TRACK_A_9_Valid = DBC.getNumpyData('TRACK_A_9',5,can_data,db_file)
TRACK_A_9_Checksum = DBC.getNumpyData('TRACK_A_9',6,can_data,db_file)

TRACK_A_10_Counter = DBC.getNumpyData('TRACK_A_10',0,can_data,db_file)
TRACK_A_10_Long_Dist = DBC.getNumpyData('TRACK_A_10',1,can_data,db_file)
TRACK_A_10_Lat_Dist = DBC.getNumpyData('TRACK_A_10',2,can_data,db_file)
TRACK_A_10_New_Track = DBC.getNumpyData('TRACK_A_10',3,can_data,db_file)
TRACK_A_10_Rel_Speed = DBC.getNumpyData('TRACK_A_10',4,can_data,db_file)
TRACK_A_10_Valid = DBC.getNumpyData('TRACK_A_10',5,can_data,db_file)
TRACK_A_10_Checksum = DBC.getNumpyData('TRACK_A_10',6,can_data,db_file)

TRACK_A_11_Counter = DBC.getNumpyData('TRACK_A_11',0,can_data,db_file)
TRACK_A_11_Long_Dist = DBC.getNumpyData('TRACK_A_11',1,can_data,db_file)
TRACK_A_11_Lat_Dist = DBC.getNumpyData('TRACK_A_11',2,can_data,db_file)
TRACK_A_11_New_Track = DBC.getNumpyData('TRACK_A_11',3,can_data,db_file)
TRACK_A_11_Rel_Speed = DBC.getNumpyData('TRACK_A_11',4,can_data,db_file)
TRACK_A_11_Valid = DBC.getNumpyData('TRACK_A_11',5,can_data,db_file)
TRACK_A_11_Checksum = DBC.getNumpyData('TRACK_A_11',6,can_data,db_file)

TRACK_A_12_Counter = DBC.getNumpyData('TRACK_A_12',0,can_data,db_file)
TRACK_A_12_Long_Dist = DBC.getNumpyData('TRACK_A_12',1,can_data,db_file)
TRACK_A_12_Lat_Dist = DBC.getNumpyData('TRACK_A_12',2,can_data,db_file)
TRACK_A_12_New_Track = DBC.getNumpyData('TRACK_A_12',3,can_data,db_file)
TRACK_A_12_Rel_Speed = DBC.getNumpyData('TRACK_A_12',4,can_data,db_file)
TRACK_A_12_Valid = DBC.getNumpyData('TRACK_A_12',5,can_data,db_file)
TRACK_A_12_Checksum = DBC.getNumpyData('TRACK_A_12',6,can_data,db_file)

TRACK_A_13_Counter = DBC.getNumpyData('TRACK_A_13',0,can_data,db_file)
TRACK_A_13_Long_Dist = DBC.getNumpyData('TRACK_A_13',1,can_data,db_file)
TRACK_A_13_Lat_Dist = DBC.getNumpyData('TRACK_A_13',2,can_data,db_file)
TRACK_A_13_New_Track = DBC.getNumpyData('TRACK_A_13',3,can_data,db_file)
TRACK_A_13_Rel_Speed = DBC.getNumpyData('TRACK_A_13',4,can_data,db_file)
TRACK_A_13_Valid = DBC.getNumpyData('TRACK_A_13',5,can_data,db_file)
TRACK_A_13_Checksum = DBC.getNumpyData('TRACK_A_13',6,can_data,db_file)

TRACK_A_14_Counter = DBC.getNumpyData('TRACK_A_14',0,can_data,db_file)
TRACK_A_14_Long_Dist = DBC.getNumpyData('TRACK_A_14',1,can_data,db_file)
TRACK_A_14_Lat_Dist = DBC.getNumpyData('TRACK_A_14',2,can_data,db_file)
TRACK_A_14_New_Track = DBC.getNumpyData('TRACK_A_14',3,can_data,db_file)
TRACK_A_14_Rel_Speed = DBC.getNumpyData('TRACK_A_14',4,can_data,db_file)
TRACK_A_14_Valid = DBC.getNumpyData('TRACK_A_14',5,can_data,db_file)
TRACK_A_14_Checksum = DBC.getNumpyData('TRACK_A_14',6,can_data,db_file)

TRACK_A_15_Counter = DBC.getNumpyData('TRACK_A_15',0,can_data,db_file)
TRACK_A_15_Long_Dist = DBC.getNumpyData('TRACK_A_15',1,can_data,db_file)
TRACK_A_15_Lat_Dist = DBC.getNumpyData('TRACK_A_15',2,can_data,db_file)
TRACK_A_15_New_Track = DBC.getNumpyData('TRACK_A_15',3,can_data,db_file)
TRACK_A_15_Rel_Speed = DBC.getNumpyData('TRACK_A_15',4,can_data,db_file)
TRACK_A_15_Valid = DBC.getNumpyData('TRACK_A_15',5,can_data,db_file)
TRACK_A_15_Checksum = DBC.getNumpyData('TRACK_A_15',6,can_data,db_file)

TRACK_B_0_Counter = DBC.getNumpyData('TRACK_B_0',0,can_data,db_file)
TRACK_B_0_Rel_Accel = DBC.getNumpyData('TRACK_B_0',1,can_data,db_file)
TRACK_B_0_Score = DBC.getNumpyData('TRACK_B_0',2,can_data,db_file)
TRACK_B_0_Checksum = DBC.getNumpyData('TRACK_B_0',3,can_data,db_file)

TRACK_B_1_Counter = DBC.getNumpyData('TRACK_B_1',0,can_data,db_file)
TRACK_B_1_Rel_Accel = DBC.getNumpyData('TRACK_B_1',1,can_data,db_file)
TRACK_B_1_Score = DBC.getNumpyData('TRACK_B_1',2,can_data,db_file)
TRACK_B_1_Checksum = DBC.getNumpyData('TRACK_B_1',3,can_data,db_file)

TRACK_B_2_Counter = DBC.getNumpyData('TRACK_B_2',0,can_data,db_file)
TRACK_B_2_Rel_Accel = DBC.getNumpyData('TRACK_B_2',1,can_data,db_file)
TRACK_B_2_Score = DBC.getNumpyData('TRACK_B_2',2,can_data,db_file)
TRACK_B_2_Checksum = DBC.getNumpyData('TRACK_B_2',3,can_data,db_file)

TRACK_B_3_Counter = DBC.getNumpyData('TRACK_B_3',0,can_data,db_file)
TRACK_B_3_Rel_Accel = DBC.getNumpyData('TRACK_B_3',1,can_data,db_file)
TRACK_B_3_Score = DBC.getNumpyData('TRACK_B_3',2,can_data,db_file)
TRACK_B_3_Checksum = DBC.getNumpyData('TRACK_B_3',3,can_data,db_file)

TRACK_B_4_Counter = DBC.getNumpyData('TRACK_B_4',0,can_data,db_file)
TRACK_B_4_Rel_Accel = DBC.getNumpyData('TRACK_B_4',1,can_data,db_file)
TRACK_B_4_Score = DBC.getNumpyData('TRACK_B_4',2,can_data,db_file)
TRACK_B_4_Checksum = DBC.getNumpyData('TRACK_B_4',3,can_data,db_file)

TRACK_B_5_Counter = DBC.getNumpyData('TRACK_B_5',0,can_data,db_file)
TRACK_B_5_Rel_Accel = DBC.getNumpyData('TRACK_B_5',1,can_data,db_file)
TRACK_B_5_Score = DBC.getNumpyData('TRACK_B_5',2,can_data,db_file)
TRACK_B_5_Checksum = DBC.getNumpyData('TRACK_B_5',3,can_data,db_file)

TRACK_B_6_Counter = DBC.getNumpyData('TRACK_B_6',0,can_data,db_file)
TRACK_B_6_Rel_Accel = DBC.getNumpyData('TRACK_B_6',1,can_data,db_file)
TRACK_B_6_Score = DBC.getNumpyData('TRACK_B_6',2,can_data,db_file)
TRACK_B_6_Checksum = DBC.getNumpyData('TRACK_B_6',3,can_data,db_file)

TRACK_B_7_Counter = DBC.getNumpyData('TRACK_B_7',0,can_data,db_file)
TRACK_B_7_Rel_Accel = DBC.getNumpyData('TRACK_B_7',1,can_data,db_file)
TRACK_B_7_Score = DBC.getNumpyData('TRACK_B_7',2,can_data,db_file)
TRACK_B_7_Checksum = DBC.getNumpyData('TRACK_B_7',3,can_data,db_file)

TRACK_B_8_Counter = DBC.getNumpyData('TRACK_B_8',0,can_data,db_file)
TRACK_B_8_Rel_Accel = DBC.getNumpyData('TRACK_B_8',1,can_data,db_file)
TRACK_B_8_Score = DBC.getNumpyData('TRACK_B_8',2,can_data,db_file)
TRACK_B_8_Checksum = DBC.getNumpyData('TRACK_B_8',3,can_data,db_file)

TRACK_B_9_Counter = DBC.getNumpyData('TRACK_B_9',0,can_data,db_file)
TRACK_B_9_Rel_Accel = DBC.getNumpyData('TRACK_B_9',1,can_data,db_file)
TRACK_B_9_Score = DBC.getNumpyData('TRACK_B_9',2,can_data,db_file)
TRACK_B_9_Checksum = DBC.getNumpyData('TRACK_B_9',3,can_data,db_file)

TRACK_B_10_Counter = DBC.getNumpyData('TRACK_B_10',0,can_data,db_file)
TRACK_B_10_Rel_Accel = DBC.getNumpyData('TRACK_B_10',1,can_data,db_file)
TRACK_B_10_Score = DBC.getNumpyData('TRACK_B_10',2,can_data,db_file)
TRACK_B_10_Checksum = DBC.getNumpyData('TRACK_B_10',3,can_data,db_file)

TRACK_B_11_Counter = DBC.getNumpyData('TRACK_B_11',0,can_data,db_file)
TRACK_B_11_Rel_Accel = DBC.getNumpyData('TRACK_B_11',1,can_data,db_file)
TRACK_B_11_Score = DBC.getNumpyData('TRACK_B_11',2,can_data,db_file)
TRACK_B_11_Checksum = DBC.getNumpyData('TRACK_B_11',3,can_data,db_file)

TRACK_B_12_Counter = DBC.getNumpyData('TRACK_B_12',0,can_data,db_file)
TRACK_B_12_Rel_Accel = DBC.getNumpyData('TRACK_B_12',1,can_data,db_file)
TRACK_B_12_Score = DBC.getNumpyData('TRACK_B_12',2,can_data,db_file)
TRACK_B_12_Checksum = DBC.getNumpyData('TRACK_B_12',3,can_data,db_file)

TRACK_B_13_Counter = DBC.getNumpyData('TRACK_B_13',0,can_data,db_file)
TRACK_B_13_Rel_Accel = DBC.getNumpyData('TRACK_B_13',1,can_data,db_file)
TRACK_B_13_Score = DBC.getNumpyData('TRACK_B_13',2,can_data,db_file)
TRACK_B_13_Checksum = DBC.getNumpyData('TRACK_B_13',3,can_data,db_file)

TRACK_B_14_Counter = DBC.getNumpyData('TRACK_B_14',0,can_data,db_file)
TRACK_B_14_Rel_Accel = DBC.getNumpyData('TRACK_B_14',1,can_data,db_file)
TRACK_B_14_Score = DBC.getNumpyData('TRACK_B_14',2,can_data,db_file)
TRACK_B_14_Checksum = DBC.getNumpyData('TRACK_B_14',3,can_data,db_file)

TRACK_B_15_Counter = DBC.getNumpyData('TRACK_B_15',0,can_data,db_file)
TRACK_B_15_Rel_Accel = DBC.getNumpyData('TRACK_B_15',1,can_data,db_file)
TRACK_B_15_Score = DBC.getNumpyData('TRACK_B_15',2,can_data,db_file)
TRACK_B_15_Checksum = DBC.getNumpyData('TRACK_B_15',3,can_data,db_file)

NEW_MSG_1_New_Signal_1 = DBC.getNumpyData('NEW_MSG_1',0,can_data,db_file)
NEW_MSG_1_New_Signal_2 = DBC.getNumpyData('NEW_MSG_1',1,can_data,db_file)

NEW_MSG_2_New_Signal_1 = DBC.getNumpyData('NEW_MSG_2',0,can_data,db_file)
NEW_MSG_2_New_Signal_2 = DBC.getNumpyData('NEW_MSG_2',1,can_data,db_file)

PCM_CRUISE_Gas_Released = DBC.getNumpyData('PCM_CRUISE',0,can_data,db_file)
PCM_CRUISE_Cruise_Active = DBC.getNumpyData('PCM_CRUISE',1,can_data,db_file)
PCM_CRUISE_Standstill_On = DBC.getNumpyData('PCM_CRUISE',2,can_data,db_file)
PCM_CRUISE_Accel_Net = DBC.getNumpyData('PCM_CRUISE',3,can_data,db_file)
# Could not convert string to float: 'active'
# PCM_CRUISE_Cruise_State = DBC.getNumpyData('PCM_CRUISE',4,can_data,db_file)
PCM_CRUISE_Checksum = DBC.getNumpyData('PCM_CRUISE',5,can_data,db_file)

PCM_CRUISE_2_Main_On = DBC.getNumpyData('PCM_CRUISE_2',0,can_data,db_file)
# Could not convert string to float: 'ok'
# PCM_CRUISE_2_Low_Speed_Lockout = DBC.getNumpyData('PCM_CRUISE_2',1,can_data,db_file)
PCM_CRUISE_2_Set_Speed = DBC.getNumpyData('PCM_CRUISE_2',2,can_data,db_file)
PCM_CRUISE_2_Checksum = DBC.getNumpyData('PCM_CRUISE_2',3,can_data,db_file)

GAS_COMMAND_Gas_Command = DBC.getNumpyData('GAS_COMMAND',0,can_data,db_file)
GAS_COMMAND_Gas_Command2 = DBC.getNumpyData('GAS_COMMAND',1,can_data,db_file)
GAS_COMMAND_Enable = DBC.getNumpyData('GAS_COMMAND',2,can_data,db_file)
GAS_COMMAND_Counter_Pedal = DBC.getNumpyData('GAS_COMMAND',3,can_data,db_file)
GAS_COMMAND_Checksum_Pedal = DBC.getNumpyData('GAS_COMMAND',4,can_data,db_file)

GAS_SENSOR_Interceptor_Gas = DBC.getNumpyData('GAS_SENSOR',0,can_data,db_file)
GAS_SENSOR_Interceptor_Gas2 = DBC.getNumpyData('GAS_SENSOR',1,can_data,db_file)
GAS_SENSOR_State = DBC.getNumpyData('GAS_SENSOR',2,can_data,db_file)
GAS_SENSOR_Counter_Pedal = DBC.getNumpyData('GAS_SENSOR',3,can_data,db_file)
GAS_SENSOR_Checksum_Pedal = DBC.getNumpyData('GAS_SENSOR',4,can_data,db_file)

BRAKE_MODULE_Brake_Pressure = DBC.getNumpyData('BRAKE_MODULE',0,can_data,db_file)
BRAKE_MODULE_Brake_Position = DBC.getNumpyData('BRAKE_MODULE',1,can_data,db_file)
BRAKE_MODULE_Brake_Pressed = DBC.getNumpyData('BRAKE_MODULE',2,can_data,db_file)

# Unpack requires at least 64 bits to unpack (got 32)
# To resolve: Changed DSU_SPEED message in DBC file from 8 to 4 bytes
ACCELEROMETER_Accel_X = DBC.getNumpyData('ACCELEROMETER',0,can_data,db_file)
ACCELEROMETER_Accel_Z = DBC.getNumpyData('ACCELEROMETER',1,can_data,db_file)

BRAKE_MODULE2_Brake_Pressed = DBC.getNumpyData('BRAKE_MODULE2',0,can_data,db_file)

GAS_PEDAL_Gas_Pedal = DBC.getNumpyData('GAS_PEDAL',0,can_data,db_file)

STEER_TORQUE_SENSOR_Steer_Override = DBC.getNumpyData('STEER_TORQUE_SENSOR',0,can_data,db_file)
STEER_TORQUE_SENSOR_Steer_Torque_Driver = DBC.getNumpyData('STEER_TORQUE_SENSOR',1,can_data,db_file)
STEER_TORQUE_SENSOR_Steer_Angle = DBC.getNumpyData('STEER_TORQUE_SENSOR',2,can_data,db_file)
STEER_TORQUE_SENSOR_Steer_Torque_Eps = DBC.getNumpyData('STEER_TORQUE_SENSOR',3,can_data,db_file)
STEER_TORQUE_SENSOR_Checksum = DBC.getNumpyData('STEER_TORQUE_SENSOR',4,can_data,db_file)

EPS_STATUS_IPAS_State = DBC.getNumpyData('EPS_STATUS',0,can_data,db_file)
# Could not convert string to float: 'standby'
# EPS_STATUS_LKA_State = DBC.getNumpyData('EPS_STATUS',1,can_data,db_file)
EPS_STATUS_Type = DBC.getNumpyData('EPS_STATUS',2,can_data,db_file)
EPS_STATUS_Checksum = DBC.getNumpyData('EPS_STATUS',3,can_data,db_file)

STEERING_IPAS_State = DBC.getNumpyData('STEERING_IPAS',0,can_data,db_file)
STEERING_IPAS_Angle = DBC.getNumpyData('STEERING_IPAS',1,can_data,db_file)
STEERING_IPAS_Set_Me_X10 = DBC.getNumpyData('STEERING_IPAS',2,can_data,db_file)
STEERING_IPAS_Direction_Cmd = DBC.getNumpyData('STEERING_IPAS',3,can_data,db_file)
STEERING_IPAS_Set_Me_X40 = DBC.getNumpyData('STEERING_IPAS',4,can_data,db_file)
STEERING_IPAS_Set_Me_X00 = DBC.getNumpyData('STEERING_IPAS',5,can_data,db_file)
STEERING_IPAS_Checksum = DBC.getNumpyData('STEERING_IPAS',6,can_data,db_file)

STEERING_LKA_Set_Me_1 = DBC.getNumpyData('STEERING_LKA',0,can_data,db_file)
STEERING_LKA_Counter = DBC.getNumpyData('STEERING_LKA',1,can_data,db_file)
STEERING_LKA_Steer_Request = DBC.getNumpyData('STEERING_LKA',2,can_data,db_file)
STEERING_LKA_Steer_Torque_Cmd = DBC.getNumpyData('STEERING_LKA',3,can_data,db_file)
STEERING_LKA_LKA_State = DBC.getNumpyData('STEERING_LKA',4,can_data,db_file)
STEERING_LKA_Checksum = DBC.getNumpyData('STEERING_LKA',5,can_data,db_file)

LEAD_INFO_Lead_Long_Dist = DBC.getNumpyData('LEAD_INFO',0,can_data,db_file)
LEAD_INFO_Lead_Rel_Speed = DBC.getNumpyData('LEAD_INFO',1,can_data,db_file)
LEAD_INFO_Checksum = DBC.getNumpyData('LEAD_INFO',2,can_data,db_file)

ACC_CONTROL_Accel_Cmd = DBC.getNumpyData('ACC_CONTROL',0,can_data,db_file)
ACC_CONTROL_Set_Me_X01 = DBC.getNumpyData('ACC_CONTROL',1,can_data,db_file)
ACC_CONTROL_Mini_Car = DBC.getNumpyData('ACC_CONTROL',2,can_data,db_file)
ACC_CONTROL_Distance = DBC.getNumpyData('ACC_CONTROL',3,can_data,db_file)
ACC_CONTROL_Set_Me_X3 = DBC.getNumpyData('ACC_CONTROL',4,can_data,db_file)
ACC_CONTROL_Release_Standstill = DBC.getNumpyData('ACC_CONTROL',5,can_data,db_file)
ACC_CONTROL_Set_Me_1 = DBC.getNumpyData('ACC_CONTROL',6,can_data,db_file)
ACC_CONTROL_Cancel_Req = DBC.getNumpyData('ACC_CONTROL',7,can_data,db_file)
ACC_CONTROL_Checksum = DBC.getNumpyData('ACC_CONTROL',8,can_data,db_file)

PCM_CRUISE_SM_Main_On = DBC.getNumpyData('PCM_CRUISE_SM',0,can_data,db_file)
PCM_CRUISE_SM_Distance_Lines = DBC.getNumpyData('PCM_CRUISE_SM',1,can_data,db_file)
# Could not convert string to float: 'disabled'
# PCM_CRUISE_SM_Cruise_Control_State = DBC.getNumpyData('PCM_CRUISE_SM',2,can_data,db_file)
PCM_CRUISE_SM_UI_Set_Speed = DBC.getNumpyData('PCM_CRUISE_SM',3,can_data,db_file)

ESP_CONTROL_TC_Disabled = DBC.getNumpyData('ESP_CONTROL',0,can_data,db_file)
ESP_CONTROL_Brake_Lights_ACC = DBC.getNumpyData('ESP_CONTROL',1,can_data,db_file)

ACC_HUD_FCW = DBC.getNumpyData('ACC_HUD',0,can_data,db_file)
ACC_HUD_Set_Me_X20 = DBC.getNumpyData('ACC_HUD',1,can_data,db_file)
ACC_HUD_Set_Me_X10 = DBC.getNumpyData('ACC_HUD',2,can_data,db_file)
ACC_HUD_Set_Me_X80 = DBC.getNumpyData('ACC_HUD',3,can_data,db_file)

LKAS_HUD_Set_Me_X01 = DBC.getNumpyData('LKAS_HUD',0,can_data,db_file)
# Could not convert string to float: 'faded'
# LKAS_HUD_Left_Line = DBC.getNumpyData('LKAS_HUD',1,can_data,db_file)
# LKAS_HUD_Right_Line = DBC.getNumpyData('LKAS_HUD',2,can_data,db_file)
# Could not convert string to float: 'none'
# LKAS_HUD_Barriers = DBC.getNumpyData('LKAS_HUD',3,can_data,db_file)
LKAS_HUD_LDA_Malfunction = DBC.getNumpyData('LKAS_HUD',4,can_data,db_file)
LKAS_HUD_Adjusting_Camera = DBC.getNumpyData('LKAS_HUD',5,can_data,db_file)
LKAS_HUD_Two_Beeps = DBC.getNumpyData('LKAS_HUD',6,can_data,db_file)
LKAS_HUD_Set_Me_X01_2 = DBC.getNumpyData('LKAS_HUD',7,can_data,db_file)
# Could not convert string to float: 'none'
# LKAS_HUD_LDA_Alert = DBC.getNumpyData('LKAS_HUD',8,can_data,db_file)
LKAS_HUD_Set_Me_X0C = DBC.getNumpyData('LKAS_HUD',9,can_data,db_file)
LKAS_HUD_Repeated_Beeps = DBC.getNumpyData('LKAS_HUD',10,can_data,db_file)
LKAS_HUD_Set_Me_X2C = DBC.getNumpyData('LKAS_HUD',11,can_data,db_file)
LKAS_HUD_Set_Me_X38 = DBC.getNumpyData('LKAS_HUD',12,can_data,db_file)
LKAS_HUD_Set_Me_X02 = DBC.getNumpyData('LKAS_HUD',13,can_data,db_file)

UI_SEETING_Units = DBC.getNumpyData('UI_SEETING',0,can_data,db_file)

# Could not convert string to float: 'none'
# STEERING_LEVERS_Turn_Signals = DBC.getNumpyData('STEERING_LEVERS',0,can_data,db_file)

SEATS_DOORS_Door_Open_FL = DBC.getNumpyData('SEATS_DOORS',0,can_data,db_file)
SEATS_DOORS_Door_Open_FR = DBC.getNumpyData('SEATS_DOORS',1,can_data,db_file)
SEATS_DOORS_Door_Open_RR = DBC.getNumpyData('SEATS_DOORS',2,can_data,db_file)
SEATS_DOORS_Door_Open_RL = DBC.getNumpyData('SEATS_DOORS',3,can_data,db_file)
SEATS_DOORS_Seatbelt_Driver_Unlatched = DBC.getNumpyData('SEATS_DOORS',4,can_data,db_file)

LIGHT_STALK_Auto_High_Beam = DBC.getNumpyData('LIGHT_STALK',0,can_data,db_file)

# Could not convert string to float: 'none'
# RSA1_Tsgn1 = DBC.getNumpyData('RSA1',0,can_data,db_file)
RSA1_Tsgngry1 = DBC.getNumpyData('RSA1',1,can_data,db_file)
RSA1_Tsgnhlt1 = DBC.getNumpyData('RSA1',2,can_data,db_file)
RSA1_Spdval1 = DBC.getNumpyData('RSA1',3,can_data,db_file)
RSA1_Splsgn1 = DBC.getNumpyData('RSA1',4,can_data,db_file)
# Could not convert string to float: 'none'
# RSA1_Splsgn2 = DBC.getNumpyData('RSA1',5,can_data,db_file)
# RSA1_Tsgn2 = DBC.getNumpyData('RSA1',6,can_data,db_file)
RSA1_Tsgngry2 = DBC.getNumpyData('RSA1',7,can_data,db_file)
RSA1_Tsgnhlt2 = DBC.getNumpyData('RSA1',8,can_data,db_file)
RSA1_Spdval2 = DBC.getNumpyData('RSA1',9,can_data,db_file)
RSA1_Bzrrq_p = DBC.getNumpyData('RSA1',10,can_data,db_file)
RSA1_Bzrrq_a = DBC.getNumpyData('RSA1',11,can_data,db_file)
RSA1_Syncid1 = DBC.getNumpyData('RSA1',12,can_data,db_file)

# Could not convert string to float: 'none'
# RSA2_Tsgn3 = DBC.getNumpyData('RSA2',0,can_data,db_file)
RSA2_Tsgngry3 = DBC.getNumpyData('RSA2',1,can_data,db_file)
RSA2_Tsgnhlt3 = DBC.getNumpyData('RSA2',2,can_data,db_file)
# Could not convert string to float: 'none'
# RSA2_Splsgn3 = DBC.getNumpyData('RSA2',3,can_data,db_file)
RSA2_Splsgn4 = DBC.getNumpyData('RSA2',4,can_data,db_file)
RSA2_Tsgn4 = DBC.getNumpyData('RSA2',5,can_data,db_file)
RSA2_Tsgngry4 = DBC.getNumpyData('RSA2',6,can_data,db_file)
RSA2_Tsgnhlt4 = DBC.getNumpyData('RSA2',7,can_data,db_file)
RSA2_Dpsgnreq = DBC.getNumpyData('RSA2',8,can_data,db_file)
RSA2_Sgnnump = DBC.getNumpyData('RSA2',9,can_data,db_file)
RSA2_Sgnnuma = DBC.getNumpyData('RSA2',10,can_data,db_file)
RSA2_Spdunt = DBC.getNumpyData('RSA2',11,can_data,db_file)
RSA2_Tsrwmsg = DBC.getNumpyData('RSA2',12,can_data,db_file)
RSA2_Syncid2 = DBC.getNumpyData('RSA2',13,can_data,db_file)

RSA3_Tsreqpd = DBC.getNumpyData('RSA3',0,can_data,db_file)
RSA3_Tsrmsw = DBC.getNumpyData('RSA3',1,can_data,db_file)
RSA3_Otsgnntm = DBC.getNumpyData('RSA3',2,can_data,db_file)
RSA3_Ntlvlspd = DBC.getNumpyData('RSA3',3,can_data,db_file)
RSA3_Ovspntm = DBC.getNumpyData('RSA3',4,can_data,db_file)
RSA3_Ovspvall = DBC.getNumpyData('RSA3',5,can_data,db_file)
RSA3_Ovspvalm = DBC.getNumpyData('RSA3',6,can_data,db_file)
RSA3_Ovspvalh = DBC.getNumpyData('RSA3',7,can_data,db_file)
RSA3_Tsrspu = DBC.getNumpyData('RSA3',8,can_data,db_file)

###############################################################################

# Plot Data
DBC.plotDBC('KINEMATICS',0,can_data,db_file)
DBC.plotDBC('KINEMATICS',1,can_data,db_file)
DBC.plotDBC('KINEMATICS',2,can_data,db_file)

DBC.plotDBC('STEER_ANGLE_SENSOR',0,can_data,db_file)
DBC.plotDBC('STEER_ANGLE_SENSOR',1,can_data,db_file)
DBC.plotDBC('STEER_ANGLE_SENSOR',2,can_data,db_file)

DBC.plotDBC('BRAKE',0,can_data,db_file)
DBC.plotDBC('BRAKE',1,can_data,db_file)

DBC.plotDBC('WHEEL_SPEEDS',0,can_data,db_file)
DBC.plotDBC('WHEEL_SPEEDS',1,can_data,db_file)
DBC.plotDBC('WHEEL_SPEEDS',2,can_data,db_file)
DBC.plotDBC('WHEEL_SPEEDS',3,can_data,db_file)

DBC.plotDBC('SPEED',0,can_data,db_file)
DBC.plotDBC('SPEED',1,can_data,db_file)
DBC.plotDBC('SPEED',2,can_data,db_file)

DBC.plotDBC('UKNOWN186',0,can_data,db_file)

DBC.plotDBC('UKNOWN291',0,can_data,db_file)
DBC.plotDBC('UKNOWN291',1,can_data,db_file)
DBC.plotDBC('UKNOWN291',2,can_data,db_file)

DBC.plotDBC('UKNOWN295',0,can_data,db_file)
DBC.plotDBC('UKNOWN295',1,can_data,db_file)
DBC.plotDBC('UKNOWN295',2,can_data,db_file)

DBC.plotDBC('UKNOWN296',0,can_data,db_file)
DBC.plotDBC('UKNOWN296',1,can_data,db_file)
DBC.plotDBC('UKNOWN296',2,can_data,db_file)

# Unpack requires at least 64 bits to unpack (got 56)
# To resolve: Changed DSU_SPEED message in DBC file from 8 to 7 bytes
DBC.plotDBC('DSU_SPEED',0,can_data,db_file)

DBC.plotDBC('STEERING_IPAS_COMMA',0,can_data,db_file)
DBC.plotDBC('STEERING_IPAS_COMMA',1,can_data,db_file)
DBC.plotDBC('STEERING_IPAS_COMMA',2,can_data,db_file)
DBC.plotDBC('STEERING_IPAS_COMMA',3,can_data,db_file)
DBC.plotDBC('STEERING_IPAS_COMMA',4,can_data,db_file)
DBC.plotDBC('STEERING_IPAS_COMMA',5,can_data,db_file)
DBC.plotDBC('STEERING_IPAS_COMMA',6,can_data,db_file)

DBC.plotDBC('TRACK_A_0',0,can_data,db_file)
DBC.plotDBC('TRACK_A_0',1,can_data,db_file)
DBC.plotDBC('TRACK_A_0',2,can_data,db_file)
DBC.plotDBC('TRACK_A_0',3,can_data,db_file)
DBC.plotDBC('TRACK_A_0',4,can_data,db_file)
DBC.plotDBC('TRACK_A_0',5,can_data,db_file)
DBC.plotDBC('TRACK_A_0',6,can_data,db_file)

DBC.plotDBC('TRACK_A_1',0,can_data,db_file)
DBC.plotDBC('TRACK_A_1',1,can_data,db_file)
DBC.plotDBC('TRACK_A_1',2,can_data,db_file)
DBC.plotDBC('TRACK_A_1',3,can_data,db_file)
DBC.plotDBC('TRACK_A_1',4,can_data,db_file)
DBC.plotDBC('TRACK_A_1',5,can_data,db_file)
DBC.plotDBC('TRACK_A_1',6,can_data,db_file)

DBC.plotDBC('TRACK_A_2',0,can_data,db_file)
DBC.plotDBC('TRACK_A_2',1,can_data,db_file)
DBC.plotDBC('TRACK_A_2',2,can_data,db_file)
DBC.plotDBC('TRACK_A_2',3,can_data,db_file)
DBC.plotDBC('TRACK_A_2',4,can_data,db_file)
DBC.plotDBC('TRACK_A_2',5,can_data,db_file)
DBC.plotDBC('TRACK_A_2',6,can_data,db_file)

DBC.plotDBC('TRACK_B_0',0,can_data,db_file)
DBC.plotDBC('TRACK_B_0',1,can_data,db_file)
DBC.plotDBC('TRACK_B_0',2,can_data,db_file)
DBC.plotDBC('TRACK_B_0',3,can_data,db_file)

DBC.plotDBC('TRACK_B_1',0,can_data,db_file)
DBC.plotDBC('TRACK_B_1',1,can_data,db_file)
DBC.plotDBC('TRACK_B_1',2,can_data,db_file)
DBC.plotDBC('TRACK_B_1',3,can_data,db_file)

DBC.plotDBC('TRACK_B_2',0,can_data,db_file)
DBC.plotDBC('TRACK_B_2',1,can_data,db_file)
DBC.plotDBC('TRACK_B_2',2,can_data,db_file)
DBC.plotDBC('TRACK_B_2',3,can_data,db_file)

DBC.plotDBC('NEW_MSG_1',0,can_data,db_file)
DBC.plotDBC('NEW_MSG_1',1,can_data,db_file)

DBC.plotDBC('NEW_MSG_2',0,can_data,db_file)
DBC.plotDBC('NEW_MSG_2',1,can_data,db_file)

DBC.plotDBC('PCM_CRUISE',0,can_data,db_file)
DBC.plotDBC('PCM_CRUISE',1,can_data,db_file)
DBC.plotDBC('PCM_CRUISE',2,can_data,db_file)
DBC.plotDBC('PCM_CRUISE',3,can_data,db_file)
# Could not convert string to float: 'active'
# DBC.plotDBC('PCM_CRUISE',4,can_data,db_file)
DBC.plotDBC('PCM_CRUISE',5,can_data,db_file)

DBC.plotDBC('PCM_CRUISE_2',0,can_data,db_file)
# Could not convert string to float: 'ok'
# DBC.plotDBC('PCM_CRUISE_2',1,can_data,db_file)
DBC.plotDBC('PCM_CRUISE_2',2,can_data,db_file)
DBC.plotDBC('PCM_CRUISE_2',3,can_data,db_file)

DBC.plotDBC('GAS_COMMAND',0,can_data,db_file)
DBC.plotDBC('GAS_COMMAND',1,can_data,db_file)
DBC.plotDBC('GAS_COMMAND',2,can_data,db_file)
DBC.plotDBC('GAS_COMMAND',3,can_data,db_file)
DBC.plotDBC('GAS_COMMAND',4,can_data,db_file)

DBC.plotDBC('GAS_SENSOR',0,can_data,db_file)
DBC.plotDBC('GAS_SENSOR',1,can_data,db_file)
DBC.plotDBC('GAS_SENSOR',2,can_data,db_file)
DBC.plotDBC('GAS_SENSOR',3,can_data,db_file)
DBC.plotDBC('GAS_SENSOR',4,can_data,db_file)

DBC.plotDBC('BRAKE_MODULE',0,can_data,db_file)
DBC.plotDBC('BRAKE_MODULE',1,can_data,db_file)
DBC.plotDBC('BRAKE_MODULE',2,can_data,db_file)

# Unpack requires at least 64 bits to unpack (got 32)
# To resolve: Changed ACCELEROMETER message in DBC file from 8 to 4 bytes
DBC.plotDBC('ACCELEROMETER',0,can_data,db_file)
DBC.plotDBC('ACCELEROMETER',1,can_data,db_file)

DBC.plotDBC('BRAKE_MODULE2',0,can_data,db_file)

DBC.plotDBC('GAS_PEDAL',0,can_data,db_file)

DBC.plotDBC('STEER_TORQUE_SENSOR',0,can_data,db_file)
DBC.plotDBC('STEER_TORQUE_SENSOR',1,can_data,db_file)
DBC.plotDBC('STEER_TORQUE_SENSOR',2,can_data,db_file)
DBC.plotDBC('STEER_TORQUE_SENSOR',3,can_data,db_file)
DBC.plotDBC('STEER_TORQUE_SENSOR',4,can_data,db_file)

DBC.plotDBC('EPS_STATUS',0,can_data,db_file)
# Could not convert string to float: 'standby'
# DBC.plotDBC('EPS_STATUS',1,can_data,db_file)
DBC.plotDBC('EPS_STATUS',2,can_data,db_file)
DBC.plotDBC('EPS_STATUS',3,can_data,db_file)

DBC.plotDBC('STEERING_IPAS',0,can_data,db_file)
DBC.plotDBC('STEERING_IPAS',1,can_data,db_file)
DBC.plotDBC('STEERING_IPAS',2,can_data,db_file)
DBC.plotDBC('STEERING_IPAS',3,can_data,db_file)
DBC.plotDBC('STEERING_IPAS',4,can_data,db_file)
DBC.plotDBC('STEERING_IPAS',5,can_data,db_file)
DBC.plotDBC('STEERING_IPAS',6,can_data,db_file)

DBC.plotDBC('STEERING_LKA',0,can_data,db_file)
DBC.plotDBC('STEERING_LKA',1,can_data,db_file)
DBC.plotDBC('STEERING_LKA',2,can_data,db_file)
DBC.plotDBC('STEERING_LKA',3,can_data,db_file)
DBC.plotDBC('STEERING_LKA',4,can_data,db_file)
DBC.plotDBC('STEERING_LKA',5,can_data,db_file)

DBC.plotDBC('LEAD_INFO',0,can_data,db_file)
DBC.plotDBC('LEAD_INFO',1,can_data,db_file)
DBC.plotDBC('LEAD_INFO',2,can_data,db_file)

DBC.plotDBC('ACC_CONTROL',0,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',1,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',2,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',3,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',4,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',5,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',6,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',7,can_data,db_file)
DBC.plotDBC('ACC_CONTROL',8,can_data,db_file)

DBC.plotDBC('PCM_CRUISE_SM',0,can_data,db_file)
DBC.plotDBC('PCM_CRUISE_SM',1,can_data,db_file)
# Could not convert string to float: 'disabled'
# DBC.plotDBC('PCM_CRUISE_SM',2,can_data,db_file)
DBC.plotDBC('PCM_CRUISE_SM',3,can_data,db_file)

DBC.plotDBC('ESP_CONTROL',0,can_data,db_file)
DBC.plotDBC('ESP_CONTROL',1,can_data,db_file)

DBC.plotDBC('ACC_HUD',0,can_data,db_file)
DBC.plotDBC('ACC_HUD',1,can_data,db_file)
DBC.plotDBC('ACC_HUD',2,can_data,db_file)
DBC.plotDBC('ACC_HUD',3,can_data,db_file)

DBC.plotDBC('LKAS_HUD',0,can_data,db_file)
# Could not convert string to float: 'faded'
# DBC.plotDBC('LKAS_HUD',1,can_data,db_file)
# DBC.plotDBC('LKAS_HUD',2,can_data,db_file)
# Could not convert string to float: 'none'
# DBC.plotDBC('LKAS_HUD',3,can_data,db_file)
DBC.plotDBC('LKAS_HUD',4,can_data,db_file)
DBC.plotDBC('LKAS_HUD',5,can_data,db_file)
DBC.plotDBC('LKAS_HUD',6,can_data,db_file)
DBC.plotDBC('LKAS_HUD',7,can_data,db_file)
# Could not convert string to float: 'none'
# DBC.plotDBC('LKAS_HUD',8,can_data,db_file)
DBC.plotDBC('LKAS_HUD',9,can_data,db_file)
DBC.plotDBC('LKAS_HUD',10,can_data,db_file)
DBC.plotDBC('LKAS_HUD',11,can_data,db_file)
DBC.plotDBC('LKAS_HUD',12,can_data,db_file)
DBC.plotDBC('LKAS_HUD',13,can_data,db_file)

DBC.plotDBC('UI_SEETING',0,can_data,db_file)

# Could not convert string to float: 'none'
# DBC.plotDBC('STEERING_LEVERS',0,can_data,db_file)

DBC.plotDBC('SEATS_DOORS',0,can_data,db_file)
DBC.plotDBC('SEATS_DOORS',1,can_data,db_file)
DBC.plotDBC('SEATS_DOORS',2,can_data,db_file)
DBC.plotDBC('SEATS_DOORS',3,can_data,db_file)
DBC.plotDBC('SEATS_DOORS',4,can_data,db_file)

DBC.plotDBC('LIGHT_STALK',0,can_data,db_file)

# Could not convert string to float: 'none'
# DBC.plotDBC('RSA1',0,can_data,db_file)
DBC.plotDBC('RSA1',1,can_data,db_file)
DBC.plotDBC('RSA1',2,can_data,db_file)
DBC.plotDBC('RSA1',3,can_data,db_file)
DBC.plotDBC('RSA1',4,can_data,db_file)
# Could not convert string to float: 'none'
# DBC.plotDBC('RSA1',5,can_data,db_file)
# DBC.plotDBC('RSA1',6,can_data,db_file)
DBC.plotDBC('RSA1',7,can_data,db_file)
DBC.plotDBC('RSA1',8,can_data,db_file)
DBC.plotDBC('RSA1',9,can_data,db_file)
DBC.plotDBC('RSA1',10,can_data,db_file)
DBC.plotDBC('RSA1',11,can_data,db_file)
DBC.plotDBC('RSA1',12,can_data,db_file)

# Could not convert string to float: 'none'
# DBC.plotDBC('RSA2',0,can_data,db_file)
DBC.plotDBC('RSA2',1,can_data,db_file)
DBC.plotDBC('RSA2',2,can_data,db_file)
# Could not convert string to float: 'none'
# DBC.plotDBC('RSA2',3,can_data,db_file)
DBC.plotDBC('RSA2',4,can_data,db_file)
DBC.plotDBC('RSA2',5,can_data,db_file)
DBC.plotDBC('RSA2',6,can_data,db_file)
DBC.plotDBC('RSA2',7,can_data,db_file)
DBC.plotDBC('RSA2',8,can_data,db_file)
DBC.plotDBC('RSA2',9,can_data,db_file)
DBC.plotDBC('RSA2',10,can_data,db_file)
DBC.plotDBC('RSA2',11,can_data,db_file)
DBC.plotDBC('RSA2',12,can_data,db_file)
DBC.plotDBC('RSA2',13,can_data,db_file)

DBC.plotDBC('RSA3',0,can_data,db_file)
DBC.plotDBC('RSA3',1,can_data,db_file)
DBC.plotDBC('RSA3',2,can_data,db_file)
DBC.plotDBC('RSA3',3,can_data,db_file)
DBC.plotDBC('RSA3',4,can_data,db_file)
DBC.plotDBC('RSA3',5,can_data,db_file)
DBC.plotDBC('RSA3',6,can_data,db_file)
DBC.plotDBC('RSA3',7,can_data,db_file)
DBC.plotDBC('RSA3',8,can_data,db_file)

###############################################################################

# Write to File
KINEMATICS_Time = KINEMATICS_Yaw_Rate[:,0]
KINEMATICS_Yaw_Rate =  KINEMATICS_Yaw_Rate[:,1]
KINEMATICS_Steering_Torque = KINEMATICS_Steering_Torque[:,1]
KINEMATICS_Accel_Y = KINEMATICS_Accel_Y[:,1]

STEER_ANGLE_SENSOR_Time = STEER_ANGLE_SENSOR_Steer_Angle[:,0]
STEER_ANGLE_SENSOR_Steer_Angle = STEER_ANGLE_SENSOR_Steer_Angle[:,1]
STEER_ANGLE_SENSOR_Steer_Fraction = STEER_ANGLE_SENSOR_Steer_Fraction[:,1]
STEER_ANGLE_SENSOR_Steer_Rate = STEER_ANGLE_SENSOR_Steer_Rate[:,1]

BRAKE_Time = BRAKE_Brake_Amount[:,0]
BRAKE_Brake_Amount = BRAKE_Brake_Amount[:,1]
BRAKE_Brake_Pedal = BRAKE_Brake_Pedal[:,1]

WHEEL_SPEEDS_Time = WHEEL_SPEEDS_Wheel_Speed_FR[:,0]
WHEEL_SPEEDS_Wheel_Speed_FR = WHEEL_SPEEDS_Wheel_Speed_FR[:,1]
WHEEL_SPEEDS_Wheel_Speed_FL = WHEEL_SPEEDS_Wheel_Speed_FL[:,1]
WHEEL_SPEEDS_Wheel_Speed_RR = WHEEL_SPEEDS_Wheel_Speed_RR[:,1]
WHEEL_SPEEDS_Wheel_Speed_RL = WHEEL_SPEEDS_Wheel_Speed_RL[:,1]

SPEED_Time = SPEED_Encoder[:,0]
SPEED_Encoder = SPEED_Encoder[:,1]
SPEED_Speed = SPEED_Speed[:,1]
SPEED_Checksum = SPEED_Checksum[:,1]

UKNOWN186_Time = UKNOWN186_1[:,0]
UKNOWN186_1 = UKNOWN186_1[:,1]

UKNOWN291_Time = UKNOWN291_1[:,0]
UKNOWN291_1 = UKNOWN291_1[:,1]
UKNOWN291_2 = UKNOWN291_2[:,1]
UKNOWN291_3 = UKNOWN291_3[:,1]

UNKNOWN295_Time = UNKNOWN295_1[:,0]
UNKNOWN295_1 = UNKNOWN295_1[:,1]
UNKNOWN295_2 = UNKNOWN295_2[:,1]
UNKNOWN295_3 = UNKNOWN295_3[:,1]

UNKNOWN296_Time = UNKNOWN296_1[:,0]
UNKNOWN296_1 = UNKNOWN296_1[:,1]
UNKNOWN296_2 = UNKNOWN296_2[:,1]
UNKNOWN296_3 = UNKNOWN296_3[:,1]

# Unpack requires at least 64 bits to unpack (got 56)
# To resolve: Changed DSU_SPEED message in DBC file from 8 to 7 bytes
DSU_SPEED_Time = DSU_SPEED_Forward_Speed[:,0]
DSU_SPEED_Forward_Speed = DSU_SPEED_Forward_Speed[:,1]

STEERING_IPAS_COMMA_Time = STEERING_IPAS_COMMA_State[:,0]
STEERING_IPAS_COMMA_State = STEERING_IPAS_COMMA_State[:,1]
STEERING_IPAS_COMMA_Angle = STEERING_IPAS_COMMA_Angle[:,1]
STEERING_IPAS_COMMA_Set_Me_X10 = STEERING_IPAS_COMMA_Set_Me_X10[:,1]
STEERING_IPAS_COMMA_Direction_Cmd = STEERING_IPAS_COMMA_Direction_Cmd[:,1]
STEERING_IPAS_COMMA_Set_Me_X40 = STEERING_IPAS_COMMA_Set_Me_X40[:,1]
STEERING_IPAS_COMMA_Set_Me_X00 = STEERING_IPAS_COMMA_Set_Me_X00[:,1]
STEERING_IPAS_COMMA_Checksum = STEERING_IPAS_COMMA_Checksum[:,1]

TRACK_A_0_Time = TRACK_A_0_Counter[:,0]
TRACK_A_0_Counter = TRACK_A_0_Counter[:,1]
TRACK_A_0_Long_Dist = TRACK_A_0_Long_Dist[:,1]
TRACK_A_0_Lat_Dist = TRACK_A_0_Lat_Dist[:,1]
TRACK_A_0_New_Track = TRACK_A_0_New_Track[:,1]
TRACK_A_0_Rel_Speed = TRACK_A_0_Rel_Speed[:,1]
TRACK_A_0_Valid = TRACK_A_0_Valid[:,1]
TRACK_A_0_Checksum = TRACK_A_0_Checksum[:,1]

TRACK_A_1_Time = TRACK_A_1_Counter[:,0]
TRACK_A_1_Counter = TRACK_A_1_Counter[:,1]
TRACK_A_1_Long_Dist = TRACK_A_1_Long_Dist[:,1]
TRACK_A_1_Lat_Dist = TRACK_A_1_Lat_Dist[:,1]
TRACK_A_1_New_Track = TRACK_A_1_New_Track[:,1]
TRACK_A_1_Rel_Speed = TRACK_A_1_Rel_Speed[:,1]
TRACK_A_1_Valid = TRACK_A_1_Valid[:,1]
TRACK_A_1_Checksum = TRACK_A_1_Checksum[:,1]

TRACK_A_2_Time = TRACK_A_2_Counter[:,0]
TRACK_A_2_Counter = TRACK_A_2_Counter[:,1]
TRACK_A_2_Long_Dist = TRACK_A_2_Long_Dist[:,1]
TRACK_A_2_Lat_Dist = TRACK_A_2_Lat_Dist[:,1]
TRACK_A_2_New_Track = TRACK_A_2_New_Track[:,1]
TRACK_A_2_Rel_Speed = TRACK_A_2_Rel_Speed[:,1]
TRACK_A_2_Valid = TRACK_A_2_Valid[:,1]
TRACK_A_2_Checksum = TRACK_A_2_Checksum[:,1]

TRACK_A_3_Time = TRACK_A_3_Counter[:,0]
TRACK_A_3_Counter = TRACK_A_3_Counter[:,1]
TRACK_A_3_Long_Dist = TRACK_A_3_Long_Dist[:,1]
TRACK_A_3_Lat_Dist = TRACK_A_3_Lat_Dist[:,1]
TRACK_A_3_New_Track = TRACK_A_3_New_Track[:,1]
TRACK_A_3_Rel_Speed = TRACK_A_3_Rel_Speed[:,1]
TRACK_A_3_Valid = TRACK_A_3_Valid[:,1]
TRACK_A_3_Checksum = TRACK_A_3_Checksum[:,1]

TRACK_A_4_Time = TRACK_A_4_Counter[:,0]
TRACK_A_4_Counter = TRACK_A_4_Counter[:,1]
TRACK_A_4_Long_Dist = TRACK_A_4_Long_Dist[:,1]
TRACK_A_4_Lat_Dist = TRACK_A_4_Lat_Dist[:,1]
TRACK_A_4_New_Track = TRACK_A_4_New_Track[:,1]
TRACK_A_4_Rel_Speed = TRACK_A_4_Rel_Speed[:,1]
TRACK_A_4_Valid = TRACK_A_4_Valid[:,1]
TRACK_A_4_Checksum = TRACK_A_4_Checksum[:,1]

TRACK_A_5_Time = TRACK_A_5_Counter[:,0]
TRACK_A_5_Counter = TRACK_A_5_Counter[:,1]
TRACK_A_5_Long_Dist = TRACK_A_5_Long_Dist[:,1]
TRACK_A_5_Lat_Dist = TRACK_A_5_Lat_Dist[:,1]
TRACK_A_5_New_Track = TRACK_A_5_New_Track[:,1]
TRACK_A_5_Rel_Speed = TRACK_A_5_Rel_Speed[:,1]
TRACK_A_5_Valid = TRACK_A_5_Valid[:,1]
TRACK_A_5_Checksum = TRACK_A_5_Checksum[:,1]

TRACK_A_6_Time = TRACK_A_6_Counter[:,0]
TRACK_A_6_Counter = TRACK_A_6_Counter[:,1]
TRACK_A_6_Long_Dist = TRACK_A_6_Long_Dist[:,1]
TRACK_A_6_Lat_Dist = TRACK_A_6_Lat_Dist[:,1]
TRACK_A_6_New_Track = TRACK_A_6_New_Track[:,1]
TRACK_A_6_Rel_Speed = TRACK_A_6_Rel_Speed[:,1]
TRACK_A_6_Valid = TRACK_A_6_Valid[:,1]
TRACK_A_6_Checksum = TRACK_A_6_Checksum[:,1]

TRACK_A_7_Time = TRACK_A_7_Counter[:,0]
TRACK_A_7_Counter = TRACK_A_7_Counter[:,1]
TRACK_A_7_Long_Dist = TRACK_A_7_Long_Dist[:,1]
TRACK_A_7_Lat_Dist = TRACK_A_7_Lat_Dist[:,1]
TRACK_A_7_New_Track = TRACK_A_7_New_Track[:,1]
TRACK_A_7_Rel_Speed = TRACK_A_7_Rel_Speed[:,1]
TRACK_A_7_Valid = TRACK_A_7_Valid[:,1]
TRACK_A_7_Checksum = TRACK_A_7_Checksum[:,1]

TRACK_A_8_Time = TRACK_A_8_Counter[:,0]
TRACK_A_8_Counter = TRACK_A_8_Counter[:,1]
TRACK_A_8_Long_Dist = TRACK_A_8_Long_Dist[:,1]
TRACK_A_8_Lat_Dist = TRACK_A_8_Lat_Dist[:,1]
TRACK_A_8_New_Track = TRACK_A_8_New_Track[:,1]
TRACK_A_8_Rel_Speed = TRACK_A_8_Rel_Speed[:,1]
TRACK_A_8_Valid = TRACK_A_8_Valid[:,1]
TRACK_A_8_Checksum = TRACK_A_8_Checksum[:,1]

TRACK_A_9_Time = TRACK_A_9_Counter[:,0]
TRACK_A_9_Counter = TRACK_A_9_Counter[:,1]
TRACK_A_9_Long_Dist = TRACK_A_9_Long_Dist[:,1]
TRACK_A_9_Lat_Dist = TRACK_A_9_Lat_Dist[:,1]
TRACK_A_9_New_Track = TRACK_A_9_New_Track[:,1]
TRACK_A_9_Rel_Speed = TRACK_A_9_Rel_Speed[:,1]
TRACK_A_9_Valid = TRACK_A_9_Valid[:,1]
TRACK_A_9_Checksum = TRACK_A_9_Checksum[:,1]

TRACK_A_10_Time = TRACK_A_10_Counter[:,0]
TRACK_A_10_Counter = TRACK_A_10_Counter[:,1]
TRACK_A_10_Long_Dist = TRACK_A_10_Long_Dist[:,1]
TRACK_A_10_Lat_Dist = TRACK_A_10_Lat_Dist[:,1]
TRACK_A_10_New_Track = TRACK_A_10_New_Track[:,1]
TRACK_A_10_Rel_Speed = TRACK_A_10_Rel_Speed[:,1]
TRACK_A_10_Valid = TRACK_A_10_Valid[:,1]
TRACK_A_10_Checksum = TRACK_A_10_Checksum[:,1]

TRACK_A_11_Time = TRACK_A_11_Counter[:,0]
TRACK_A_11_Counter = TRACK_A_11_Counter[:,1]
TRACK_A_11_Long_Dist = TRACK_A_11_Long_Dist[:,1]
TRACK_A_11_Lat_Dist = TRACK_A_11_Lat_Dist[:,1]
TRACK_A_11_New_Track = TRACK_A_11_New_Track[:,1]
TRACK_A_11_Rel_Speed = TRACK_A_11_Rel_Speed[:,1]
TRACK_A_11_Valid = TRACK_A_11_Valid[:,1]
TRACK_A_11_Checksum = TRACK_A_11_Checksum[:,1]

TRACK_A_12_Time = TRACK_A_12_Counter[:,0]
TRACK_A_12_Counter = TRACK_A_12_Counter[:,1]
TRACK_A_12_Long_Dist = TRACK_A_12_Long_Dist[:,1]
TRACK_A_12_Lat_Dist = TRACK_A_12_Lat_Dist[:,1]
TRACK_A_12_New_Track = TRACK_A_12_New_Track[:,1]
TRACK_A_12_Rel_Speed = TRACK_A_12_Rel_Speed[:,1]
TRACK_A_12_Valid = TRACK_A_12_Valid[:,1]
TRACK_A_12_Checksum = TRACK_A_12_Checksum[:,1]

TRACK_A_13_Time = TRACK_A_13_Counter[:,0]
TRACK_A_13_Counter = TRACK_A_13_Counter[:,1]
TRACK_A_13_Long_Dist = TRACK_A_13_Long_Dist[:,1]
TRACK_A_13_Lat_Dist = TRACK_A_13_Lat_Dist[:,1]
TRACK_A_13_New_Track = TRACK_A_13_New_Track[:,1]
TRACK_A_13_Rel_Speed = TRACK_A_13_Rel_Speed[:,1]
TRACK_A_13_Valid = TRACK_A_13_Valid[:,1]
TRACK_A_13_Checksum = TRACK_A_13_Checksum[:,1]

TRACK_A_14_Time = TRACK_A_14_Counter[:,0]
TRACK_A_14_Counter = TRACK_A_14_Counter[:,1]
TRACK_A_14_Long_Dist = TRACK_A_14_Long_Dist[:,1]
TRACK_A_14_Lat_Dist = TRACK_A_14_Lat_Dist[:,1]
TRACK_A_14_New_Track = TRACK_A_14_New_Track[:,1]
TRACK_A_14_Rel_Speed = TRACK_A_14_Rel_Speed[:,1]
TRACK_A_14_Valid = TRACK_A_14_Valid[:,1]
TRACK_A_14_Checksum = TRACK_A_14_Checksum[:,1]

TRACK_A_15_Time = TRACK_A_15_Counter[:,0]
TRACK_A_15_Counter = TRACK_A_15_Counter[:,1]
TRACK_A_15_Long_Dist = TRACK_A_15_Long_Dist[:,1]
TRACK_A_15_Lat_Dist = TRACK_A_15_Lat_Dist[:,1]
TRACK_A_15_New_Track = TRACK_A_15_New_Track[:,1]
TRACK_A_15_Rel_Speed = TRACK_A_15_Rel_Speed[:,1]
TRACK_A_15_Valid = TRACK_A_15_Valid[:,1]
TRACK_A_15_Checksum = TRACK_A_15_Checksum[:,1]

TRACK_B_0_Time = TRACK_B_0_Counter[:,0]
TRACK_B_0_Counter = TRACK_B_0_Counter[:,1]
TRACK_B_0_Rel_Accel = TRACK_B_0_Rel_Accel[:,1]
TRACK_B_0_Score = TRACK_B_0_Score[:,1]
TRACK_B_0_Checksum = TRACK_B_0_Checksum[:,1]

TRACK_B_1_Time = TRACK_B_1_Counter[:,0]
TRACK_B_1_Counter = TRACK_B_1_Counter[:,1]
TRACK_B_1_Rel_Accel = TRACK_B_1_Rel_Accel[:,1]
TRACK_B_1_Score = TRACK_B_1_Score[:,1]
TRACK_B_1_Checksum = TRACK_B_1_Checksum[:,1]

TRACK_B_2_Time = TRACK_B_2_Counter[:,0]
TRACK_B_2_Counter = TRACK_B_2_Counter[:,1]
TRACK_B_2_Rel_Accel = TRACK_B_2_Rel_Accel[:,1]
TRACK_B_2_Score = TRACK_B_2_Score[:,1]
TRACK_B_2_Checksum = TRACK_B_2_Checksum[:,1]

TRACK_B_3_Time = TRACK_B_3_Counter[:,0]
TRACK_B_3_Counter = TRACK_B_3_Counter[:,1]
TRACK_B_3_Rel_Accel = TRACK_B_3_Rel_Accel[:,1]
TRACK_B_3_Score = TRACK_B_3_Score[:,1]
TRACK_B_3_Checksum = TRACK_B_3_Checksum[:,1]

TRACK_B_4_Time = TRACK_B_4_Counter[:,0]
TRACK_B_4_Counter = TRACK_B_4_Counter[:,1]
TRACK_B_4_Rel_Accel = TRACK_B_4_Rel_Accel[:,1]
TRACK_B_4_Score = TRACK_B_4_Score[:,1]
TRACK_B_4_Checksum = TRACK_B_4_Checksum[:,1]

TRACK_B_5_Time = TRACK_B_5_Counter[:,0]
TRACK_B_5_Counter = TRACK_B_5_Counter[:,1]
TRACK_B_5_Rel_Accel = TRACK_B_5_Rel_Accel[:,1]
TRACK_B_5_Score = TRACK_B_5_Score[:,1]
TRACK_B_5_Checksum = TRACK_B_5_Checksum[:,1]

TRACK_B_6_Time = TRACK_B_6_Counter[:,0]
TRACK_B_6_Counter = TRACK_B_6_Counter[:,1]
TRACK_B_6_Rel_Accel = TRACK_B_6_Rel_Accel[:,1]
TRACK_B_6_Score = TRACK_B_6_Score[:,1]
TRACK_B_6_Checksum = TRACK_B_6_Checksum[:,1]

TRACK_B_7_Time = TRACK_B_7_Counter[:,0]
TRACK_B_7_Counter = TRACK_B_7_Counter[:,1]
TRACK_B_7_Rel_Accel = TRACK_B_7_Rel_Accel[:,1]
TRACK_B_7_Score = TRACK_B_7_Score[:,1]
TRACK_B_7_Checksum = TRACK_B_7_Checksum[:,1]

TRACK_B_8_Time = TRACK_B_8_Counter[:,0]
TRACK_B_8_Counter = TRACK_B_8_Counter[:,1]
TRACK_B_8_Rel_Accel = TRACK_B_8_Rel_Accel[:,1]
TRACK_B_8_Score = TRACK_B_8_Score[:,1]
TRACK_B_8_Checksum = TRACK_B_8_Checksum[:,1]

TRACK_B_9_Time = TRACK_B_9_Counter[:,0]
TRACK_B_9_Counter = TRACK_B_9_Counter[:,1]
TRACK_B_9_Rel_Accel = TRACK_B_9_Rel_Accel[:,1]
TRACK_B_9_Score = TRACK_B_9_Score[:,1]
TRACK_B_9_Checksum = TRACK_B_9_Checksum[:,1]

TRACK_B_10_Time = TRACK_B_10_Counter[:,0]
TRACK_B_10_Counter = TRACK_B_10_Counter[:,1]
TRACK_B_10_Rel_Accel = TRACK_B_10_Rel_Accel[:,1]
TRACK_B_10_Score = TRACK_B_10_Score[:,1]
TRACK_B_10_Checksum = TRACK_B_10_Checksum[:,1]

TRACK_B_11_Time = TRACK_B_11_Counter[:,0]
TRACK_B_11_Counter = TRACK_B_11_Counter[:,1]
TRACK_B_11_Rel_Accel = TRACK_B_11_Rel_Accel[:,1]
TRACK_B_11_Score = TRACK_B_11_Score[:,1]
TRACK_B_11_Checksum = TRACK_B_11_Checksum[:,1]

TRACK_B_12_Time = TRACK_B_12_Counter[:,0]
TRACK_B_12_Counter = TRACK_B_12_Counter[:,1]
TRACK_B_12_Rel_Accel = TRACK_B_12_Rel_Accel[:,1]
TRACK_B_12_Score = TRACK_B_12_Score[:,1]
TRACK_B_12_Checksum = TRACK_B_12_Checksum[:,1]

TRACK_B_13_Time = TRACK_B_13_Counter[:,0]
TRACK_B_13_Counter = TRACK_B_13_Counter[:,1]
TRACK_B_13_Rel_Accel = TRACK_B_13_Rel_Accel[:,1]
TRACK_B_13_Score = TRACK_B_13_Score[:,1]
TRACK_B_13_Checksum = TRACK_B_13_Checksum[:,1]

TRACK_B_14_Time = TRACK_B_14_Counter[:,0]
TRACK_B_14_Counter = TRACK_B_14_Counter[:,1]
TRACK_B_14_Rel_Accel = TRACK_B_14_Rel_Accel[:,1]
TRACK_B_14_Score = TRACK_B_14_Score[:,1]
TRACK_B_14_Checksum = TRACK_B_14_Checksum[:,1]

TRACK_B_15_Time = TRACK_B_15_Counter[:,0]
TRACK_B_15_Counter = TRACK_B_15_Counter[:,1]
TRACK_B_15_Rel_Accel = TRACK_B_15_Rel_Accel[:,1]
TRACK_B_15_Score = TRACK_B_15_Score[:,1]
TRACK_B_15_Checksum = TRACK_B_15_Checksum[:,1]

NEW_MSG_1_Time = NEW_MSG_1_New_Signal_1[:,0]
NEW_MSG_1_New_Signal_1 = NEW_MSG_1_New_Signal_1[:,1]
NEW_MSG_1_New_Signal_2 = NEW_MSG_1_New_Signal_2[:,1]

NEW_MSG_2_Time = NEW_MSG_2_New_Signal_1[:,0]
NEW_MSG_2_New_Signal_1 = NEW_MSG_2_New_Signal_1[:,1]
NEW_MSG_2_New_Signal_2 = NEW_MSG_2_New_Signal_2[:,1]

PCM_CRUISE_Time = PCM_CRUISE_Gas_Released[:,0]
PCM_CRUISE_Gas_Released = PCM_CRUISE_Gas_Released[:,1]
PCM_CRUISE_Cruise_Active = PCM_CRUISE_Cruise_Active[:,1]
PCM_CRUISE_Standstill_On = PCM_CRUISE_Standstill_On[:,1]
PCM_CRUISE_Accel_Net = PCM_CRUISE_Accel_Net[:,1]
# Could not convert string to float: 'active'
# PCM_CRUISE_Cruise_State = PCM_CRUISE_Cruise_State[:,1]
PCM_CRUISE_Checksum = PCM_CRUISE_Checksum[:,1]

PCM_CRUISE_2_Time = PCM_CRUISE_2_Main_On[:,0]
PCM_CRUISE_2_Main_On = PCM_CRUISE_2_Main_On[:,1]
# Could not convert string to float: 'ok'
# PCM_CRUISE_2_Low_Speed_Lockout = PCM_CRUISE_2_Low_Speed_Lockout[:,1]
PCM_CRUISE_2_Set_Speed = PCM_CRUISE_2_Set_Speed[:,1]
PCM_CRUISE_2_Checksum = PCM_CRUISE_2_Checksum[:,1]

GAS_COMMAND_Time = GAS_COMMAND_Gas_Command[:,0]
GAS_COMMAND_Gas_Command = GAS_COMMAND_Gas_Command[:,1]
GAS_COMMAND_Gas_Command2 = GAS_COMMAND_Gas_Command2[:,1]
GAS_COMMAND_Enable = GAS_COMMAND_Enable[:,1]
GAS_COMMAND_Counter_Pedal = GAS_COMMAND_Counter_Pedal[:,1]
GAS_COMMAND_Checksum_Pedal = GAS_COMMAND_Checksum_Pedal[:,1]

GAS_SENSOR_Time = GAS_SENSOR_Interceptor_Gas[:,0]
GAS_SENSOR_Interceptor_Gas = GAS_SENSOR_Interceptor_Gas[:,1]
GAS_SENSOR_Interceptor_Gas2 = GAS_SENSOR_Interceptor_Gas2[:,1]
GAS_SENSOR_State = GAS_SENSOR_State[:,1]
GAS_SENSOR_Counter_Pedal = GAS_SENSOR_Counter_Pedal[:,1]
GAS_SENSOR_Checksum_Pedal = GAS_SENSOR_Checksum_Pedal[:,1]

BRAKE_MODULE_Time = BRAKE_MODULE_Brake_Pressure[:,0]
BRAKE_MODULE_Brake_Pressure = BRAKE_MODULE_Brake_Pressure[:,1]
BRAKE_MODULE_Brake_Position = BRAKE_MODULE_Brake_Position[:,1]
BRAKE_MODULE_Brake_Pressed = BRAKE_MODULE_Brake_Pressed[:,1]

# Unpack requires at least 64 bits to unpack (got 32)
# To resolve: Changed DSU_SPEED message in DBC file from 8 to 4 bytes
ACCELEROMETER_Time = ACCELEROMETER_Accel_X[:,0]
ACCELEROMETER_Accel_X = ACCELEROMETER_Accel_X[:,1]
ACCELEROMETER_Accel_Z = ACCELEROMETER_Accel_Z[:,1]

BRAKE_MODULE2_Time = BRAKE_MODULE2_Brake_Pressed[:,0]
BRAKE_MODULE2_Brake_Pressed = BRAKE_MODULE2_Brake_Pressed[:,1]

GAS_PEDAL_Time = GAS_PEDAL_Gas_Pedal[:,0]
GAS_PEDAL_Gas_Pedal = GAS_PEDAL_Gas_Pedal[:,1]

STEER_TORQUE_SENSOR_Time = STEER_TORQUE_SENSOR_Steer_Override[:,0]
STEER_TORQUE_SENSOR_Steer_Override = STEER_TORQUE_SENSOR_Steer_Override[:,1]
STEER_TORQUE_SENSOR_Steer_Torque_Driver = STEER_TORQUE_SENSOR_Steer_Torque_Driver[:,1]
STEER_TORQUE_SENSOR_Steer_Angle = STEER_TORQUE_SENSOR_Steer_Angle[:,1]
STEER_TORQUE_SENSOR_Steer_Torque_Eps = STEER_TORQUE_SENSOR_Steer_Torque_Eps[:,1]
STEER_TORQUE_SENSOR_Checksum = STEER_TORQUE_SENSOR_Checksum[:,1]

EPS_STATUS_IPAS_Time = EPS_STATUS_IPAS_State[:,0]
EPS_STATUS_IPAS_State = EPS_STATUS_IPAS_State[:,1]
# Could not convert string to float: 'standby'
# EPS_STATUS_LKA_State = EPS_STATUS_LKA_State[:,1]
EPS_STATUS_Type = EPS_STATUS_Type[:,1]
EPS_STATUS_Checksum = EPS_STATUS_Checksum[:,1]

STEERING_IPAS_Time = STEERING_IPAS_State[:,0]
STEERING_IPAS_State = STEERING_IPAS_State[:,1]
STEERING_IPAS_Angle = STEERING_IPAS_Angle[:,1]
STEERING_IPAS_Set_Me_X10 = STEERING_IPAS_Set_Me_X10[:,1]
STEERING_IPAS_Direction_Cmd = STEERING_IPAS_Direction_Cmd[:,1]
STEERING_IPAS_Set_Me_X40 = STEERING_IPAS_Set_Me_X40[:,1]
STEERING_IPAS_Set_Me_X00 = STEERING_IPAS_Set_Me_X00[:,1]
STEERING_IPAS_Checksum = STEERING_IPAS_Checksum[:,1]

STEERING_LKA_LKA_Time = STEERING_LKA_Set_Me_1[:,0]
STEERING_LKA_Set_Me_1 = STEERING_LKA_Set_Me_1[:,1]
STEERING_LKA_Counter = STEERING_LKA_Counter[:,1]
STEERING_LKA_Steer_Request = STEERING_LKA_Steer_Request[:,1]
STEERING_LKA_Steer_Torque_Cmd = STEERING_LKA_Steer_Torque_Cmd[:,1]
STEERING_LKA_LKA_State = STEERING_LKA_LKA_State[:,1]
STEERING_LKA_Checksum = STEERING_LKA_Checksum[:,1]

LEAD_INFO_Time = LEAD_INFO_Lead_Long_Dist[:,0]
LEAD_INFO_Lead_Long_Dist = LEAD_INFO_Lead_Long_Dist[:,1]
LEAD_INFO_Lead_Rel_Speed = LEAD_INFO_Lead_Rel_Speed[:,1]
LEAD_INFO_Checksum = LEAD_INFO_Checksum[:,1]

ACC_CONTROL_Time = ACC_CONTROL_Accel_Cmd[:,0]
ACC_CONTROL_Accel_Cmd = ACC_CONTROL_Accel_Cmd[:,1]
ACC_CONTROL_Set_Me_X01 = ACC_CONTROL_Set_Me_X01[:,1]
ACC_CONTROL_Mini_Car = ACC_CONTROL_Mini_Car[:,1]
ACC_CONTROL_Distance = ACC_CONTROL_Distance[:,1]
ACC_CONTROL_Set_Me_X3 = ACC_CONTROL_Set_Me_X3[:,1]
ACC_CONTROL_Release_Standstill = ACC_CONTROL_Release_Standstill[:,1]
ACC_CONTROL_Set_Me_1 = ACC_CONTROL_Set_Me_1[:,1]
ACC_CONTROL_Cancel_Req = ACC_CONTROL_Cancel_Req[:,1]
ACC_CONTROL_Checksum = ACC_CONTROL_Checksum[:,1]

PCM_CRUISE_SM_Time = PCM_CRUISE_SM_Main_On[:,0]
PCM_CRUISE_SM_Main_On = PCM_CRUISE_SM_Main_On[:,1]
PCM_CRUISE_SM_Distance_Lines = PCM_CRUISE_SM_Distance_Lines[:,1]
# Could not convert string to float: 'disabled'
# PCM_CRUISE_SM_Cruise_Control_State = PCM_CRUISE_SM_Cruise_Control_State[:,1]
PCM_CRUISE_SM_UI_Set_Speed = PCM_CRUISE_SM_UI_Set_Speed[:,1]

ESP_CONTROL_TC_Time = ESP_CONTROL_TC_Disabled[:,0]
ESP_CONTROL_TC_Disabled = ESP_CONTROL_TC_Disabled[:,1]
ESP_CONTROL_Brake_Lights_ACC = ESP_CONTROL_Brake_Lights_ACC[:,1]

ACC_HUD_Time = ACC_HUD_FCW[:,0]
ACC_HUD_FCW = ACC_HUD_FCW[:,1]
ACC_HUD_Set_Me_X20 = ACC_HUD_Set_Me_X20[:,1]
ACC_HUD_Set_Me_X10 = ACC_HUD_Set_Me_X10[:,1]
ACC_HUD_Set_Me_X80 = ACC_HUD_Set_Me_X80[:,1]

LKAS_HUD_Time = LKAS_HUD_Set_Me_X01[:,0]
LKAS_HUD_Set_Me_X01 = LKAS_HUD_Set_Me_X01[:,1]
# Could not convert string to float: 'faded'
# LKAS_HUD_Left_Line = LKAS_HUD_Left_Line[:,1]
# LKAS_HUD_Right_Line = LKAS_HUD_Right_Line[:,1]
# Could not convert string to float: 'none'
# LKAS_HUD_Barriers = LKAS_HUD_Barriers[:,1]
LKAS_HUD_LDA_Malfunction = LKAS_HUD_LDA_Malfunction[:,1]
LKAS_HUD_Adjusting_Camera = LKAS_HUD_Adjusting_Camera[:,1]
LKAS_HUD_Two_Beeps = LKAS_HUD_Two_Beeps[:,1]
LKAS_HUD_Set_Me_X01_2 = LKAS_HUD_Set_Me_X01_2[:,1]
# Could not convert string to float: 'none'
# LKAS_HUD_LDA_Alert = LKAS_HUD_LDA_Alert[:,1]
LKAS_HUD_Set_Me_X0C = LKAS_HUD_Set_Me_X0C[:,1]
LKAS_HUD_Repeated_Beeps = LKAS_HUD_Repeated_Beeps[:,1]
LKAS_HUD_Set_Me_X2C = LKAS_HUD_Set_Me_X2C[:,1]
LKAS_HUD_Set_Me_X38 = LKAS_HUD_Set_Me_X38[:,1]
LKAS_HUD_Set_Me_X02 = LKAS_HUD_Set_Me_X02[:,1]

UI_SEETING_Time = UI_SEETING_Units[:,0]
UI_SEETING_Units = UI_SEETING_Units[:,1]

# Could not convert string to float: 'none'
# STEERING_LEVERS_Time = STEERING_LEVERS_Turn_Signals[:,0]
# STEERING_LEVERS_Turn_Signals = STEERING_LEVERS_Turn_Signals[:,1]

SEATS_DOORS_Time = SEATS_DOORS_Door_Open_FL[:,0]
SEATS_DOORS_Door_Open_FL = SEATS_DOORS_Door_Open_FL[:,1]
SEATS_DOORS_Door_Open_FR = SEATS_DOORS_Door_Open_FR[:,1]
SEATS_DOORS_Door_Open_RR = SEATS_DOORS_Door_Open_RR[:,1]
SEATS_DOORS_Door_Open_RL = SEATS_DOORS_Door_Open_RL[:,1]
SEATS_DOORS_Seatbelt_Driver_Unlatched = SEATS_DOORS_Seatbelt_Driver_Unlatched[:,1]

LIGHT_STALK_Time = LIGHT_STALK_Auto_High_Beam[:,0]
LIGHT_STALK_Auto_High_Beam = LIGHT_STALK_Auto_High_Beam[:,1]

RSA1_Time = RSA1_Tsgngry1[:,0]
# Could not convert string to float: 'none'
# RSA1_Tsgn1 = RSA1_Tsgn1[:,1]
RSA1_Tsgngry1 = RSA1_Tsgngry1[:,1]
RSA1_Tsgnhlt1 = RSA1_Tsgnhlt1[:,1]
RSA1_Spdval1 = RSA1_Spdval1[:,1]
RSA1_Splsgn1 = RSA1_Splsgn1[:,1]
# Could not convert string to float: 'none'
# RSA1_Splsgn2 = RSA1_Splsgn2[:,1]
# RSA1_Tsgn2 = RSA1_Tsgn2[:,1]
RSA1_Tsgngry2 = RSA1_Tsgngry2[:,1]
RSA1_Tsgnhlt2 = RSA1_Tsgnhlt2[:,1]
RSA1_Spdval2 = RSA1_Spdval2[:,1]
RSA1_Bzrrq_p = RSA1_Bzrrq_p[:,1]
RSA1_Bzrrq_a = RSA1_Bzrrq_a[:,1]
RSA1_Syncid1 = RSA1_Syncid1[:,1]

# Could not convert string to float: 'none'
RSA2_Time = RSA2_Tsgngry3[:,0]
# RSA2_Tsgn3 = RSA2_Tsgn3[:,1])
RSA2_Tsgngry3 = RSA2_Tsgngry3[:,1]
RSA2_Tsgnhlt3 = RSA2_Tsgnhlt3[:,1]
# Could not convert string to float: 'none'
# RSA2_Splsgn3 = RSA2_Splsgn3[:,1]
RSA2_Splsgn4 = RSA2_Splsgn4[:,1]
RSA2_Tsgn4 = RSA2_Tsgn4[:,1]
RSA2_Tsgngry4 = RSA2_Tsgngry4[:,1]
RSA2_Tsgnhlt4 = RSA2_Tsgnhlt4[:,1]
RSA2_Dpsgnreq = RSA2_Dpsgnreq[:,1]
RSA2_Sgnnump = RSA2_Sgnnump[:,1]
RSA2_Sgnnuma = RSA2_Sgnnuma[:,1]
RSA2_Spdunt = RSA2_Spdunt[:,1]
RSA2_Tsrwmsg = RSA2_Tsrwmsg[:,1]
RSA2_Syncid2 = RSA2_Syncid2[:,1]

RSA3_Time = RSA3_Tsreqpd[:,0]
RSA3_Tsreqpd = RSA3_Tsreqpd[:,1]
RSA3_Tsrmsw = RSA3_Tsrmsw[:,1]
RSA3_Otsgnntm = RSA3_Otsgnntm[:,1]
RSA3_Ntlvlspd = RSA3_Ntlvlspd[:,1]
RSA3_Ovspntm = RSA3_Ovspntm[:,1]
RSA3_Ovspvall = RSA3_Ovspvall[:,1]
RSA3_Ovspvalm = RSA3_Ovspvalm[:,1]
RSA3_Ovspvalh = RSA3_Ovspvalh[:,1]
RSA3_Tsrspu = RSA3_Tsrspu[:,1]

Header = ['KINEMATICS_Time',\
          'KINEMATICS_Yaw_Rate',\
          'KINEMATICS_Steering_Torque',\
          'KINEMATICS_Accel_Y',\
          'STEER_ANGLE_SENSOR_Time',\
          'STEER_ANGLE_SENSOR_Steer_Angle',\
          'STEER_ANGLE_SENSOR_Steer_Fraction',\
          'STEER_ANGLE_SENSOR_Steer_Rate',\
          'BRAKE_Time',\
          'BRAKE_Brake_Amount',\
          'BRAKE_Brake_Pedal',\
          'WHEEL_SPEEDS_Time',\
          'WHEEL_SPEEDS_Wheel_Speed_FR',\
          'WHEEL_SPEEDS_Wheel_Speed_FL',\
          'WHEEL_SPEEDS_Wheel_Speed_RR',\
          'WHEEL_SPEEDS_Wheel_Speed_RL',\
          'SPEED_Time',\
          'SPEED_Encoder',\
          'SPEED_Speed',\
          'SPEED_Checksum',\
          'UKNOWN186_Time',\
          'UKNOWN186_1',\
          'UKNOWN291_Time',\
          'UKNOWN291_1',\
          'UKNOWN291_2',\
          'UKNOWN291_3',\
          'UNKNOWN295_Time',\
          'UNKNOWN295_1',\
          'UNKNOWN295_2',\
          'UNKNOWN295_3',\
          'UNKNOWN296_Time',\
          'UNKNOWN296_1',\
          'UNKNOWN296_2',\
          'UNKNOWN296_3',\
          'DSU_SPEED_Time',\
          'DSU_SPEED_Forward_Speed',\
          'STEERING_IPAS_COMMA_Time',\
          'STEERING_IPAS_COMMA_State',\
          'STEERING_IPAS_COMMA_Angle',\
          'STEERING_IPAS_COMMA_Set_Me_X10',\
          'STEERING_IPAS_COMMA_Direction_Cmd',\
          'STEERING_IPAS_COMMA_Set_Me_X40',\
          'STEERING_IPAS_COMMA_Set_Me_X00',\
          'STEERING_IPAS_COMMA_Checksum',\
          'TRACK_A_0_Time',\
          'TRACK_A_0_Counter',\
          'TRACK_A_0_Long_Dist',\
          'TRACK_A_0_Lat_Dist',\
          'TRACK_A_0_New_Track',\
          'TRACK_A_0_Rel_Speed',\
          'TRACK_A_0_Valid',\
          'TRACK_A_0_Checksum',\
          'TRACK_A_1_Time',\
          'TRACK_A_1_Counter',\
          'TRACK_A_1_Long_Dist',\
          'TRACK_A_1_Lat_Dist',\
          'TRACK_A_1_New_Track',\
          'TRACK_A_1_Rel_Speed',\
          'TRACK_A_1_Valid',\
          'TRACK_A_1_Checksum',\
          'TRACK_A_2_Time',\
          'TRACK_A_2_Counter',\
          'TRACK_A_2_Long_Dist',\
          'TRACK_A_2_Lat_Dist',\
          'TRACK_A_2_New_Track',\
          'TRACK_A_2_Rel_Speed',\
          'TRACK_A_2_Valid',\
          'TRACK_A_2_Checksum',\
          'TRACK_A_3_Time',\
          'TRACK_A_3_Counter',\
          'TRACK_A_3_Long_Dist',\
          'TRACK_A_3_Lat_Dist',\
          'TRACK_A_3_New_Track',\
          'TRACK_A_3_Rel_Speed',\
          'TRACK_A_3_Valid',\
          'TRACK_A_3_Checksum',\
          'TRACK_A_4_Time',\
          'TRACK_A_4_Counter',\
          'TRACK_A_4_Long_Dist',\
          'TRACK_A_4_Lat_Dist',\
          'TRACK_A_4_New_Track',\
          'TRACK_A_4_Rel_Speed',\
          'TRACK_A_4_Valid',\
          'TRACK_A_4_Checksum',\
          'TRACK_A_5_Time',\
          'TRACK_A_5_Counter',\
          'TRACK_A_5_Long_Dist',\
          'TRACK_A_5_Lat_Dist',\
          'TRACK_A_5_New_Track',\
          'TRACK_A_5_Rel_Speed',\
          'TRACK_A_5_Valid',\
          'TRACK_A_5_Checksum',\
          'TRACK_A_6_Time',\
          'TRACK_A_6_Counter',\
          'TRACK_A_6_Long_Dist',\
          'TRACK_A_6_Lat_Dist',\
          'TRACK_A_6_New_Track',\
          'TRACK_A_6_Rel_Speed',\
          'TRACK_A_6_Valid',\
          'TRACK_A_6_Checksum',\
          'TRACK_A_7_Time',\
          'TRACK_A_7_Counter',\
          'TRACK_A_7_Long_Dist',\
          'TRACK_A_7_Lat_Dist',\
          'TRACK_A_7_New_Track',\
          'TRACK_A_7_Rel_Speed',\
          'TRACK_A_7_Valid',\
          'TRACK_A_7_Checksum',\
          'TRACK_A_8_Time',\
          'TRACK_A_8_Counter',\
          'TRACK_A_8_Long_Dist',\
          'TRACK_A_8_Lat_Dist',\
          'TRACK_A_8_New_Track',\
          'TRACK_A_8_Rel_Speed',\
          'TRACK_A_8_Valid',\
          'TRACK_A_8_Checksum',\
          'TRACK_A_9_Time',\
          'TRACK_A_9_Counter',\
          'TRACK_A_9_Long_Dist',\
          'TRACK_A_9_Lat_Dist',\
          'TRACK_A_9_New_Track',\
          'TRACK_A_9_Rel_Speed',\
          'TRACK_A_9_Valid',\
          'TRACK_A_9_Checksum',\
          'TRACK_A_10_Time',\
          'TRACK_A_10_Counter',\
          'TRACK_A_10_Long_Dist',\
          'TRACK_A_10_Lat_Dist',\
          'TRACK_A_10_New_Track',\
          'TRACK_A_10_Rel_Speed',\
          'TRACK_A_10_Valid',\
          'TRACK_A_10_Checksum',\
          'TRACK_A_11_Time',\
          'TRACK_A_11_Counter',\
          'TRACK_A_11_Long_Dist',\
          'TRACK_A_11_Lat_Dist',\
          'TRACK_A_11_New_Track',\
          'TRACK_A_11_Rel_Speed',\
          'TRACK_A_11_Valid',\
          'TRACK_A_11_Checksum',\
          'TRACK_A_12_Time',\
          'TRACK_A_12_Counter',\
          'TRACK_A_12_Long_Dist',\
          'TRACK_A_12_Lat_Dist',\
          'TRACK_A_12_New_Track',\
          'TRACK_A_12_Rel_Speed',\
          'TRACK_A_12_Valid',\
          'TRACK_A_12_Checksum',\
          'TRACK_A_13_Time',\
          'TRACK_A_13_Counter',\
          'TRACK_A_13_Long_Dist',\
          'TRACK_A_13_Lat_Dist',\
          'TRACK_A_13_New_Track',\
          'TRACK_A_13_Rel_Speed',\
          'TRACK_A_13_Valid',\
          'TRACK_A_13_Checksum',\
          'TRACK_A_14_Time',\
          'TRACK_A_14_Counter',\
          'TRACK_A_14_Long_Dist',\
          'TRACK_A_14_Lat_Dist',\
          'TRACK_A_14_New_Track',\
          'TRACK_A_14_Rel_Speed',\
          'TRACK_A_14_Valid',\
          'TRACK_A_14_Checksum',\
          'TRACK_A_15_Time',\
          'TRACK_A_15_Counter',\
          'TRACK_A_15_Long_Dist',\
          'TRACK_A_15_Lat_Dist',\
          'TRACK_A_15_New_Track',\
          'TRACK_A_15_Rel_Speed',\
          'TRACK_A_15_Valid',\
          'TRACK_A_15_Checksum',\
          'TRACK_B_0_Time',\
          'TRACK_B_0_Counter',\
          'TRACK_B_0_Rel_Accel',\
          'TRACK_B_0_Score',\
          'TRACK_B_0_Checksum',\
          'TRACK_B_1_Time',\
          'TRACK_B_1_Counter',\
          'TRACK_B_1_Rel_Accel',\
          'TRACK_B_1_Score',\
          'TRACK_B_1_Checksum',\
          'TRACK_B_2_Time',\
          'TRACK_B_2_Counter',\
          'TRACK_B_2_Rel_Accel',\
          'TRACK_B_2_Score',\
          'TRACK_B_2_Checksum',\
          'TRACK_B_3_Time',\
          'TRACK_B_3_Counter',\
          'TRACK_B_3_Rel_Accel',\
          'TRACK_B_3_Score',\
          'TRACK_B_3_Checksum',\
          'TRACK_B_4_Time',\
          'TRACK_B_4_Counter',\
          'TRACK_B_4_Rel_Accel',\
          'TRACK_B_4_Score',\
          'TRACK_B_4_Checksum',\
          'TRACK_B_5_Time',\
          'TRACK_B_5_Counter',\
          'TRACK_B_5_Rel_Accel',\
          'TRACK_B_5_Score',\
          'TRACK_B_5_Checksum',\
          'TRACK_B_6_Time',\
          'TRACK_B_6_Counter',\
          'TRACK_B_6_Rel_Accel',\
          'TRACK_B_6_Score',\
          'TRACK_B_6_Checksum',\
          'TRACK_B_7_Time',\
          'TRACK_B_7_Counter',\
          'TRACK_B_7_Rel_Accel',\
          'TRACK_B_7_Score',\
          'TRACK_B_7_Checksum',\
          'TRACK_B_8_Time',\
          'TRACK_B_8_Counter',\
          'TRACK_B_8_Rel_Accel',\
          'TRACK_B_8_Score',\
          'TRACK_B_8_Checksum',\
          'TRACK_B_9_Time',\
          'TRACK_B_9_Counter',\
          'TRACK_B_9_Rel_Accel',\
          'TRACK_B_9_Score',\
          'TRACK_B_9_Checksum',\
          'TRACK_B_10_Time',\
          'TRACK_B_10_Counter',\
          'TRACK_B_10_Rel_Accel',\
          'TRACK_B_10_Score',\
          'TRACK_B_10_Checksum',\
          'TRACK_B_11_Time',\
          'TRACK_B_11_Counter',\
          'TRACK_B_11_Rel_Accel',\
          'TRACK_B_11_Score',\
          'TRACK_B_11_Checksum',\
          'TRACK_B_12_Time',\
          'TRACK_B_12_Counter',\
          'TRACK_B_12_Rel_Accel',\
          'TRACK_B_12_Score',\
          'TRACK_B_12_Checksum',\
          'TRACK_B_13_Time',\
          'TRACK_B_13_Counter',\
          'TRACK_B_13_Rel_Accel',\
          'TRACK_B_13_Score',\
          'TRACK_B_13_Checksum',\
          'TRACK_B_14_Time',\
          'TRACK_B_14_Counter',\
          'TRACK_B_14_Rel_Accel',\
          'TRACK_B_14_Score',\
          'TRACK_B_14_Checksum',\
          'TRACK_B_15_Time',\
          'TRACK_B_15_Counter',\
          'TRACK_B_15_Rel_Accel',\
          'TRACK_B_15_Score',\
          'TRACK_B_15_Checksum',\
          'TRACK_B_14_Counter',\
          'TRACK_B_14_Rel_Accel',\
          'TRACK_B_14_Score',\
          'TRACK_B_14_Checksum',\
          'TRACK_B_15_Time',\
          'TRACK_B_15_Counter',\
          'TRACK_B_15_Rel_Accel',\
          'TRACK_B_15_Score',\
          'TRACK_B_15_Checksum',\
          'NEW_MSG_1_Time',\
          'NEW_MSG_1_New_Signal_1',\
          'NEW_MSG_1_New_Signal_2',\
          'NEW_MSG_2_Time',\
          'NEW_MSG_2_New_Signal_1',\
          'NEW_MSG_2_New_Signal_2',\
          'PCM_CRUISE_Time',\
          'PCM_CRUISE_Gas_Released',\
          'PCM_CRUISE_Cruise_Active',\
          'PCM_CRUISE_Standstill_On',\
          'PCM_CRUISE_Accel_Net',\
          #'PCM_CRUISE_Cruise_State',\
          'PCM_CRUISE_Checksum',\
          'PCM_CRUISE_2_Time',\
          'PCM_CRUISE_2_Main_On',\
          #'PCM_CRUISE_2_Low_Speed_Lockout',\
          'PCM_CRUISE_2_Set_Speed',\
          'PCM_CRUISE_2_Checksum',\
          'GAS_COMMAND_Time',\
          'GAS_COMMAND_Gas_Command',\
          'GAS_COMMAND_Gas_Command2',\
          'GAS_COMMAND_Enable',\
          'GAS_COMMAND_Counter_Pedal',\
          'GAS_COMMAND_Checksum_Pedal',\
          'GAS_SENSOR_Time',\
          'GAS_SENSOR_Interceptor_Gas',\
          'GAS_SENSOR_Interceptor_Gas2',\
          'GAS_SENSOR_State',\
          'GAS_SENSOR_Counter_Pedal',\
          'GAS_SENSOR_Checksum_Pedal',\
          'BRAKE_MODULE_Time',\
          'BRAKE_MODULE_Brake_Pressure',\
          'BRAKE_MODULE_Brake_Position',\
          'BRAKE_MODULE_Brake_Pressed',\
          'ACCELEROMETER_Time',\
          'ACCELEROMETER_Accel_X',\
          'ACCELEROMETER_Accel_Z',\
          'BRAKE_MODULE2_Time',\
          'BRAKE_MODULE2_Brake_Pressed',\
          'GAS_PEDAL_Time',\
          'GAS_PEDAL_Gas_Pedal',\
          'STEER_TORQUE_SENSOR_Time',\
          'STEER_TORQUE_SENSOR_Steer_Override',\
          'STEER_TORQUE_SENSOR_Steer_Torque_Driver',\
          'STEER_TORQUE_SENSOR_Steer_Angle',\
          'STEER_TORQUE_SENSOR_Steer_Torque_Eps',\
          'STEER_TORQUE_SENSOR_Checksum',\
          'EPS_STATUS_IPAS_Time',\
          'EPS_STATUS_IPAS_State',\
          #'EPS_STATUS_LKA_State',\
          'EPS_STATUS_Type',\
          'EPS_STATUS_Checksum',\
          'STEERING_IPAS_Time',\
          'STEERING_IPAS_State',\
          'STEERING_IPAS_Angle',\
          'STEERING_IPAS_Set_Me_X10',\
          'STEERING_IPAS_Direction_Cmd',\
          'STEERING_IPAS_Set_Me_X40',\
          'STEERING_IPAS_Set_Me_X00',\
          'STEERING_IPAS_Checksum',\
          'STEERING_LKA_LKA_Time',\
          'STEERING_LKA_Set_Me_1',\
          'STEERING_LKA_Counter',\
          'STEERING_LKA_Steer_Request',\
          'STEERING_LKA_Steer_Torque_Cmd',\
          'STEERING_LKA_LKA_State',\
          'STEERING_LKA_Checksum',\
          'LEAD_INFO_Time',\
          'LEAD_INFO_Lead_Long_Dist',\
          'LEAD_INFO_Lead_Rel_Speed',\
          'LEAD_INFO_Checksum',\
          'ACC_CONTROL_Time',\
          'ACC_CONTROL_Accel_Cmd',\
          'ACC_CONTROL_Set_Me_X01',\
          'ACC_CONTROL_Mini_Car',\
          'ACC_CONTROL_Distance',\
          'ACC_CONTROL_Set_Me_X3',\
          'ACC_CONTROL_Release_Standstill',\
          'ACC_CONTROL_Set_Me_1',\
          'ACC_CONTROL_Cancel_Req',\
          'ACC_CONTROL_Checksum',\
          'PCM_CRUISE_SM_Time',\
          'PCM_CRUISE_SM_Main_On',\
          'PCM_CRUISE_SM_Distance_Lines',\
          #'PCM_CRUISE_SM_Cruise_Control_State',\
          'PCM_CRUISE_SM_UI_Set_Speed',\
          'ESP_CONTROL_TC_Time',\
          'ESP_CONTROL_TC_Disabled',\
          'ESP_CONTROL_Brake_Lights_ACC',\
          'ACC_HUD_Time',\
          'ACC_HUD_FCW',\
          'ACC_HUD_Set_Me_X20',\
          'ACC_HUD_Set_Me_X10',\
          'ACC_HUD_Set_Me_X80',\
          'LKAS_HUD_Time',\
          'LKAS_HUD_Set_Me_X01',\
          #'LKAS_HUD_Left_Line',\
          #'LKAS_HUD_Right_Line',\
          #'LKAS_HUD_Barriers',\
          'LKAS_HUD_LDA_Malfunction',\
          'LKAS_HUD_Adjusting_Camera',\
          'LKAS_HUD_Two_Beeps',\
          'LKAS_HUD_Set_Me_X01_2',\
          #'LKAS_HUD_LDA_Alert',\
          'LKAS_HUD_Set_Me_X0C',\
          'LKAS_HUD_Repeated_Beeps',\
          'LKAS_HUD_Set_Me_X2C',\
          'LKAS_HUD_Set_Me_X38',\
          'LKAS_HUD_Set_Me_X02',\
          'UI_SEETING_Time',\
          'UI_SEETING_Units',\
          #'STEERING_LEVERS_Time',\
          #'STEERING_LEVERS_Turn_Signals',\
          'SEATS_DOORS_Time',\
          'SEATS_DOORS_Door_Open_FL',\
          'SEATS_DOORS_Door_Open_FR',\
          'SEATS_DOORS_Door_Open_RR',\
          'SEATS_DOORS_Door_Open_RL',\
          'SEATS_DOORS_Seatbelt_Driver_Unlatched',\
          'LIGHT_STALK_Time',\
          'LIGHT_STALK_Auto_High_Beam',\
          'RSA1_Time',\
          #'RSA1_Tsgn1',\
          'RSA1_Tsgngry1',\
          'RSA1_Tsgnhlt1',\
          'RSA1_Spdval1',\
          'RSA1_Splsgn1',\
          #'RSA1_Splsgn2',\
          #'RSA1_Tsgn2',\
          'RSA1_Tsgngry2',\
          'RSA1_Tsgnhlt2',\
          'RSA1_Spdval2',\
          'RSA1_Bzrrq_p',\
          'RSA1_Bzrrq_a',\
          'RSA1_Syncid1',\
          'RSA2_Time',\
          #'RSA2_Tsgn3',\
          'RSA2_Tsgngry3',\
          'RSA2_Tsgnhlt3',\
          #'RSA2_Splsgn3',\
          'RSA2_Splsgn4',\
          'RSA2_Tsgn4',\
          'RSA2_Tsgngry4',\
          'RSA2_Tsgnhlt4',\
          'RSA2_Dpsgnreq',\
          'RSA2_Sgnnump',\
          'RSA2_Sgnnuma',\
          'RSA2_Spdunt',\
          'RSA2_Tsrwmsg',\
          'RSA2_Syncid2',\
          'RSA3_Time',\
          'RSA3_Tsreqpd',\
          'RSA3_Tsrmsw',\
          'RSA3_Otsgnntm',\
          'RSA3_Ntlvlspd',\
          'RSA3_Ovspntm',\
          'RSA3_Ovspvall',\
          'RSA3_Ovspvalm',\
          'RSA3_Ovspvalh',\
          'RSA3_Tsrspu']

df = pd.concat([pd.DataFrame(KINEMATICS_Time),\
                pd.DataFrame(KINEMATICS_Yaw_Rate),\
                pd.DataFrame(KINEMATICS_Steering_Torque),\
                pd.DataFrame(KINEMATICS_Accel_Y),\
                pd.DataFrame(STEER_ANGLE_SENSOR_Time),\
                pd.DataFrame(STEER_ANGLE_SENSOR_Steer_Angle),\
                pd.DataFrame(STEER_ANGLE_SENSOR_Steer_Fraction),\
                pd.DataFrame(STEER_ANGLE_SENSOR_Steer_Rate),\
                pd.DataFrame(BRAKE_Time),\
                pd.DataFrame(BRAKE_Brake_Amount),\
                pd.DataFrame(BRAKE_Brake_Pedal),\
                pd.DataFrame(WHEEL_SPEEDS_Time),\
                pd.DataFrame(WHEEL_SPEEDS_Wheel_Speed_FR),\
                pd.DataFrame(WHEEL_SPEEDS_Wheel_Speed_FL),\
                pd.DataFrame(WHEEL_SPEEDS_Wheel_Speed_RR),\
                pd.DataFrame(WHEEL_SPEEDS_Wheel_Speed_RL),\
                pd.DataFrame(SPEED_Time),\
                pd.DataFrame(SPEED_Encoder),\
                pd.DataFrame(SPEED_Speed),\
                pd.DataFrame(SPEED_Checksum),\
                pd.DataFrame(UKNOWN186_Time),\
                pd.DataFrame(UKNOWN186_1),\
                pd.DataFrame(UKNOWN291_Time),\
                pd.DataFrame(UKNOWN291_1),\
                pd.DataFrame(UKNOWN291_2),\
                pd.DataFrame(UKNOWN291_3),\
                pd.DataFrame(UNKNOWN295_Time),\
                pd.DataFrame(UNKNOWN295_1),\
                pd.DataFrame(UNKNOWN295_2),\
                pd.DataFrame(UNKNOWN295_3),\
                pd.DataFrame(UNKNOWN296_Time),\
                pd.DataFrame(UNKNOWN296_1),\
                pd.DataFrame(UNKNOWN296_2),\
                pd.DataFrame(UNKNOWN296_3),\
                pd.DataFrame(DSU_SPEED_Time),\
                pd.DataFrame(DSU_SPEED_Forward_Speed),\
                pd.DataFrame(STEERING_IPAS_COMMA_Time),\
                pd.DataFrame(STEERING_IPAS_COMMA_State),\
                pd.DataFrame(STEERING_IPAS_COMMA_Angle),\
                pd.DataFrame(STEERING_IPAS_COMMA_Set_Me_X10),\
                pd.DataFrame(STEERING_IPAS_COMMA_Direction_Cmd),\
                pd.DataFrame(STEERING_IPAS_COMMA_Set_Me_X40),\
                pd.DataFrame(STEERING_IPAS_COMMA_Set_Me_X00),\
                pd.DataFrame(STEERING_IPAS_COMMA_Checksum),\
                pd.DataFrame(TRACK_A_0_Time),\
                pd.DataFrame(TRACK_A_0_Counter),\
                pd.DataFrame(TRACK_A_0_Long_Dist),\
                pd.DataFrame(TRACK_A_0_Lat_Dist),\
                pd.DataFrame(TRACK_A_0_New_Track),\
                pd.DataFrame(TRACK_A_0_Rel_Speed),\
                pd.DataFrame(TRACK_A_0_Valid),\
                pd.DataFrame(TRACK_A_0_Checksum),\
                pd.DataFrame(TRACK_A_1_Time),\
                pd.DataFrame(TRACK_A_1_Counter),\
                pd.DataFrame(TRACK_A_1_Long_Dist),\
                pd.DataFrame(TRACK_A_1_Lat_Dist),\
                pd.DataFrame(TRACK_A_1_New_Track),\
                pd.DataFrame(TRACK_A_1_Rel_Speed),\
                pd.DataFrame(TRACK_A_1_Valid),\
                pd.DataFrame(TRACK_A_1_Checksum),\
                pd.DataFrame(TRACK_A_2_Time),\
                pd.DataFrame(TRACK_A_2_Counter),\
                pd.DataFrame(TRACK_A_2_Long_Dist),\
                pd.DataFrame(TRACK_A_2_Lat_Dist),\
                pd.DataFrame(TRACK_A_2_New_Track),\
                pd.DataFrame(TRACK_A_2_Rel_Speed),\
                pd.DataFrame(TRACK_A_2_Valid),\
                pd.DataFrame(TRACK_A_2_Checksum),\
                pd.DataFrame(TRACK_A_3_Time),\
                pd.DataFrame(TRACK_A_3_Counter),\
                pd.DataFrame(TRACK_A_3_Long_Dist),\
                pd.DataFrame(TRACK_A_3_Lat_Dist),\
                pd.DataFrame(TRACK_A_3_New_Track),\
                pd.DataFrame(TRACK_A_3_Rel_Speed),\
                pd.DataFrame(TRACK_A_3_Valid),\
                pd.DataFrame(TRACK_A_3_Checksum),\
                pd.DataFrame(TRACK_A_4_Time),\
                pd.DataFrame(TRACK_A_4_Counter),\
                pd.DataFrame(TRACK_A_4_Long_Dist),\
                pd.DataFrame(TRACK_A_4_Lat_Dist),\
                pd.DataFrame(TRACK_A_4_New_Track),\
                pd.DataFrame(TRACK_A_4_Rel_Speed),\
                pd.DataFrame(TRACK_A_4_Valid),\
                pd.DataFrame(TRACK_A_4_Checksum),\
                pd.DataFrame(TRACK_A_5_Time),\
                pd.DataFrame(TRACK_A_5_Counter),\
                pd.DataFrame(TRACK_A_5_Long_Dist),\
                pd.DataFrame(TRACK_A_5_Lat_Dist),\
                pd.DataFrame(TRACK_A_5_New_Track),\
                pd.DataFrame(TRACK_A_5_Rel_Speed),\
                pd.DataFrame(TRACK_A_5_Valid),\
                pd.DataFrame(TRACK_A_5_Checksum),\
                pd.DataFrame(TRACK_A_6_Time),\
                pd.DataFrame(TRACK_A_6_Counter),\
                pd.DataFrame(TRACK_A_6_Long_Dist),\
                pd.DataFrame(TRACK_A_6_Lat_Dist),\
                pd.DataFrame(TRACK_A_6_New_Track),\
                pd.DataFrame(TRACK_A_6_Rel_Speed),\
                pd.DataFrame(TRACK_A_6_Valid),\
                pd.DataFrame(TRACK_A_6_Checksum),\
                pd.DataFrame(TRACK_A_7_Time),\
                pd.DataFrame(TRACK_A_7_Counter),\
                pd.DataFrame(TRACK_A_7_Long_Dist),\
                pd.DataFrame(TRACK_A_7_Lat_Dist),\
                pd.DataFrame(TRACK_A_7_New_Track),\
                pd.DataFrame(TRACK_A_7_Rel_Speed),\
                pd.DataFrame(TRACK_A_7_Valid),\
                pd.DataFrame(TRACK_A_7_Checksum),\
                pd.DataFrame(TRACK_A_8_Time),\
                pd.DataFrame(TRACK_A_8_Counter),\
                pd.DataFrame(TRACK_A_8_Long_Dist),\
                pd.DataFrame(TRACK_A_8_Lat_Dist),\
                pd.DataFrame(TRACK_A_8_New_Track),\
                pd.DataFrame(TRACK_A_8_Rel_Speed),\
                pd.DataFrame(TRACK_A_8_Valid),\
                pd.DataFrame(TRACK_A_8_Checksum),\
                pd.DataFrame(TRACK_A_9_Time),\
                pd.DataFrame(TRACK_A_9_Counter),\
                pd.DataFrame(TRACK_A_9_Long_Dist),\
                pd.DataFrame(TRACK_A_9_Lat_Dist),\
                pd.DataFrame(TRACK_A_9_New_Track),\
                pd.DataFrame(TRACK_A_9_Rel_Speed),\
                pd.DataFrame(TRACK_A_9_Valid),\
                pd.DataFrame(TRACK_A_9_Checksum),\
                pd.DataFrame(TRACK_A_10_Time),\
                pd.DataFrame(TRACK_A_10_Counter),\
                pd.DataFrame(TRACK_A_10_Long_Dist),\
                pd.DataFrame(TRACK_A_10_Lat_Dist),\
                pd.DataFrame(TRACK_A_10_New_Track),\
                pd.DataFrame(TRACK_A_10_Rel_Speed),\
                pd.DataFrame(TRACK_A_10_Valid),\
                pd.DataFrame(TRACK_A_10_Checksum),\
                pd.DataFrame(TRACK_A_11_Time),\
                pd.DataFrame(TRACK_A_11_Counter),\
                pd.DataFrame(TRACK_A_11_Long_Dist),\
                pd.DataFrame(TRACK_A_11_Lat_Dist),\
                pd.DataFrame(TRACK_A_11_New_Track),\
                pd.DataFrame(TRACK_A_11_Rel_Speed),\
                pd.DataFrame(TRACK_A_11_Valid),\
                pd.DataFrame(TRACK_A_11_Checksum),\
                pd.DataFrame(TRACK_A_12_Time),\
                pd.DataFrame(TRACK_A_12_Counter),\
                pd.DataFrame(TRACK_A_12_Long_Dist),\
                pd.DataFrame(TRACK_A_12_Lat_Dist),\
                pd.DataFrame(TRACK_A_12_New_Track),\
                pd.DataFrame(TRACK_A_12_Rel_Speed),\
                pd.DataFrame(TRACK_A_12_Valid),\
                pd.DataFrame(TRACK_A_12_Checksum),\
                pd.DataFrame(TRACK_A_13_Time),\
                pd.DataFrame(TRACK_A_13_Counter),\
                pd.DataFrame(TRACK_A_13_Long_Dist),\
                pd.DataFrame(TRACK_A_13_Lat_Dist),\
                pd.DataFrame(TRACK_A_13_New_Track),\
                pd.DataFrame(TRACK_A_13_Rel_Speed),\
                pd.DataFrame(TRACK_A_13_Valid),\
                pd.DataFrame(TRACK_A_13_Checksum),\
                pd.DataFrame(TRACK_A_14_Time),\
                pd.DataFrame(TRACK_A_14_Counter),\
                pd.DataFrame(TRACK_A_14_Long_Dist),\
                pd.DataFrame(TRACK_A_14_Lat_Dist),\
                pd.DataFrame(TRACK_A_14_New_Track),\
                pd.DataFrame(TRACK_A_14_Rel_Speed),\
                pd.DataFrame(TRACK_A_14_Valid),\
                pd.DataFrame(TRACK_A_14_Checksum),\
                pd.DataFrame(TRACK_A_15_Time),\
                pd.DataFrame(TRACK_A_15_Counter),\
                pd.DataFrame(TRACK_A_15_Long_Dist),\
                pd.DataFrame(TRACK_A_15_Lat_Dist),\
                pd.DataFrame(TRACK_A_15_New_Track),\
                pd.DataFrame(TRACK_A_15_Rel_Speed),\
                pd.DataFrame(TRACK_A_15_Valid),\
                pd.DataFrame(TRACK_A_15_Checksum),\
                pd.DataFrame(TRACK_B_0_Time),\
                pd.DataFrame(TRACK_B_0_Counter),\
                pd.DataFrame(TRACK_B_0_Rel_Accel),\
                pd.DataFrame(TRACK_B_0_Score),\
                pd.DataFrame(TRACK_B_0_Checksum),\
                pd.DataFrame(TRACK_B_1_Time),\
                pd.DataFrame(TRACK_B_1_Counter),\
                pd.DataFrame(TRACK_B_1_Rel_Accel),\
                pd.DataFrame(TRACK_B_1_Score),\
                pd.DataFrame(TRACK_B_1_Checksum),\
                pd.DataFrame(TRACK_B_2_Time),\
                pd.DataFrame(TRACK_B_2_Counter),\
                pd.DataFrame(TRACK_B_2_Rel_Accel),\
                pd.DataFrame(TRACK_B_2_Score),\
                pd.DataFrame(TRACK_B_2_Checksum),\
                pd.DataFrame(TRACK_B_3_Time),\
                pd.DataFrame(TRACK_B_3_Counter),\
                pd.DataFrame(TRACK_B_3_Rel_Accel),\
                pd.DataFrame(TRACK_B_3_Score),\
                pd.DataFrame(TRACK_B_3_Checksum),\
                pd.DataFrame(TRACK_B_4_Time),\
                pd.DataFrame(TRACK_B_4_Counter),\
                pd.DataFrame(TRACK_B_4_Rel_Accel),\
                pd.DataFrame(TRACK_B_4_Score),\
                pd.DataFrame(TRACK_B_4_Checksum),\
                pd.DataFrame(TRACK_B_5_Time),\
                pd.DataFrame(TRACK_B_5_Counter),\
                pd.DataFrame(TRACK_B_5_Rel_Accel),\
                pd.DataFrame(TRACK_B_5_Score),\
                pd.DataFrame(TRACK_B_5_Checksum),\
                pd.DataFrame(TRACK_B_6_Time),\
                pd.DataFrame(TRACK_B_6_Counter),\
                pd.DataFrame(TRACK_B_6_Rel_Accel),\
                pd.DataFrame(TRACK_B_6_Score),\
                pd.DataFrame(TRACK_B_6_Checksum),\
                pd.DataFrame(TRACK_B_7_Time),\
                pd.DataFrame(TRACK_B_7_Counter),\
                pd.DataFrame(TRACK_B_7_Rel_Accel),\
                pd.DataFrame(TRACK_B_7_Score),\
                pd.DataFrame(TRACK_B_7_Checksum),\
                pd.DataFrame(TRACK_B_8_Time),\
                pd.DataFrame(TRACK_B_8_Counter),\
                pd.DataFrame(TRACK_B_8_Rel_Accel),\
                pd.DataFrame(TRACK_B_8_Score),\
                pd.DataFrame(TRACK_B_8_Checksum),\
                pd.DataFrame(TRACK_B_9_Time),\
                pd.DataFrame(TRACK_B_9_Counter),\
                pd.DataFrame(TRACK_B_9_Rel_Accel),\
                pd.DataFrame(TRACK_B_9_Score),\
                pd.DataFrame(TRACK_B_9_Checksum),\
                pd.DataFrame(TRACK_B_10_Time),\
                pd.DataFrame(TRACK_B_10_Counter),\
                pd.DataFrame(TRACK_B_10_Rel_Accel),\
                pd.DataFrame(TRACK_B_10_Score),\
                pd.DataFrame(TRACK_B_10_Checksum),\
                pd.DataFrame(TRACK_B_11_Time),\
                pd.DataFrame(TRACK_B_11_Counter),\
                pd.DataFrame(TRACK_B_11_Rel_Accel),\
                pd.DataFrame(TRACK_B_11_Score),\
                pd.DataFrame(TRACK_B_11_Checksum),\
                pd.DataFrame(TRACK_B_12_Time),\
                pd.DataFrame(TRACK_B_12_Counter),\
                pd.DataFrame(TRACK_B_12_Rel_Accel),\
                pd.DataFrame(TRACK_B_12_Score),\
                pd.DataFrame(TRACK_B_12_Checksum),\
                pd.DataFrame(TRACK_B_13_Time),\
                pd.DataFrame(TRACK_B_13_Counter),\
                pd.DataFrame(TRACK_B_13_Rel_Accel),\
                pd.DataFrame(TRACK_B_13_Score),\
                pd.DataFrame(TRACK_B_13_Checksum),\
                pd.DataFrame(TRACK_B_14_Time),\
                pd.DataFrame(TRACK_B_14_Counter),\
                pd.DataFrame(TRACK_B_14_Rel_Accel),\
                pd.DataFrame(TRACK_B_14_Score),\
                pd.DataFrame(TRACK_B_14_Checksum),\
                pd.DataFrame(TRACK_B_15_Time),\
                pd.DataFrame(TRACK_B_15_Counter),\
                pd.DataFrame(TRACK_B_15_Rel_Accel),\
                pd.DataFrame(TRACK_B_15_Score),\
                pd.DataFrame(TRACK_B_15_Checksum),\
                pd.DataFrame(TRACK_B_14_Counter),\
                pd.DataFrame(TRACK_B_14_Rel_Accel),\
                pd.DataFrame(TRACK_B_14_Score),\
                pd.DataFrame(TRACK_B_14_Checksum),\
                pd.DataFrame(TRACK_B_15_Time),\
                pd.DataFrame(TRACK_B_15_Counter),\
                pd.DataFrame(TRACK_B_15_Rel_Accel),\
                pd.DataFrame(TRACK_B_15_Score),\
                pd.DataFrame(TRACK_B_15_Checksum),\
                pd.DataFrame(NEW_MSG_1_Time),\
                pd.DataFrame(NEW_MSG_1_New_Signal_1),\
                pd.DataFrame(NEW_MSG_1_New_Signal_2),\
                pd.DataFrame(NEW_MSG_2_Time),\
                pd.DataFrame(NEW_MSG_2_New_Signal_1),\
                pd.DataFrame(NEW_MSG_2_New_Signal_2),\
                pd.DataFrame(PCM_CRUISE_Time),\
                pd.DataFrame(PCM_CRUISE_Gas_Released),\
                pd.DataFrame(PCM_CRUISE_Cruise_Active),\
                pd.DataFrame(PCM_CRUISE_Standstill_On),\
                pd.DataFrame(PCM_CRUISE_Accel_Net),\
                #pd.DataFrame(PCM_CRUISE_Cruise_State),\
                pd.DataFrame(PCM_CRUISE_Checksum),\
                pd.DataFrame(PCM_CRUISE_2_Time),\
                pd.DataFrame(PCM_CRUISE_2_Main_On),\
                #pd.DataFrame(PCM_CRUISE_2_Low_Speed_Lockout),\
                pd.DataFrame(PCM_CRUISE_2_Set_Speed),\
                pd.DataFrame(PCM_CRUISE_2_Checksum),\
                pd.DataFrame(GAS_COMMAND_Time),\
                pd.DataFrame(GAS_COMMAND_Gas_Command),\
                pd.DataFrame(GAS_COMMAND_Gas_Command2),\
                pd.DataFrame(GAS_COMMAND_Enable),\
                pd.DataFrame(GAS_COMMAND_Counter_Pedal),\
                pd.DataFrame(GAS_COMMAND_Checksum_Pedal),\
                pd.DataFrame(GAS_SENSOR_Time),\
                pd.DataFrame(GAS_SENSOR_Interceptor_Gas),\
                pd.DataFrame(GAS_SENSOR_Interceptor_Gas2),\
                pd.DataFrame(GAS_SENSOR_State),\
                pd.DataFrame(GAS_SENSOR_Counter_Pedal),\
                pd.DataFrame(GAS_SENSOR_Checksum_Pedal),\
                pd.DataFrame(BRAKE_MODULE_Time),\
                pd.DataFrame(BRAKE_MODULE_Brake_Pressure),\
                pd.DataFrame(BRAKE_MODULE_Brake_Position),\
                pd.DataFrame(BRAKE_MODULE_Brake_Pressed),\
                pd.DataFrame(ACCELEROMETER_Time),\
                pd.DataFrame(ACCELEROMETER_Accel_X),\
                pd.DataFrame(ACCELEROMETER_Accel_Z),\
                pd.DataFrame(BRAKE_MODULE2_Time),\
                pd.DataFrame(BRAKE_MODULE2_Brake_Pressed),\
                pd.DataFrame(GAS_PEDAL_Time),\
                pd.DataFrame(GAS_PEDAL_Gas_Pedal),\
                pd.DataFrame(STEER_TORQUE_SENSOR_Time),\
                pd.DataFrame(STEER_TORQUE_SENSOR_Steer_Override),\
                pd.DataFrame(STEER_TORQUE_SENSOR_Steer_Torque_Driver),\
                pd.DataFrame(STEER_TORQUE_SENSOR_Steer_Angle),\
                pd.DataFrame(STEER_TORQUE_SENSOR_Steer_Torque_Eps),\
                pd.DataFrame(STEER_TORQUE_SENSOR_Checksum),\
                pd.DataFrame(EPS_STATUS_IPAS_Time),\
                pd.DataFrame(EPS_STATUS_IPAS_State),\
                #pd.DataFrame(EPS_STATUS_LKA_State),\
                pd.DataFrame(EPS_STATUS_Type),\
                pd.DataFrame(EPS_STATUS_Checksum),\
                pd.DataFrame(STEERING_IPAS_Time),\
                pd.DataFrame(STEERING_IPAS_State),\
                pd.DataFrame(STEERING_IPAS_Angle),\
                pd.DataFrame(STEERING_IPAS_Set_Me_X10),\
                pd.DataFrame(STEERING_IPAS_Direction_Cmd),\
                pd.DataFrame(STEERING_IPAS_Set_Me_X40),\
                pd.DataFrame(STEERING_IPAS_Set_Me_X00),\
                pd.DataFrame(STEERING_IPAS_Checksum),\
                pd.DataFrame(STEERING_LKA_LKA_Time),\
                pd.DataFrame(STEERING_LKA_Set_Me_1),\
                pd.DataFrame(STEERING_LKA_Counter),\
                pd.DataFrame(STEERING_LKA_Steer_Request),\
                pd.DataFrame(STEERING_LKA_Steer_Torque_Cmd),\
                pd.DataFrame(STEERING_LKA_LKA_State),\
                pd.DataFrame(STEERING_LKA_Checksum),\
                pd.DataFrame(LEAD_INFO_Time),\
                pd.DataFrame(LEAD_INFO_Lead_Long_Dist),\
                pd.DataFrame(LEAD_INFO_Lead_Rel_Speed),\
                pd.DataFrame(LEAD_INFO_Checksum),\
                pd.DataFrame(ACC_CONTROL_Time),\
                pd.DataFrame(ACC_CONTROL_Accel_Cmd),\
                pd.DataFrame(ACC_CONTROL_Set_Me_X01),\
                pd.DataFrame(ACC_CONTROL_Mini_Car),\
                pd.DataFrame(ACC_CONTROL_Distance),\
                pd.DataFrame(ACC_CONTROL_Set_Me_X3),\
                pd.DataFrame(ACC_CONTROL_Release_Standstill),\
                pd.DataFrame(ACC_CONTROL_Set_Me_1),\
                pd.DataFrame(ACC_CONTROL_Cancel_Req),\
                pd.DataFrame(ACC_CONTROL_Checksum),\
                pd.DataFrame(PCM_CRUISE_SM_Time),\
                pd.DataFrame(PCM_CRUISE_SM_Main_On),\
                pd.DataFrame(PCM_CRUISE_SM_Distance_Lines),\
                #pd.DataFrame(PCM_CRUISE_SM_Cruise_Control_State),\
                pd.DataFrame(PCM_CRUISE_SM_UI_Set_Speed),\
                pd.DataFrame(ESP_CONTROL_TC_Time),\
                pd.DataFrame(ESP_CONTROL_TC_Disabled),\
                pd.DataFrame(ESP_CONTROL_Brake_Lights_ACC),\
                pd.DataFrame(ACC_HUD_Time),\
                pd.DataFrame(ACC_HUD_FCW),\
                pd.DataFrame(ACC_HUD_Set_Me_X20),\
                pd.DataFrame(ACC_HUD_Set_Me_X10),\
                pd.DataFrame(ACC_HUD_Set_Me_X80),\
                pd.DataFrame(LKAS_HUD_Time),\
                pd.DataFrame(LKAS_HUD_Set_Me_X01),\
                #pd.DataFrame(LKAS_HUD_Left_Line),\
                #pd.DataFrame(LKAS_HUD_Right_Line),\
                #pd.DataFrame(LKAS_HUD_Barriers),\
                pd.DataFrame(LKAS_HUD_LDA_Malfunction),\
                pd.DataFrame(LKAS_HUD_Adjusting_Camera),\
                pd.DataFrame(LKAS_HUD_Two_Beeps),\
                pd.DataFrame(LKAS_HUD_Set_Me_X01_2),\
                #pd.DataFrame(LKAS_HUD_LDA_Alert),\
                pd.DataFrame(LKAS_HUD_Set_Me_X0C),\
                pd.DataFrame(LKAS_HUD_Repeated_Beeps),\
                pd.DataFrame(LKAS_HUD_Set_Me_X2C),\
                pd.DataFrame(LKAS_HUD_Set_Me_X38),\
                pd.DataFrame(LKAS_HUD_Set_Me_X02),\
                pd.DataFrame(UI_SEETING_Time),\
                pd.DataFrame(UI_SEETING_Units),\
                #pd.DataFrame(STEERING_LEVERS_Time),\
                #pd.DataFrame(STEERING_LEVERS_Turn_Signals),\
                pd.DataFrame(SEATS_DOORS_Time),\
                pd.DataFrame(SEATS_DOORS_Door_Open_FL),\
                pd.DataFrame(SEATS_DOORS_Door_Open_FR),\
                pd.DataFrame(SEATS_DOORS_Door_Open_RR),\
                pd.DataFrame(SEATS_DOORS_Door_Open_RL),\
                pd.DataFrame(SEATS_DOORS_Seatbelt_Driver_Unlatched),\
                pd.DataFrame(LIGHT_STALK_Time),\
                pd.DataFrame(LIGHT_STALK_Auto_High_Beam),\
                pd.DataFrame(RSA1_Time),\
                #pd.DataFrame(RSA1_Tsgn1),\
                pd.DataFrame(RSA1_Tsgngry1),\
                pd.DataFrame(RSA1_Tsgnhlt1),\
                pd.DataFrame(RSA1_Spdval1),\
                pd.DataFrame(RSA1_Splsgn1),\
                #pd.DataFrame(RSA1_Splsgn2),\
                #pd.DataFrame(RSA1_Tsgn2),\
                pd.DataFrame(RSA1_Tsgngry2),\
                pd.DataFrame(RSA1_Tsgnhlt2),\
                pd.DataFrame(RSA1_Spdval2),\
                pd.DataFrame(RSA1_Bzrrq_p),\
                pd.DataFrame(RSA1_Bzrrq_a),\
                pd.DataFrame(RSA1_Syncid1),\
                pd.DataFrame(RSA2_Time),\
                #pd.DataFrame(RSA2_Tsgn3),\
                pd.DataFrame(RSA2_Tsgngry3),\
                pd.DataFrame(RSA2_Tsgnhlt3),\
                #pd.DataFrame(RSA2_Splsgn3),\
                pd.DataFrame(RSA2_Splsgn4),\
                pd.DataFrame(RSA2_Tsgn4),\
                pd.DataFrame(RSA2_Tsgngry4),\
                pd.DataFrame(RSA2_Tsgnhlt4),\
                pd.DataFrame(RSA2_Dpsgnreq),\
                pd.DataFrame(RSA2_Sgnnump),\
                pd.DataFrame(RSA2_Sgnnuma),\
                pd.DataFrame(RSA2_Spdunt),\
                pd.DataFrame(RSA2_Tsrwmsg),\
                pd.DataFrame(RSA2_Syncid2),\
                pd.DataFrame(RSA3_Time),\
                pd.DataFrame(RSA3_Tsreqpd),\
                pd.DataFrame(RSA3_Tsrmsw),\
                pd.DataFrame(RSA3_Otsgnntm),\
                pd.DataFrame(RSA3_Ntlvlspd),\
                pd.DataFrame(RSA3_Ovspntm),\
                pd.DataFrame(RSA3_Ovspvall),\
                pd.DataFrame(RSA3_Ovspvalm),\
                pd.DataFrame(RSA3_Ovspvalh),\
                pd.DataFrame(RSA3_Tsrspu)],
                axis=1)

df.to_csv('../../Data/RAV-4_Giraffe_Data/Processed_Data/2020-03-24-16-42-54_CAN_Messages_Decoded_Messages2.csv',header = Header)