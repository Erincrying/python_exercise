# jpeg压缩原理：https://www.cnblogs.com/Arvin-JIN/p/9133745.html
import RGB2YUV
import DCT
import Quantization
import AC
import DC
import Compress
import cv2
import numpy as np

def printBlock(block):
    for row in block:
        print(row)

# 离散余弦变换
DCT = DCT.DCT()
# 量化
Quantization = Quantization.Quantization()
# AC系数
AC = AC.AC()
# DC系数
DC = DC.DC()
# 压缩
Compress = Compress.Compress()

'''
    压缩
'''
def compress(path):
    img = cv2.imread(path)
    # (682, 1024, 3) img.shape,通过.shape[0]和.shape[1]获取图片的宽高
    height = img.shape[0]
    width = img.shape[1]
    print(height, width, '原图像宽，高')
    # RGB 转 YUV，得到三张分别用 Y、U、 V 生成的灰度图
    Y, U, V = RGB2YUV.rgb2yuv(img, img.shape[1], img.shape[0])
    # print(np.array(Y).shape, 'Y.shape')
    # print(np.array(U).shape, 'U.shape')
    # print(np.array(V).shape, 'V.shape')
    # 生成三个灰度的例子
    # showYUV(img, Y, U, V)


    # 图像边长填充为 8 的倍数并等分
    # 用 DCT.fill(img)函数对二次采样得到的 Y、U、V 图像分别用 0 填充直到其矩阵的height 和 width 都是 8 的倍数
    # 因为 DCT 函数的参数是一个 8*8 的矩阵。同样用DCT.split(img)函数将图像以左到右，上到下的顺序分成多个 8*8 矩阵
    Y = DCT.fill(Y)
    U = DCT.fill(U)
    V = DCT.fill(V)
    # print(np.array(Y).shape, 'DCT.fill后的Y.shape') # (688, 1024) DCT.fill后的Y.shape
    # 用DCT.split(img)函数将图像以左到右，上到下的顺序分成多个 8*8 矩阵，并返回这些矩阵连成的数组。
    blocksY = DCT.split(Y)
    blocksU = DCT.split(U)
    blocksV = DCT.split(V)
    # print(np.array(blocksY), 'np.array(blocksY)')
    # print(np.array(blocksY).shape, 'blocksY.shape') #(11008, 8, 8) blocksY.shape，301个8*8的矩阵

    # 离散余弦变换blocksY
    FDCT = []
    Quan = []
    Z = []
    ACnum = []
    # 循环每个8*8矩阵
    for block in blocksY:
        # 用 DCT.FDCT(block)函数对一个 8*8 矩阵进行二维离散余弦变换，保存得到的矩阵。
        FDCT.append(DCT.FDCT(block))
        # 用 Quantization.quanY(img)与 Quantization.quanUV(img)分别用于对 Y 图像与 U、 V 图像量化。
        Quan.append(Quantization.quanY(FDCT[-1]))
        # 用 AC 类中的 ZScan(img)对一个图像进行 Z 型扫描，得到一个长度为 63 的数组,方便后续的编码
        Z.append(AC.ZScan(Quan[-1]))
        ACnum.append(AC.RLC(Z[-1]))
    DCnum = DC.DPCM(Quan)
    #print('Y: ')
    # 开始哈夫曼编码，转换为0001111这种数据
    Bstr0 = ''
    for i in range(len(ACnum)):
        Bstr0 += Compress.AllCompressY(DCnum[i], ACnum[i])
    # print(Bstr0, 'Bstr0')
    # print(len(Bstr0), 'len(Bstr0)')


    # 离散余弦变换blocksU
    FDCT = []
    Quan = []
    Z = []
    ACnum = []
    for block in blocksU:
        FDCT.append(DCT.FDCT(block))
        # quanUV: U、 V 图像量化。
        Quan.append(Quantization.quanUV(FDCT[-1]))
        Z.append(AC.ZScan(Quan[-1]))
        ACnum.append(AC.RLC(Z[-1]))
    DCnum = DC.DPCM(Quan)
    #print('U: ')
    Bstr1 = ''
    for i in range(len(ACnum)):
        Bstr1 += Compress.AllCompressUV(DCnum[i], ACnum[i])
    #print(Bstr1)
    #print(len(Bstr1))


    # 离散余弦变换blocksV
    FDCT = []
    Quan = []
    Z = []
    ACnum = []
    for block in blocksV:
        FDCT.append(DCT.FDCT(block))
        Quan.append(Quantization.quanUV(FDCT[-1]))
        Z.append(AC.ZScan(Quan[-1]))
        ACnum.append(AC.RLC(Z[-1]))
    DCnum = DC.DPCM(Quan)
    #print('V: ')
    Bstr2 = ''
    for i in range(len(ACnum)):
        Bstr2 += Compress.AllCompressUV(DCnum[i], ACnum[i])
    #print(Bstr2)
    #print(len(Bstr2))
    s = Bstr0 + Bstr1 + Bstr2
    print(len(s), 'len(s)') # 1395606,原图像682*1024*8*3=16760832，这里计算压缩比1395606/16760832=8.3%

    return height, width, s

