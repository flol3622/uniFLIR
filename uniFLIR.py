import os
import matplotlib.pyplot as plt
from flir_image_extractor import FlirImageExtractor


def main():
    inFolder = "."
    outFolder = "out/"
    min_temp = int(input('Enter the minimum temperature: ').strip() or "20")
    max_temp = int(input('Enter the maximum temperature: ').strip() or "40")

    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    files = [filename for filename in os.listdir(inFolder) if filename.endswith(".jpg")]
    total_files = len(files)
    for index, filename in enumerate(files):
        filePath = os.path.join(inFolder, filename)
        raw = FlirImageExtractor()
        raw.process_image(filePath)
        thermal = raw.get_thermal_np()

        outPath = os.path.join(outFolder, filename)
        plt.imsave(outPath, thermal, cmap="plasma", vmin=min_temp, vmax=max_temp)

        remaining_files = total_files - (index + 1)
        print(f"Processed {filename}. Remaining files: {remaining_files}", end="\r")


if __name__ == "__main__":
    print("Starting...")
    main()
