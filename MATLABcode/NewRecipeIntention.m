clc;
clear;
%THIS SCRIPT PRODUCES THE PLOT WHERE DEMONSTRATION IS COMPARED TO NEW
%COOKBOOK


% Recipe Exploration Steps:
% 1. Learn from part of data - input salad numbers to learn from
% 2. Get composition of the known salads
% 3. On newly seen video run prediction at every 12 sec of the video and
% compute cosine similarity

%STATES IN THIS FILE WERE CHANGED TO FOLLOW EXPERIMENT PROTOCOL MORE:
%1 - nothing
%2 - brocoli
%3 - carrot
%4 - apple
%5 - banana
%6 - orange
%7 - knife


clear

%Step 1.
%TrainingSalads = ["1", "2", "3", "4", "5", "6", "7", "8"];
TrainingSalads = ["11", "12", "13", "14", "15", "16", "17", "18"];
%TrainingSalads = ["1", "2", "3", "4", "5", "6", "7", "8", "11", "12", "13", "14", "15", "16", "17", "18"];
%PredictedSalad = '12';
PredictedSalad = '31';
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

Recipe9_Vector = [0	2 0	0 2];



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

%Recipe9 
Recipe9_cosSim = [];
for prediction_no = 1:size(vectors,1)
   prediction = vectors(prediction_no,:);
   a = prediction;
   b = Recipe9_Vector;
   cosSim = sum(a.*b)/sqrt(sum(a.^2)*sum(b.^2));
   if isnan(cosSim)
      cosSim = 0; 
   end
   Recipe9_cosSim = [Recipe9_cosSim cosSim];
end


figure(2)
hold on
set(gcf,'position',[15,10,650,480])
%title('Similarity between actions of observed human and known recipes', 'FontSize', 12, 'FontWeight', 'bold')
%title("Intention Estimation for Recepie 1 with Triple Portion" + newline + "and One Undetected Ingredient", 'FontSize', 12, 'FontWeight', 'bold')
%title("Intention Estimation for Recepie 1 with Triple Portion" + newline + "and All Apples Added before Carrot", 'FontSize', 12, 'FontWeight', 'bold')
%title("Intention Estimation for Recepie 1 with Triple Portion" + newline + "and Orange Added as Mistake", 'FontSize', 12, 'FontWeight', 'bold')
title("Intention Estimation for the New Recipe after it was Learned", 'FontSize', 12, 'FontWeight', 'bold')
plot(Recipe1_cosSim, "LineWidth", 3)
plot(Recipe2_cosSim, "LineWidth", 3)
plot(Recipe3_cosSim, "LineWidth", 3)
plot(Recipe4_cosSim, "LineWidth", 3)
plot(Recipe5_cosSim, "LineWidth", 3)
plot(Recipe6_cosSim, "LineWidth", 3)
plot(Recipe7_cosSim, "LineWidth", 3)
plot(Recipe8_cosSim, "LineWidth", 3)
plot(Recipe9_cosSim, "b--", "LineWidth", 3)
ax = gca; 
ax.FontSize = 12;
xlabel("Time since begining of preparation[24s steps]", 'FontSize', 12, 'FontWeight', 'bold')
ylabel("Cosine Similarity with Recipes", 'FontSize', 12, 'FontWeight', 'bold')
legend('Recipe 1','Recipe 2','Recipe 3','Recipe 4','Recipe 5','Recipe 6','Recipe 7','Recipe 8','Recipe 9', location = "southeast")

TRANS;
EMIT;
