import glob
import cv2
import os
import sys
import json
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def clean_temp_files():
    files = glob.glob("./TEMP_FILES/*")
    for f in files:
        os.remove(f)

    files = glob.glob("./TEMP_FILES_2/*")
    for f in files:
        os.remove(f)

    files = glob.glob("./TEMP_FILES_3/*")
    for f in files:
        os.remove(f)

def video_into_temporary_frames(video_path):
    print("Video path: " + str(video_path))
    capture = cv2.VideoCapture(video_path)
    frameNr = 0
    while (True):
        success, frame = capture.read()
        if success:
            cv2.imwrite(f'./TEMP_FILES/frame_{frameNr}.jpg', frame)
        else:
            break
        frameNr = frameNr + 1
        #print(frameNr)
    capture.release()

'''
def import_open_pose():
    # Import Openpose (Windows/Ubuntu/OSX)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append(dir_path + './openpose/bin/python/openpose/Release');
        os.environ['PATH'] = os.environ['PATH'] + ';' + dir_path + '/../x64/Release;' + dir_path + './openpose/bin'
        import pyopenpose as op
        return op
    except ImportError as e:
        print(
            'Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e
'''

def draw_bounding_box(img, x, y, x_plus_w, y_plus_h, label, color):
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


def stitch_frames_into_video(processed_video_name):
    image_folder = 'TEMP_FILES_3'
    video_name = processed_video_name

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images_sorted = []
    for r in range(len(images)):
        images_sorted.append("frame_" + str(r) + ".jpg")
        #print("Sorting Frames: " +str(r))
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, 25, (width, height))

    for image in images_sorted:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

def return_color_for_class(class_name):
    if class_name == "person":
        return (0,0,0)
    elif class_name == "bowl":
        return (50,255,50)
    elif class_name == "broccoli":
        return (0,100,0)
    elif class_name == "carrot":
        return (0,160,255)
    elif class_name == "banana":
        return (0,255,255)
    elif class_name == "apple":
        return (0,255,255)
    elif class_name == "bottle":
        return (100,180,255)
    elif class_name == "cup":
        return (190,190,190)
    else:
        return (255,0,0)


def load_json_data(name):
    #paths
    JSON_path_YOLO_det = name + "_YOLO_detections" + ".json"
    detections_json_path = name + "_openpose_detections.json"
    #read in
    with open(JSON_path_YOLO_det, 'r') as f:
        YOLO_detections = json.load(f)
    with open(detections_json_path, 'r') as f:
        openpose_detections = json.load(f)
    #make yolo pandas again - otherwise they are a string
    for i in range(len(YOLO_detections)):
        YOLO_detections[i] = pd.read_json(YOLO_detections[i], orient='split')


    return YOLO_detections, openpose_detections

def replace_padding_with_prevous_value_hands(name):
    detections_json_path = name + "_openpose_detections.json"

    f = open(detections_json_path, 'r', encoding='utf-8')
    all_data = json.load(f)
    f.close()

    #print(type(all_data))
    #print(len(all_data))
    #print(all_data[0])
    #print(all_data[0][0])
    #print(all_data[0][0][4])
    #print(all_data[0][0][4][0])

    #For both hands
    for frame_no in range(len(all_data)):
        #print("Frame no. = " + str(frame_no))
        if frame_no > 0:
            #pad right hand with actual value
            if all_data[frame_no][0][4][0] == 0:
                #print("I did something!")
                all_data[frame_no][0][4][0] = int(all_data[frame_no-1][0][4][0])
            if all_data[frame_no][0][4][1] == 0:
                #print("I did something!")
                all_data[frame_no][0][4][1] = int(all_data[frame_no-1][0][4][1])
            # pad left hand with actual value
            if all_data[frame_no][0][7][0] == 0:
                #print("I did something!")
                all_data[frame_no][0][7][0] = int(all_data[frame_no-1][0][7][0])
            if all_data[frame_no][0][7][1] == 0:
                #print("I did something!")
                all_data[frame_no][0][7][1] = int(all_data[frame_no-1][0][7][1])

    output_file = open(detections_json_path, 'w', encoding='utf-8')
    json.dump(all_data, output_file)
    output_file.close()

##################################################################################################
###########            COMPUTING CORRELATIONS                         ############################
##################################################################################################

