function [vectors] = HMMPrediction_Iter(salad_number)
    vectors = []

    correlations = readNPY(['Correlations/FinalSalad', salad_number, '.npy']);
    corr_size = size(correlations);
    data_length = corr_size(2);
    
    prediction_points = 12:12:data_length
    for point = prediction_points
       [commands, vector] = HMMPrediction(salad_number, point);
       vectors = [vectors;vector];
    end


end

