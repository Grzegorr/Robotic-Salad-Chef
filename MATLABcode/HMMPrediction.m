%Just test values - real ones are read in below
%States:
%1 - nothing
%2 - banana
%3 - apple
%4 - orange
%5 - brocoli
%6 - carrot
%7 - knife

function [commands,vector] = HMMPrediction(salad_number,stop_point)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%   USE LAST TRAINING TO ESTIMATE        %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

    estimatedStates = hmmviterbi(seq(1:stop_point),TRANS,EMIT);
    estimatedStates;


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%      PLOTS
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    %%% LOAD GT for plotting only
    GT = readNPY(['GroundTruth/FinalSalad', salad_number, '_GTstates.npy']);
    GT;
    
    figure(1)
    title('Correlations and Markov Filtered Corrleations')
    plot(estimatedStates(1:stop_point), '-b')
    xlabel("Correlation Window")
    ylabel("State no.")
    hold on
    plot(seq(1:stop_point), 'xr')
    plot(GT(1:stop_point), 'og')
    legend('HMM estimation','Correlation Detection','Ground Truth')
    hold off


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
    
    commands;
    %Compute Vector
    if isempty(commands)
        broccoli_content = 0;
        carrot_content = 0;
        apple_content = 0;
        banana_content = 0;
        orange_content = 0;
    else
        broccoli_content = nnz(commands=="broccoli");
        carrot_content = nnz(commands=="carrot");
        apple_content = nnz(commands=="apple");
        banana_content = nnz(commands=="banana");
        orange_content = nnz(commands=="orange");
    end
    
    vector = [broccoli_content, carrot_content, apple_content, banana_content, orange_content];
end












