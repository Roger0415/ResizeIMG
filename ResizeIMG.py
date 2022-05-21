import cv2
import os

def resize_img(DATADIR, data_k, img_size):
    w=img_size[0]
    h=img_size[1]
    path=os.path.join(DATADIR, data_k) #返回path路徑下所有文件的名字,以及文件夾的名字
    img_list=os.listdir(path) #os.listdir() 方法用於返回指定的文件夾包含的文件或文件夾
    
    for i in img_list:
        if i.endswith('.PNG'): #判斷圖片名稱是否已".PNG"結尾
            img_array=cv2.imread((path + '/' + i),cv2.IMREAD_COLOR) #調用cv2.imread讀入圖片,讀入格式為IMREAD_COLOR
            new_array=cv2.resize(img_array,(w,h),interpolation=cv2.INTER_CUBIC) #調用cv2.resize函數resize圖片
            img_name=str(i) 
            
            '''生成圖片儲存的目標路徑'''
            save_path=path + 'D403_NEW/' 
            if os.path.exists(save_path):
                print(i)
                '''調用cv2.imwrite函數保存圖片'''
                save_img=save_path + img_name
                cv2.imwrite(save_img, new_array)
            else:
                os.mkdir(save_path)
                save_img=save_path + img_name
                cv2.imwrite(save_img, new_array)
                
if __name__ == '__main__':
  '''設置圖片路徑'''
    DATADIR= "C:/Users/user/"
    data_k= "D403"
    '''設置目標像素大小,此處設為512*512'''
    img_size=[512,512]
    resize_img(DATADIR, data_k, img_size)