def get_item_of_class_position(YOLO_data, class_no):
    x = []
    y = []

    for frame_no in range(len(YOLO_data)):
        #print(YOLO_data[frame_no])

        YOLO_frame = YOLO_data[frame_no]
        entries = YOLO_frame.loc[YOLO_frame['class'] == class_no]
        #print(entries)

        #Checks
        if entries.empty:
            #print("Item of class number " +str(class_no) + " not found.")
            if frame_no == 0:
                x.append(0)
                y.append(0)
            else:
                #print("___________")
                #print(x[-1])
                x.append(x[-1])
                y.append(y[-1])
        else:
            # from now we just work on entry with this class at the top
            top_entry = entries.head(1)
            #print(top_entry)
            middle_box_x = float((top_entry["xmin"] + top_entry["xmax"])/2)
            middle_box_y = float((top_entry["ymin"] + top_entry["ymax"])/2)
            #print("___________")
            #print(middle_box_x)
            #print(type(float(middle_box_x)))
            #print(middle_box_y)
            x.append(middle_box_x)
            y.append(middle_box_y)

    #print(x)
    #print(y)

    return [x, y]

def get_right_hand_position(data):
    x = []
    y = []
    for frame_no in range(len(data)):
        first_person_data = data[frame_no][0]
        #print(first_person_data)
        right_hand = first_person_data[4]
        #print("Right hand: " + str(right_hand))
        x.append(right_hand[0])
        y.append(right_hand[1])

    return [x,y]


def get_left_hand_position(data):
    x = []
    y = []
    for frame_no in range(len(data)):
        first_person_data = data[frame_no][0]
        #print(first_person_data)
        right_hand = first_person_data[7]
        #print("Right hand: " + str(right_hand))
        x.append(int(right_hand[0]))
        y.append(int(right_hand[1]))

    return [x,y]


def get_all_imprtant_correlations(YOLO_data, openpose_data):

    ##Basic Paths

    chair_path = get_item_of_class_position(YOLO_data, class_no = 56)
    person_path = get_item_of_class_position(YOLO_data, class_no = 0)
    laptop_path = get_item_of_class_position(YOLO_data, class_no = 63)

    #Hands
    hand_path = get_right_hand_position(openpose_data)
    hand2_path = get_left_hand_position(openpose_data)

    #print("Paths:")
    #print(hand2_path)

    ####Foods Paths####
    banana_path = get_item_of_class_position(YOLO_data, class_no=46)
    apple_path = get_item_of_class_position(YOLO_data, class_no=47)
    sandwich_path = get_item_of_class_position(YOLO_data, class_no=48)
    orange_path = get_item_of_class_position(YOLO_data, class_no=49)
    broccoli_path = get_item_of_class_position(YOLO_data, class_no=50)
    carrot_path = get_item_of_class_position(YOLO_data, class_no=51)

    ####Cutlery Paths####
    knife_path = get_item_of_class_position(YOLO_data, class_no = 43)
    spoon_path = get_item_of_class_position(YOLO_data, class_no = 44)
    fork_path = get_item_of_class_position(YOLO_data, class_no = 42)

    ####Tableware Paths####
    bottle_path = get_item_of_class_position(YOLO_data, class_no=39)
    wine_glass_path = get_item_of_class_position(YOLO_data, class_no=40)
    cup_path = get_item_of_class_position(YOLO_data, class_no=41)
    bowl_path = get_item_of_class_position(YOLO_data, class_no=45)
    #print(apple_path)

    #print("Path length control.\n Bottle path len: " + str(len(bottle_path[0])) + ". Right Hand path len: " + str(len(hand_path[0])) + ". Left Hand path len: " + str(len(hand2_path[0])) + ". Wine Glass path len: " + str(len(wine_glass_path[0])))

    path_length = len(hand_path[0])

    ###################################################################
    #######             Vorrelations to right hand               ######
    #################################################################
    hand1_corrs = []
    corr = []
    corr_window = 50
    #for path in [hand2_path, banana_path, apple_path, sandwich_path, orange_path, broccoli_path, carrot_path, knife_path, spoon_path, fork_path, bottle_path, wine_glass_path, cup_path, bowl_path]:
        #print("Prtining path after path")
        #print(path)

    for path in [hand2_path, banana_path, apple_path,sandwich_path, orange_path, broccoli_path, carrot_path, knife_path, spoon_path, fork_path, bottle_path, wine_glass_path, cup_path, bowl_path]:
        corr = []
        for r in range(path_length // corr_window):
            paths = [hand_path[0][r * corr_window:(r + 1) * corr_window], path[0][r * corr_window:(r + 1) * corr_window]]
            #print("Paths: " + str(paths))
            paths2 = [hand_path[1][r * corr_window:(r + 1) * corr_window], path[1][r * corr_window:(r + 1) * corr_window]]
            corr_matrix = draw_a_multiplied_correlation_matrix(paths_x=paths, paths_y=paths2, labels=["A","B"], title="Title",if_show_plot=False)
            #print(corr_matrix)
            corr.append(corr_matrix[0][1])
        hand1_corrs.append(corr)

    return hand1_corrs




###############################################################################
############                   PLOTTING                      ##################
###############################################################################
def draw_a_multiplied_correlation_matrix(paths_x, paths_y, labels, title, if_show_plot = True):
    try:
        n = len(paths_x)
    except:
        n = 2
    #print("Paths x: " + str(paths_x))
    multi_corr_x = np.corrcoef(paths_x)
    reduced_corr_matrix_x = multi_corr_x[0:n,0:n]
    multi_corr_y = np.corrcoef(paths_y)
    reduced_corr_matrix_y = multi_corr_y[0:n, 0:n]
    XY_corr = [a.clip(min=0) * b.clip(min=0) for a, b in zip(reduced_corr_matrix_x, reduced_corr_matrix_y)]
    #print(XY_corr)

    n = len(XY_corr)
    m = len(XY_corr[0])

    #print(n)
    #print(m)

    for a in range(n):
        for b in range(m):
            if XY_corr[a][b] != XY_corr[a][b]:
                XY_corr[a][b] = 0
    #print(XY_corr)

    if if_show_plot:
        plt.figure(figsize=(12, 8))
        plt.title(title)
        sns.heatmap(XY_corr, annot = True, xticklabels = labels, yticklabels = labels)
        plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False, labeltop=True)
        plt.show()
    return XY_corr



