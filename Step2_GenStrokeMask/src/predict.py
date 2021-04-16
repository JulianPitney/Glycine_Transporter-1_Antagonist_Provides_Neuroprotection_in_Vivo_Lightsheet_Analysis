from model import *

import matplotlib.pyplot as plt
from dataProcess import *
from tqdm import tqdm


from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QLabel,
                             QGridLayout, QComboBox, QRadioButton, QButtonGroup,
                             QApplication, QLineEdit)
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.messagebox import showwarning, showinfo
from tkinter import Tk


def predict(threshold=0.5, batchSize=4):
    weights_folder = os.path.join('..', 'weights')
    if not os.path.exists(weights_folder):
        os.mkdir(weights_folder)
    result_folder = os.path.join('..', 'result')
    if not os.path.exists(result_folder):
        os.mkdir(result_folder)
    val_txt = os.path.join("..", "dataset", "val.txt")
    inputs, xception_inputs, ans = get_model()
    m = Model(inputs=[inputs, xception_inputs], outputs=[ans])
    best_model_weights = os.path.join(weights_folder,
                                      [item for item in os.listdir(weights_folder) if ".index" in item][0].replace(
                                          ".index", ""))
    m.load_weights(best_model_weights)
    print("Weights have been loaded!")
    val_generator = data_generator(val_txt, batchSize=batchSize, aug=False)
    with open(val_txt, 'r') as f:
        val_steps = len(f.readlines()) // batchSize + 1
    index = 0
    for i in range(val_steps):
        x, y = next(val_generator)
        predictions = m.predict_on_batch(x)
        for j in range(predictions.shape[0]):
            prediction = label2Color(predict2Mask(predictions[j]))
            input = np.asarray(x[0][j], dtype='uint8')
            label = label2Color(np.asarray(y[j], dtype='uint8'))
            cv2.imwrite(os.path.join(result_folder, str(index) + '_predict.png'), prediction)
            cv2.imwrite(os.path.join(result_folder, str(index) + '_input.png'), input)
            cv2.imwrite(os.path.join(result_folder, str(index) + '_label.png'), label)
            index += 1

def predictScan(tifPath, scanPath, consider_list):
    x, oriX = prepareScanForPredict(tifPath)
    oriHeight, oriWidth = oriX[0].shape[1], oriX[0].shape[0]
    scan_folder = scanPath
    if not os.path.exists(scan_folder):
        os.mkdir(scan_folder)
    assert os.path.isdir(scan_folder)
    inputs, xception_inputs, ans = get_model()
    m = Model(inputs=[inputs, xception_inputs], outputs=[ans])
    weights_folder = os.path.join('..', 'weights')
    assert os.path.exists(weights_folder)
    best_model_weights = os.path.join(weights_folder,
                                      [item for item in os.listdir(weights_folder) if ".index" in item][0].replace(
                                          ".index", ""))
    m.load_weights(best_model_weights)
    print("Weights have been loaded!")
    predictions = m.predict(x, batch_size=4, verbose=1)
    print("Writing Predicted results...")

    background, normal, stroke = False, False, False


    if 'background' in consider_list:
        background = True
    if 'normal' in consider_list:
        normal = True
    if 'stroke' in consider_list:
        stroke = True
    for i in tqdm(range(predictions.shape[0])):
        prediction = label2Color(predict2Mask(predictions[i]), background=background, normal=normal, stroke=stroke)
        # input = np.asarray(x[0][i], dtype='uint8')
        input = oriX[i]
        cv2.imwrite(os.path.join(scan_folder, str(i) + '_predict.png'), prediction)
        cv2.imwrite(os.path.join(scan_folder, str(i) + '_input.png'), input)
    return oriHeight, oriWidth

def calculateVolume(tifPath,considerList,
                    widthRatio=0.00143, heightRatio=0.00143, thicknessRatio=0.005,
                    colorDict=None, rawImageShape=(2448, 2048), inputShape=(608, 608)):
    if not colorDict:
        global COLOR_DICT
        colorDict = COLOR_DICT
    assert os.path.isdir(tifPath), 'Path not exist!'
    widthRatio = widthRatio * (float(rawImageShape[0])/ float(inputShape[0]))
    heightRatio = heightRatio * (float(rawImageShape[1]) / float(inputShape[1]))
    numDict = {}
    for img in tqdm([cv2.imread(os.path.join(tifPath, imgPath)) for imgPath in os.listdir(tifPath) if 'predict' in imgPath]):
        imgArray = np.asarray(img)
        for key in colorDict.keys():
            if key not in considerList:
                continue
            if key not in numDict.keys():
                numDict[key] = 0
            mask = np.all(imgArray == colorDict[key], axis=-1)
            numDict[key] += np.asarray(mask, dtype=np.float).sum() * widthRatio * heightRatio * thicknessRatio
    # print(numDict)
    return numDict

