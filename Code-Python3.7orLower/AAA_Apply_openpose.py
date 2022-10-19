from Process_Video import *
import json
#from DataProcessing import *
#from CorrelationExtraction import *

if True:
    name = "FakeVsRealApple"
    openpose_detections = []
    detections_json_path = "C:/Users/grzeg/Desktop/SaladRobot/" + name + "_openpose_detections.json"

    import_open_pose()
    op, classes, COLORS = load_packages_classes_etc()
    opWrapper = run_open_pose(image_path="image_path", op=op, saving_path="save_path")

    files = glob.glob("C:/Users/grzeg/Desktop/SaladRobot/TEMP_FILES/*")
    for i in range(len(files)):
        print("\nProcessing a frame no: " + str(i) + " out of " + str(len(files)) + " frames.\n")
        image_path = "C:/Users/grzeg/Desktop/SaladRobot/TEMP_FILES/frame_" + str(i) + ".jpg"
        save_path = "C:/Users/grzeg/Desktop/SaladRobot/TEMP_FILES_2/frame_" + str(i) + ".jpg"

        # Process Image
        datum = op.Datum()
        imageToProcess = cv2.imread(image_path)

        # Print Image Info
        height, width, channels = imageToProcess.shape
        print("Image width: " + str(width) + ".")
        print("Image height: " + str(height) + ".")

        datum.cvInputData = imageToProcess
        opWrapper.emplaceAndPop(op.VectorDatum([datum]))

        # Display Image and Save Image
        # print("Body keypoints: \n" + str(datum.poseKeypoints))
        # cv2.imshow("OpenPose Only", datum.cvOutputData)
        cv2.imwrite(save_path, datum.cvOutputData)

        if datum.poseKeypoints is None:
            print("The empty array was found!")
            openpose_data = get_empty_openPose_data()
        else:
            openpose_data = np.ndarray.tolist(datum.poseKeypoints)

        openpose_detections.append(openpose_data)

    print(len(openpose_detections[0]))
    print(openpose_detections[0])
    print(len(openpose_detections[1]))
    print(openpose_detections[1])
    print(len(openpose_detections[2]))
    print(openpose_detections[2])

    #Save to json
    with open(detections_json_path, 'w') as f:
        json.dump(openpose_detections, f)


