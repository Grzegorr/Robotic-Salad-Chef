%Just test values - real ones are read in below
%States:
%1 - nothing
%2 - banana
%3 - apple
%4 - orange
%5 - brocoli
%6 - carrot
%7 - knife


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%           MOCK EXAMPLE                 %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
trans = [0.88 0.02 0.02 0.02 0.02 0.02 0.02
        0.02 0.88 0.02 0.02 0.02 0.02 0.02
        0.02 0.02 0.88 0.02 0.02 0.02 0.02
        0.02 0.02 0.02 0.88 0.02 0.02 0.02
        0.02 0.02 0.02 0.02 0.88 0.02 0.02
        0.02 0.02 0.02 0.02 0.02 0.88 0.02
        0.02 0.02 0.02 0.02 0.02 0.02 0.88];
    
emit = [0.7 0.05 0.05 0.05 0.05 0.05 0.05
        0.05 0.7 0.05 0.05 0.05 0.05 0.05
        0.05 0.05 0.7 0.05 0.05 0.05 0.05
        0.05 0.05 0.05 0.7 0.05 0.05 0.05
        0.05 0.05 0.05 0.05 0.7 0.05 0.05
        0.05 0.05 0.05 0.05 0.05 0.7 0.05
        0.05 0.05 0.05 0.05 0.05 0.05 0.7];

seq = [1 1 1 1 1 1 1 1 5 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 5 2 2 2 2 7 7 7 7 7 7 7 7 3 7 7 7 7 7 7 7 7 1 1 1 1 1 1 1 2 1 1 1 1 5 5 5 5 5 5 5 5 1 5 1 5 5 5 1 1 1 7 7 7 7 7 1 7 7 7 7 7 1 1 7 7 7 7 7 7 7 7 1 1 1 1 1 1 1 1];

estimatedStates = hmmviterbi(seq,trans,emit);
estimatedStates;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%   USE LAST TRAINING TO ESTIMATE        %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
salad_number = ['5'];
load('LastTraining.mat')

%%%   READING IN EMMISSIONS
threshold = 0.6;

correlations = readNPY(['Correlations/FinalSalad', salad_number, '.npy']);
size(correlations);
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

estimatedStates = hmmviterbi(seq,TRANS,EMIT);
estimatedStates


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%      PLOTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% LOAD GT for plotting only
GT = readNPY(['GroundTruth/FinalSalad', salad_number, '_GTstates.npy']);
GT;

title('Correlations and Markov Filtered Corrleations')
plot(estimatedStates, '-b')
xlabel("Correlation Window")
ylabel("State no.")
hold on
plot(seq, 'xr')
plot(GT, 'og')
legend('HMM estimation','Correlation Detection','Ground Truth')


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%          GENERATE COMMANDS             %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%flags
ingredient_found = 0;
commands = [];

%Iterate through states
for state = estimatedStates
    %Looking for ingredients
    if ingredient_found == 0
        if state == 2
        commands = [commands "banana"];
        ingredient_found = 1;
        end
        if state == 3
        commands = [commands "apple"];
        ingredient_found = 1;
        end
        if state == 4
        commands = [commands "orange"];
        ingredient_found = 1;
        end
        if state == 5
        commands = [commands "broccoli"];
        ingredient_found = 1;
        end
        if state == 6
        commands = [commands "carrot"];
        ingredient_found = 1;
        end
    end
    %Looking for cutting
    if ingredient_found == 1
        if state == 7
            commands = [commands "cut"];
            ingredient_found = 0;
        end
    end
end

commands



    
