clear
clc

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
%%%   USE LAST TRAINING TO ESTIMATE        %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

salad_numbers = ['1' '2' '3' '4' '5' '6', '7', '8'];
%salad_numbers = ['11' '12' '13' '14' '15' '16', '17', '18'];
load('LastTraining.mat')
EMIT
TRANS

%GT - ground truth
%seq - before markov
%estimated staes - after markov

confusion_before_markov = [
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    ];

confusion_after_markov = [
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    0 0 0 0 0 0 0 
    ];

for salad_number = salad_numbers
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
        if maximum == broccoli_corr(i)
            number = 2;
        end
        if maximum == carrot_corr(i)
            number = 3;
        end
        if maximum == apple_corr(i)
            number = 4;
        end
        if maximum == banana_corr(i)
            number = 5;
        end
        if maximum == orange_corr(i)
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
    %reshuffle for better presentation
    newGT = [];
    for u = 1:size(GT)
        u;
        new_u = 999;
        if GT(u) == 1
            new_u = 1;
        end
        if GT(u) == 2
            new_u = 5;
        end
        if GT(u) == 3
            new_u = 4;
        end
        if GT(u) == 4
            new_u = 6;
        end
        if GT(u) == 5
            new_u = 2;
        end
        if GT(u) == 6
            new_u = 3;
        end
        if GT(u) == 7
            new_u = 7;
        end
        newGT = [newGT new_u];
    end
    GT = newGT
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
            commands = [commands "broccoli"];
            ingredient_found = 1;
            end
            if state == 3
            commands = [commands "carrot"];
            ingredient_found = 1;
            end
            if state == 4
            commands = [commands "apple"];
            ingredient_found = 1;
            end
            if state == 5
            commands = [commands "banana"];
            ingredient_found = 1;
            end
            if state == 6
            commands = [commands "orange"];
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

    %Filling in confusion matrix
    no_entries = size(GT)
    no_entries = no_entries(2)
    for n = 1:no_entries

        GT_current = GT(n);
        seq_current = seq(n);
        predicted_current = estimatedStates(n);

        confusion_before_markov(GT_current,seq_current) = confusion_before_markov(GT_current,seq_current) + 1;
        confusion_after_markov(GT_current,predicted_current) = confusion_after_markov(GT_current,predicted_current) + 1;

    end

    confusion_before_markov
    confusion_after_markov

end

    
