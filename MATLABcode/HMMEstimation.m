%Function to train HMM (find transmission and emmision matrxies) from
%multiple videos.
%Takes in an array of numbers which are salad numbers

%States AND emissions meaning:
%1 - nothing
%2 - banana
%3 - applecorrelations
%4 - orange
%5 - brocoli
%6 - carrot
%7 - knife

%STATES - human ground truth
%EMMISIONS - what correlations say

function [TRANS,EMIT] = HMMEstimation(saladNumberList)
% Files with extracted correlations and Ground Truth
correlation_files = [];
GT_files = [];

%Change Numbers into file names
for salad_no = saladNumberList
    corr_file = strcat("Correlations/FinalSalad", salad_no ,".npy");
    GT_file = strcat("GroundTruth/FinalSalad", salad_no ,"_GTstates.npy");
    correlation_files = [correlation_files, corr_file];
    GT_files = [GT_files, GT_file];
end

%prints for check
correlation_files;
GT_files;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%   READING IN EMMISSIONS                %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
threshold = 0.6;
correlations = [];

for file = correlation_files
correlations_single = readNPY(file);
correlations = [correlations, correlations_single];
size(correlations)
end

correlations(1,:);

%put in separate arrays
banana_corr = correlations(2,:);
apple_corr = correlations(3,:);
orange_corr = correlations(5,:);
broccoli_corr = correlations(6,:);
carrot_corr = correlations(7,:);
knife_corr = correlations(8,:);

% analogue correlation to binary correlation
seq = [];
length = size(banana_corr);
length = length(2);
for i = 1:length
    number = 999;
    maximum = max([banana_corr(i) apple_corr(i) orange_corr(i) broccoli_corr(i) carrot_corr(i) knife_corr(i)]);
    if maximum == banana_corr(i)
        number = 2;
    end
    if maximum == apple_corr(i)
        number = 3;
    end
    if maximum == orange_corr(i)
        number = 4;
    end
    if maximum == broccoli_corr(i)
        number = 5;
    end
    if maximum == carrot_corr(i)
        number = 6;
    end
    if maximum == knife_corr(i)
        number = 7;
    end
    if maximum < threshold
        number = 1;
    end   
    seq = [seq number];
end
seq;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%          READING IN STATES             %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
states = [];

for file = GT_files
states_single = readNPY(file);
states = [states, states_single'];
size(states);
end



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%               TRAINING                 %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[TRANS,EMIT] = hmmestimate(seq,states);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%               SAVE DATA                %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

save('LastTraining.mat', 'TRANS', 'EMIT');

end