def dict2Piechart(volumePath, resultDict, considerList):
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    keys = [key for key in resultDict.keys() if key in considerList]
    data = [resultDict[key] for key in keys]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate("%5s: %.2f mm3, %.2f%%" %
                    (keys[i], resultDict[keys[i]], 100. * float(resultDict[keys[i]]) / float(sum(data))),
                    xy=(x, y), xytext=(1.35 * np.sign(x), 1.1 * y),
                    horizontalalignment=horizontalalignment, **kw)


    brainId = os.path.basename(volumePath)
    title = plt.title("Stroke Volume: %s" % brainId)

    figuresPath = os.path.dirname(volumePath)

    if not os.path.exists(figuresPath):
        os.mkdir(figuresPath)
    imgSavePath = os.path.join(figuresPath, brainId + '.png')
    plt.tight_layout()
    fig.savefig(imgSavePath, bbox_inches="tight")


def gui_entrance():

    class StartWindow(QMainWindow):
        """
        Main entrance of the whole process.
        """

        def __init__(self):
            super().__init__()
            self.root_dir = "/"
            self.save_dir = "/"
            self.widget_main = QWidget()
            self.layout_main = QGridLayout()
            self.widget_main.setLayout(self.layout_main)

            self.widget_radio = QWidget()
            self.layout_radio = QGridLayout()
            self.widget_radio.setLayout(self.layout_radio)

            self.widget_thickness = QWidget()
            self.layout_thickness = QGridLayout()
            self.widget_thickness.setLayout(self.layout_thickness)

            self.widget_ratio = QWidget()
            self.layout_ratio = QGridLayout()
            self.widget_ratio.setLayout(self.layout_ratio)

            self.radio_label_background = QRadioButton("Background")
            self.radio_group = QButtonGroup(self.widget_main)
            self.radio_group.setExclusive(False)
            self.radio_group.addButton(self.radio_label_background)

            self.radio_label_normal = QRadioButton("Normal")
            self.radio_group.addButton(self.radio_label_normal)

            self.radio_label_stroke = QRadioButton("Stroke")
            self.radio_group.addButton(self.radio_label_stroke)


            self.radio_label_background.setChecked(True)
            self.radio_label_stroke.setChecked(True)
            self.radio_label_normal.setChecked(True)

            self.radio_label_background.clicked.connect(self.on_radio_clicked)
            self.radio_label_stroke.clicked.connect(self.on_radio_clicked)
            self.radio_label_normal.clicked.connect(self.on_radio_clicked)

            self.labelnote = QLabel("*Select which category to consider")

            self.labelRootDir = QLabel("Select tiff file to perform segmentation. (i.e. images/1.tif)")
            self.btnRootDir = QPushButton('Select')
            self.btnRootDir.clicked.connect(self.select_rootDir)
            self.lineRootDir = QLabel(self.root_dir)

            self.labelSaveDir = QLabel("Select directory to save results (different from root directory)")
            self.btnSaveDir = QPushButton('Select')
            self.btnSaveDir.clicked.connect(self.select_saveDir)
            self.lineSaveDir = QLabel(self.save_dir)

            self.btnRun = QPushButton("Run")
            self.btnRun.clicked.connect(self.analyse)
            self.btnCal = QPushButton("Calculate Volume")
            self.btnCal.clicked.connect(self.calVolume)


            self.thickness_label = QLabel(self)
            self.thickness_label.setText('Section thickness:')
            self.thickness_combo = QComboBox(self)

            self.thickness_combo.addItem("50")
            self.thickness_combo.addItem("100")

            self.layout_main.addWidget(self.labelRootDir, 1, 0)
            self.layout_main.addWidget(self.lineRootDir, 2, 0)
            self.layout_main.addWidget(self.btnRootDir, 2, 1)

            self.layout_main.addWidget(self.labelSaveDir, 3, 0)
            self.layout_main.addWidget(self.lineSaveDir, 4, 0)
            self.layout_main.addWidget(self.btnSaveDir, 4, 1)


            self.layout_main.addWidget(self.labelnote, 7, 0)

            self.layout_radio.addWidget(self.radio_label_normal, 0, 0)
            self.layout_radio.addWidget(self.radio_label_background, 0, 1)
            self.layout_radio.addWidget(self.radio_label_stroke, 0, 2)
            self.layout_main.addWidget(self.widget_radio, 8, 0)


            self.layout_thickness.addWidget(self.thickness_label, 0, 0)
            self.layout_thickness.addWidget(self.thickness_combo, 0, 1)

            self.textinput_width_ratio = QLineEdit()
            self.textinput_height_ratio = QLineEdit()
            self.textinput_depth_ratio = QLineEdit()
            self.label_width_ratio = QLabel("Width ratio:")
            self.label_height_ratio = QLabel("Height ratio:")
            self.label_depth_ratio = QLabel("Depth ratio:")

            self.layout_ratio.addWidget(self.label_width_ratio, 0, 0)
            self.layout_ratio.addWidget(self.textinput_width_ratio, 0, 1)
            self.layout_ratio.addWidget(self.label_height_ratio, 0, 2)
            self.layout_ratio.addWidget(self.textinput_height_ratio, 0, 3)
            self.layout_ratio.addWidget(self.label_depth_ratio, 0, 4)
            self.layout_ratio.addWidget(self.textinput_depth_ratio, 0, 5)

            self.layout_main.addWidget(self.widget_ratio, 12, 0)

            # self.layout_main.addWidget(self.widget_thickness, 13, 0)

            self.layout_main.addWidget(self.btnRun, 13, 0)
            self.layout_main.addWidget(self.btnCal, 14, 0)

            self.setCentralWidget(self.widget_main)
            self.textinput_height_ratio.setText("1.43")
            self.textinput_width_ratio.setText("1.43")
            self.textinput_depth_ratio.setText("5.")
            self.show()

        def choosePath(self, file=False):
            root = Tk()
            root.withdraw()
            if not file:
                result = askdirectory(initialdir="/", title="Select Tiff File")
            else:
                result = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Tiff files","*.tif"),("all files","*.*")))
            return result

        def on_radio_clicked(self):

            if not (
                self.radio_label_background.isChecked() or
                self.radio_label_normal.isChecked() or
                self.radio_label_stroke.isChecked()
            ):
                self.sender().setChecked(True)
                root = Tk()
                root.withdraw()
                showwarning("Warning!", "At least one category should be selected!!")


        def select_rootDir(self):
            self.root_dir = self.choosePath(file=True)
            if type(self.root_dir) is str:
                self.lineRootDir.setText(self.root_dir)
            else:
                pass

        def select_saveDir(self):
            self.save_dir = self.choosePath()
            if type(self.save_dir) is str:
                self.lineSaveDir.setText(self.save_dir)
            else:
                pass

        def analyse(self):
            thickness = float(self.textinput_depth_ratio.text()) * 0.001
            consider_list = [btn.text().lower() for btn in
                             [self.radio_label_normal, self.radio_label_background, self.radio_label_stroke]
                             if btn.isChecked()]
            tif_path = self.lineRootDir.text()
            volume_path = self.lineSaveDir.text()
            volume_path = os.path.join(volume_path, os.path.basename(tif_path).split('.')[0])
            if not os.path.exists(volume_path):
                os.mkdir(volume_path)
            oriHeight, oriWidth = predictScan(tif_path, volume_path, consider_list)


        def calVolume(self):
            thickness = float(self.textinput_depth_ratio.text()) * 0.001
            consider_list = [btn.text().lower() for btn in
                             [self.radio_label_normal, self.radio_label_background, self.radio_label_stroke]
                             if btn.isChecked()]
            tif_path = self.lineRootDir.text()
            volume_path = self.lineSaveDir.text()
            volume_path = os.path.join(volume_path, os.path.basename(tif_path).split('.')[0])

            x, oriX = prepareScanForPredict(tif_path)
            oriHeight, oriWidth = oriX[0].shape[1], oriX[0].shape[0]

            dataDict = calculateVolume(volume_path, considerList=consider_list,
                                       rawImageShape=(oriHeight, oriWidth),
                                       thicknessRatio=thickness,
                                       widthRatio=float(self.textinput_width_ratio.text()) * 0.001,
                                       heightRatio=float(self.textinput_height_ratio.text()) * 0.001
                                       )
            dict2Piechart(volume_path, dataDict, considerList=consider_list)
            showinfo("Finshed!", "Current task %s completed!" % os.path.basename(tif_path))

    app = QApplication([])
    start_window = StartWindow()
    start_window.show()
    app.exit(app.exec_())

