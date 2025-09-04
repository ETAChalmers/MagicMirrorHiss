import time
import cv2

capture = cv2.VideoCapture('etamirror.mp4')

loadingBlockStartPosition = (137, 145)

loadingBlockSize = (28, 18)

spacing = 3

maxBlocks = 19

def tupleAdd(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

def drawLoadingBar(blockCount, target):
    
    blockCount = min(maxBlocks, blockCount)
        
    for i in range(0, blockCount):
        
        loadingBlockPosition = tupleAdd(loadingBlockStartPosition, (0, i * (loadingBlockSize[1] + spacing)))
        
        loadingBlockEnd = tupleAdd(loadingBlockPosition, loadingBlockSize)
        
        cv2.rectangle(target, loadingBlockPosition, loadingBlockEnd, (255, 255, 255), -1)
     
def show():
    frameCount = 0   
            
    while(capture.isOpened()):
        #frameFound bool that is true if we have a valid frame
        frameFound, frame = capture.read() 
        
        #Rotate our current frame
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        
        if frameFound:
            frameCount += 1
            
            drawLoadingBar(round(frameCount/10), frame)
            
            cv2.imshow("Image", frame)
            
            #Is this needed?
            #cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
            
            cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        #No clue wtf this does    
        else:
           capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
           continue
        
        # If q is pressed, quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        time.sleep(1/60)

show()
capture.release()
cv2.destroyAllWindows()
