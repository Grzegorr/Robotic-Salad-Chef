from UtilityFunctions import *

name = "FinalSalad18"

### Fill in the no detections
replace_padding_with_prevous_value_hands(name)

YOLO_detections, openpose_detections = load_json_data(name)

#get_item_of_class_position(YOLO_detections, 47)
#get_item_of_class_position(YOLO_detections, 0)

correlations = get_all_imprtant_correlations(YOLO_detections, openpose_detections)
print(correlations)
print(len(correlations))
print(len(correlations[0]))

#Ingredients and knife
plot_correlation_ingredients_and_knife(correlations)
#Other
#plot_a_lot_of_correlations(correlations)
#plot_correlation_ingredients_and_orange(correlations)
#plot_correlation_bottle_and_apple(correlations)
#plot_correlation_cutlery(correlations)

#Single Ingredient and knife
#plot_correlation_knife_and_apple(correlations)
#plot_correlation_knife_and_banana(correlations)
#plot_correlation_knife_and_brocoli(correlations)
#plot_correlation_knife_and_carrot(correlations)
#plot_correlation_knife_and_orange(correlations)



CORRs = np.array(correlations)
numpy_name = name + ".npy"
np.save(numpy_name, CORRs)
















