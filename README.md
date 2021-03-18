# yolov3_tiny_tf2

#### 

## 实验环境

- tensorflow==2.4.1
- opencv-python==3.4.2.16
- lxml
- tqdm

## 相关说明

- voc2012.py # 预处理数据
- train.py # 训练模型
- detect.py # 测试图片
- detect_video.py # 测试视频
- voc2012.names # 类别名文件

## 相关命令

```
# 预处理训练数据集
python voc2012.py --data_dir ./data/voc2012_raw/VOCdevkit/VOC2012 --split train --output_file ./data/voc2012_train.tfrecord

# 预处理验证数据集
python voc2012.py --data_dir ./data/voc2012_raw/VOCdevkit/VOC2012 --split val --output_file ./data/voc2012_val.tfrecord

#训练tiny
python train.py --dataset ./data/voc2012_train.tfrecord --val_dataset ./data/voc2012_val.tfrecord --classes ./data/voc2012.names --num_classes 4 --batch_size 1 --epochs 10

# 识别
# yolov3-tiny
python detect.py --classes ./data/voc2012.names --weights ./checkpoints/yolov3_tiny_train_5.tf  --tiny --image ./data/head.jpg --num_classes 4

# webcam
python detect_video.py --classes ./data/voc2012.names --weights ./checkpoints/yolov3_train_6.tf  --tiny --num_classes 1 --video 0

# CSI camera
python3 detect_video.py --classes ./data/voc2012.names --weights ./checkpoints/yolov3_tiny_train_5.tf  --tiny --video CSI --num_classes 4

# video file
python detect_video.py --video path_to_file.mp4 --weights ./checkpoints/yolov3_train_5.tf  --tiny

# video file with output
python detect_video.py --video path_to_file.mp4 --output ./output.avi
```
