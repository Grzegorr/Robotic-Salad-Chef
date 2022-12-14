% Recipe Exploration Steps:
% 1. Learn from part of data - input salad numbers to learn from
% 2. Get composition of the known salads
% 3. On newly seen video run prediction at every 12 sec of the video and
% compute cosine similarity

clear

%Step 1.
TrainingSalads = ["1", "2", "3", "4", "5", "6", "7", "8"];
PredictedSalad = '12';
[TRANS, EMIT] = HMMEstimation(TrainingSalads);

%Step 2.
Recipe1_Vector = [0	1 1	0 0];
Recipe2_Vector = [0	3 1	0 0];
Recipe3_Vector = [0	1 2	0 0];
Recipe4_Vector = [0	0 1	1 1];
Recipe5_Vector = [0	0 1	1 3];
Recipe6_Vector = [1	1 0	0 0];
Recipe7_Vector = [3	1 0	0 0];
Recipe8_Vector = [0	0 0	2 2];



%Step 3.
vectors = HMMPrediction_Iter(PredictedSalad)

%Recipe1 
Recipe1_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe1_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe1_cosSim = [Recipe1_cosSim cosSim];
end

%Recipe2 
Recipe2_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe2_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe2_cosSim = [Recipe2_cosSim cosSim];
end

%Recipe3 
Recipe3_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe3_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe3_cosSim = [Recipe3_cosSim cosSim];
end

%Recipe4 
Recipe4_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe4_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe4_cosSim = [Recipe4_cosSim cosSim];
end

%Recipe5 
Recipe5_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe5_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe5_cosSim = [Recipe5_cosSim cosSim];
end

%Recipe6 
Recipe6_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe6_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe6_cosSim = [Recipe6_cosSim cosSim];
end

%Recipe7 
Recipe7_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe7_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe7_cosSim = [Recipe7_cosSim cosSim];
end

%Recipe8 
Recipe8_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe8_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe8_cosSim = [Recipe8_cosSim cosSim];
end

figure(2)
hold on
title('Similarity between actions of observed human and known recipes.')
plot(Recipe1_cosSim)
plot(Recipe2_cosSim)
plot(Recipe3_cosSim)
plot(Recipe4_cosSim)
plot(Recipe5_cosSim)
plot(Recipe6_cosSim)
plot(Recipe7_cosSim)
plot(Recipe8_cosSim)
xlabel("Time since begining of preparation[24s steps]")
ylabel("Cosine Similarity with Recipes")
legend('Recipe 1','Recipe 2','Recipe 3','Recipe 4','Recipe 5','Recipe 6','Recipe 7','Recipe 8', location = "southwest")
