from solutions_funciton import count_apples

if __name__ == "__main__":
    # 以59号苹果图片测试
    test_image_path = r'D:\Attachment\Attachment 1\59.jpg'
    apple_count = count_apples(test_image_path)
    print(f"在图像'{test_image_path}'中检测到的苹果数量为: {apple_count}")