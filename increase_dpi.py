import os
from PIL import Image

def change_dpi_of_images(input_folder, output_folder, dpi=(300, 300)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                img.save(os.path.join(output_folder, filename), dpi=dpi)
            print(f"Processed {filename}")

def main():
    input_folder = 'path_to_your_folder/'  # 入力フォルダのパス
    output_folder = 'output/'  # 出力フォルダのパス

    # DPIを変更
    change_dpi_of_images(input_folder, output_folder)

if __name__ == '__main__':
    main()