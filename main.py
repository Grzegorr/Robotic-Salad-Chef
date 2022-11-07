from UtilityFunctions import *

import pandas as pd
import json
import torch


if True:
    # Model
    YOLO = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)

    # Videos
    names = ['CarrotTuning'] ###put one name only, sorry
    processed_video_name = names[0] + "_processed.mp4"
    results_YOLO = []
    results_YOLO_JSON = []

    for name in names:
        #File naming and placement
        video_path = "Data/" + name + ".mp4"
        processed_video_name = name + ".mp4"
        JSON_path_YOLO_det = name + "_YOLO_detections" + ".json"

        #Prepare files and frames
        clean_temp_files()
        video_into_temporary_frames(video_path)



        files = glob.glob("TEMP_FILES/*")
        print(files)
        for i in range(len(files)):
            print("\nProcessing a frame no: " + str(i) + " out of " + str(len(files)) + " frames.\n")
            image_path = "TEMP_FILES/frame_" + str(i) + ".jpg"
            #save_path = "TEMP_FILES_3/frame_" + str(i) + ".jpg"

            #Apply YOLO
            results = YOLO(image_path)
            #img = results.render()[0].copy()
            #cv2.imshow("Image", img)
            #cv2.waitKey(0)
            #cv2.imwrite(save_path, img)

            # Results
            result_pandas = results.pandas().xyxy[0]
            print("Full results:")
            print(result_pandas)
            print("Name only:")
            print(result_pandas.name)
            print("0th entry:")
            print(result_pandas.loc[0])
            print("0th entry x min:")
            print(result_pandas.loc[0]["xmin"])
            print("Length:")
            print(len(result_pandas.index))

            results_YOLO_JSON.append(result_pandas.to_json(orient='split', index=True))
            results_YOLO.append(result_pandas)


    #print("Print 1")
    #print(results_YOLO)
    #print("Print 2")
    #print(results_YOLO[0])

    #Save results as JSON
    with open(JSON_path_YOLO_det, 'w') as f:
        json.dump(results_YOLO_JSON, f)
    #Now run openpose
    input("Run openpose Now, then click to continue.")

#Here we draw the boxes finally
files = glob.glob("TEMP_FILES/*")
print(files)
for i in range(len(files)):
    print("\nProcessing a frame no: " + str(i) + " out of " + str(len(files)) + " frames.\n")
    image_path = "TEMP_FILES_2/frame_" + str(i) + ".jpg"
    save_path = "TEMP_FILES_3/frame_" + str(i) + ".jpg"

    img = cv2.imread(image_path)
    results_for_image = results_YOLO[i]
    for j in range(len(results_for_image.index)):
        x_min = int(results_for_image.loc[j]["xmin"])
        y_min = int(results_for_image.loc[j]["ymin"])
        x_max = int(results_for_image.loc[j]["xmax"])
        y_max = int(results_for_image.loc[j]["ymax"])
        label = results_for_image.loc[j]["name"]
        color = return_color_for_class(label)
        draw_bounding_box(img, x_min, y_min, x_max, y_max, label, color)

    cv2.imwrite(save_path, img)

stitch_frames_into_video(processed_video_name)