def draw_a_multiplied_correlation_matrix_OLD(paths_x, paths_y, labels, title, if_show_plot = True):
    try:
        n = len(paths_x)
    except:
        n = 2
    #print("Paths x: " + str(paths_x))
    multi_corr_x = np.corrcoef(paths_x)
    reduced_corr_matrix_x = multi_corr_x[0:n,0:n]
    multi_corr_y = np.corrcoef(paths_y)
    reduced_corr_matrix_y = multi_corr_y[0:n, 0:n]
    XY_corr = [abs(a * b) for a, b in zip(reduced_corr_matrix_x, reduced_corr_matrix_y)]
    #print(XY_corr)

    n = len(XY_corr)
    m = len(XY_corr[0])

    #print(n)
    #print(m)

    for a in range(n):
        for b in range(m):
            if XY_corr[a][b] != XY_corr[a][b]:
                XY_corr[a][b] = 0
    #print(XY_corr)

    if if_show_plot:
        plt.figure(figsize=(12, 8))
        plt.title(title)
        sns.heatmap(XY_corr, annot = True, xticklabels = labels, yticklabels = labels)
        plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False, labeltop=True)
        plt.show()
    return XY_corr



############################################################################################
#                            CORELATIONS PLOT
###########################################################################################

def plot_a_lot_of_correlations(hand1_corrs):
    ####Give names to correlations
    hand_to_hand_corr = hand1_corrs[0]
    hand_to_banana_corr = hand1_corrs[1]
    hand_to_apple_corr = hand1_corrs[2]
    hand_to_sandwich_corr = hand1_corrs[3]
    hand_to_orange_corr = hand1_corrs[4]
    hand_to_broccoli_corr = hand1_corrs[5]
    hand_to_bottle_corr = hand1_corrs[10]
    hand_to_cup_corr = hand1_corrs[12]
    hand_to_bowl_corr = hand1_corrs[13]

    plt.plot(hand_to_hand_corr, "b-", label="Hand to Hand Corr")
    plt.plot(hand_to_banana_corr, "b--", label="Hand to Banana Corr")
    plt.plot(hand_to_apple_corr, "g-", label="Hand to Apple Corr")
    plt.plot(hand_to_sandwich_corr, "g--", label="Hand to Sandwich Corr")
    plt.plot(hand_to_orange_corr, "r-.", label="Hand to Orange Corr")
    plt.plot(hand_to_broccoli_corr, "g-.", label="Hand to Broccoli Corr")
    plt.plot(hand_to_bottle_corr, "c-", label="Hand to Bottle Corr")
    plt.plot(hand_to_cup_corr, "r-", label="Hand to Cup Corr")
    plt.plot(hand_to_bowl_corr, "r--", label="Hand to Bowl Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Frame Number")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()


def plot_correlation_ingredients_and_orange(hand1_corrs):
    ####Give names to correlations
    hand_to_banana_corr = hand1_corrs[1]
    hand_to_apple_corr = hand1_corrs[2]
    hand_to_orange_corr = hand1_corrs[4]
    hand_to_broccoli_corr = hand1_corrs[5]
    hand_to_carrot_corr = hand1_corrs[6]


    plt.plot(hand_to_carrot_corr, "r--", label="Hand to Carrot Corr")
    plt.plot(hand_to_banana_corr, "y-", label="Hand to Banana Corr")
    plt.plot(hand_to_apple_corr, "r-", label="Hand to Apple Corr")
    plt.plot(hand_to_orange_corr, "o-.", label="Hand to Orange Corr")
    plt.plot(hand_to_broccoli_corr, "g-.", label="Hand to Broccoli Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Frame Number")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()


