% Plot DBC Radar Data
clear all; close all; clc;
set(0,'DefaultFigureWindowStyle','docked');

% Load csv file
data = csvread('C:\Users\glee\Documents\UA\Research\Sprinkle\Data\RAV-4_Giraffe_Data\Processed_Data\2020-03-24-16-42-54_CAN_Messages_Decoded_Messages.csv',1,0);

% Initialize variables
num_idx = data(:,1);
num_trks = 16;
radar_start_idx = 46;
radar_data_length = sum(data(:,radar_start_idx)>0);
track_A_time = zeros(radar_data_length,num_trks);
track_A_counter = zeros(radar_data_length,num_trks);
track_A_lon_dist = zeros(radar_data_length,num_trks);
track_A_lat_dist = zeros(radar_data_length,num_trks);
track_A_new_track = zeros(radar_data_length,num_trks);
track_A_rel_speed = zeros(radar_data_length,num_trks);
track_A_valid = zeros(radar_data_length,num_trks);
track_A_checksum = zeros(radar_data_length,num_trks);
track_B_time = zeros(radar_data_length,num_trks);
track_B_counter = zeros(radar_data_length,num_trks);
track_B_rel_accel = zeros(radar_data_length,num_trks);
track_B_score = zeros(radar_data_length,num_trks);
track_B_checksum = zeros(radar_data_length,num_trks);
    
% Load TRACK A/B data 
for trk_idx = 1:num_trks
    track_A_time(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx);
    track_A_counter(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx+1);
    track_A_lon_dist(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx+2);
    track_A_lat_dist(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx+3);
    track_A_new_track(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx+4);
    track_A_rel_speed(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx+5);
    track_A_valid(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx+6);
    track_A_checksum(:,trk_idx) = data(1:radar_data_length,8*(trk_idx-1)+radar_start_idx+7);    
    track_B_time(:,trk_idx) = data(1:radar_data_length,5*(trk_idx-1)+radar_start_idx+128);
    track_B_counter(:,trk_idx) = data(1:radar_data_length,5*(trk_idx-1)+radar_start_idx+129);
    track_B_rel_accel(:,trk_idx) = data(1:radar_data_length,5*(trk_idx-1)+radar_start_idx+130);
    track_B_score(:,trk_idx) = data(1:radar_data_length,5*(trk_idx-1)+radar_start_idx+131);
    track_B_checksum(:,trk_idx) = data(1:radar_data_length,5*(trk_idx-1)+radar_start_idx+132);
end

% Synchronize Track A/B data
% radar_syncA_data_length = length(start_idxA:last_idxA);
% radar_syncB_data_length = length(start_idxB:last_idxB);
% track_A_time_sync = zeros(radar_syncA_data_length,num_trks);
% track_A_counter_sync = zeros(radar_syncA_data_length,num_trks);
% track_A_lon_dist_sync = zeros(radar_syncA_data_length,num_trks);
% track_A_lat_dist_sync = zeros(radar_syncA_data_length,num_trks);
% track_A_new_track_sync = zeros(radar_syncA_data_length,num_trks);
% track_A_rel_speed_sync = zeros(radar_syncA_data_length,num_trks);
% track_A_valid_sync = zeros(radar_syncA_data_length,num_trks);
% track_A_checksum_sync = zeros(radar_syncA_data_length,num_trks);
% track_B_time_sync = zeros(radar_syncB_data_length,num_trks);
% track_B_counter_sync = zeros(radar_syncB_data_length,num_trks);
% track_B_rel_accel_sync = zeros(radar_syncB_data_length,num_trks);
% track_B_score_sync = zeros(radar_syncB_data_length,num_trks);
% track_B_checksum_sync = zeros(radar_syncB_data_length,num_trks);
for trk_idx = 1:num_trks
    start_idxA = find(track_A_counter(:,trk_idx)==0,1,'first');
    last_idxA = find(track_A_counter(:,trk_idx)==255,1,'last');
    track_A_time_sync(:,trk_idx) = track_A_time(start_idxA:last_idxA,trk_idx);
    track_A_counter_sync(:,trk_idx) = track_A_counter(start_idxA:last_idxA,trk_idx);
    track_A_lon_dist_sync(:,trk_idx) = track_A_lon_dist(start_idxA:last_idxA,trk_idx);
    track_A_lat_dist_sync(:,trk_idx) = track_A_lat_dist(start_idxA:last_idxA,trk_idx);
    track_A_new_track_sync(:,trk_idx) = track_A_new_track(start_idxA:last_idxA,trk_idx);
    track_A_rel_speed_sync(:,trk_idx) = track_A_rel_speed(start_idxA:last_idxA,trk_idx);
    track_A_valid_sync(:,trk_idx) = track_A_valid(start_idxA:last_idxA,trk_idx);
    track_A_checksum_sync(:,trk_idx) = track_A_checksum(start_idxA:last_idxA,trk_idx);
    
    track_A_lon_dist_sync_valid(:,trk_idx) = track_A_lon_dist_sync(:,trk_idx).*track_A_valid_sync(:,trk_idx);
    track_A_lat_dist_sync_valid(:,trk_idx) = track_A_lat_dist_sync(:,trk_idx).*track_A_valid_sync(:,trk_idx);
    
    % There are issues with TRACK_B_1
    if trk_idx == 2
        start_idxB = find(track_B_counter(:,1)==0,1,'first');
        last_idxB = find(track_B_counter(:,1)==255,1,'last');
    else
        start_idxB = find(track_B_counter(:,trk_idx)==0,1,'first');
        last_idxB = find(track_B_counter(:,trk_idx)==255,1,'last');
    end
    track_B_time_sync(:,trk_idx) = track_B_time(start_idxB:last_idxB,trk_idx);
    track_B_counter_sync(:,trk_idx) = track_B_counter(start_idxB:last_idxB,trk_idx);
    track_B_rel_accel_sync(:,trk_idx) = track_B_rel_accel(start_idxB:last_idxB,trk_idx);
    track_B_score_sync(:,trk_idx) = track_B_score(start_idxB:last_idxB,trk_idx);
    track_B_checksum_sync(:,trk_idx) = track_B_checksum(start_idxB:last_idxB,trk_idx);
