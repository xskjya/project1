"""
这是基于模型的车道检测的类
封装了基于图片，视频和摄像头的车道检测
并同时增加了透视变换获得车道相对坐标车道序列的封装
"""
import cv2
from lane_detection.ultrafastLaneDetector import UltrafastLaneDetector, ModelType



class LaneDetection:
    
    def __init__(self,
                 path: str = "lane_detection/models/saved_model_tusimple//model_float32.tflite",
                 model_type:  ModelType = ModelType.TUSIMPLE
                 ):
        """
        初始化相关参数
        """
        # 初始化检测器
        self.detector = UltrafastLaneDetector(model_path, model_type)
    

    def from_image(self,
                   image: str = "lane_detection/input.jpg"
                   ):
        """
        来源于图片的车道检测
        """
        # 读取图像
        self.img = cv2.imread(image_path, cv2.IMREAD_COLOR)

        # 检测车道
        output_img = self.detector.detect_lanes(img)

        # Draw estimated depth
        cv2.namedWindow("Detected lanes", cv2.WINDOW_NORMAL) 
        cv2.imshow("Detected lanes", output_img)
        cv2.waitKey(0)

        cv2.imwrite("output.jpg",output_img)
    
    def from_video(self):
        """
        来源于视频的车道检测
        """
        pass
    
    
    def from_camera(self):
        """
        来源于摄像头的车道检测
        """
        pass
    
    def perspective_trans(self):
        """
        对图片的透视变换函数
        """
        pass
    
    
        
    