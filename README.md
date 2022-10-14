
# Plant Disease Detection


## Introduction


It is very important to get an accurate diagnosis of plant diseases for global health and well being.
In this ever changing environment, identifying the disease including early prevention is important
to avoid problems that we might face otherwise. Some of these problems could have devastating
impacts on humanity including global shortage of food. It is crucial to prevent unnecessary waste of
financial resources achieving a healthier lifestyle, by addressing climate change from an ecological
perspective. It is difficult for the naked eye of a human being to catch all sorts of problems with plant
diseases. Also doing this time and time again is also laborious and unproductive work. In order to
achieve accurate plant disease detection, a plant pathologist should possess good observation skills
so that one can identify characteristic symptoms. An automated system designed to help identify
plant diseases by the plant’s appearance and visual symptoms could be of great help. This can be
deployed in agricultural fields so that the whole pipeline can be automated. This would not only lead
to better efficiency as machines could perform better than humans in these redundant tasks but also
improve the productivity of the farm. Our work solves the above mentioned problem of automating
plant disease classification using deep learning and computer vision techniques.

## Building

**_Prequired Python3 (https://www.python.org/downloads/)_**
</br>
```bash
# clone the repo
git clone https://github.com/NischayGoyal1/WhatThe_hAIck.git .

# install dependecies
pip install -r requirements.txt

# run the python file
python app.py
```
**Copy the Url http://127.0.0.1:5000/ and run on your preferred browser**
![WhatsApp Image 2021-11-12 at 00 19 18](https://user-images.githubusercontent.com/81116984/141352783-f4eb5a8b-5a86-4c09-a707-93fa50f0b5f8.jpeg)




## Plant Disease Detection


Disease detection in plants plays an important role in agriculture as farmers have often to decide
whether the crop they are harvesting is good enough. It is of utmost importance to take these seriously
as it can lead to serious problems in plants due to which respective product quality, quantity or
productivity is affected. Plant diseases cause a periodic outbreak of diseases leading to large-scale
death which severely affects the economy. These problems need to be solved at the initial stage,
to save the lives and money of people. Automatic classification of plant diseases is an important research topic as it is important in monitoring large fields of crops and at a very early stage, if we can
detect the symptoms of diseases when they appear on plant leaves. This enables computer vision
algorithms to provide image-based automatic inspection. Comparatively, manual identification is
labor intensive, less accurate and can be done only in small areas at a time. By this method, the plant
diseases can be identified at the initial stage itself and the pest and infection control tools can be used
to solve pest problems while minimizing risks to people and the environment.



## About Dataset 

[**Link**](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset)

This dataset is recreated using offline augmentation from the original dataset. This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes. The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure. A new directory containing 33 test images is created later for prediction purpose.
![data.jpeg](https://www.dropbox.com/s/mf18plqppjt4og2/data.jpeg?dl=0&raw=1)![data1.jpeg](https://www.dropbox.com/s/3b5yvbm9gb74r8j/data1.jpeg?dl=0&raw=1)








## Model architecture 

We used VGG19 for enhancing the accuracy of our model.
![flowchart.jpg](https://www.dropbox.com/s/4sw176a2zlxy3ie/flowchart.jpg?dl=0&raw=1)

## Loss and accuracy plot

![Capture (2).PNG](https://www.dropbox.com/s/nxlll3vijl8ejkq/Capture%20%282%29.PNG?dl=0&raw=1)![Capture (1).PNG](https://www.dropbox.com/s/7c4upiiummo7rvp/Capture%20%281%29.PNG?dl=0&raw=1)



## Results
Now the best models with best accuracy detects the plant disease with accuracy

Accuracy 85%
![accuracy (1).png](https://www.dropbox.com/s/wgs3rcgrqpt35zj/accuracy%20%281%29.png?dl=0&raw=1)

## Web Application

![MyVideo_1](https://user-images.githubusercontent.com/83203229/141359598-29e2f040-c0b0-4a78-907a-43f2f8e040d0.gif)



## DONUT CHART OF ACCURACY TABLE ->
![accuracyy1.png](https://www.dropbox.com/s/8yu15ixi1b4qol2/accuracyy1.png?dl=0&raw=1)

## Conclusion 

The model was successfully able to determine whether the plant whose image is provided has the disease or not and if yes,which disease the plant is suffering from.

Knowing if the plant is suffering with a disease we can conclude which pesticide should be selected for its further prevention.

## Challenges we ran into
1. Faced Diffilculty in finding a appropriate Data-set with large number of images
2. As a newbie to Machine learning domain it is very difficult to work with huge number of funtions and libraries.3)As we have used VGG 19 architure so most of the common inbuilt functions are not working , we have encounterd with number of errors , So finding new functions and there respective libraries is quite a troublesome.
3. As we have used VGG 19 architure so most of the common inbuilt functions are not working , we have encounterd with number of errors , So finding new functions and there respective libraries is quite a troublesome.
4. Faced Pixel Related issue for showing false result for Feed images
5. Had Trouble in deployment of our model on website , and linking backend with  the frontend.

## Contributors
[Nischay](https://github.com/NischayGoyal1)

[Samridhi](https://github.com/samridhikapoor)

[Niranjan](https://github.com/NiranjanHebli)

[Rohan](https://github.com/Rohan5202)

## Conclusion 

The model was successfully able to determine whether the plant whose image is provided has the disease or not and if yes,which disease the plant is suffering from.

Knowing if the plant is suffering with a disease we can conclude which pesticide should be selected for its further prevention.