'''
    译码
'''
def encoding(bs, width, height):
    DCY, DCU, DCV, ACY, ACU, ACV = Compress.encoding(bs, height, width)
    YBlocks = DC.DPCM2(DCY)
    UBlocks = DC.DPCM2(DCU)
    VBlocks = DC.DPCM2(DCV)
    for i in range(len(YBlocks)):
        AC.Z2Tab(ACY[i], YBlocks[i])
        YBlocks[i] = Quantization.reY(YBlocks[i])
        YBlocks[i] = DCT.IDCT(YBlocks[i])
    for i in range(len(UBlocks)):
        AC.Z2Tab(ACU[i], UBlocks[i])
        UBlocks[i] = Quantization.reUV(UBlocks[i])
        UBlocks[i] = DCT.IDCT(UBlocks[i])
    for i in range(len(VBlocks)):
        AC.Z2Tab(ACV[i], VBlocks[i])
        VBlocks[i] = Quantization.reUV(VBlocks[i])
        VBlocks[i] = DCT.IDCT(VBlocks[i])

    Y, U, V = DCT.merge(YBlocks, UBlocks, VBlocks, height, width)
    img = RGB2YUV.yuv2rgb(Y, U, V, width, height)
    cv2.imwrite(r'../imgCompression/JPEG/photograph_JPEG.jpeg', img)
    cv2.imshow("img after encoding", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
    生成三个灰度的例子
'''
def showYUV(img, Y, U, V):
    imgY = np.zeros([img.shape[0], img.shape[1], 1], dtype=np.uint8)
    imgU = np.zeros([img.shape[0] // 2, img.shape[1] // 2, 1], dtype=np.uint8)
    imgV = np.zeros([img.shape[0] // 2, img.shape[1] // 2, 1], dtype=np.uint8)
    for i in range(682):
        for j in range(1024):
            imgY[i][j][0] = Y[i][j]
    for i in range(341):
        for j in range(512):
            imgU[i][j][0] = U[i][j]
    for i in range(341):
        for j in range(512):
            imgV[i][j][0] = V[i][j]
    cv2.imshow("created_imgY", imgY)
    cv2.imshow("created_imgU", imgU)
    cv2.imshow("created_imgV", imgV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

height, width, s = compress(r"../imgCompression/JPEG/photograph.jpg")
print(height, width, '高、宽')
f = open(r'../imgCompression/JPEG/txt.txt', 'w', encoding='utf-8')
f.write(s)
f.close()



f = open(r'../imgCompression/JPEG/txt.txt', 'r', encoding='utf-8')
s = f.read()
encoding(s, width, height)
f.close()