end

% Integrate Track B relative accelerations
DT_20Hz = 0.05;
track_B_true_time = 0:DT_20Hz:length(start_idxA:last_idxB)*DT_20Hz-DT_20Hz;
calc_rel_speed = zeros(length(track_B_true_time),num_trks);
for trk_idx = 1:num_trks
    calc_rel_speed(:,trk_idx) = cumtrapz(track_B_true_time,track_B_rel_accel_sync(:,trk_idx)/40); %relative velocity
end

% Load KINEMATICS Data
KINEMATICS_length = sum(data(:,2)-data(1,2)>0);
KINEMATICS_Time = data(1:KINEMATICS_length,2)-data(1,2);
KINEMATICS_Yaw_Rate_Raw = data(1:KINEMATICS_length,3);

% Deadband
for i = 1:KINEMATICS_length
    if abs(KINEMATICS_Yaw_Rate_Raw(i)) <= 1
        KINEMATICS_Yaw_Rate(i) = 0;
    else
        KINEMATICS_Yaw_Rate(i) = KINEMATICS_Yaw_Rate_Raw(i);
    end
end
KINEMATICS_Steering_Torque = data(1:KINEMATICS_length,4);
KINEMATICS_Accel_Y = data(1:KINEMATICS_length,5);

DT_50Hz = 0.02;
KINEMATICS_true_time = 0:DT_50Hz:KINEMATICS_length*DT_50Hz-DT_50Hz;
Heading = cumtrapz(KINEMATICS_true_time,KINEMATICS_Yaw_Rate)-80;

% Load SPEED Data
SPEED_length = sum(data(:,18)-data(1,18)>0);
SPEED_Time = data(1:SPEED_length,18)-data(1,18);
SPEED_Encoder = data(1:SPEED_length,19);
SPEED_Speed = data(1:SPEED_length,20);
SPEED_Checksum = data(1:SPEED_length,21);

%% Plot data
figure
subplot(2,1,1)
plot(KINEMATICS_true_time,KINEMATICS_Yaw_Rate_Raw)
title('Yaw Rate')
subplot(2,1,2)
plot(KINEMATICS_true_time,Heading)
title('Heading')

% Simple Trajectory Finder
Initial_Position = [0,0]';
X_Pos = Initial_Position(1);
Y_Pos = Initial_Position(2);
kph_to_mps = 1000/3600;
for i = 1:SPEED_length       
    Vx(i) = cosd(Heading(i))*kph_to_mps*SPEED_Speed(i);
    Vy(i) = sind(Heading(i))*kph_to_mps*SPEED_Speed(i);
    X_Pos(i) = X_Pos(end) + Vx(i)*DT_50Hz;
    Y_Pos(i) = Y_Pos(end) + Vy(i)*DT_50Hz;
end
figure
plot(X_Pos,Y_Pos)
title('Ground Trajectory from CAN Data (Yaw Rate & Speed)')
xlabel('Meters');ylabel('Meters')
% ylim([-650 550])
% xlim([-450 1850])
grid on; box on;

figure
subplot(2,1,1)
plot(KINEMATICS_true_time,X_Pos)
title('X-Position')
subplot(2,1,2)
plot(KINEMATICS_true_time,Y_Pos)
title('Y-Position')

figure
subplot(2,1,1)
plot(KINEMATICS_true_time,Heading)
title('Heading')
subplot(2,1,2)
plot(SPEED_Time,SPEED_Speed)
title('Y-Position')