def plot_correlation_ingredients_and_knife(hand1_corrs):
    ####Give names to correlations
    hand_to_banana_corr = hand1_corrs[1]
    hand_to_apple_corr = hand1_corrs[2]
    hand_to_orange_corr = hand1_corrs[4]
    hand_to_broccoli_corr = hand1_corrs[5]
    hand_to_carrot_corr = hand1_corrs[6]
    hand_to_knife_corr = hand1_corrs[7]

    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)

    plt.plot(hand_to_carrot_corr, "r-", label="Hand to Carrot")
    plt.plot(hand_to_banana_corr, "y-", label="Hand to Banana")
    plt.plot(hand_to_apple_corr, "pink", label="Hand to Apple")
    plt.plot(hand_to_orange_corr, "orange", label="Hand to Orange")
    plt.plot(hand_to_broccoli_corr, "g-", label="Hand to Broccoli")
    plt.plot(hand_to_knife_corr, "b-", label="Hand to Knife Corr")

    plt.ylabel('Correlation Value', fontsize = 14)
    plt.xlabel("Window Number", fontsize = 14)
    plt.title("Correlations between right hand and objects\nrelevant to recipe.", fontsize = 16)
    #plt.legend(loc = 'lower right')
    plt.legend(loc = 'lower right', prop=dict(weight='bold'))
    plt.show()







def plot_correlation_knife_and_apple(hand1_corrs):
    ####Give names to correlations
    hand_to_knife_corr = hand1_corrs[7]
    hand_to_apple_corr = hand1_corrs[2]

    plt.plot(hand_to_apple_corr, "r-", label="Hand to Apple Corr")
    plt.plot(hand_to_knife_corr, "b-.", label="Hand to Knife Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Window NUmber")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()

def plot_correlation_knife_and_orange(hand1_corrs):
    ####Give names to correlations
    hand_to_knife_corr = hand1_corrs[7]
    hand_to_orange_corr = hand1_corrs[4]

    plt.plot(hand_to_orange_corr, "o-", label="Hand to Orange Corr")
    plt.plot(hand_to_knife_corr, "b-.", label="Hand to Knife Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Window NUmber")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()

def plot_correlation_knife_and_banana(hand1_corrs):
    ####Give names to correlations
    hand_to_knife_corr = hand1_corrs[7]
    hand_to_banana_corr = hand1_corrs[1]

    plt.plot(hand_to_banana_corr, "y-", label="Hand to Banana Corr")
    plt.plot(hand_to_knife_corr, "b-.", label="Hand to Knife Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Window NUmber")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()

def plot_correlation_knife_and_brocoli(hand1_corrs):
    ####Give names to correlations
    hand_to_knife_corr = hand1_corrs[7]
    hand_to_brocoli_corr = hand1_corrs[5]

    plt.plot(hand_to_brocoli_corr, "g-", label="Hand to Brocoli Corr")
    plt.plot(hand_to_knife_corr, "b-.", label="Hand to Knife Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Window NUmber")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()

def plot_correlation_knife_and_carrot(hand1_corrs):
    ####Give names to correlations
    hand_to_knife_corr = hand1_corrs[7]
    hand_to_carrot_corr = hand1_corrs[6]

    plt.plot(hand_to_carrot_corr, "r-", label="Hand to Carrot Corr")
    plt.plot(hand_to_knife_corr, "b-.", label="Hand to Knife Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Window NUmber")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()





def plot_correlation_bottle_and_apple(hand1_corrs):
    ####Give names to correlations
    hand_to_bottle_corr = hand1_corrs[10]
    hand_to_apple_corr = hand1_corrs[2]

    plt.plot(hand_to_apple_corr, "r-", label="Hand to Apple Corr")
    plt.plot(hand_to_bottle_corr, "g-.", label="Hand to Bottles Corr")

    plt.ylabel('Correlation Value')
    plt.xlabel("Window NUmber")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()

def plot_correlation_cutlery(hand1_corrs):
    ####Give names to correlations
    hand_to_knife_corr = hand1_corrs[7]
    hand_to_spoon_corr = hand1_corrs[8]
    hand_to_fork_corr = hand1_corrs[9]


    plt.plot(hand_to_knife_corr, "r-", label="Hand to Knife Corr")
    plt.plot(hand_to_spoon_corr, "g-", label="Hand to Spoon Corr")
    plt.plot(hand_to_fork_corr, "b-", label="Hand to Fork Corr")


    plt.ylabel('Correlation Value')
    plt.xlabel("Window Number")
    plt.title("Correlations between object pairs computed for short windows.")
    plt.legend()
    plt.show()



















