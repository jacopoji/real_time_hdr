import cv2
import machine_vision
fourcc = cv2.VideoWriter_fourcc(*'XVID')
vidcap = cv2.VideoCapture('2.avi')
success,image = vidcap.read()
count = 0
success = True

edge_out=cv2.VideoWriter('edge2_v2.avi',fourcc, 60.0, (720,540))
proc_out=cv2.VideoWriter('proc2_v2.avi',fourcc, 60.0, (720,540))
while success and count < 3000:
    try:
        if count == 2000:
            cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        processed,edgedetection=machine_vision.lane_detection(image)
        edge_out.write(edgedetection)
        proc_out.write(processed)
        count += 1
    except:
        vidcap.release()
        edge_out.release()
        proc_out.release()
        break

vidcap.release()
edge_out.release()
proc_out.release()