track_B_1_idx = [3];skip = 0;
for i = 1:18423
    num=track_B_counter(track_B_1_idx(end),2)+1;
    if num == 256
        num = 0;
    end
    if (track_B_counter(i,2) == num) && skip > 2
        track_B_1_idx = [track_B_1_idx, i];
        skip = 0;
    end
    skip = skip + 1;
end

figure
plot(track_A_time(:,1),track_A_valid(:,1),'b');
hold on
plot(track_B_time(:,1),track_B_score(:,1)/100,'r');

figure
plot(track_A_time(:,3)-track_A_time(1,1),track_A_valid(:,3),'b');
hold on
plot(track_B_time(:,3)-track_B_time(1,1),track_B_score(:,3)/100,'r');

%% Radar Plot
max_lat = max(max(track_A_lat_dist_sync));
max_lon = max(max(track_A_lon_dist_sync));
min_lat = min(min(track_A_lat_dist_sync));
min_lon = min(min(track_A_lon_dist_sync));
msize = 10;
lwidth = 2;

time_start = 1; 
time_end = 50;

for i = time_start*20:time_end*20
    figure(10)
    plot(track_A_lat_dist_sync(i,1),track_A_lon_dist_sync(i,1),'r.','Markersize',msize,'LineWidth',lwidth)
    hold on
        for j = 1:16
        if track_A_new_track_sync(i,j) > 0
            plot(track_A_lat_dist_sync_valid(i,j),track_A_lon_dist_sync_valid(i,j),'g.','Markersize',msize,'LineWidth',lwidth)
        elseif track_B_score_sync(i,j) == 0
            plot(track_A_lat_dist_sync_valid(i,j),track_A_lon_dist_sync_valid(i,j),'r.','Markersize',msize,'LineWidth',lwidth)
            color_str = 'red';
        else
            plot(track_A_lat_dist_sync_valid(i,j),track_A_lon_dist_sync_valid(i,j),'b.','Markersize',msize,'LineWidth',lwidth)
            color_str = 'blue';
        end
        if (track_A_lat_dist_sync_valid(i,j)+track_A_lon_dist_sync_valid(i,j))~=0
            if j>8
                if track_A_new_track_sync(i,j) > 0
                    str_label = [num2str(j),' (',num2str(track_B_score_sync(i,j)),',',num2str(track_A_rel_speed_sync(i,j)),',',num2str(track_B_rel_accel_sync(i,j)),')'];
                    text(track_A_lat_dist_sync_valid(i,j)+0.2,track_A_lon_dist_sync_valid(i,j)-4,str_label,'Color','green')
                else
                    str_label = [num2str(j),' (',num2str(track_B_score_sync(i,j)),',',num2str(track_A_rel_speed_sync(i,j)),',',num2str(track_B_rel_accel_sync(i,j)),')'];
                    text(track_A_lat_dist_sync_valid(i,j)+0.2,track_A_lon_dist_sync_valid(i,j)-4,str_label,'Color',color_str)
                end
            else
                if track_A_new_track_sync(i,j) > 0
                    str_label = [num2str(j),' (',num2str(track_B_score_sync(i,j)),',',num2str(track_A_rel_speed_sync(i,j)),',',num2str(track_B_rel_accel_sync(i,j)),')'];
                    text(track_A_lat_dist_sync_valid(i,j)+0.2,track_A_lon_dist_sync_valid(i,j)+4,str_label,'Color','green')
                else
                    str_label = [num2str(j),' (',num2str(track_B_score_sync(i,j)),',',num2str(track_A_rel_speed_sync(i,j)),',',num2str(track_B_rel_accel_sync(i,j)),')'];
                    text(track_A_lat_dist_sync_valid(i,j)+0.2,track_A_lon_dist_sync_valid(i,j)+4,str_label,'Color',color_str)
                end
            end
        end
    end
    rectangle('Position',[-1 -5 2 5],'LineWidth',3)
    line([-1.85 -1.85],[-5 350],'LineWidth',2)
    line([-1.85 -1.85]+3.7,[-5 350],'LineWidth',2)
    line([-1.85 -1.85]-3.7,[-5 350],'LineWidth',2)
    line([1.85 1.85],[-5 350],'LineWidth',2)
    line([1.85 1.85]+3.7,[-5 350],'LineWidth',2)
    line([1.85 1.85]-3.7,[-5 350],'LineWidth',2)
%     axis([-45 45 -5 350])
    axis([-30 30 -5 200])
    hold off
    time = track_A_time_sync(i,1)-track_A_time_sync(1,1)+24;    
    title(['Time: ',num2str(floor(time/60)),':',num2str(mod(time,60))])
    box on; grid on;
    pause(0.001)
end














