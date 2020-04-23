% Read in Dash Cam Video and Overlay Radar Tracks
clear all; close all; clc;
set(0,'DefaultFigureWindowStyle','docked');

% Load csv file
data = csvread('C:\Users\glee\Documents\UA\Research\Sprinkle\Data\RAV-4_Giraffe_Data\Processed_Data\2020-03-24-16-42-54_CAN_Messages_Decoded_Messages.csv',1,0);

% Load video file
vid = VideoReader('C:\Users\glee\Documents\UA\Research\Sprinkle\Data\RAV-4_Giraffe_Data\2020_03_24\2020-03-24-16-42-54_dashcam.mov');

%% Video Properties
% 24-bits per pixel (8 in each channel RGB)
bpp = vid.BitsPerPixel;
% 30 Hz frame rate
framerate = vid.FrameRate;
% 720 rows x 1280 columns
rows = vid.Height;
cols = vid.Width;
% Duration
duration = vid.Duration;
numframes = vid.NumFrames;
currenttime = vid.CurrentTime;

%% Grab Radar Data
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

%% Plot Radar Tracks on Dash Cam Video
start_time = 132;
end_time = start_time+12;
timestep = 0.1;
msize = 5; lwidth = 2;
radar_offset = 24.1; %CAN radar data starts X seconds after Dash Cam Video
row_offset = 3;
col_offset = row_offset*(1280/720);
for time = start_time:timestep:end_time
    radar_time = time - radar_offset;
    radar_idx = int64(radar_time*20); %radar data at 20Hz
    frame = read(vid,int64(time*30)); %video data at 30Hz
    figure(1)
    image(frame)
    title(['Time: ',num2str(time)])
    hold on
    plot(670,390,'rx','MarkerSize',5)
    vec = [track_A_lon_dist_sync_valid(radar_idx,:)',track_A_lat_dist_sync_valid(radar_idx,:)',track_A_valid_sync(radar_idx,:)'];
    for j = 1:16
        lon_sf(radar_idx,j) = 29/track_A_lon_dist_sync_valid(radar_idx,j);
        lat_sf(radar_idx,j) = 26.5/track_A_lon_dist_sync_valid(radar_idx,j);
        camera_from_body = [0 1 0; -1 0 0; 0 0 1];
        fpa_from_camera = [lat_sf(radar_idx,j)*35 0 670; 0 lon_sf(radar_idx,j)*6.1 600; 0 0 0];
        fpa_from_body = fpa_from_camera*camera_from_body;
        fpa_vec(j,:) = fpa_from_body*[track_A_lon_dist_sync_valid(radar_idx,j),track_A_lat_dist_sync_valid(radar_idx,j),1]';
        if track_A_new_track_sync(radar_idx,j) > 0            
            plot(fpa_vec(j,1),fpa_vec(j,2),'go','Markersize',msize,'LineWidth',lwidth)
        elseif track_B_score_sync(radar_idx,j) == 0
            plot(fpa_vec(j,1),fpa_vec(j,2),'ro','Markersize',msize,'LineWidth',lwidth)
            color_str = 'red';
        else
            plot(fpa_vec(j,1),fpa_vec(j,2),'bo','Markersize',msize,'LineWidth',lwidth)
            color_str = 'blue';
        end
        if (track_A_lat_dist_sync_valid(radar_idx,j)+track_A_lon_dist_sync_valid(radar_idx,j))~=0
            if j>8
                if track_A_new_track_sync(radar_idx,j) > 0
                    str_label = [num2str(j),' (',num2str(track_A_lon_dist_sync_valid(radar_idx,j)),',',num2str(track_A_lat_dist_sync_valid(radar_idx,j)),',',num2str(track_B_score_sync(radar_idx,j)),',',num2str(track_A_rel_speed_sync(radar_idx,j)),',',num2str(track_B_rel_accel_sync(radar_idx,j)),')'];
                    text(fpa_vec(j,1)+0.5*col_offset,fpa_vec(j,2)+4*row_offset,str_label,'Fontsize',12,'Color','green')
                else
                    str_label = [num2str(j),' (',num2str(track_A_lon_dist_sync_valid(radar_idx,j)),',',num2str(track_A_lat_dist_sync_valid(radar_idx,j)),',',num2str(track_B_score_sync(radar_idx,j)),',',num2str(track_A_rel_speed_sync(radar_idx,j)),',',num2str(track_B_rel_accel_sync(radar_idx,j)),')'];
                    text(fpa_vec(j,1)+0.5*col_offset,fpa_vec(j,2)+4*row_offset,str_label,'Fontsize',12,'Color',color_str)
                end
            else
                if track_A_new_track_sync(radar_idx,j) > 0
                    str_label = [num2str(j),' (',num2str(track_A_lon_dist_sync_valid(radar_idx,j)),',',num2str(track_A_lat_dist_sync_valid(radar_idx,j)),',',num2str(track_B_score_sync(radar_idx,j)),',',num2str(track_A_rel_speed_sync(radar_idx,j)),',',num2str(track_B_rel_accel_sync(radar_idx,j)),')'];
                    text(fpa_vec(j,1)+0.5*col_offset,fpa_vec(j,2)-4*row_offset,str_label,'Fontsize',12,'Color','green')
                else
                    str_label = [num2str(j),' (',num2str(track_A_lon_dist_sync_valid(radar_idx,j)),',',num2str(track_A_lat_dist_sync_valid(radar_idx,j)),',',num2str(track_B_score_sync(radar_idx,j)),',',num2str(track_A_rel_speed_sync(radar_idx,j)),',',num2str(track_B_rel_accel_sync(radar_idx,j)),')'];
                    text(fpa_vec(j,1)+0.5*col_offset,fpa_vec(j,2)-4*row_offset,str_label,'Fontsize',12,'Color',color_str)
                end
            end
        end
    end
    [vec(:,1:2),fpa_vec(:,1:2),lon_sf(radar_idx,:)',lat_sf(radar_idx,:)'];
    axis([0 1280 0 720])
    hold off
    pause
end