if __name__ == '__main__':
    # args = parser.ArgumentParser(description='Model training arguments')
    #
    # args.add_argument('-tif', '--tifScanPath', type=str, default=None,
    #                   help='tif path')
    #
    # args.add_argument('-volume', '--tifVolumePath', type=str, default=None,
    #                   help='tif path')
    #
    # args.add_argument('-threshold', '--threshold', type=str, default=0.5,
    #                   help='threshold')
    #
    # args.add_argument('-pie', '--pie', type=int, default=None,
    #                   help='show pie chart, integer 1 means True')
    #
    # args.add_argument('-width', '--rawWidth', type=int, default=2448,
    #                   help='width of raw Tif scan')
    #
    # args.add_argument('-height', '--rawHeight', type=int, default=2048,
    #                   help='height of raw tif scan')
    #
    # args.add_argument('-step', '--stepThickness', type=float, default=0.005,
    #                   help='thinkness, step interval')
    #
    #
    # parsed_arg = args.parse_args()
    # if parsed_arg.tifScanPath:
    #     predictScan(parsed_arg.tifScanPath, parsed_arg.tifVolumePath)
    # if parsed_arg.tifVolumePath:
    #     dataDict = calculateVolume(parsed_arg.tifVolumePath,
    #                                rawImageShape=(parsed_arg.rawWidth, parsed_arg.rawHeight),
    #                                thicknessRatio=parsed_arg.stepThickness)
    #     if parsed_arg.pie == 1:
    #         dict2Piechart(parsed_arg.tifVolumePath, dataDict)
    # else:
    #     predict(threshold=float(parsed_arg.threshold))
    gui_entrance()