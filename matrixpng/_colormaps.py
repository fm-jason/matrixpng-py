#!/usr/bin/env python3
"""Color maps for matrixpng

The canonical source for this package is https://github.com/finitemobius/matrixpng-py
Currently, the only RGB colormap is Extended Black Body"""

__author__ = "Finite Mobius, LLC"
__credits__ = ["Jason R. Miller"]
__license__ = "MIT"
__version__ = "alpha"
__maintainer__ = "Finite Mobius, LLC"
__email__ = "jason@finitemobius.com"
__status__ = "Development"


def ColorMaps(mode="RGB", bd=8, colormap="ebb"):
    if mode.startswith("RGB"):
        return {
            "ebb": {
                # These were pre-computed based on Kenneth Moreland's Extended Black Body scale
                # http://www.kennethmoreland.com/color-advice/#extended-black-body
                8: [
                    [0, 0, 0], [1, 0, 1], [1, 0, 2], [2, 1, 4], [3, 1, 5],
                    [3, 1, 6], [4, 1, 7], [5, 1, 8], [5, 2, 10], [6, 2, 11],
                    [6, 2, 12], [7, 2, 13], [8, 2, 14], [8, 3, 15], [9, 3, 16],
                    [10, 3, 17], [11, 3, 18], [12, 4, 19], [12, 4, 20], [13, 4, 20],
                    [13, 4, 21], [14, 4, 22], [14, 5, 23], [15, 5, 23], [15, 5, 24],
                    [16, 5, 24], [16, 5, 25], [17, 6, 26], [18, 6, 27], [18, 6, 28],
                    [19, 7, 29], [20, 7, 30], [20, 7, 31], [21, 8, 32], [21, 8, 33],
                    [21, 8, 34], [22, 8, 34], [22, 9, 35], [22, 9, 36], [23, 9, 37],
                    [23, 10, 38], [23, 10, 39], [24, 10, 39], [24, 10, 40], [24, 10, 41],
                    [24, 11, 41], [24, 11, 42], [25, 11, 43], [25, 11, 44], [25, 12, 44],
                    [25, 12, 45], [25, 12, 46], [26, 12, 46], [26, 12, 47], [26, 12, 48],
                    [26, 13, 48], [26, 13, 49], [27, 13, 50], [27, 13, 51], [27, 13, 52],
                    [28, 13, 53], [28, 13, 54], [28, 14, 54], [28, 14, 55], [28, 14, 56],
                    [29, 14, 57], [29, 14, 58], [29, 14, 59], [30, 14, 59], [30, 14, 60],
                    [30, 14, 61], [30, 14, 62], [31, 14, 63], [31, 14, 64], [31, 14, 65],
                    [32, 14, 65], [32, 14, 66], [32, 14, 67], [32, 14, 68], [32, 15, 68],
                    [33, 15, 69], [33, 15, 70], [33, 15, 71], [34, 15, 72], [34, 15, 73],
                    [34, 15, 74], [34, 15, 75], [35, 15, 75], [35, 15, 76], [35, 15, 77],
                    [35, 15, 78], [36, 15, 79], [36, 15, 80], [36, 15, 81], [37, 15, 82],
                    [37, 15, 83], [37, 15, 84], [37, 15, 85], [38, 15, 86], [38, 15, 87],
                    [38, 15, 88], [39, 15, 89], [39, 15, 90], [39, 15, 91], [39, 15, 92],
                    [40, 15, 93], [40, 15, 94], [40, 15, 95], [40, 15, 96], [41, 15, 97],
                    [41, 15, 98], [41, 15, 99], [41, 15, 100], [42, 15, 100], [42, 15, 101],
                    [42, 15, 102], [42, 15, 103], [42, 15, 104], [43, 15, 105], [43, 15, 106],
                    [43, 15, 107], [43, 15, 108], [44, 15, 109], [44, 15, 110], [44, 15, 111],
                    [44, 15, 112], [45, 15, 112], [45, 15, 113], [45, 15, 114], [45, 15, 115],
                    [45, 15, 116], [46, 15, 117], [46, 15, 118], [46, 15, 119], [46, 14, 120],
                    [47, 14, 121], [47, 14, 122], [47, 14, 123], [47, 14, 124], [47, 14, 125],
                    [48, 14, 126], [48, 14, 127], [48, 14, 128], [48, 14, 129], [49, 14, 130],
                    [49, 14, 131], [49, 14, 132], [49, 14, 133], [50, 14, 134], [50, 14, 135],
                    [50, 13, 136], [50, 13, 137], [50, 13, 138], [51, 13, 139], [51, 13, 140],
                    [51, 13, 141], [51, 13, 142], [51, 13, 143], [52, 13, 144], [52, 13, 145],
                    [52, 12, 146], [52, 12, 147], [52, 12, 148], [52, 12, 149], [53, 12, 149],
                    [53, 12, 150], [53, 12, 151], [53, 12, 152], [53, 12, 153], [54, 11, 154],
                    [54, 11, 155], [54, 11, 156], [54, 11, 157], [54, 11, 158], [55, 11, 159],
                    [55, 11, 160], [55, 10, 161], [55, 10, 162], [55, 10, 163], [55, 10, 164],
                    [56, 10, 165], [56, 10, 166], [56, 9, 166], [56, 9, 167], [56, 9, 168],
                    [56, 9, 169], [57, 9, 169], [58, 9, 170], [58, 8, 170], [59, 8, 171],
                    [60, 8, 171], [60, 7, 172], [61, 7, 172], [62, 7, 173], [63, 6, 174],
                    [64, 6, 175], [65, 6, 176], [65, 5, 176], [66, 5, 176], [66, 5, 177],
                    [67, 4, 177], [68, 4, 178], [69, 4, 179], [69, 3, 179], [70, 3, 180],
                    [71, 3, 181], [71, 2, 181], [72, 2, 182], [73, 1, 182], [73, 1, 183],
                    [74, 1, 183], [74, 1, 184], [75, 0, 184], [76, 0, 185], [77, 0, 186],
                    [78, 0, 187], [79, 0, 188], [80, 0, 188], [80, 0, 189], [81, 0, 189],
                    [81, 0, 190], [82, 0, 190], [82, 0, 191], [83, 0, 191], [83, 0, 192],
                    [84, 0, 192], [84, 0, 193], [85, 0, 193], [85, 0, 194], [86, 0, 194],
                    [87, 0, 195], [88, 0, 195], [88, 0, 196], [89, 0, 196], [89, 0, 197],
                    [90, 0, 197], [90, 0, 198], [91, 0, 198], [91, 0, 199], [92, 0, 199],
                    [92, 0, 200], [93, 0, 200], [93, 0, 201], [94, 0, 201], [95, 0, 202],
                    [96, 0, 203], [97, 0, 204], [98, 0, 205], [99, 0, 206], [100, 0, 207],
                    [101, 0, 208], [102, 0, 208], [102, 0, 209], [103, 0, 209], [103, 0, 210],
                    [104, 0, 210], [104, 0, 211], [105, 0, 211], [105, 0, 212], [106, 0, 212],
                    [106, 0, 213], [107, 0, 213], [107, 0, 214], [108, 0, 214], [108, 0, 215],
                    [109, 0, 215], [109, 0, 216], [110, 0, 216], [110, 0, 217], [111, 0, 217],
                    [112, 0, 218], [113, 0, 219], [114, 0, 219], [114, 0, 220], [115, 0, 220],
                    [115, 0, 221], [116, 0, 221], [116, 0, 222], [117, 0, 222], [117, 0, 223],
                    [118, 0, 223], [118, 0, 224], [119, 0, 224], [119, 0, 225], [120, 0, 225],
                    [120, 0, 226], [121, 0, 226], [121, 0, 227], [122, 0, 227], [123, 0, 228],
                    [124, 0, 229], [125, 0, 228], [127, 0, 226], [128, 0, 225], [129, 0, 223],
                    [131, 0, 222], [132, 0, 221], [134, 0, 219], [135, 0, 218], [136, 0, 217],
                    [137, 0, 215], [139, 0, 214], [140, 0, 213], [141, 0, 211], [142, 0, 210],
                    [144, 0, 208], [145, 0, 207], [146, 0, 206], [147, 0, 204], [148, 0, 203],
                    [149, 0, 202], [150, 0, 200], [151, 0, 199], [152, 0, 198], [153, 0, 196],
                    [154, 0, 195], [155, 0, 194], [156, 0, 192], [157, 0, 191], [158, 0, 190],
                    [159, 0, 188], [160, 0, 187], [161, 0, 186], [162, 0, 184], [163, 0, 183],
                    [164, 0, 182], [165, 0, 180], [165, 0, 179], [166, 0, 178], [167, 0, 176],
                    [168, 0, 175], [169, 0, 174], [170, 0, 172], [170, 0, 171], [171, 0, 170],
                    [172, 0, 168], [173, 0, 167], [173, 0, 166], [174, 0, 165], [175, 0, 163],
                    [176, 0, 162], [176, 0, 161], [177, 0, 159], [178, 0, 158], [179, 0, 157],
                    [179, 0, 155], [180, 0, 154], [181, 0, 153], [181, 0, 151], [182, 0, 150],
                    [183, 0, 149], [183, 0, 148], [184, 0, 146], [185, 0, 145], [185, 0, 144],
                    [186, 0, 142], [187, 0, 141], [187, 0, 140], [188, 0, 139], [188, 0, 137],
                    [189, 0, 136], [190, 0, 135], [190, 0, 133], [191, 0, 132], [191, 0, 131],
                    [192, 0, 130], [192, 0, 128], [193, 0, 127], [194, 0, 126], [194, 0, 124],
                    [195, 0, 123], [195, 0, 122], [196, 0, 121], [196, 0, 119], [197, 0, 118],
                    [197, 0, 117], [198, 0, 115], [198, 0, 114], [199, 0, 113], [199, 0, 112],
                    [200, 0, 110], [200, 0, 109], [201, 0, 108], [201, 0, 107], [202, 0, 105],
                    [202, 0, 104], [203, 0, 103], [203, 0, 102], [204, 0, 100], [204, 0, 99],
                    [205, 0, 98], [205, 0, 96], [206, 0, 95], [206, 0, 94], [207, 0, 93],
                    [207, 0, 91], [208, 0, 90], [208, 0, 89], [208, 0, 87], [209, 0, 86],
                    [209, 0, 85], [210, 0, 84], [210, 0, 82], [211, 1, 81], [211, 2, 80],
                    [211, 3, 79], [212, 4, 77], [212, 5, 76], [213, 6, 75], [213, 7, 73],
                    [213, 8, 72], [214, 9, 71], [214, 10, 69], [215, 11, 68], [215, 12, 67],
                    [215, 13, 65], [216, 14, 64], [216, 15, 63], [217, 16, 61], [217, 17, 61],
                    [217, 19, 61], [217, 20, 61], [217, 21, 61], [218, 23, 61], [218, 24, 61],
                    [218, 25, 61], [218, 26, 61], [218, 27, 61], [218, 28, 61], [219, 29, 61],
                    [219, 30, 61], [219, 31, 61], [219, 32, 61], [219, 33, 61], [220, 33, 61],
                    [220, 34, 61], [220, 35, 61], [220, 36, 61], [220, 37, 61], [221, 37, 61],
                    [221, 38, 61], [221, 39, 61], [221, 40, 61], [221, 41, 61], [222, 42, 61],
                    [222, 43, 61], [222, 44, 61], [222, 45, 61], [223, 45, 61], [223, 46, 61],
                    [223, 47, 61], [223, 48, 61], [223, 49, 61], [224, 49, 61], [224, 50, 61],
                    [224, 51, 61], [224, 52, 61], [225, 52, 61], [225, 53, 61], [225, 54, 61],
                    [225, 55, 61], [226, 56, 61], [226, 57, 61], [226, 58, 61], [227, 59, 61],
                    [227, 60, 61], [227, 61, 61], [228, 62, 61], [228, 63, 61], [228, 64, 61],
                    [229, 65, 60], [229, 66, 60], [229, 67, 60], [230, 68, 60], [230, 69, 60],
                    [230, 70, 60], [231, 70, 60], [231, 71, 60], [231, 72, 60], [231, 73, 60],
                    [232, 73, 60], [232, 74, 60], [232, 75, 60], [233, 76, 60], [233, 77, 60],
                    [233, 78, 60], [234, 78, 60], [234, 79, 60], [234, 80, 60], [234, 81, 60],
                    [235, 81, 60], [235, 82, 60], [235, 83, 60], [236, 83, 60], [236, 84, 60],
                    [236, 85, 60], [236, 85, 59], [236, 86, 59], [237, 86, 59], [237, 87, 59],
                    [237, 88, 59], [238, 89, 59], [238, 90, 59], [239, 91, 59], [239, 92, 59],
                    [239, 93, 59], [240, 93, 59], [240, 94, 59], [240, 95, 59], [240, 96, 59],
                    [241, 96, 59], [241, 97, 59], [241, 98, 59], [241, 98, 58], [242, 98, 58],
                    [242, 99, 58], [242, 100, 58], [243, 101, 58], [243, 102, 58], [243, 103, 58],
                    [244, 103, 58], [244, 104, 58], [244, 105, 58], [245, 105, 58], [245, 106, 58],
                    [245, 107, 58], [246, 108, 57], [246, 109, 57], [246, 110, 57], [247, 110, 57],
                    [247, 111, 57], [247, 112, 57], [248, 113, 57], [248, 114, 57], [249, 115, 57],
                    [249, 116, 57], [249, 116, 56], [249, 117, 56], [250, 117, 56], [250, 118, 56],
                    [250, 119, 56], [249, 119, 56], [249, 120, 56], [249, 121, 56], [249, 122, 55],
                    [249, 123, 55], [249, 124, 55], [249, 125, 55], [249, 126, 55], [249, 127, 54],
                    [249, 128, 54], [248, 128, 54], [248, 129, 54], [248, 130, 54], [248, 131, 54],
                    [248, 132, 53], [248, 133, 53], [248, 134, 53], [248, 135, 53], [248, 136, 53],
                    [247, 136, 52], [247, 137, 52], [247, 138, 52], [247, 139, 52], [247, 140, 52],
                    [247, 140, 51], [247, 141, 51], [247, 142, 51], [246, 143, 51], [246, 144, 51],
                    [246, 144, 50], [246, 145, 50], [246, 146, 50], [246, 147, 50], [246, 148, 49],
                    [246, 149, 49], [245, 149, 49], [245, 150, 49], [245, 151, 49], [245, 151, 48],
                    [245, 152, 48], [245, 153, 48], [245, 154, 48], [245, 154, 47], [244, 155, 47],
                    [244, 156, 47], [244, 157, 47], [244, 157, 46], [244, 158, 46], [244, 159, 46],
                    [244, 160, 46], [243, 160, 45], [243, 161, 45], [243, 162, 45], [243, 163, 45],
                    [243, 163, 44], [243, 164, 44], [243, 165, 44], [242, 165, 44], [242, 166, 43],
                    [242, 167, 43], [242, 168, 43], [242, 168, 42], [242, 169, 42], [241, 169, 42],
                    [241, 170, 42], [241, 171, 41], [241, 172, 41], [241, 173, 40], [240, 174, 40],
                    [240, 175, 40], [240, 175, 39], [240, 176, 39], [240, 177, 38], [239, 178, 38],
                    [239, 179, 38], [239, 179, 37], [239, 180, 37], [239, 181, 37], [239, 181, 36],
                    [238, 182, 36], [238, 183, 35], [238, 184, 35], [238, 184, 34], [238, 185, 34],
                    [237, 185, 34], [237, 186, 34], [237, 186, 33], [237, 187, 33], [237, 188, 33],
                    [237, 188, 32], [236, 188, 32], [236, 189, 32], [236, 189, 31], [236, 190, 31],
                    [236, 191, 30], [236, 192, 30], [235, 192, 29], [235, 193, 29], [235, 193, 28],
                    [235, 194, 28], [235, 195, 27], [234, 195, 27], [234, 196, 27], [234, 196, 26],
                    [234, 197, 26], [234, 197, 25], [234, 198, 25], [233, 198, 24], [233, 199, 24],
                    [233, 199, 23], [233, 200, 23], [233, 201, 22], [232, 201, 22], [232, 201, 21],
                    [232, 202, 21], [232, 202, 20], [232, 203, 20], [232, 203, 19], [232, 204, 19],
                    [231, 204, 18], [231, 205, 18], [231, 205, 17], [231, 205, 16], [231, 206, 16],
                    [231, 206, 15], [230, 207, 15], [230, 207, 14], [230, 208, 13], [230, 208, 12],
                    [230, 209, 12], [230, 209, 11], [229, 209, 10], [229, 210, 9], [229, 210, 8],
                    [229, 211, 8], [229, 211, 7], [229, 212, 8], [229, 212, 15], [229, 212, 20],
                    [230, 212, 24], [230, 213, 27], [230, 213, 31], [230, 213, 34], [231, 213, 37],
                    [231, 214, 39], [231, 214, 42], [231, 214, 44], [232, 214, 47], [232, 215, 49],
                    [232, 215, 51], [233, 215, 53], [233, 215, 55], [233, 216, 57], [233, 216, 59],
                    [234, 216, 61], [234, 216, 63], [234, 217, 65], [234, 217, 66], [235, 217, 68],
                    [235, 217, 70], [235, 218, 72], [235, 218, 73], [236, 218, 75], [236, 219, 77],
                    [236, 219, 78], [236, 219, 80], [237, 219, 81], [237, 220, 83], [237, 220, 84],
                    [237, 220, 86], [238, 220, 88], [238, 221, 89], [238, 221, 91], [238, 221, 92],
                    [238, 221, 94], [239, 222, 95], [239, 222, 96], [239, 222, 98], [239, 222, 99],
                    [240, 223, 101], [240, 223, 102], [240, 223, 104], [240, 223, 105], [240, 224, 107],
                    [241, 224, 108], [241, 224, 109], [241, 225, 111], [241, 225, 112], [242, 225, 113],
                    [242, 225, 115], [242, 226, 116], [242, 226, 118], [242, 226, 119], [243, 226, 120],
                    [243, 227, 122], [243, 227, 123], [243, 227, 124], [243, 227, 126], [244, 228, 127],
                    [244, 228, 128], [244, 228, 130], [244, 228, 131], [244, 229, 132], [245, 229, 134],
                    [245, 229, 135], [245, 230, 136], [245, 230, 138], [245, 230, 139], [246, 230, 140],
                    [246, 231, 142], [246, 231, 143], [246, 231, 144], [246, 231, 145], [246, 232, 147],
                    [247, 232, 148], [247, 232, 149], [247, 232, 151], [247, 233, 152], [247, 233, 153],
                    [247, 233, 155], [248, 234, 156], [248, 234, 157], [248, 234, 158], [248, 234, 160],
                    [248, 235, 161], [248, 235, 162], [249, 235, 164], [249, 235, 165], [249, 236, 166],
                    [249, 236, 167], [249, 236, 169], [249, 237, 170], [249, 237, 171], [250, 237, 172],
                    [250, 237, 174], [250, 238, 175], [250, 238, 176], [250, 238, 178], [250, 238, 179],
                    [250, 239, 180], [251, 239, 181], [251, 239, 183], [251, 239, 184], [251, 240, 185],
                    [251, 240, 186], [251, 240, 188], [251, 241, 189], [251, 241, 190], [252, 241, 192],
                    [252, 241, 193], [252, 242, 194], [252, 242, 195], [252, 242, 197], [252, 242, 198],
                    [252, 243, 199], [252, 243, 200], [252, 243, 202], [253, 244, 203], [253, 244, 204],
                    [253, 244, 205], [253, 244, 207], [253, 245, 208], [253, 245, 209], [253, 245, 211],
                    [253, 246, 212], [253, 246, 213], [253, 246, 214], [253, 246, 216], [254, 247, 217],
                    [254, 247, 218], [254, 247, 219], [254, 247, 221], [254, 248, 222], [254, 248, 223],
                    [254, 248, 224], [254, 249, 226], [254, 249, 227], [254, 249, 228], [254, 249, 230],
                    [254, 250, 231], [254, 250, 232], [254, 250, 233], [254, 251, 235], [254, 251, 236],
                    [255, 251, 237], [255, 251, 238], [255, 252, 240], [255, 252, 241], [255, 252, 242],
                    [255, 252, 244], [255, 253, 245], [255, 253, 246], [255, 253, 247], [255, 254, 249],
                    [255, 254, 250], [255, 254, 251], [255, 254, 252], [255, 255, 254], [255, 255, 255]
                ]
            }
        }[colormap][bd]
    else:
        # Grayscale; we can compute these on the fly
        return list(map(lambda x: [x], range(0, 2**bd, 1)))
