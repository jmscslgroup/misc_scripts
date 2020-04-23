% Determine Output Rates of Messages
% This script uses RANSAC to determine the true output rates of the
% different CAN BUS messages

clear all; close all; clc;
set(0,'DefaultFigureWindowStyle','docked');
warning('off')

% Load csv file
filename = 'C:\Users\glee\Documents\UA\Research\Sprinkle\Data\RAV-4_Giraffe_Data\Processed_Data\2020-03-24-16-42-54_CAN_Messages_Decoded_Messages.csv';
data = csvread(filename,1,0);

% Grab variable names
fileID = fopen(filename);
formatSpec = '%s';
N = size(data,2);
names = textscan(fileID,formatSpec,N,'delimiter',',');
fclose(fileID);

var_names = names{1,1};

%% RANSAC

for var_idx = 1:N
    idx = strfind(var_names{var_idx,1},'Time');
    length = sum(data(:,var_idx)-data(1,var_idx)>0);
    if isempty(idx) || length == 0
        continue;
    end
    time = data(1:length,var_idx)-data(1,var_idx);
    time_DT = time(2:end)-time(1:end-1);
    var = var_names{var_idx,1}(1:idx-2);
    points(:,1) = [1:length-1]';
    points(:,2) = time_DT;
    modelLeastSquares = polyfit(points(:,1),points(:,2),1)
    xLS = [min(points(:,1)) max(points(:,1))];
    yLS = modelLeastSquares(1)*xLS + modelLeastSquares(2);
    if length > 4000
        sampleSize = 2000; 
    else
        sampleSize = round(length/2);
    end
    maxDistance = 0.00025*modelLeastSquares(2);
    fitLineFcn = @(points) polyfit(points(:,1),points(:,2),1);
    distFcn = @(model, points) sum((points(:, 2) - polyval(model, points(:,1))).^2,2);
    [modelRANSAC, inlierIdx] = ransac(points,fitLineFcn,distFcn,sampleSize,maxDistance);
    modelInliers = polyfit(points(inlierIdx,1),points(inlierIdx,2),1)
    inlierPts = points(inlierIdx,:);
    xRANSAC = [min(inlierPts(:,1)) max(inlierPts(:,1))];
    yRANSAC = modelInliers(1)*xRANSAC + modelInliers(2);

    figure()
    hold all
    plot(points(:,1),points(:,2),'b.','MarkerSize',10);
    plot(points(inlierIdx,:),time_DT(inlierIdx),'g.','MarkerSize',10)
%     plot(xLS,yLS,'r-')
%     plot(xRANSAC, yRANSAC, 'k:')
    ylabel('Timesteps (sec)');
    title([var,' Message = ',num2str(round(1/modelInliers(2),2)),' Hz'],'Interpreter', 'none');
    legend('Outliers','Inliers');
    grid on; box on;
    fprintf('%20s Mean / RANSAC Output Rates = (%5.2f / %5.2f) Hz\n',var,round(1/modelLeastSquares(2),2),round(1/modelInliers(2),2));
    clear points 
end