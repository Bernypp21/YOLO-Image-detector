from ultralytics import YOLOWorld


# use opencv for extracting color from an image


# yolo --> finds object --> give opencv that value --> opencv checks color --> if matches then true


#yolo does classification, opencv does color dectection

'''
#how to extract object from yolo model 
    - capture the image? 
    - create  a numpy array with values? -- maybe the same as image
    - can we give open cv the view box of yolo????
    * Is their a yolo model that can do everything instead?

#Once image from yolo extracted opencv can find color
    - use opencv functions to find color

#once color is found
    - notify that color matches and object is found

'''




model = YOLOWorld("yolov8m-world.pt")
go = 1



def yolo_model(userInput:list[str]):
    model.set_classes(userInput) 
    result = model.predict(
    source=0,
    show=True)


def get_list_string()->list[str]:
    switch = 1
    to_find = []

    while switch == 1:
        user_input = input("enter object you want to find >>> ")
        to_find.append(user_input)
        switch = int(input("to stop type(1:continue,0:stop)>>> "))
    return to_find


def main():
    while(go == 1):
       list_item = get_list_string()
       yolo_model(list_item)



if __name__ == "__main__":
    main()
