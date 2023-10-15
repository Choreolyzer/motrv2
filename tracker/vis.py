import cv2,json, os
import matplotlib.cm as cm

image_folder = "../data/Dataset/mot/DanceTrack/test/blackpink/img1/"
text_folder = "./blackpink.txt"
video_name = 'out.webm'

images = [cv2.imread(os.path.join(image_folder, img)) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]
frame = images[0]

height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'VP80'), 20, (width,height))

# rects
with open(text_folder, "r") as file:
    for line in file.readlines():
        ll = line.split(',')
        img_id = int(ll[0]) - 1
        obj_id = int(ll[1])

        bbox = [float(ll[2]), float(ll[3]),
                float(ll[2]) + float(ll[4]),
                float(ll[3]) + float(ll[5]), int(obj_id)]

        color = cm.hot(obj_id / 20)
        cv2.rectangle(images[img_id], (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255,255,0), 3)
        cv2.putText(images[img_id], "{}".format(int(bbox[4])), (int(bbox[0])+5, int(bbox[1])+30), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0), 2)


for img in images:
    video.write(img)


cv2.destroyAllWindows()
video.release()
